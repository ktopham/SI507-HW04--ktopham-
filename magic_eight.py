import random
def ask_question():
    question = input("What is your question?  ")
    possible_answers = ["it is certain", "it is decidedly so", "without a doubt", "yes definitely", "you may rely on it", "as i see it, yes", "most likely","outlook good","yes","signs point to yes", "reply hazy try again", "ask again later", "better not tell you now", "cannot predict now", "concentrate and ask again","don't count on it", "my sources say no", "outlook not so goood", "very doubtful"]
    return random.choice(possible_answers)
    return question

while True:
    q = ask_question()
    if q == "quit":
        break
    elif q[-1] != "?":
        print("Sorry, I only answer questions.")

#This is a change



