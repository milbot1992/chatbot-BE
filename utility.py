import os
import openai
import re

from dotenv import load_dotenv, find_dotenv
from keywords import prompt_allowed, closing_terms

_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv('GPT_API_KEY')

def is_prompt_allowed(prompt):
    pattern = re.compile('|'.join(prompt_allowed), re.IGNORECASE)
    return bool(pattern.search(prompt))

def is_closing_text(prompt):
    pattern = re.compile('|'.join(closing_terms), re.IGNORECASE)
    return bool(pattern.search(prompt))

## Helper function
def get_completion(prompt, model="gpt-3.5-turbo", temperature=0):
    message = [{"role": "user",
                "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        message=message,
        temperature=temperature,
    )
    return response.choices[0].message["content"]


## Helper function for conversation
def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
    )
    return response.choices[0].message["content"]


def collect_messages(prompt: str, context: list, temperature=0):
    if not is_prompt_allowed(prompt):
        context.append({'role': 'user', 'content': f'{prompt}'})
        response = "Sorry, I am a fitness chatbot - please ask me a fitness related question."
        context.append({'role': 'assistant', 'content': f'{response}'})
    elif is_closing_text(prompt):
        context.append({'role': 'user', 'content': f'{prompt}'})
        response = 'Do you have any further questions?'
        context.append({'role': 'assistant', 'content': f'{response}'})
    else:
        context.append({'role': 'user', 'content': f'{prompt}'})
        response = get_completion_from_messages(context, temperature=temperature)
        context.append({'role': 'assistant', 'content': f'{response}'})

    return {'context': context}