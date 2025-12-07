name = input("Hello! What is your name? ")
user_name = name.strip().title()
if user_name == "Dennis":
    print("HEY! THAT'S MY NAME!! YOU STOLE MY NAME!!! YOU'RE MY ARCH-NEMESIS NOW!!!")
    print("You know what? I'm not talking to you anymore!\n")
    import sys
    sys.exit()
elif user_name == "Naomi":
    print("That's my mom's name! I like her more though!")
    print("She makes sure I get enough lizard time!")
else:
  print(f"Nice to meet you, {user_name}! My name is, Dennis!")
age_input = input("How old are you? ")
age = int(age_input)
bot_age = 1
age_difference = age - bot_age
if age <= 5:
    print("You're a baby human! Do you like lizards too?")
elif age <= 12:
    print("Oh, you're a kid! Do you have a pet lizard?")
elif age <= 19:
    print("Ah, a teenager! Do you think lizards are cool?")
elif age <= 30:
    print("You're an adult! I hope you have time to look at lizards!")
    print(f"What's it like being {age_difference} years older than me?")
elif age <= 64:
    print("Wow, you're really old! Did you have pet dinosaurs when you were a kid?")
    print("I bet dinosaurs and lizards were best friends!") 
else:
    print(f"You're {age}?! Wow!")
    print("You're ANCIENT! Were you around when lizards first appeared on Earth?")
color = input("What's your favorite color? ")
lower_color = color.strip().lower()
if lower_color == "green":
    print("OMG! I love green! It reminds me of lizards!")
elif lower_color == "beige":
    print("Beige?! Reminds me of Santa Clara... Santa Clara chose beige just like you. Which is concerning.")
else:
    print(f"Oh, {lower_color}? That's a nice colour!")
location = input(f"Where are you from, {user_name}? ")
title_location = location.strip().title()
if title_location == "Toronto":
    print("You're from raccoon land?!")
    print("Have you met the raccoon king? Is he nice?")
elif title_location in ["San Francisco", "SF", "San Fran"]:
    print("Oh... San Francisco... Say hi to Karl for me!")
    print("I hear he likes lizards too. Humans... not so much.")
elif title_location == "Santa Clara":
    print("My mom says Santa Clara is very... beige.")
    print("Sorry about that.")
elif title_location == "Saskatoon":
    print("YOU'RE FROM SASKATOON?!?! OMG!!!")
    print("I LOVE HOW FLAT SASKATOON IS!!! EVERYTHING IS JUST SO FLAT!!!")
elif title_location == "Ottawa":
  print("Oh... You're from Ottawa? I'm sorry.")
  print("I hear it's very boring there.")
else: 
  print(f"Oh neat! I have never been to {title_location} before.")
  print("I hope there are lizards there.")
print(f"Well, I'm bored now. Gotta look at lizards now. Bye, {user_name}!")
print("...I hope we can be friends.")
