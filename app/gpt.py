import os
import openai

from dotenv import load_dotenv

load_dotenv()

GPT_API_KEY = os.getenv('GPT_API_KEY')
openai.api_key = GPT_API_KEY

def gpt_response(question):
  res = openai.Completion.create(
    model='text-davinci-003',
    prompt=question,
    temperature=0.7,
    max_tokens=1000
  )
  return res.choices[0].text if len(res.choices) > 0 else "GPT does not response T_T"
