from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from openai import OpenAI
import base64
from pydantic import BaseModel
import json

class Car(BaseModel):
    license: str
    make: str
    model: str
    year: int
    seats: int
    color: str
    availability: bool
    damage: str


class Inventory(BaseModel):
    car: list[Car]


car_inventory_agent = Agent(
    model=LiteLlm('openai/gpt-4.1'),
    name='car_inventory_agent',
    description='A helpful assistant for processing parking lot images.',
    instruction='Count the number of cars in the photo. For each car, create a car object and fill in the license plate number, make, model, year, seats, and color. If a value is unknown, generate a reasonable placeholder for that value. Make sure there are no blank values.  All availability is True.  All damage is none.',
    output_schema=Inventory,
    output_key="Inventory"
)