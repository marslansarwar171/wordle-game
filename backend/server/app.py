import os
from fastapi import FastAPI, Body, status
from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, EmailStr
from dotenv import load_dotenv, find_dotenv
from bson import ObjectId
from typing import List
from motor.motor_asyncio import AsyncIOMotorClient
import uvicorn

load_dotenv(find_dotenv())
client: AsyncIOMotorClient = None
db = None

def connect_db():
    global client
    global db
    client = AsyncIOMotorClient(os.environ["MONGODB_URI"])
    db = client["wordle-db"]

def close_db():
    client.close()

app = FastAPI()
app.add_event_handler("startup", connect_db)
app.add_event_handler("shutdown", close_db)

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")

class WordleModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    word: str = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "word": "apple",
            }
        }

@app.post("/add-wordle/", response_description="Add new wordle", response_model=WordleModel)
async def create_wordle(wordle: WordleModel = Body(...)):
    wordle = jsonable_encoder(wordle)
    new_wordle = await db["wordles"].insert_one(wordle)
    created_wordle = await db["wordles"].find_one({"_id": new_wordle.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_wordle)


@app.get("/wordle-list/", response_description="List all wordles", response_model=List[WordleModel])
async def list_wordles():
    wordles = await db["wordles"].find().to_list(100)
    return wordles


if __name__ == "__main__":
  uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=true)
