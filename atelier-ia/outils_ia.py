# outils_ia.py = fonction ask à utiliser pour tout le projet

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

GEMINI_MODEL = "gemini-3.1-flash-lite"

def ask(prompt, system=None, temperature=0.2, max_tokens=1024):
    client = genai.Client(
        api_key=os.environ["GEMINI_API_KEY"]
    )

    config = types.GenerateContentConfig(
        system_instruction=system,
        temperature=temperature,
        max_output_tokens=max_tokens
    )

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
        config=config
    )

    return response.text or ""
