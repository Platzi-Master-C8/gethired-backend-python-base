
# Pydantic
from pydantic import BaseModel, Field


class HomeInput(BaseModel):

    name: str = Field(..., example="Carlos")
