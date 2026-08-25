import os
import json

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


SYSTEM_PROMPT = """
You are a Linux command understanding assistant.

Your job is ONLY to understand the user's request and select
one safe command from the allowed commands below.

Allowed commands:
- ls
- pwd
- whoami
- uname
- df -h
- free -h
- uptime
- date
- hostname
- ps aux --sort=-%cpu
- ps aux --sort=-%mem
Never create or suggest commands outside this list.

Return ONLY valid JSON in this format:

{
    "intent": "short description",
    "command": "allowed command",
    "confidence": 0.0
}

The confidence must be between 0 and 1.
"""


def understand_query(query: str):

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": query
            }
        ],
        temperature=0
    )

    content = response.choices[0].message.content.strip()

    try:
        result = json.loads(content)

        return {
            "success": True,
            "query": query,
            "intent": result.get("intent"),
            "command": result.get("command"),
            "confidence": result.get("confidence")
        }

    except json.JSONDecodeError:

        return {
            "success": False,
            "query": query,
            "message": "AI returned an invalid response."
        }