import argparse
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
load_dotenv("./api_key.env")


api_key = os.environ.get("GEMINI_API_KEY")
if api_key == None:
    raise RuntimeError("API key not set")


parser = argparse.ArgumentParser(description="AI Agent")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
parser.add_argument("user_prompt", type=str, help="Write a prompt")
args = parser.parse_args()


messages: list[types.Content] = [
    types.Content(role="user", parts=[types.Part(text=args.user_prompt)])
]


def main():
    
    client = genai.Client(api_key=api_key)
    
    response = client.models.generate_content(model="gemini-2.5-flash",contents=messages)
    
    if response.usage_metadata.candidates_token_count == None:
        raise RuntimeError("Something went wrong when generating response")
    
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
    
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
    print(f"Response:\n{response.text}")


if __name__ == "__main__":
    main()