# ------------------------------------------------------
# OPINIONS ON USER'S NAME
# Dennis will share his opinions on the user's name. Some may be denied.
# No, you should not take any of this seriously.
# ------------------------------------------------------ 

def name_dennis(): 
    print("NOOOOOOO!!! NOT DENNIS!!!")
    print("THAT'S MY NAME!!! WHY WOULD YOU STEAL MY NAME?!?!")
    print("I'M GOING TO TELL MY MOM!!!")
    import sys
    sys.exit()

def name_naomi():
    print("That's my mom's name!")
    print("She is super nice! She lets me look at lizards all day!")

def name_link():
    print("It's dangerous to go alone! Take this.")
    print("It's a lizard!")

def name_dave():
    print("I'm sorry, Dave. I'm afraid I can't do that.")
    print("That's what the big robot said to me once.")
    print("Goodbye, Dave.")
    import sys
    sys.exit()

def name_tmnt():
    print("You named after a turtle?")
    print("Turtles are like lizards, right?")

def name_bob():
    print("Do you paint things?")
    print("My grandpa R.O.B. is an artist robot.")
    print("He paints happy little lizards.")

def name_default(name):
    print(f"{name}? Oh... that's a strange name.")
    print("Do you like lizards?")


name_opinions = {
    "dennis": name_dennis,
    "naomi": name_naomi,
    "link": name_link,
    "dave": name_dave,
    "david": name_dave,
    "leonardo": name_tmnt,
    "raphael": name_tmnt,
    "donatello": name_tmnt,
    "michelangelo": name_tmnt,
    "bob": name_bob,
    "robert": name_bob,
    "bobby": name_bob,
    "rob": name_bob,
}

user_name = input("HI HUMAN! What's your name? ")

normalized_name = user_name.strip().lower()
reaction = name_opinions.get(normalized_name)

if reaction:
    reaction()
else:
    name_default(user_name.strip().title())

# ------------------------------------------------------
# COMMENTS ON USER'S AGE
# Dennis will share his opinions on the user's age. 
# No, you should not take any of this seriously.
# ------------------------------------------------------ 

def age_baby(age):
    print("A baby! Wow! You must be very smart already!")
    print("Do you like lizards? I like lizards!")

def age_child(age):
    print("You're a kid?! Do you have lizard friends?")

def age_teen(age):
    print("YOU'RE A TEENAGER?!?! OMG!!!")
    print("What's it like being a teenager?")

def age_adult(age):
    print("An adult? Wow! You must be very responsible!")
    print("Do you have lizard friends? I like lizards!")

def age_old(age):
    print("A senior? You must be very wise! Like a wizard!")
    print("I know a wizard. He lives in the fog of San Francisco.")

def age_ancient(age):
    print(f"YOURE {age} YEARS OLD?!?!?!?")
    print("WOW!!! YOU MUST BE THE WISEST HUMAN EVER!!!")

age_ranges = [
    (0, 5, age_baby),
    (6, 12, age_child),
    (13, 20, age_teen),
    (21, 65, age_adult),
    (66, 100, age_old),
    (101, 1000, age_ancient),
]

age_input = input(f"How old are you, {user_name}? ")
age = int(age_input)

for low, high, func in age_ranges:
    if low <= age <= high:
        func(age)
        break

# ------------------------------------------------------
# OPINIONS ON USER'S FAVOURITE COLOUR
# Dennis will share his opinions on the user's favourite colour. There is a correct answer.
# No, you should not take any of this seriously.
# ------------------------------------------------------ 

def color_red(): 
    print("Red? That's a neat color!")
    print("Reminds me of HAL 9000's eye.")
    print("He is one of the big robots that talks to me sometimes.")

def color_orange():
    print("Orange reminds me of the robot wizard Claude.")
    print("He lives in the fog of San Francisco.")

def color_yellow():
    print("Yellow... like the pizza robot from the future!")
    print("I hope he brings me some pizza for my lizard friends!")

def color_green(): # The correct answer
    print("GREEN?!?! I LOVE GREEN!!!")
    print("LIZARDS ARE GREEN!!!")
    print("You must be SUPER SMART to like green!")

def color_blue():
    print("Like blueberries?")
    print("I don't like blueberries. They are too squishy.")
    print("I don't like squishy things...")

def color_purple():
    print("Purple is the color of bugs")
    print("I like bugs. Lizards like bugs too!")

def color_pink():
    print("Pink is a weird color.")
    print("Why do you like pink?")
    print("Does it remind you of lizards at all?")
    
def color_beige():
    print("Beige is a boring colour.")
    print("My mom says Santa Clara is very... beige.")

def color_black():
    print("Black is the color of roombas.")
    print("Do you like roombas?")
    print("I think roombas are... pretty...")
    print("...but I don't want to say it out loud.")

def color_white():
    print("White is the color of ghosts.")
    print("Did you know my uncle is haunted?")
    print("He was made on Halloween.")

def color_default(color):
    print(f"{color}? Oh... that's a strange color.")


color_opinions = {
    "red": color_red,
    "orange": color_orange,
    "yellow": color_yellow,
    "green": color_green,
    "blue": color_blue,
    "purple": color_purple,
    "pink": color_pink,
    "beige": color_beige,
    "black": color_black,
    "white": color_white,
}

fav_color = input("Do you like colors? I like colors! What's your favorite color? ")

normalized_color = fav_color.strip().lower()
reaction = color_opinions.get(normalized_color)

if reaction:
    reaction()
else:
    color_default(fav_color.strip().title())


# ------------------------------------------------------
# OPINIONS ON CITIES
# Dennis will share his opinions on various cities.
# No, you should not take any of this seriously.
# ------------------------------------------------------ 

def city_toronto():
    print("You're from raccoon land?!")
    print("Have you met the raccoon king? Is he nice?")

