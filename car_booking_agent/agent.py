from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools.tool_context import ToolContext
from pydantic import BaseModel


def booking_function(tool_context: ToolContext, license_plate: str) -> dict:
    inventory = tool_context.state.get("Inventory")
    print("*************", type(inventory), inventory)
    for car in inventory["car"]:
        print("***************", car["availability"], type(car["availability"]), car["license"])
        if car["license"] == license_plate and car["availability"]:
            car["availability"] = False
            tool_context.state["Inventory"] = inventory
            return {"status": "Success! You've booked this car."}
    
    return {"status": "This car is not available for rent."}


car_booking_agent = Agent(
    model=LiteLlm('openai/gpt-4.1'),
    name='car_booking_agent',
    description='A helpful assistant for booking car rentals.',
    instruction='Use available tools to book a car.',
    tools = [booking_function]
)