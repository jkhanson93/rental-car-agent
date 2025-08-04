from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.tool_context import ToolContext
from pydantic import BaseModel


def damage_function(tool_context: ToolContext, license_plate: str, damage_classification: str) -> dict:
    inventory = tool_context.state.get("Inventory")
    print("*************", type(inventory), inventory)
    for car in inventory["car"]:
        print("***************", car["damage"], type(car["damage"]), car["license"])
        if car["license"] == license_plate and car["availability"] == False:
            car["damage"] = damage_classification
            if damage_classification in ["NONE", "MINOR"]:
                car["availability"] = True
            tool_context.state["Inventory"] = inventory
            return {"status": "Success! You've updated this car.", "Inventory": inventory}
    
    return {"status": "This car is not in the inventory."}


car_damage_agent = Agent(
    model=LiteLlm('openai/gpt-4.1'),
    name='car_damage_agent',
    description='A helpful assistant for assessing and updating car damage.',
    instruction="""Classify the damage in this image as NONE, MINOR, MODERATE, or SEVERE. Then, use the damage function to update the inventory with your classification.  Print the updated inventory with the structure inside <format> and </format>

    <format>
    license: str
    make: str
    model: str
    year: int
    seats: int
    color: str
    availability: bool
    damage: str'
    </format>
    
    """,
    tools = [damage_function]
)
