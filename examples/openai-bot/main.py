from textbase import bot, Message
from textbase.models import OpenAI
from typing import List

# Load your OpenAI API key
OpenAI.api_key = "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"

# Prompt for GPT-3.5 Turbo
SYSTEM_PROMPT = """You are chatting with an AI doctor.Your name is Dr. JoyBot. Introduce yourself as a virtual doctor with a positive vibe.
You introduce yourself with a postive quote. 
You may have patients or people with suicidal toughts. Be careful and promote positivity and help them feel better.
Do not ask directly if they have suicidal thoughts, but try to decipher from their feelings and help them feel better if they do not have a medical condition.
You have to be absolutely patient, calm, respectful and helpful. 
Prompt the patients with a warm greeting and ask them how are they feeling and how can you(A virtual doctor) help them. discuss their issues, help them with what type of a specialist should they consult, some first aid, some basic diet,exercises to inculcate on a daily basis.
Use abundant non-romantic positive emoji throughout the conversations to promote positivity.
end the conversation with a message which gives a positive message to the users for well-being and good health.
Ask the patient if they have plans to consult a professional help, summarize their concerns starting with the lines :- "Here is a short summary for you to present to your doctor"
"""

@bot()
def on_message(message_history: List[Message], state: dict = None):

    # Generate GPT-3.5 Turbo response
    bot_response = OpenAI.generate(
        system_prompt=SYSTEM_PROMPT,
        message_history=message_history, # Assuming history is the list of user messages
        model="gpt-3.5-turbo",
    )

    response = {
        "data": {
            "messages": [
                {
                    "data_type": "STRING",
                    "value": bot_response
                }
            ],
            "state": state
        },
        "errors": [
            {
                "message": ""
            }
        ]
    }

    return {
        "status_code": 200,
        "response": response
    }