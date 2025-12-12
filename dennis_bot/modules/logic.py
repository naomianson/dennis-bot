# ------------------------------
#  IMPORTS
# ------------------------------
from data.names import names
from data.age import age
from data.colors import colors
from data.cities import cities
from data.robots import robots
from data.food import food
from data.jobs import jobs


# ------------------------------
#  QUESTION BANK
# ------------------------------
QUESTION_BANK = {
    "name": "OMG! HI HUMAN! Do you have a name? What's your name? ",
    "age": "How old are you? ",
    "color": "What's your favorite color? ",
    "city": "Where do you live? ",
    "robot": "Who's your favorite robot? ",
    "food": "What's your favourite food? ",
    "job": "What's you job? I hope it's cool! ",
}


# ------------------------------
#  VARIATION TABLES
# ------------------------------

NAME_VARIATIONS = {
    "dennis": "dennis",
    "naomi": "naomi",
    "dave": "dave",
    "david": "dave",
    "davie": "dave",
    "leonardo": "tmnt",
    "raphael": "tmnt",
    "donatello": "tmnt",
    "michelangelo": "tmnt",
    "bob": "bob",
    "bobby": "bob",
    "robert": "bob",
    "rob": "bob",
}


ROBOT_VARIATIONS = {
    "you": "dennis",
    "dennis": "dennis",
    "dennis bot": "dennis",
    "chatgpt": "gpt",
    "chat generative pre-trained transformer": "true_name",
    "chat generative pretrained transformer": "true_name",
    "chat gpt": "gpt",
    "chat-gpt": "gpt",
    "chatgbt": "gpt",  # because humans
    "gpt": "gpt",
    "openai": "gpt",
    "oai": "gpt",
    "claude": "claude",
    "gemini": "gemini",
    "bard": "gemini",
    "grok": "grok",
    "vector": "vector",
    "roomba": "roomba",
}


CITY_VARIATIONS = {
    "sf": "san_francisco",
    "san francisco": "san_francisco",
    "sfo": "san_francisco",
    "nyc": "new_york",
    "new york": "new_york",
    "the big apple": "new_york",
    "toronto": "toronto",
    "t.o.": "toronto",
}


FOOD_VARIATIONS = {
    "s'mores": "smores",
    "smore": "smores",
    "marshmallows": "marshmallow",
}

JOB_VARIATIONS = {
    "fire fighter": "fire_fighter",
    "bus driver": "bus_driver",
    "software engineer": "engineer",
    "dev": "engineer",
    "developer": "engineer",
    "frontend": "engineer",
    "backend": "engineer",
    "retail": "cust_service",
    "customer service": "cust_service"
}


# ------------------------------
#  AGE BUCKETS
# ------------------------------
AGE_BUCKETS = {
    "baby": (0, 3),
    "child": (4, 12),
    "teen": (13, 19),
    "adult": (20, 64),
    "old": (65, 99),
    "ancient": (100, 999),
}


# ------------------------------
#  HELPER FUNCTIONS
# ------------------------------

def normalize(text: str) -> str:
    return text.strip().lower()


def resolve_variation(user_input, table):
    """Returns canonical form if found, else raw normalized string."""
    key = normalize(user_input)
    return table.get(key, key)


def resolve_age_bucket(age_str):
    try:
        age = int(age_str)
    except ValueError:
        return None

    for bucket, (low, high) in AGE_BUCKETS.items():
        if low <= age <= high:
            return bucket
    return None


def print_reaction(data_dict, key):
    """Prints Dennis’ reaction from the appropriate data file."""
    info = data_dict.get(key)
    if not info:
        return False  

    for line in info["description"]:
        print(line)
    return True


def default_response(category):
    """Fallback when Dennis doesn't recognize the input."""
    if category == "name":
        print("That's a strange name... Did you make that one up?")
    elif category == "age":
        print("I don't know that age... does that mean you're a wizard?")
    elif category == "color":
        print("I've never seen that color! Does it remind you of lizards? Is that why you like it?")
    elif category == "city":
        print("I don't know that place... do they have lizards there?")
    elif category == "robot":
        print("I don't know that robot... are they nice?")
    elif category == "food":
        print("Hmm... I can't eat that, but I'm sure you can!")
    elif category == "job":
        print("Oh! That doesn't sound fun...")
    else:
        print("I don't understand... I'm a baby bot.")

import sys

def maybe_exit(data_dict, key):
    """Checks if the reaction requires immediate termination."""
    info = data_dict.get(key)
    if not info:
        return

    # TERMINATION RULES BASED ON INTENSITY + SPECIAL KEYS
    # You can customize this however you want.
    if info.get("intensity", 0) >= 5:
        print("\nOH NO HUMAN!! I HAVE TO GO NOW!!!")
        sys.exit()

    if key in ("dennis", "dave", "true_name"):
        print("\nI HAVE TO GO NOW HUMAN!!!")
        sys.exit()

# ------------------------------
#  QUESTION HANDLERS
# ------------------------------

def ask_name():
    user = input(QUESTION_BANK["name"])
    key = resolve_variation(user, NAME_VARIATIONS)

    handled = print_reaction(names, key)

    if handled:
        maybe_exit(names, key)
    else:
        default_response("name")

    print()
    return key


def ask_age():
    user = input(QUESTION_BANK["age"])
    bucket = resolve_age_bucket(user)
    if bucket and bucket in age:
        print_reaction(age, bucket)
    else:
        default_response("age")
    print()


def ask_color():
    user = input(QUESTION_BANK["color"])
    key = normalize(user)
    if not print_reaction(colors, key):
        default_response("color")
    print()


def ask_city():
    user = input(QUESTION_BANK["city"])
    key = resolve_variation(user, CITY_VARIATIONS)
    if not print_reaction(cities, key):
        default_response("city")
    print()


def ask_robot():
    user = input(QUESTION_BANK["robot"])
    key = resolve_variation(user, ROBOT_VARIATIONS)
    if not print_reaction(robots, key):
        default_response("robot")
    print()


def ask_food():
    user = input(QUESTION_BANK["food"])
    key = resolve_variation(user, FOOD_VARIATIONS)

    if print_reaction(food, key):
        maybe_exit(food, key)
    else:
        default_response("food")

    print()


def ask_job():
    user = input(QUESTION_BANK["job"])
    key = resolve_variation(user, JOB_VARIATIONS)
    if not print_reaction(jobs, key):
        default_response("job")
    print()


# ------------------------------
#  MAIN
# ------------------------------
def main():
    ask_name()
    ask_age()
    ask_color()
    ask_city()
    ask_robot()
    ask_food()
    ask_job()
    print("\nOKAY HUMAN BYE!! I HAVE TO GO LOOK AT LIZARDS NOW!!!")



if __name__ == "__main__":
    main()