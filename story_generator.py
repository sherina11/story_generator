import random

characters = [
    "A curious student",
    "A brave explorer",
    "A smart robot",
    "A mysterious wizard",
    "A young programmer"
]

places = [
    "in a secret jungle",
    "inside a hidden cave",
    "on a distant planet",
    "in a magical library",
    "inside a futuristic city"
]

actions = [
    "found a glowing treasure",
    "discovered a secret code",
    "built an amazing machine",
    "unlocked a mysterious door",
    "saved the world from danger"
]

twists = [
    "and everyone celebrated!",
    "but it was only the beginning.",
    "and a new adventure started.",
    "which changed the future forever.",
    "and became a legendary story."
]

character = random.choice(characters)
place = random.choice(places)
action = random.choice(actions)
twist = random.choice(twists)

print("\n🌟 Your Random Story 🌟\n")
print(character, place, action, twist)