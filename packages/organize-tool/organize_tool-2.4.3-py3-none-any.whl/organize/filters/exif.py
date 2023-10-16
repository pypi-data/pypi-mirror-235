import collections
from datetime import datetime, date, timedelta
from pathlib import Path
from typing import Any, DefaultDict, Dict, Mapping, Optional, Union

import exifread

from .filter import Filter, FilterResult

ExifValue = Union[datetime, date, timedelta, str]
ExifDict = Mapping[str, Union[ExifValue, Mapping[str, ExifValue]]]


def to_datetime(key: str, value: str) -> ExifValue:
    """Converts exif datetime/date/offsettime fields to datetime objects

    Value is converted to datetime, date or timedelta by following rules:
    - If `key` contains "datetime" convert `value` to 'datetime.datetime'
        (e.g. image.datetime, exif.datetimeoriginal, exif.datetimedigitized)
    - If `key` contains "date" convert `value` to 'datetime.date'
        (e.g. gps.date)
    - If `key` contains "offsettime" convert `value` to 'datetime.timedelta'
        (e.g. exif.offsettimeoriginal, exif.offsettimedigitized)
    - Otherwise `value` is not converted and returned as is

    Args:
        key (str): Key of entry in ExifDict
        value (str): Value of entry in ExifDict

    Returns:
        value (datetime | date | timedelta | str) :
            Value of entry in ExifDict converted to datetime, date or timedelta
            if applicable
    """
    try:
        converted_value: ExifValue = value
        if "datetime" in key:
            # value = "YYYY:MM:DD HH:MM:SS" --> convert to 'datetime.datetime'
            converted_value = datetime.strptime(value[:19], "%Y:%m:%d %H:%M:%S")
        elif "date" in key:
            # value = "YYYY:MM:DD" --> convert to datetime.date
            converted_value = datetime.strptime(value[:10], "%Y:%m:%d").date()
        elif "offsettime" in key:
            # value = "+HHMM" or "+HH:MM[:SS]" or "UTC+HH:MM[:SS]"
            # --> convert to 'datetime.timedelta'
            if value[:3].upper() == "UTC":
                # Remove UTC
                value = value[3:]
            converted_value = datetime.strptime(
                value.replace(":", ""), "%z"
            ).utcoffset() or timedelta(seconds=0)
        return converted_value
    except ValueError:
        return value


class Exif(Filter):
    """Filter by image EXIF data

    The `exif` filter can be used as a filter as well as a way to get exif information
    into your actions.

    Exif fields which contain "datetime", "date" or "offsettime" in their fieldname
    will have their value converted to 'datetime.datetime', 'datetime.date' and
    'datetime.timedelta' respectivly.
    - `datetime.datetime` : exif.image.datetime, exif.exif.datetimeoriginal, ...
    - `datetime.date` : exif.gps.date, ...
    - `datetime.timedelta` : exif.exif.offsettimeoriginal, exif.exif.offsettimedigitized, ...

    Returns:
        ``{exif}``:
            a dict of all the collected exif inforamtion available in the
            file. Typically it consists of the following tags (if present in the file):

            - `{exif.image}`: information related to the main image
            - `{exif.exif}`: Exif information
            - `{exif.gps}`: GPS information
            - `{exif.interoperability}`:  Interoperability information
    """

    name = "exif"
    arg_schema = None
    schema_support_instance_without_args = True

    def __init__(self, *required_tags: str, **tag_filters: str) -> None:
        self.args = required_tags  # expected exif keys
        self.kwargs = tag_filters  # exif keys with expected values

    def category_dict(self, tags: Mapping[str, str]) -> ExifDict:
        result = collections.defaultdict(dict)  # type: DefaultDict
        for key, value in tags.items():
            if " " in key:
                category, field = key.split(" ", maxsplit=1)
                result[category][field] = to_datetime(field, value)
            else:
                result[key] = to_datetime(key, value)
        return dict(result)

    def matches(self, exiftags: dict) -> bool:
        if not exiftags:
            return False
        tags = {k.lower(): v for k, v in exiftags.items()}

        # no match if expected tag is not found
        normkey = lambda k: k.replace(".", " ").lower()
        for key in self.args:
            if normkey(key) not in tags:
                return False
        # no match if tag has not expected value
        for key, value in self.kwargs.items():
            key = normkey(key)
            if not (key in tags and tags[key].lower() == value.lower()):
                return False
        return True

    def pipeline(self, args: dict) -> FilterResult:
        fs = args["fs"]
        fs_path = args["fs_path"]
        with fs.openbin(fs_path) as f:
            exiftags = exifread.process_file(f, details=False)

        tags = {k.lower(): v.printable for k, v in exiftags.items()}
        matches = self.matches(tags)
        exif_result = self.category_dict(tags)

        return FilterResult(
            matches=matches,
            updates={self.get_name(): exif_result},
        )

    def __str__(self) -> str:
        return "EXIF(%s)" % ", ".join("%s=%s" % (k, v) for k, v in self.kwargs.items())
