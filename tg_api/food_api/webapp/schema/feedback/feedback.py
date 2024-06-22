from pydantic import BaseModel


class FeedbackData(BaseModel):
    score: int
    description: str