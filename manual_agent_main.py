
from agent_manual import run_agent


while True:

    user_input = input("\nYou: ")

    if user_input.lower() in ["exit", "quit"]:
        break

    answer = run_agent(user_input)

    print("\nAgent:")
    print(answer)