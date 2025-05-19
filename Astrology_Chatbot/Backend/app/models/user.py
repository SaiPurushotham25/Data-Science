from pydantic import BaseModel

class UserInput(BaseModel):
    date_of_birth: str
    time_of_birth: str
    place_of_birth: str
    question: str