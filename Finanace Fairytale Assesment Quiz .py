
answer = input( "What is a bugdet?\n(A) A plan on how to spend your money\n(B) A place where you can keep all of your money\n(C) A person who helps with money\n(D) I don't know" )

answer = input( "Why should we have a budget?\n(A) To save money\n(B) To have a good amount of debt\n(C) So you can brag to your friends\n(D) I don't know")

answer = input( "What is the first step to starting a budget?\n(A)Go on a shopping spree\n(B) Figure out monthly expenses\n(C) Start saving your money\n(D) I don't know" )

answer = input( "Why should you learn how to manage your money?\n(A) Because it is fun\n(B) So that you save enough to purchase things\n(C) You set yourself up for the future\n(D) All of the above" )


Wizard = 0
Ruler = 0
Knight = 0
Creature = 0

if answer == "A":
  Wizard += 1
elif answer == "B":
  Knight += 1
elif answer == "C":
  Ruler += 1
elif answer == "D":
  Creature += 1
else:
  print("You did not select one of the answers for question 1. We're going to say you selected D")
  Creature += 1
  
if answer == "A":
  Wizard += 1
elif answer == "B":
  Ruler += 1
elif answer == "C":
  Knight += 1
elif answer == "D":
  Creature += 1
else:
  print("You did not select one of the answers for question 2. We're going to say you selected D")
  Creature += 1
  
if answer == "A" or "D":
  Creature += 1
  Knight += 1
elif answer == "B":
  Wizard += 1
elif answer == "C":
  Ruler += 1;  
else:
  print("You did not select one of the answers for question 3. We're going to say you selected D")
  Creature += 1  
  
if answer == "A":
  Creature += 1
elif answer == "B":
  Knight  += 1
elif answer == "C":
  Wizard += 1;
elif answer == "D":
  Ruler += 1
else:
  print("You did not select one of the answers for question 4.")
  Creature += 1
	
if (Wizard > Ruler and Knight and Creature):
	print("Congratulations! You will start off as The Wizard!")
elif (Ruler > Wizard and Knight and Creature):
  print("Congratulations! You will start  of as The Kingdom Ruler!")
elif (Knight > Wizard and Ruler and Creature):
  print("Congratulations! You will start of a The Head Knight!")
else:
  print("Congratulations! You will start of as a Magical Creature!")
