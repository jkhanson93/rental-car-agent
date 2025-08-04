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


# <class 'dict'> {'car': [{'license': 'ABC1234', 'make': 'Toyota', 'model': 'Camry', 'year': 2016, 'seats': 5, 'color': 'black', 'availability': True}, {'license': 'XYZ5678', 'make': 'Honda', 'model': 'Accord', 'year': 2017, 'seats': 5, 'color': 'red', 'availability': True}, {'license': 'LMN9101', 'make': 'Chevrolet', 'model': 'Malibu', 'year': 2018, 'seats': 5, 'color': 'yellow', 'availability': True}, {'license': 'UVW3456', 'make': 'Ford', 'model': 'Focus', 'year': 2015, 'seats': 5, 'color': 'grey', 'availability': True}, {'license': 'QRS2345', 'make': 'Toyota', 'model': 'Corolla', 'year': 2019, 'seats': 5, 'color': 'white', 'availability': True}, {'license': 'DEF6789', 'make': 'Honda', 'model': 'Civic', 'year': 2016, 'seats': 5, 'color': 'blue', 'availability': True}, {'license': 'PQR1122', 'make': 'Nissan', 'model': 'Altima', 'year': 2017, 'seats': 5, 'color': 'black', 'availability': True}, {'license': 'JKL3344', 'make': 'Hyundai', 'model': 'Elantra', 'year': 2016, 'seats': 5, 'color': 'white', 'availability': True}, {'license': 'GHI4567', 'make': 'Mazda', 'model': 'Mazda3', 'year': 2018, 'seats': 5, 'color': 'silver', 'availability': True}, {'license': 'TUV6677', 'make': 'Volkswagen', 'model': 'Jetta', 'year': 2017, 'seats': 5, 'color': 'grey', 'availability': True}, {'license': 'ASD9087', 'make': 'Kia', 'model': 'Optima', 'year': 2016, 'seats': 5, 'color': 'black', 'availability': True}, {'license': 'ZXC1239', 'make': 'Ford', 'model': 'Fusion', 'year': 2015, 'seats': 5, 'color': 'white', 'availability': True}, {'license': 'RTY4532', 'make': 'Honda', 'model': 'Accord', 'year': 2018, 'seats': 5, 'color': 'blue', 'availability': True}, {'license': 'BNM7755', 'make': 'Chevrolet', 'model': 'Impala', 'year': 2017, 'seats': 5, 'color': 'silver', 'availability': True}, {'license': 'QWE8796', 'make': 'Toyota', 'model': 'Camry', 'year': 2016, 'seats': 5, 'color': 'black', 'availability': True}, {'license': 'HJK3347', 'make': 'Nissan', 'model': 'Altima', 'year': 2017, 'seats': 5, 'color': 'white', 'availability': True}]}













# from google.adk.agents import BaseAgent
# class BookingAgent(BaseAgent):
#     @override
#     async def _run_async_impl(self, ctx: InvocationContext) -> AsyncGenerator[Event, None]:
#         inventory = ctx.session.state.get('inventory', {})
#         invventory.list[3].available = False
#         #Save it back in state
#         ctx.session.state['inventory'] = inventory


# def search_flights(from_airport : str, to_airport : str, date_of_flight : str) -> dict:
#     """
#     Searches for available flights between two airports on a specified date.

#     Args:
#         from_airport (str): The IATA code or name of the departure airport.
#         to_airport (str): The IATA code or name of the destination airport.
#         date_of_flight (str): The date of the flight in 'YYYY-MM-DD' format.
#     Returns:
#         dict: A dictionary containing a list of available flights, where each flight is represented as a dictionary with keys:
#             - 'flight_number' (str): The flight's unique identifier.
#             - 'from' (str): The departure airport.
#             - 'to' (str): The destination airport.
#             - 'date' (str): The date of the flight.
#             - 'price' (float): The price of the flight.
#     """


#     return {
#         "flights": [
#             {
#                 "flight_number": "AB123",
#                 "from": from_airport,
#                 "to": to_airport,
#                 "date": date_of_flight,
#                 "price": 199.99
#             },
#             {
#                 "flight_number": "CD456",
#                 "from": from_airport,
#                 "to": to_airport,
#                 "date": date_of_flight,
#                 "price": 299.99
#             }
#         ]
#     }

# flight_search_agent = Agent(
#     model=LiteLlm(model="openai/gpt-4o"),
#     name='flight_search_agent',
#     description='An agent that helps with searching for flights.',
#     instruction='Use the available tools to search for flights.',
#     tools=[search_flights]
# )
