"""
An Enum class representing available tennis court locations for reservations.
"""
from enum import Enum


class Court(str, Enum):
    """
    Enum class for tennis court locations.

    Attributes:
        - BANPO: Represents "반포종합운동장 테니스장."
        - DONGJAK: Represents "동작주차공원 테니스장."

    Methods:
        - to_xpath(court: Enum): Returns an XPath query for an HTML element based on the court's value.
    """

    BANPO = "반포종합운동장 테니스장"
    DONGJAK = "동작주차공원 테니스장"

    @staticmethod
    def to_xpath(court: Enum):
        """Return XPath for HTML element."""
        return f"//div[./h1/text()='{court.value}']"
