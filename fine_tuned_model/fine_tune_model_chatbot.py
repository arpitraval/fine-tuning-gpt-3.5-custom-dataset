from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

model_name = "ft:gpt-3.5-turbo-0613:personal::7qZjgwWl"
chat = ChatOpenAI(model=model_name)

messages = [
    HumanMessage(content="How many calories are there in a slice of watermelon?")
]

response = chat(messages)
print(response.content)