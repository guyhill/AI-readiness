from openai import OpenAI
from google import genai
from datetime import datetime
import sys

def query_chatgpt(model, instructions, prompt):

    client = OpenAI()

    prompt_time = datetime.now().isoformat()

    response_text = ""
    exception_text = ""
    try:
        response = client.responses.create(
            model=model,
            instructions=instructions,
            input=prompt
        )
        response_text = response.output_text
    except:
        exception_text = repr(sys.exception())

    response_time = datetime.now().isoformat()

    return {
        "provider": model,
        "instructions": instructions,
        "prompt": prompt,
        "response": response_text,
        "exception": exception_text,
        "prompt_time": prompt_time,
        "response_time": response_time
    }

def query_gemini(model, instructions, prompt):

    client = genai.Client()
    chat = client.chats.create(
        model=model,
        config=genai.types.GenerateContentConfig(system_instruction=instructions),
    )

    prompt_time = datetime.now().isoformat()

    response_text = ""
    exception_text = ""
    try:
        response = chat.send_message(prompt)
        response_text = response.text
    except:
        exception_text = repr(sys.exception())

    response_time = datetime.now().isoformat()

    return {
        "provider": model,
        "instructions": instructions,
        "prompt": prompt,
        "response": response_text,
        "exception": exception_text,
        "prompt_time": prompt_time,
        "response_time": response_time
    }

def query(model, instructions, prompt):
    if model.startswith("gemini"):
        return query_gemini(model, instructions, prompt)
    elif model.startswith("gpt"):
        return query_chatgpt(model, instructions, prompt)
    else:
        raise Exception(f"Unknown model {model}")
