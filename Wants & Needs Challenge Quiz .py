answer = input( "Dimitri is thinking about buying a dragon to make getting into town more fun.\n(A) Want \n(B) Need" )

answer = input( "Dimitri is running low on food but he doesn't know if he should go to the market to buy some.\n(A) Want \n(B) Need" )

answer = input( "Dimitri likes his current cape, but he was thinking about getting a cape to match the blue on his staff.\n(A) Want \n(B) Need" )

Correct = 0
Incorrect= 0

if answer == "Want":
  Correct += 1
elif answer == "Need":
  Incorrect += 1
else:
  print("You did not select one of the answers for question 1.")
  Incorrect += 1
  
if answer == "Want":
  Inorrect += 1
elif answer == "Need":
  Correct += 1
else:
  print("You did not select one of the answers for question 2. ")
  Incorrect += 1
   
if answer == "Want":
  Correct += 1
elif answer == "Need":
  Incorrect += 1
else:
  print("You did not select one of the answers for question 3.")
  Incorrect += 1  
  
if (Correct> Incorrect ):
	print("Congratulations! You passed this challenge")
else:
  print("You did not pass this challenge ")