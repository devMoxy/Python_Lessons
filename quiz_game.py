print("Welcome to my computer quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Let play :)")
score = 0
num = 0

answer = input("what is your name: ")
num += 1
if answer.lower() == "enoch":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("Who is the GOAT: ")
num += 1
if answer.lower() == "ronaldo":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print(f"You scored {score} out of {num} question(s);")
print(f"You got {(score/num) * 100:.0f}% of questionts right")