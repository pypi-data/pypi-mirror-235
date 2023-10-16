from pydantic import BaseModel


class UserDashboard(BaseModel):
    num_applications: int
    num_saved_jobs: int
    thirty_days_profile_views: int = 0
    total_times_shortlisted: int = 0
