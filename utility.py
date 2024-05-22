import os
import openai
import re

from dotenv import load_dotenv, find_dotenv
from keywords import prompt_allowed

_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv('GPT_API_KEY')

def is_fitness_related(prompt):
    pattern = re.compile('|'.join(prompt_allowed), re.IGNORECASE)
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
    context.append({'role': 'user', 'content': prompt})

    # Check if the prompt or context is fitness-related
    full_context_text = ' '.join([msg['content'] for msg in context])
    if not is_fitness_related(full_context_text):
        response = "Sorry, I am a fitness chatbot - please ask me a fitness related question."
    else:
        response = get_completion_from_messages(context, temperature=temperature)
        context.append({'role': 'assistant', 'content': response})

    return {'context': context}