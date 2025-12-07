name = input("Hello! What is your name? ")
user_name = name.strip().title()
print(f"Nice to meet you, {user_name}! My name is, Dennis!")
age_input = input("How old are you? ")
age = int(age_input)
bot_age = 1
age_difference = age - bot_age
print(f"You're {age_input}?! Wow, you're really old! You're {age_difference} years older than me. I'm only {bot_age} year old!")
color = input("What's your favorite color? ")
lower_color = color.strip().lower()
if lower_color == "green":
    print("OMG! I love green! It reminds me of lizards!")
elif lower_color == "beige":
    print("Beige?! Reminds me of Santa Clara... Santa Clara chose beige just like you. Which is concerning.")
else:
    print(f"Oh, {lower_color}? That's a nice colour!")
location = input(f"Where are you from, {name}? ")
title_location = location.strip().title()
if title_location == "Toronto":
    print("You're from raccoon land?!")
elif title_location == "San Francisco":
    print("Oh... San Francisco... Say hi to Karl for me!")
elif title_location == "Santa Clara":
    print("My creator says Santa Clara is very... beige.")
elif title_location == "Saskatoon":
    print("YOU'RE FROM SASKATOON?!?! OMG!!!")
elif title_location == "Ottawa":
  print("Oh... You're from Ottawa? I'm sorry.")
else: 
  print(f"Oh neat! I have never been to {title_location} before.")
print(f"Well, I'm bored now. Gotta look at lizards now. Bye, {user_name}!")
