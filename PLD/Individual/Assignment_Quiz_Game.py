#Python Quiz Game
#list down the questions for the quiz
questions = ("What programming language is a widely-used, interpreted, object-oriented, and high-level programming language with dynamic semantics, used for general-purpose programming?: ",
             "Who created python?: ",
             "What is the date of first released of python?: ",
             "Where did the name of Python came from?: ", 
             "The python is maintained by?: ")
#list down the choices of each questions
options = (("A. Python", "B. CSS", "C. C++", "D. Java"),
           ("A. Anders Hejlsberg", "B. Bjarne Stroustrup", "C. Ada Lovelace", "D. Guido van Rossum"),
           ("A. February 21, 1989", "B. January 21, 1991", "C. February 20, 1991", "D. March 20, 1989"),
           ("A. Large Snake", "B. Kaa from The Jungle Book", "C. Ekans from Pokémon", "D. Monty Python's Flying Circus"),
           ("A. Guido van Rossum", "B. Python Software Foundation", "C. Rossum Foundation", "D. Python Programming Association"))
#list down the correct answer of each questions
answers = ("A", "D", "C", "D", "B")
#make a list of player's guesses, score, and question number
guesses = []
score = 0
question_num = 0
#print the questions and options/answers
for question in questions:
    print("-----------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
        
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
    question_num +=1
#print the result which is the correct answers of each questions, answers of the player, and score in percentage
print("-----------------------------------")
print("             RESULTS               ")
print("-----------------------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")


#reference video https://www.youtube.com/watch?v=zehwgTB0vV8
#reference of questions and answers https://pythoninstitute.org/about-python#:~:text=Python%20was%20created%20by%20Guido,called%20Monty%20Python's%20Flying%20Circus.