# Agent

This is my third Boot.Dev project.

I will be building an AI coding agent using Gemini-2.5-Flash that can

1. List files and directories
2. Read file contents
3. Execute Python files with optional arguments
4. Write or overwrite files

## How To Use

1. Clone repository

`gh repo clone smail1111/Agent`

2. Use your own API key

Create api_key.env and set GEMINI_API_KEY to your own API key.

3. Run main.py 

`python3 main.py "Your request"`

- Add `--verbose` toggle to recieve more information about token usage.

## Notes

* Your own API key is required for the agent to work.

* For safety precautions, the agent can only access files within the calculator directory.

* This should not be used as an actual AI coding agent for serious projects, as it does not have any safety guards that actual coding agents have.