"""
These might be better suited as a database table, or even just json files locally
"""

from enum import Enum


class PayEnum(str, Enum):
    HOURLY = "Hourly"
    WEEKLY = "Weekly"
    BI_WEEKLY = "Bi-weekly"
    MONTHLY = "Monthly"
    ANNUALLY = "Annually"


class WorkSettingEnum(str, Enum):
    REMOTE = "Remote"
    IN_PERSON = "In-person"
    HYBRID = "Hybrid"
    TEMPORARILY_REMOTE = "Temporarily Remote"


class IndustryEnum(str, Enum):
    TECHNOLOGY = "Technology"
    FINANCE = "Finance"
    HEALTHCARE = "Healthcare"
    EDUCATION = "Education"
    GOVERNMENT = "Government"
    RETAIL = "Retail"
    HOSPITALITY = "Hospitality"
    CONSTRUCTION = "Construction"
    MANUFACTURING = "Manufacturing"


class JobTypeEnum(str, Enum):
    FULL_TIME = "Full-time"
    PART_TIME = "Part-time"
    CONTRACT = "Contract"
    TEMPORARY = "Temporary"
    INTERNSHIP = "Internship"
    VOLUNTEER = "Volunteer"


class LanguageEnum(str, Enum):
    ENGLISH = "English"
    SPANISH = "Spanish"
    FRENCH = "French"
    GERMAN = "German"
    MANDARIN = "Mandarin"
    JAPANESE = "Japanese"
    KOREAN = "Korean"
    ARABIC = "Arabic"
