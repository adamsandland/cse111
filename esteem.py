responses = []
pos_neg = [1,1,0,1,0,1,1,0,0,0]
questions = ["I feel that I am a person of worth, at least on an equal plane with others.",
            "I feel that I have a number of good qualities.",
            "All in all, I am inclined to feel that I am a failure.",
            "I am able to do things as well as most other people.",
            "I feel I do not have much to be proud of.",
            "I take a positive attitude toward myself.",
            "On the whole, I am satisfied with myself.",
            "I wish I could have more respect for myself.",
            "I certainly feel useless at times.",
            "At times I think I am no good at all."]

def ask_a_question(index):
    score = input(f"{index+1}. {questions[index]} D/d/a/A:\n")
    if score in ["D","d","A","a"]:
        return score
    else:
        print("That was not a valid response.\n")
        ask_a_question(index)
        
def main():
    totalScore = 0
    print("This program is an implementation of the Rosenberg\nSelf-Esteem Scale. This program will show you ten\nstatements that you could possibly apply to yourself.\nPlease rate how much you agree with each of the\nstatements by responding with one of these four letters:")
    print("\nD means you strongly disagree with the statement.\nd means you disagree with the statement.\na means you agree with the statement.\nA means you strongly agree with the statement.\n")
    
    for i in questions:
        answer = ask_a_question(questions.index(i))
        if pos_neg[questions.index(i)] == 1:
            if answer == "D":
                totalScore+=0
            elif answer == "d":
                totalScore+=1
            elif answer == "a":
                totalScore+=2
            else:
                totalScore+=3
        else:
            if answer == "D":
                totalScore+=3
            elif answer == "d":
                totalScore+=2
            elif answer == "a":
                totalScore+=1
            else:
                totalScore+=0
    print(f"Your score is {totalScore}")
    if totalScore<=15:
        print("Wow, you have a very low self esteem. Scrub. Please see a doctor.")
    else:
        print("You have a great self esteem!")

        


main()