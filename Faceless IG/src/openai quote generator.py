import openai
import os
from openai import OpenAI


client = OpenAI(
  organization='org-3Dfx5xAWObkJGK4nMEsd0Roz',
  project='proj_Lc6g1OgKOXo6KSeb1cRjE8OI',
  api_key = openai.api_key
  
)


def generate_spiritual_quote():
    try:
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "developer", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Give me a quote from a spiritual guru. Just give the quote and the name of the guru, with no  additional explanation"}
            ]
        )
        return completion.choices[0].message
    except Exception as e:
        print("Error generating quote:", e)
        return None

if __name__ == "__main__":
    quote = generate_spiritual_quote()
    if quote:
        print("Generated Quote:", quote)
    else:
        print("Failed to generate quote.")
import sys
from dotenv import load_dotenv
import os
# Load environment variables from .env file
load_dotenv()
print("Python executable:", sys.executable)
print("Current working directory:", os.getcwd())
print("sys.path:", sys.path)
import openai

from openai import OpenAI

# Keys stored as env variables for security purposes
api_key = os.environ.get("OPENAI_API_KEY")
oai_org = os.environ.get("OPENAI_ORGANIZATION")
oai_proj = os.environ.get("OPENAI_PROJECT")
if api_key is None:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")



client = openai.OpenAI(
  organization= oai_org, 
  project=oai_proj,
  api_key = api_key
  
)

spiritual_teachers = [
        "Neville Goddard", "Buddha", "Jesus", "Robert Hawkins", "Eckhart Tolle", 
        "Raam Daas","Florence Scovel Shinn"
    ]
selected_teacher = random.choice(spiritual_teachers)


def generate_spiritual_quote():
    try:
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "developer", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Give me a short, impactful quote from {selected_teacher}. Just 
provide the quote and the name of the guru, with no additional explanation."}
                ],
            temperature = .8
        )
        return completion.choices[0].message
    except Exception as e:
        print("Error generating quote:", e)
        return None

if __name__ == "__main__":
    quote = generate_spiritual_quote()
    if quote:
        print("Generated Quote:", quote)
    else:
        print("Failed to generate quote.")
