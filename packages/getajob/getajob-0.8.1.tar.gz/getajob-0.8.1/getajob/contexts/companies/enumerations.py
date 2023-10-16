from enum import Enum


class NumEmployeesEnum(str, Enum):
    one_to_ten = "1-10"
    eleven_to_fifty = "11-50"
    fiftyone_to_twohundred = "51-200"
    twohundredone_to_fivehundred = "201-500"
    fivehundredone_to_onethousand = "501-1000"
    morethan_onethousand = "1001+"


class ExperienceLevel(str, Enum):
    no_experience = "No Experience"
    under_one_year = "Under 1 Year"
    one_year = "1 Year"
    two_years = "2 Years"
    three_years = "3 Years"
    five_years = "5 Years"
    ten_years = "10 Years"
    eleven_or_more_years = "11+ Years"


class ScheduleType(str, Enum):
    FULL_TIME = "Full Time"
    PART_TIME = "Part Time"
    CONTRACT = "Contract"
    TEMPORARY = "Temporary"
    SEASONAL = "Seasonal"
    INTERNSHIP = "Internship"


class WeeklyScheduleType(str, Enum):
    monday_to_friday = "Monday to Friday"
    weekends_as_needed = "Weekends as Needed"
    every_weekend = "Every Weekend"
    no_weekends = "No Weekends"
    rotating_weekends = "Rotating Weekends"
    weekends_only = "Weekends Only"
    other = "Other"
    none = "None"


class ShiftType(str, Enum):
    morning = "Morning"
    day = "Day"
    evening = "Evening"
    night = "Night"
    eight_hour = "8 Hour"
    ten_hour = "10 Hour"
    twelve_hour = "12 Hour"
    other = "Other"
    none = "None"


class JobLocationType(str, Enum):
    REMOTE = "Remote"
    WITHIN_TEN_MILES = "Within 10 Miles"
    WITHIN_FIFTY_MILES = "Within 50 Miles"
    WITHIN_ONE_HUNDRED_MILES = "Within 100 Miles"
    ON_THE_ROAD = "On the Road"
    HYBRID = "Hybrid"


class JobContractLength(str, Enum):
    SHORT_TERM = "Short Term"
    LONG_TERM = "Long Term"


class PayType(str, Enum):
    HOURLY = "Hourly"
    DAILY = "Daily"
    WEEKLY = "Weekly"
    MONTHLY = "Monthly"
    YEARLY = "Yearly"


class ResumeRequirement(str, Enum):
    required = "Required"
    optional = "Optional"
    no_resume = "No Resume"


class Benefits(str, Enum):
    medical = "Medical"
    dental = "Dental"
    vision = "Vision"
    four_one_k = "401K"
    maternity_leave = "Maternity Leave"
    paternity_leave = "Paternity Leave"
    bereavement_leave = "Bereavement Leave"
    profit_sharing = "Profit Sharing"
    stock_options = "Stock Options"
    team_building_events = "Team Building Events"
    bonuses = "Bonuses"
