#Note: The openai-python library support for Azure OpenAI is in preview.
      #Note: This code sample requires OpenAI Python library version 1.0.0 or higher.
import os
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AzureOpenAI(
  azure_endpoint = "https://wolfai.openai.azure.com/", 
  api_key=os.getenv("OPENAI_API_KEY"),  
  api_version="2024-02-15-preview"
)

deployment_name = "gpt-35"

message_text = [{"role":"system","content":"You are an AI assistant that helps people find information."}]
start_phrase = 'Write a tagline for Wing Chun martial arts.  '

completion = client.chat.completions.create(
  model="gpt-35", # model = "deployment_name"
  messages = message_text,
  temperature=0.7,
  max_tokens=800,
  top_p=0.95,
  frequency_penalty=0,
  presence_penalty=0,
  stop=None
)

print('Sending a test completion job')
response = client.completions.create(model=deployment_name, prompt=start_phrase, max_tokens=10)
print(start_phrase+response.choices[0].text)

