answer = input( "If Dimitri was to buy a koi fish for his pond, would he be buying a want or a need?\n(A) Want \n(B) Need" )

answer = input( "Winston wants to buy a suit of armour for 300 coins, but he still has to buy a potion for his brother for 150 coins. If he makes 100 coins a year, how long will he have to save for?\n(A) 4.5 years \n(B) 5 years" )

answer = input( "Gwen wants to start a cat adoption business with 7 employees. She can sell each cat for 120 coins but she has to pay each employee 300 coins a month. How many cats does she have to sell per month to make a profit?\n(A) 18 cats \n(B) 17 cats" )

answer = input( "Clarice has had her eyes on a new start up company promoting more education and jobs for minorities in the workforce. The company has been successful this far and has made a good amount of profit. Should she invest?\n(A) Invest \n(B) Don't Invest" )

Correct = 0
Incorrect= 0

if answer == "Want":
  Correct += 1
elif answer == "Need":
  Incorrect += 1
else:
  print("You did not select one of the answers for question 1.")
  Incorrect += 1
  
if answer == "4.5 years":
  Correct += 1
elif answer == "5 years":
  Incorrect += 1
else:
  print("You did not select one of the answers for question 2. ")
  Incorrect += 1
   
if answer == "18 Cats":
  Correct += 1
elif answer == "17 Cats":
  Incorrect += 1
else:
  print("You did not select one of the answers for question 3.")
  Incorrect += 1  
  
  if answer == "Invest":
  Correct += 1
elif answer == "Don't Invest":
  Incorrect += 1
else:
  print("You did not select one of the answers for question 3.")
  Incorrect += 1  
  
if (Correct> Incorrect ):
	print("Congratulations! You have defeted Sir Debton and saved the town of Budgetburg")
else:
  print("Sir Debtonhas beaten you this time but keep praticing and you will defeat them in no time")