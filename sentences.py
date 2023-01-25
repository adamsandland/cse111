import random

def make_sentence(quantity, tense):
    print(f"{get_determiner(quantity)} {get_noun(quantity)} {get_verb(quantity, tense)}")


def get_determiner(quantity):
    if quantity==1:
        wordList = ["a", "one", "the"]
    else:
        wordList = ["some", "many", "the"]
    return random.choice(wordList)


def get_noun(quantity):
    if quantity==1:
        wordList = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:
        wordList = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    return random.choice(wordList)


def get_verb(quantity, tense):
    if tense=="past":
        wordList=["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense=="present" and quantity==1:
        wordList=["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense=="present" and quantity!=1:
        wordList=["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    else:
        wordList=["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    
    return random.choice(wordList) #random word from wordList        


# define and call the instructions from the specified functions
def main():
    make_sentence(1,"past")
    make_sentence(1,"present")
    make_sentence(1,"future")
    make_sentence(0,"past")
    make_sentence(0,"present")
    make_sentence(0,"future")
main()