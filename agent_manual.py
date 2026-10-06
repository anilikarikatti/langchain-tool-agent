
from langchain_groq import ChatGroq

from langchain_core.messages import ToolMessage

from tools import (
    get_weather,
    get_stock_price,
    search_web
)


# --------------------------------------------------
# 1. Create the LLM
# --------------------------------------------------

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0,
)

# --------------------------------------------------
# 2. Register tools
# --------------------------------------------------

tools = [
    get_weather,
    get_stock_price,
    search_web
]


# --------------------------------------------------
# 3. Give tools to the LLM
# --------------------------------------------------

model_with_tools = model.bind_tools(tools)


# --------------------------------------------------
# 4. Create tool registry
# --------------------------------------------------

tool_map = {
    tool.name: tool
    for tool in tools
}


# --------------------------------------------------
# 5. Manual Agent Loop
# --------------------------------------------------

def run_agent(user_input: str):

    messages = [
        {
            "role": "user",
            "content": user_input
        }
    ]

    while True:

        print("\n>>> Calling LLM...")

        # Ask the LLM what to do
        response = model_with_tools.invoke(messages)

        # Store LLM response
        messages.append(response)

        print("LLM response received.")

        # --------------------------------------------------
        # No tool required → final answer
        # --------------------------------------------------

        if not response.tool_calls:

            print("\n>>> Agent finished.")

            return response.content

        # --------------------------------------------------
        # Tool required
        # --------------------------------------------------

        print(
            f">>> LLM requested "
            f"{len(response.tool_calls)} tool(s)"
        )

        for tool_call in response.tool_calls:

            tool_name = tool_call["name"]
            tool_args = tool_call["args"]

            print(
                f"\n>>> Executing tool: {tool_name}"
            )

            print(
                f">>> Arguments: {tool_args}"
            )

            # Find the actual Python function
            tool = tool_map[tool_name]

            # Execute the function
            tool_result = tool.invoke(tool_args)

            print(
                f">>> Tool result: {tool_result}"
            )

            # --------------------------------------------------
            # Send tool result back to LLM
            # --------------------------------------------------

            tool_message = ToolMessage(
                content=str(tool_result),
                tool_call_id=tool_call["id"]
            )

            messages.append(tool_message)




  