
from fastapi import APIRouter
from app.models.user import UserInput
from app.core.astro import  fetch_astrology_data
from app.core.LLM import interpret_with_llm
from app.Database.storage import store_log

router = APIRouter()



@router.post("/Chatbot")
def interpret(user: UserInput):
    planets = fetch_astrology_data(user.date_of_birth, user.time_of_birth, user.place_of_birth)
    response = interpret_with_llm(user.question, planets)
    store_log(user, planets, response)
    return {"response": response}

