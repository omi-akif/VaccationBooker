from langchain.llms import OpenAI
from langchain.agents import create_csv_agent

# import os
# os.environ["OPENAI_API_KEY"] = "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"


agent = create_csv_agent(OpenAI(temperature=0.9), 'hotel_bookings.csv', verbose=True)


while True:
    user_input = input("USER: ")


    if user_input == "EXIT":
        print("Exiting the program...")
        break

    # Perform the desired operation based on the input
    # Add your own logic here
    agent.run(user_input)

print("Program terminated.")