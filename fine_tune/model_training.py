import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
file_id = "file-s9BnQ6r8JaGN6KgKUihqMmNc"

response = openai.FineTuningJob.create(training_file=file_id, 
model="gpt-3.5-turbo")
print(response)