from langchain.agents.agent_toolkits import create_csv_agent
from langchain.llms import OpenAI


llm = OpenAI(temperature=0.9, openai_api_key="YOUR-API-KEY")


agent_executor = create_csv_agent(llm, 'hotel_bookings.csv', verbose=True)


while True:
    text = input("USER: ")


    if text == "EXIT":
        print("Exiting the program...")
        break

    print("Bot: ", agent_executor.run(text)) 
