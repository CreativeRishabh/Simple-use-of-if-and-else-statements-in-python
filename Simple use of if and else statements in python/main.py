print("Welcome it's me, game! Let's Start!")

name = input('What is your name ? ')
age = int(input('What is your age ? '))

print("Hello", name, ", your age is", age)

if age >= 18:
   print("You are old enough to play me!")

   ask_for_play = input("Do you want to play me ? [Yes/No]")
   
   if ask_for_play.lower().strip() == "yes":
     print("Okk, let's play!")
   elif ask_for_play.lower().strip() == "no":
     print("As you wish , bye bye.")
else:
  print("Everybody can play me and you are one of them!")
