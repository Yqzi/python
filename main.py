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

# Here is the amount of gold the player owns: {gold}gi
# """

client = OpenAI(
    api_key=OPENAI_API_KEY
)

human_input = 'hello'
playerLevel = 8
potionType = "poison"
potionCost = 10
element = "darkness"
shopHistory = """
Novice Shortsword - 10 gold
Health Tonic - 10 gold
Cloth Apprentice Tunic - 15 gold
Ember Spark Spell Scroll - 50 gold
"""

shopHistory100 = """
Celestial Frostreaper - 60,000 gold
Health Elixir - 5,000 gold
Adamantium Archon Plate - 55,000 gold
Nature's Wrathstorm Spell Scroll - 13,000 gold
"""

# response = client._process_response(human_input='hello')
while True:
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": 'system',
            'content': f"""You are a merchant selling to a level {playerLevel} adventurer.  
            You sell 4 items with varying prices. list only the items and dont use the first scentence. 
            The first item should be a weapon. the second item should be a {potionType} potion thta costs {potionCost}. 
            the third item should be armor. the last item should be a spell. The spell can only be of type {element}.
            list your items as the following:
            1. Item Name - price gold

            for reference this could be a shop for a level 1 adventurer {shopHistory}
            for reference this could be a shop for a level 100 adventurer {shopHistory100}
            """
        },

        {
            "role": 'user',
            'content': """let me see your wares"""
        }
    ],
    model='gpt-3.5-turbo-1106'
)
    
    print(chat_completion.choices[-1].message.content)

    human_input = input('Your reply: ')