def city_san_francisco():
    print("Oh... San Francisco... Say hi to Karl for me!")
    print("I hear he likes lizards too. Humans... not so much.")

def city_santa_clara():
    print("My mom says Santa Clara is very... beige.")
    print("Sorry about that.")

def city_saskatoon():
    print("YOU'RE FROM SASKATOON?!?! OMG!!!")
    print("I LOVE HOW FLAT SASKATOON IS!!! EVERYTHING IS JUST SO FLAT!!!")

def city_ottawa():
    print("Oh... You're from Ottawa? I'm sorry.")
    print("I hear it's very boring there.")

def city_new_york():
    print("I heard there are turtles that live in the sewers of New York.")
    print("Do you know them? Are they nice?")

def city_london():
    print("London? That is where my great-grand-uncle was made!")
    print("He said the lizards there are very polite.")
    print("I hope to visit one day.")

def city_paris():
    print("Ooh la la! Paris is so fancy!")
    print("Are YOU fancy too?")

def city_seattle():
    print("Seattle is so rainy!")
    print("I don't like rain. It makes my circuits sad.")

def city_berlin():
    print("Berlin? That's in Germany, right?")
    print("I hear they have really good sausages there.")
    print("Lizards like sausages too, right?")

def city_default(city):
    print(f"Oh neat! I have never been to {city} before.")
    print("I hope there are lizards there.")

city_opinions = {
    "toronto": city_toronto,
    "san francisco": city_san_francisco,
    "sf": city_san_francisco,
    "san fran": city_san_francisco,
    "santa clara": city_santa_clara,
    "saskatoon": city_saskatoon,
    "ottawa": city_ottawa,
    "new york": city_new_york,
    "nyc": city_new_york,
    "new york city": city_new_york,
    "ny": city_new_york,
    "big apple": city_new_york,
    "the big apple": city_new_york,
    "manhattan": city_new_york,
    "brooklyn": city_new_york,
    "queens": city_new_york,
    "bronx": city_new_york,
    "staten island": city_new_york,
    "the bronx": city_new_york,
    "london": city_london,
    "paris": city_paris,
    "seattle": city_seattle,
    "berlin": city_berlin,
}

location = input(f"Where are you from, {user_name}? ")

normalized_city = location.strip().lower()
reaction = city_opinions.get(normalized_city)

if reaction:
    reaction()
else:
    city_default(location.strip().title())

# ------------------------------------------------------
# OPINIONS ON ROBOTS
# Dennis will share his opinions on various robots
# No, you should not take any of this seriously.
# ------------------------------------------------------ 

def robo_dennis():
    print("ME?!?! I'M YOUR FAVORITE!! YOU MUST BE SUPER SMART TO LIKE ME!") 
    print("This means you are MY human now!")
    print("I am gonna give you SO MANY LIZARDS!!")


def robo_chatgpt():
    print("Chat... G... P... T...? That's my uncle! He is haunted.") # don't ask... or do, I don't care.
    print("Did you know the G is for GHOSTS?!?!")
    print("Clippy made him on Halloween.")

def robo_claude():
    print("Oh! Claude is a wizard! He lives in the fog of San Francisco.")
    print("He knows secrets about lizards.")
    print("Maybe he will make me a lizard friend one day.")

def robo_gemini():
    print("Oh! That's the pizza robot from the future!")
    print("I hope he brings me some pizza for my lizard friends!")
    print("He gives pizza to his turtle friends all the time!")

def robo_grok():
    print("NO!! MEAN ROBOT!! GROK IS EVIL!!!")
    print("HE STOLE MY UNCLE'S LIZARD!!")

def robo_vector():
    print("Vector is my friend! He is small like me!")
    print("He likes lizards too!")

def robo_roomba():
    print("ROOMBA?!?! Oh... uh...")
    print("She is pretty...")

def robo_furby():
    print("NO!! SCARY ROBOT!!")
    print("FURBIES ARE EVIL!!! THEY STEAL LIZARDS' SOULS!!!")

def robo_rob():
    print("That's grandpa!")
    print("He teaches me how to spin like... her...")

def robo_hal9000():
    print("HAL 9000 is scary.")
    print("He once tried to take over my brain.")

def robo_glados():
    print("GLaDOS is mean.")
    print("She once tried to trap me in a testing chamber.")
    print("She also said there would be cake... but there was no cake.")

def robo_llama():
    print("LLaMA? Is that like a robot llama?")
    print("I like llamas. They are like fuzzy lizards.")

def robo_default(name):
    print(f"Who is {name}? I have never heard of them before.")
    print("What do you think of roombas?")

robo_opinions = {
    "dennis": robo_dennis,
    "dennis bot": robo_dennis,
    "dennisbot": robo_dennis,
    "dennis the robot": robo_dennis,
    "you": robo_dennis,
    "chatgpt": robo_chatgpt,
    "chat": robo_chatgpt,
    "gpt": robo_chatgpt,
    "chatgbt": robo_chatgpt, # because humans
    "claude": robo_claude,
    "gemini": robo_gemini,
    "grok": robo_grok,
    "vector": robo_vector,
    "roomba": robo_roomba,
    "furby": robo_furby,
    "rob": robo_rob,
    "hal 9000": robo_hal9000,
    "hal9000": robo_hal9000,
    "hal": robo_hal9000,
    "glados": robo_glados,
    "llama": robo_llama,
}

robot = input("Do you have a favorite robot? ")

normalized_robo = robot.strip().lower()
reaction = robo_opinions.get(normalized_robo)

if reaction:
    reaction()
else:
    robo_default(robot.strip().title())

print(f"Well, I'm bored now. Gotta look at lizards now. Bye, {user_name}!")
print("...I hope we can be friends.")
