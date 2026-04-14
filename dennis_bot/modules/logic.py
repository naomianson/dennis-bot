# ------------------------------
#  IMPORTS
# ------------------------------
import json
import sys
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parents[1] / "data"


def load_json(filename):
    with open(DATA_DIR / filename, "r", encoding="utf-8") as f:
        return json.load(f)


names = load_json("names.json")
age = load_json("age.json")
colors = load_json("colors.json")
cities = load_json("cities.json")
hobbies = load_json("hobbies.json")
robots = load_json("robots.json")
food = load_json("food.json")
jobs = load_json("jobs.json")
animals = load_json("animals.json")


# ------------------------------
#  QUESTION BANK
# ------------------------------
QUESTION_BANK = {
    "name": "OMG! HI MEAT CREATURE! Do you have a name? What's your name? ",
    "age": "So... how old are you? ",
    "color": "What's your favorite color, meaty one? ",
    "city": "Where do you live? I hope it's somewhere cool. ",
    "hobby": "My mom said people like to do things? I like to look at lizards. What's your hobby? ",
    "robot": "Do you like robots? Who's your favorite robot? ",
    "food": "What's your favorite food? ",
    "job": "My mom said people have jobs where they go to a place and do things to earn money. Do you have a job? What is it? ",
    "animal": "Do you like animals? I like animals. Especially lizards. Lizards are super cool! What animal do you like? "
}


# ------------------------------
#  VARIATION TABLES
# ------------------------------

NAME_VARIATIONS = {
    "dennis": "dennis",
    "naomi": "naomi",
    "nomi": "naomi",
    "link": "link",
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
    "claude": "claude",
    "pete": "peter",
    "steve": "steve",
    "steven": "steve",
    "stephen": "steve",
    "mark": "mark",
    "marc": "mark",
    "marcus": "mark",
    "markus": "mark",
    "marty": "marty",
    "martin": "marty",
    "martina": "marty",
    "alex": "alex",
    "alexander": "alex",
    "alexandra": "alex",
    "kevin": "kevin",
    "kev": "kevin",
    "kevvy": "kevin",
    "bill": "bill",
    "william": "bill",
    "billy": "bill",
    "pauly": "paul",
    "paul": "paul",
    "frank": "frank",
    "frankie": "frank",
    "francis": "frank",
    "francesca": "frank",
    "franklin": "frank",
    "jess": "jessica",
    "ollie" : "oliver",
    "jackson" : "jack",
    "samuel" : "sam",
    "samantha" : "sam",
    "sammy" : "sam",
    "sammie" : "sam",
    "tommy" : "tom",
    "thomas" : "tom",
    "benjamin" : "ben",
    "benny" : "ben"
}

COLOR_VARIATIONS = {
    "lime green" : "lime",
    "neon green" : "lime",
    "coral pink" : "coral"
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
    "claude": "claude",
    "gemini": "gemini",
    "bard": "gemini",
    "grok": "grok",
    "vector": "vector",
    "roomba": "roomba",
    "R.O.B" : "rob",
    "hal" : "hal9000",
    "GLaDOS" : "glados",
    "LLaMA" : "llama",
    "WALL-E" : "wall_e",
    "wall-e" : "wall_e",
    "optimus prime" : "optimus",

}


CITY_VARIATIONS = {
    "toronto": "toronto",
    "t.o.": "toronto",
    "t dot o": "toronto",  # why?
    "the 6ix": "toronto",  # also criminal. you should know better...
    "the 6": "toronto", # eww
    "sf": "san_francisco",
    "san francisco": "san_francisco",
    "sfo": "san_francisco",
    "frisco": "san_francisco",  # criminal. shame on you. straight to jail. do not pass go. do not collect $200.
    "santa clara" : "santa_clara",
    "ny": "new_york",
    "nyc": "new_york",
    "new york": "new_york",
    "the big apple": "new_york",
    "la": "los_angeles",
    "l.a.": "los_angeles",
    "los angeles": "los_angeles",
    "round rock": "round_rock",
    "san jose" : "san_jose",
    "niagara falls" : "niagara_falls",
    "nf" : "niagara_falls",
    "mexico city" : "mexico_city",
    "montréal" : "montreal",
    "cape town" : "cape_town",
    "buenos ares" : "buenos_ares",
    "hong kong" : "hong_kong"
}

HOBBY_VARIATIONS = {
    "crocheting": "crochet",
    "video games": "gaming",
    "dance": "dancing",
    "karate": "martial_arts",
    "taekwondo": "martial_arts",
}


FOOD_VARIATIONS = {
    "s'mores": "smores",
    "smore": "smores",
    "marshmallows": "marshmallow",
    "ice cream": "ice_cream",
    "icecream": "ice_cream",
    "hot dog": "hot_dog",
    "hotdog": "hot_dog",
    "baguette": "bread",
    "flapjacks": "pancakes",
    "pancakes": "pancakes",
    "cheddar": "cheese",
    "mozzarella": "cheese",
    "brie": "cheese",
    "marble cheese": "cheese",
    "ricotta": "cheese",
    "doughnut" : "donut",
    "fried rice" : "fried_rice",
    "bubble tea" : "bubble_tea",
    "boba" : "bubble_tea",
    "mac and cheese" : "mac and cheese",
    "macaroni and cheese" : "mac and cheese",
    "kd" : "mac and cheese"
}

