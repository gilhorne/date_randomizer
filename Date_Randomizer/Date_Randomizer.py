import random

# list of date ideas. (Research more date ideas)
dates = [
    "Go for a picnic in the park",
    "Take a cooking class together",
    "Visit a local museum",
    "Go hiking in the mountains",
    "Have a movie night at home",
    "Go for a bike ride",
    "Visit a nearby beach",
    "Have a game night with board games",
    "Go stargazing",
    "Take a scenic drive",
    "Visit a botanical garden",
    "Go on a wine tasting tour",
    "Have a DIY craft night",
    "Go to a comedy show",
    "Visit a local farmer's market",
    "Have a karaoke night",
    "Go on a scenic hike",
    "Take a dance class together",
    "Visit an art gallery",
    "Have a themed dinner night",
    "Go on a brewery tour",
    "Take a pottery class",
    "Visit a local zoo",
    "Have a photo shoot in a scenic location",
    "Go on a ghost tour",
    "Take a scenic boat ride",
    "Visit a nearby amusement park",
    "Have a picnic by the lake",
    "Go on a nature walk",
    "Take a yoga class together",
    "Visit a local historical site",
    "Go to a live music concert",
    "Have a spa day at home",
    "Go to a sports game",
    "Visit a planetarium",
    "Go to a drive-in movie theater",
    "Have a breakfast date at a cozy cafe",
    "Go horseback riding",
    "Visit a trampoline park",
    "Go to a paint and sip event",
    "Take a hot air balloon ride",
    "Go to a food festival",
    "Have a beach bonfire",
    "Go to an escape room",
    "Visit a science center",
    "Go to a botanical garden",
    "Have a progressive dinner (appetizers at one place, main course at another, dessert at another)",
    "Go to a flea market",
    "Take a scenic train ride",
    "Go to a local theater production",
    "Have a fondue night",
    "Go to a zoo or aquarium",
    "Visit a nearby city for a day trip",
    "Go to a farmers market and cook a meal together",
    "Take a pottery or art class",
    "Go to a local festival or fair",
    "Have a picnic at a vineyard",
    "Go to a comedy club",
    "Visit a historical landmark",
    "Go to a cooking demonstration",
    "Have a backyard camping night",
    "Go to a local brewery for a tasting",
    "Visit a wildlife sanctuary",
    "Go to a local arcade",
    "Have a themed movie marathon",
    "Go to a botanical garden",
    "Take a scenic helicopter ride",
    "Go to a local art walk",
    "Visit a nearby castle or mansion",
    "Go to a local aquarium",
    "Have a DIY pizza night",
    "Go to a local chocolate factory tour"
]

# list of budget options.
budget = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]


# Selction of dates.
date_selector = random.choice(dates)

# Selection of budget.
budget_selector = random.choice(budget)

print(f"Date Idea: {date_selector}")
print(f"Budget: ${budget_selector}")