
from agent import agent


def print_agent_steps(result):
    print("\n" + "=" * 70)
    print("AGENT EXECUTION TRACE")
    print("=" * 70)

    messages = result["messages"]


    print("\n" + "=" * 70)
    print(messages)
    print("=" * 70)
    

    for i, message in enumerate(messages):

        print(f"\n--- MESSAGE {i + 1} ---")
        print("TYPE:", type(message).__name__)

        # AI message
        if type(message).__name__ == "AIMessage":

            print("CONTENT:", message.content)

            if message.tool_calls:
                print("\nTOOL CALLS:")

                for tool_call in message.tool_calls:
                    print("  Tool:", tool_call["name"])
                    print("  Arguments:", tool_call["args"])

        # Tool message
        elif type(message).__name__ == "ToolMessage":

            print("TOOL RESULT:")
            print(message.content)

    print("\n" + "=" * 70)


while True:

    user_input = input("\nYou: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        }
    )

    print_agent_steps(result)



# OpenAI       → some provider-specific fields
# Groq         → reasoning_content
# Anthropic    → different metadata
# Google       → different metadata
