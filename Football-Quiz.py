#Football where I will be asking 5 Questions to know the user's knowledge on Footballers
print("Greetings! Are you ready test your knowledge on football?")
prompt = input("Are you ready to take up the quiz? ")

if prompt.lower() != "yes":
    quit()
else:
    print("Lets get started!")

score = 0

#Question-1
answer = input("Who is the Greatest player of all time to play football? ")
if answer.lower() == "messi":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("Who is the second Greatest player of all time to play football? ")
if answer.lower() == "ronaldo":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("Which team won the World-Cup in 2022? ")
if answer.lower() == "argentina":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("Which team won the UCL in 2023? ")
if answer.lower() == "manchester city":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
answer = input("Who has won the most number of golden boots? ")
if answer.lower() == "messi":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")
    
print("Results:")
print(f"You have got {score} right out of 5!")
print(f"You have got {(score/5)*100}%.")
