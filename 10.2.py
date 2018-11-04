class Trivia:  # sets the class and all the needed info for the game
    def __init__(self, question, ans_1, ans_2, ans_3, ans_4, correct):
        self.question = question
        self.ans_1 = ans_1
        self.ans_2 = ans_2
        self.ans_3 = ans_3
        self.ans_4 = ans_4
        self.correct = correct


# these are the data sets from the class that we use for each question In dictonary for
the_questions = {"q1": Trivia("What color is they sky?", "1. Blue", "2. Red", "3. Green", "4. Yellow", 1),
                 "q2": Trivia("When did america declare thier independence?", "1. 1776", "2. 1896", "3. 1200", "4. 2016", 1),
                 "q3": Trivia("How many letters are in the word cat?", "1. Two letters", "2. Three letters", "3. One letter", "4. Seven letters", 2),
                 "q4": Trivia("What day was the declaration of indepenence signed?", "1. June 8th", "2. Novemeber 11th", "3. July 4th", "4. January 28th", 3),
                 "q5": Trivia("How long did it take to write this code?", "1. One hour", "2. Two hours", "3. Three hours", "4. Four hours", 2),
                 "q6": Trivia("What color is the grass?", "1.Green", "2. Red", "3. Orange", "4. Grey", 1),
                 "q7": Trivia("What is MCC's school color?", "1. Red", "2. Orange", "3. Green", "4. Purple", 4),
                 "q8": Trivia("What is the antonym of this word: wild", "1. tame", "2. Crazy", "3. Loud", "4. Aggresive", 1),
                 "q9": Trivia("What is the synonym of this word: beautiful", "1. Ugly", "2. Smart", "3. Pretty", "4. Quite", 3),
                 "q10": Trivia("How many syllables does this word have: Thanksgiving", "1. Three syllables", "2. Four syllables", "3. Two syllables", "4. No syllables", 1)}


def main():
    p1 = 0  # this is the player one score
    p2 = 0  # this is eh player two score
    print("Hello and welcome to the trivia game!")
    print("This is a two player game so grab a friend and play!")
    print("----------------------")
    quest_1(score_1=p1)
    blank_spaces()  # This creates spacing for better legebiliy
    quest_2(score_2=p2)
    blank_spaces()
    quest_3(score_1=p1)
    blank_spaces()
    quest_4(score_2=p2)
    blank_spaces()
    quest_5(score_1=p1)
    blank_spaces()
    quest_6(score_2=p2)
    blank_spaces()
    quest_7(score_1=p1)
    blank_spaces()
    quest_8(score_2=p2)
    blank_spaces()
    quest_9(score_1=p2)
    blank_spaces()
    quest_10(score_2=p2)
    if p1 == p2:  # This checks if the players had a draw or who won
        print("It was a draw!")
    else:
        if p1 > p2:
            print("Player one wins!")
        else:
            print("Player two wins!")


def blank_spaces():  # This is how the blank_spaces function was defined
    print()
    print("Now it's the other players turn!")
    print("----------------------")


# These sort the individual data for each question into the correct format
def quest_1(score_1):
    print("Here is your question player one,")
    print(the_questions["q1"].question)
    print(the_questions["q1"].ans_1, the_questions["q1"].ans_2, the_questions["q1"].ans_3, the_questions["q1"].ans_4)
    a1 = int(input("select an answer: "))
    if a1 == the_questions["q1"].correct:
        score_1 + int(1)
        print("Nice job, player two!")
    else:
        print("You'll get it next time I'm sure!")


def quest_2(score_2):
    print("Here is your question player two,")
    print(the_questions["q2"].question)
    print(the_questions["q2"].ans_1, the_questions["q2"].ans_2, the_questions["q2"].ans_3, the_questions["q2"].ans_4)
    a1 = int(input("select an answer: "))
    if a1 == the_questions["q2"].correct:
        score_2 + int(1)
        print("Nice job, player two!")
    else:
        print("You'll get it next time I'm sure!")


def quest_3(score_1):
    print("Here is your question player one,")
    print(the_questions["q3"].question)
    print(the_questions["q3"].ans_1, the_questions["q3"].ans_2, the_questions["q3"].ans_3, the_questions["q3"].ans_4)
    a1 = int(input("select an answer: "))
    if a1 == the_questions["q3"].correct:
        score_1 + int(1)
        print("Nice job, player one!")
    else:
        print("You'll get it next time I'm sure!")


def quest_4(score_2):
    print("Here is your question player two,")
    print(the_questions["q4"].question)
    print(the_questions["q4"].ans_1, the_questions["q4"].ans_2, the_questions["q4"].ans_3, the_questions["q4"].ans_4)
    a1 = int(input("select an answer: "))
    if a1 == the_questions["q4"].correct:
        score_2 + int(1)
        print("Nice job, player two!")
    else:
        print("You'll get it next time I'm sure!")


def quest_5(score_1):
    print("Here is your question player one,")
    print(the_questions["q5"].question)
    print(the_questions["q5"].ans_1, the_questions["q5"].ans_2, the_questions["q5"].ans_3, the_questions["q5"].ans_4)
    a1 = int(input("select an answer: "))
    if a1 == the_questions["q5"].correct:
        score_1 + int(1)
        print("Nice job, player one!")
    else:
        print("You'll get it next time I'm sure!")


def quest_6(score_2):
    print("Here is your question player two,")
    print(the_questions["q6"].question)
    print(the_questions["q6"].ans_1, the_questions["q6"].ans_2, the_questions["q6"].ans_3, the_questions["q6"].ans_4)
    a1 = int(input("select an answer: "))
    if a1 == the_questions["q6"].correct:
        score_2 + int(1)
        print("Nice job, player two!")
    else:
        print("You'll get it next time I'm sure!")


def quest_7(score_1):
    print("Here is your question player one,")
    print(the_questions["q7"].question)
    print(the_questions["q7"].ans_1, the_questions["q7"].ans_2, the_questions["q7"].ans_3, the_questions["q7"].ans_4)
    a1 = int(input("select an answer: "))
    if a1 == the_questions["q7"].correct:
        score_1 + int(1)
        print("Nice job, player one!")
    else:
        print("You'll get it next time I'm sure!")


def quest_8(score_2):
    print("Here is your question player two,")
    print(the_questions["q8"].question)
    print(the_questions["q8"].ans_1, the_questions["q8"].ans_2, the_questions["q8"].ans_3, the_questions["q8"].ans_4)
    a1 = int(input("select an answer: "))
    if a1 == the_questions["q8"].correct:
        score_2 + int(1)
        print("Nice job, player two!")
    else:
        print("You'll get it next time I'm sure!")


def quest_9(score_1):
    print("Here is your question player one,")
    print(the_questions["q9"].question)
    print(the_questions["q9"].ans_1, the_questions["q9"].ans_2, the_questions["q9"].ans_3, the_questions["q9"].ans_4)
    a1 = int(input("select an answer: "))
    if a1 == the_questions["q9"].correct:
        score_1 + int(1)
        print("Nice job, player one!")
    else:
        print("You'll get it next time I'm sure!")


def quest_10(score_2):
    print("Here is your question player two,")
    print(the_questions["q10"].question)
    print(the_questions["q10"].ans_1, the_questions["q10"].ans_2, the_questions["q10"].ans_3, the_questions["q10"].ans_4)
    a1 = int(input("select an answer: "))
    if a1 == the_questions["q10"].correct:
        score_2 + int(1)
        print("Nice job, player two!")
    else:
        print("You'll get it next time I'm sure!")


main()
