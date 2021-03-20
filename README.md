# rock_paper_scissors.py
a = input()
b = input()
a_move = input()
b_move = input()
if a_move == "Paper" and b_move == "Rock":
    print(a+" Win")
elif a_move == "Scissor" and b_move == "Paper":
    print(a+" Win")
elif a_move == "Rock" and b_move == "Scissor":
    print(a+" Win")
elif a_move == "Rock" and b_move == "Paper":
    print(b+" Win")
elif a_move == "Paper" and b_move == "Scissor":
    print(b+" Win")
elif a_move == "Scissor" and b_move == "Rock":
    print(b+" Win")
