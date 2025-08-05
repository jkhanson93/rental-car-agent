from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from openai import OpenAI
import base64
from pydantic import BaseModel
import json


car_display_inventory_agent = Agent(
    model=LiteLlm('openai/gpt-4.1'),
    name='car_display_inventory_agent',
    description='A helpful assistant that outputs the current inventory of the car rental company.',
    instruction="""
    Output the current car inventory in the parking lot from the
    information below:

    {Inventory}"""
)