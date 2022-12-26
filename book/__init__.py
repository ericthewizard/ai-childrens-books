import os
import logging
import openai

KEY = os.getenv('OPENAI_API_KEY')

if KEY is None:
    logging.error('Can not find API key; please set the "OPENAI_API_KEY" environment variable and restart.')
    breakpoint()

openai.api_key = KEY
logging.basicConfig(format='%(asctime)s: %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO)


def write(concept,
          age=5,
          temperature=0.9,
          max_tokens=1024,
          top_p=1.0,
          frequency_penalty=0.0,
          presence_penalty=0.0,
          best_of=3,
          save=None
          ):
    if not isinstance(age, str):
        age = str(age)
    prompt = "We're going to write a children's book. The reader age is " + age + ". The concept is: " + concept + '\n\n'
    prompt += 'First draft of our book:\n'
    return call_api(prompt,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    top_p=top_p,
                    frequency_penalty=frequency_penalty,
                    presence_penalty=presence_penalty,
                    best_of=best_of,
                    save=save)


def ideas(concept,
          age=5,
          temperature=0.9,
          max_tokens=256,
          top_p=1.0,
          frequency_penalty=0.0,
          presence_penalty=0.0,
          best_of=3,
          save=None):
    if not isinstance(age, str):
        age = str(age)
    prompt = "We're going to write a children's book. The reader age is " + age + ". The concept is: " + concept + '\n\n'
    prompt += 'Bulleted list of ideas for our book:\n'
    return call_api(prompt,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    top_p=top_p,
                    frequency_penalty=frequency_penalty,
                    presence_penalty=presence_penalty,
                    best_of=best_of,
                    save=save)


def call_api(prompt,
             temperature,
             max_tokens,
             top_p,
             frequency_penalty,
             presence_penalty,
             best_of,
             save=None):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=temperature,
        max_tokens=int(max_tokens),
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        best_of=best_of
    )

    output = response['choices'][0]['text']

    if save is not None:
        with open(save, 'w') as f:
            f.write(output)

    return output
