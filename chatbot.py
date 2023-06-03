from langchain.llms import OpenAI
from langchain.agents import create_csv_agent


agent = create_csv_agent(OpenAI(temperature=0), 'titanic.csv', verbose=True)

openai_api_key="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"


while True:
    user_input = input("USER: ")


    if user_input == "EXIT":
        print("Exiting the program...")
        break

    # Perform the desired operation based on the input
    # Add your own logic here
    agent.run(user_input)

print("Program terminated.")