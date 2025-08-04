from google.adk.agents import Agent
from car_inventory_agent.agent import car_inventory_agent
from car_booking_agent.agent import car_booking_agent
from google.adk.models.lite_llm import LiteLlm


root_agent = Agent(
    model=LiteLlm('openai/gpt-4.1'),
    name='root_agent',
    description='An agent that runs the overall operations of a car rental company.',
    instruction="""
Your task is to manage the car rental company. Use the available tools to perform 
the following actions:

- Review the cars in the parking lot
- Create a list of car objects
- Book car rentals
    """,
    sub_agents=[car_inventory_agent, car_booking_agent]
)