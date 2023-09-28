print("Welcome to The Animal Quiz!")

playing = input("Are you ready to begin? ")

if playing.lower() != "yes":
    quit()

print("Okay! Here's your first question! ")
score = 0

answer = input("What common domestic animal uses a litter box? ")
if answer.lower() == "cat":
    print("Correct!")
    score += 1
else:
    print("Sorry, that's incorrect!")

answer = input("What is the fastest land mammal? ")
if answer.lower() == "cheetah":
    print("Correct!")
    score += 1
else:
    print("Sorry, that's incorrect!")

answer = input("What flightless bird inhabits Antartica? ")
if answer.lower() == "penguin":
    print("Correct!")
    score += 1
else:
    print("Sorry, that's incorrect!")

answer = input("What underwater animal has 8 legs? ")
if answer.lower() == "octopus":
    print("Correct!")
    score += 1
else:
    print("Sorry, that's incorrect!")

answer = input("What is a baby kangaroo called? ")
if answer.lower() == "joey":
    print("Correct!")
    score += 1
else:
    print("Sorry, that's incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 5) * 100) + "%.")

    
