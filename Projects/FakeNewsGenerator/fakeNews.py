# 1. import random
import random

# 2. create objects
subjects =[
    'virat kohli',
    "vineet baghel",
    'rohit sharma',
    'sachin tendulkar',
    'sanju samson',
    'rahul dravid',
]

# 3. create actions
actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "playing",
    "praciticing",
    "celebrates",
    "going to"
]

# 4 places
places_or_things=[
    'at wankhede',
    "during IPL match",
    "winning IPL final",
    "inside dressing room",
    'at Ahmedabad',
    'a plate of samosa'
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"
    print("\n" + headline)

    user_input = input("\nDo you want another headling? (Yes/No)").strip().lower()
    
    if user_input == 'no':
        break

print("\n Thanks for using the Fake News Headling Generator")
