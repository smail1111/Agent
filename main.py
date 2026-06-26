import argparse
import sys
import os
from dotenv import load_dotenv
from google import genai
from prompts import system_prompt
from google.genai import types
from functions.functions_info import available_functions
from functions.call_function import call_function

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
    
    for i in range(0,10):
        
        response = client.models.generate_content(model="gemini-2.5-flash",contents=messages,
            config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
            )
    
        if not response.usage_metadata.candidates_token_count:
            raise RuntimeError("Something went wrong when generating response")
    
        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
    
            print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    
            print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        
        if response.candidates:
            for canditate in response.candidates:
                messages.append(canditate.content)
        
        results = []
    
        if response.function_calls:
            for call in response.function_calls:
            
                result = call_function(call)
            
                if not result.parts:
                    raise Exception("No parts")
                if not result.parts[0].function_response:
                    raise Exception("No function response")
                if not result.parts[0].function_response.response:
                    raise Exception("No response")
            
                results.append(result.parts[0])
            
                if args.verbose:
                    print(f"-> {result.parts[0].function_response.response}")

                messages.append(types.Content(role="user", parts=results))
            

        else:
            print(f"Response:\n{response.text}")
            return

    print("Max iterations reached")
    sys.exit(1)

if __name__ == "__main__":
    main()