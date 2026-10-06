from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_groq import ChatGroq

from tools import (
    get_weather,
    get_stock_price,
    search_web,
)

load_dotenv()

tools = [
    get_weather,
    get_stock_price,
    search_web,
]

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
)

agent = create_agent(
    model=model,
    tools=tools,
    system_prompt="""
You are a helpful personal assistant.

You have access to three tools:

1. get_weather
   Use this for current weather information.

2. get_stock_price
   Use this for current stock prices.

3. search_web
   Use this when the user needs current information
   or information that you don't know.

Choose the appropriate tool based on the user's request.

You may call multiple tools if necessary.

After getting the required information, provide a concise
answer to the user.
""",
)
