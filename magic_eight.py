def ask_question():
    question = input("What is your question?  ")
    return question

while True:
    q = ask_question()
    if q == "quit":
        break
    elif q[-1] != "?":
        print("Sorry, I only answer questions.")

#This is a change



