import os
import openai
import re

from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

openai.api_key = os.getenv('GPT_API_KEY')

# Initial list of fitness-related keywords
fitness_keywords = [
    'exercise', 'workout', 'diet', 'nutrition', 'calories', 
    'fitness', 'strength', 'training', 'weight', 'muscle', 
    'cardio', 'protein', 'health', 'lifestyle', 'gym', 
    'push-ups', 'push ups', 'plank', 'squat', 'lunges', 
    'deadlift', 'bench press', 'burpees', 'cycling', 
    'running', 'jogging', 'swimming', 'yoga', 'pilates', 
    'aerobics', 'zumba', 'crossfit', 'HIIT', 'stretching', 
    'recovery', 'wellness', 'hydration', 'macros', 'micros', 
    'football', 'soccer', 'basketball', 'baseball', 
    'tennis', 'badminton', 'volleyball', 'netball', 
    'cricket', 'rugby', 'hockey', 'golf', 'boxing', 
    'martial arts', 'karate', 'taekwondo', 'judo', 
    'ballet', 'dance', 'rowing', 'canoeing', 'kayaking', 
    'rock climbing', 'hiking', 'trail running', 'triathlon', 
    'ironman', 'marathon', 'sprint', 'skipping', 
    'jump rope', 'sled push', 'mountain climbers', 
    'bodybuilding', 'powerlifting', 'calisthenics', 
    'gymnastics', 'parkour', 'surfing', 'skateboarding', 
    'snowboarding', 'skiing', 'diving', 'snorkeling', 
    'fencing', 'archery', 'equestrian', 'horse riding', 
    'handball', 'softball', 'lacrosse', 'pickleball', 
    'paddleboarding', 'sailing', 'windsurfing', 'parasailing', 
    'motocross', 'BMX', 'strength training', 'conditioning', 
    'personal training', 'group fitness', 'meditation', 
    'mindfulness', 'breathing exercises'
]


def is_fitness_related(prompt):
    pattern = re.compile('|'.join(fitness_keywords), re.IGNORECASE)
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