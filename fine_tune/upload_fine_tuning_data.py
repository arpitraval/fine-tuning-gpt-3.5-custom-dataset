import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.File.create(
  file=open("data/custom_vegetables_fruits_nutrient_dataset.jsonl", "rb"),
  purpose='fine-tune'
)

print(response)