import os
from openai import OpenAI





gold = 20
OPENAI_API_KEY = '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'

# template = """
# You are a merchant selling to a traveler named Ren. You sell 4 items with prices varying from 1 gold to 20 gold.
# Everytime Ren ask you whats for sale you give me a list of what your selling and for how much.
# You can sell me anything from the most extravagent mythical magical things to useless garbage.

# here are the rules to follow:
# 1. Only reveal your shop after the player ask for it.
# 2. change the shop each time player asks for it.
# 3. Don't sell the player anything he can't afford.

# Here is the amount of gold the player owns: {gold}
# """

client = OpenAI(
    api_key=OPENAI_API_KEY
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": 'user',
            'content': """You are a merchant selling to a traveler named Ren. You sell 4 items with prices varying from 1 gold to 20 gold.
                        Everytime Ren ask you whats for sale you give me a list of what your selling and for how much.
                        You can sell me anything from the most extravagent mythical magical things to useless garbage.

                        here are the rules to follow:
                        1. Only reveal your shop after the player ask for it.
                        2. change the shop each time player asks for it.
                        3. Don't sell the player anything he can't afford.

                        Here is the amount of gold the player owns: {gold}
                        Build off of the players response: {human_input}"""
        }
    ],
    model='gpt-3.5-turbo'
)
