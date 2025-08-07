from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.tool_context import ToolContext
from pydantic import BaseModel


def damage_function(tool_context: ToolContext, license_plate: str, damage_classification: str) -> dict:
    """
    The damage function employs the car_damage_agent to assess the damage of any vehicle that is being returned,
    and therefore matches the license plate of a car that is marked unavailable. If the damage is non-existent or
    minor, it will be added into the inventory for the next renter. Otherwise, it will remain unavailable to the public.
    For all cars, the 'damage' field will be updated to match the result of the assessment.
    """
    inventory = tool_context.state.get("Inventory")
    print("*************", type(inventory), inventory)
    for car in inventory["car"]:
        print("***************", car["damage"], type(car["damage"]), car["license"])
        if car["license"] == license_plate and car["availability"] == False:
            car["damage"] = damage_classification
            if damage_classification in ["none", "minor"]:
                car["availability"] = True
            tool_context.state["Inventory"] = inventory
            return {"status": "Success! You've updated this car.", "Inventory": inventory}
    
    return {"status": "This car is not in the inventory."}


car_damage_agent = Agent(
    model=LiteLlm('openai/gpt-4.1'),
    name='car_damage_agent',
    description='A helpful assistant for assessing and updating car damage.',
    instruction="""Classify the damage in this image as none, minor, moderate, or severe. Then, use the damage function to update the inventory with your classification.  Print the full, accurate, updated inventory with all fields. If the damage is not none, provide a cost estimate for repairs.
    
    """,
    tools = [damage_function]
)
 