JOB_VARIATIONS = {
    "software engineer": "engineer",
    "dev": "engineer",
    "developer": "engineer",
    "frontend": "engineer",
    "backend": "engineer",
    "fire fighter": "fire_fighter",
    "bus driver": "bus_driver",
    "retail": "customer_service",
    "server" : "customer_service",
    "customer service": "customer_service",
    "graphic designer": "graphic_designer",
    "police officer" : "police_officer",
    "cop" : "police_officer",
    "game dev" : "game_developer",
    "game developer" : "game_developer",
    "marine biologist" : "marine_biologist",
    "mail carrier" : "mail_marrier",
    "mailman" : "mail_carrier",
    "postman" : "mail_carrier",
    "train conductor" : "train_conductor",
    "taxi driver" : "taxi_driver",
    "cab driver" : "taxi_driver"
}

ANIMAL_VARIATIONS = {
    "lizards": "lizards",
    "cats": "cat",
    "dogs": "dog",
    "frog": "frog",
    "snakes": "snake",
    "turtles": "turtle",
    "birds": "bird",
    "hamsters": "hamster",
    "rabbits": "rabbit",
    "horses": "horse",
    "cows": "cow",
    "spiders": "spider",
    "sharks": "shark",
    "elephants": "elephant",
    "parrots": "parrot",
    "iguanas": "iguana",
    "dragons": "dragon",
    "axolotls": "axolotl",
    "croc": "crocodile",
    "crocodiles": "crocodile",
    "crocs": "crocodile",
    "penguins": "penguin",
    "octopi": "octopus",
    "octopuses": "octopus",
    "bears" : "bear",
    "wolves" : "wolf",
    "dolphins" : "dolphin",
    "goats" : "goat",
    "platypuses" : "platypus",
    "peacocks" : "peacock",
    "crabs" : "crabs",
    "sloths" : "sloth",
    "foxes" :  "fox",
    "skinks" : "skink",
    "capybaras" : "capybara",
    "mantises" : "praying_mantis",
    "praying mantis" : "praying_mantis",
    "praying mantises" : "praying_mantis",
    "narwhales" : "narwhal"

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
    """Prints Dennis reaction from the appropriate data file."""
    info = data_dict.get(key)
    if not info:
        return False

    for line in info["description"]:
        print(line)
    return True


_DEFAULT_RESPONSES = {
    "name": "That's a strange name... Did you make that one up?",
    "age": "I don't know that age... does that mean you're a wizard?",
    "color": "I've never seen that color! Does it remind you of lizards? Is that why you like it?",
    "city": "I don't know that place... do they have lizards there?",
    "hobby": "I don't know what that is. Does it involve lizards?",
    "robot": "I don't know that robot... are you sure that's a real robot?",
    "food": "Hmm... I can't eat that, but I'm sure you can!",
    "job": "Oh! That doesn't sound fun...",
    "animal": "What's that? Did you make that up?",
}


def default_response(category):
    """Fallback when Dennis doesn't recognize the input."""
    print(_DEFAULT_RESPONSES.get(category, "I don't understand... I'm a baby bot. I don't know many things yet..."))


def maybe_exit(data_dict, key):
    """Checks if the reaction requires immediate termination."""
    info = data_dict.get(key)
    if not info:
        return

    # Termination rules based on intensity + special keys
    if info.get("intensity", 0) >= 5:
        print(
            "\nYOU ARE MEAN TO ME!! I DON'T WANT TO TALK TO YOU ANYMORE!! I AM TELLING MY MOM!!!"
        )
        sys.exit()

    if key in ("dennis", "dave", "kevin"):
        print("\nYOU MAKE ME SAD... I DON'T WANT TO TALK TO YOU ANYMORE!")
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
    key = resolve_variation(user, COLOR_VARIATIONS)
    if not print_reaction(colors, key):
        default_response("color")
    print()


def ask_city():
    user = input(QUESTION_BANK["city"])
    key = resolve_variation(user, CITY_VARIATIONS)
    if not print_reaction(cities, key):
        default_response("city")
    print()


def ask_hobby():
    user = input(QUESTION_BANK["hobby"])
    key = resolve_variation(user, HOBBY_VARIATIONS)
    if not print_reaction(hobbies, key):
        default_response("hobby")
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


def ask_animal():
    user = input(QUESTION_BANK["animal"])
    key = resolve_variation(user, ANIMAL_VARIATIONS)
    if not print_reaction(animals, key):
        default_response("animal")
    print()



# ------------------------------
#  MAIN
# ------------------------------
def main():
    ask_name()
    ask_age()
    ask_color()
    ask_city()
    ask_hobby()
    ask_robot()
    ask_food()
    ask_job()
    ask_animal()

    print("\nOKAY I WANNA LOOK AT LIZARDS NOW!!!")


if __name__ == "__main__":
    main()
