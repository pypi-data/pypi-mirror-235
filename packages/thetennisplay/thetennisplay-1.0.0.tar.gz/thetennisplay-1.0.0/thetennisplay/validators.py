"""
Input validation functions for user-provided data.
"""
from datetime import datetime
from typing import Optional

import typer


def validate_date(date: str):
    """
    Validate the user-provided date in the YYYY-MM-DD format.

    Args:
        date (str): The date string to validate.

    Returns:
        str: The valid date string.

    Raises:
        typer.BadParameter: If the date is not in the proper format.
    """
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return date
    except ValueError as exc:
        raise typer.BadParameter("Please follow the format YYYY-MM-DD") from exc


def validate_refresh_rate(value: int):
    """
    Validate the refresh rate, ensuring it is at least 5 seconds.

    Args:
        value (int): The refresh rate value to validate.

    Returns:
        int: The valid refresh rate value.

    Raises:
        typer.BadParameter: If the refresh rate is less than 5 seconds.
    """
    if value >= 5:
        return value
    raise typer.BadParameter("The refresh rate must be at least 5 seconds")


def validate_hour(value: Optional[str]):
    """
    Validate the user-provided hour format.

    Args:
        value (Optional[str]): The hour value to validate.

    Returns:
        Optional[Tuple[int, int]]: A valid hour range represented as a tuple.

    Raises:
        typer.BadParameter: If the hour is not in the proper format or represents an invalid range.
    """
    if value is None:
        return value
    if len(value.split("-")) == 2:
        duration = tuple(map(int, value.split("-")))
        if duration[0] > duration[1]:
            raise typer.BadParameter("The start time cannot be after the end time")
        return duration

    if value.isdigit() and 0 <= int(value) <= 24:
        value = int(value)
        return (value, value)
    raise typer.BadParameter("Please enter the hour in the correct format")
