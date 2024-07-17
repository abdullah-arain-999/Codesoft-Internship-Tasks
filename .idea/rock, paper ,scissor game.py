import random

print(('---------------------------------------'))
print(('     ROCK - PAPER - SCISSOR - GAME     '))
print(('---------------------------------------'))
print()

user_score=0
comp_score=0
ties_score=0
user_name=input('Enter your name : ')
print('Welcome To The Game --<>-- ',user_name,"\n")
print("""WINNING RULE :
1.Paper vs Rock -->Paper
2.Rock vs Scissor -->Rock
3.Scissor vs Paper -->Scissor
""")

def data():
    print('''Choices Are :
    1.Paper
    2.Rock 
    3.Scissor
    ''')
    choice = int(input('Enter Your Choice From (1 To 3) : '))
    while choice < 1 or choice > 3:
        choice = int(input('Enter Valid Input : '))
    if (choice == 1):
        user_choice = 'Paper'
    elif (choice == 2):
        user_choice = 'Rock'
    else:
        user_choice = 'Scissor'
    print("User's choice is ", user_choice)
    print('Now Its Computer Turn --> ')
    comp = []
    comp.extend(list("1"))
    comp.extend(list("3"))
    comp.extend(list("2"))
    random.shuffle(comp)
    b = 1
    a = "".join(comp[0:b])
    if (a == '1'):
        com_choice = 'Rock'
    elif (a == '2'):
        com_choice = 'Paper'
    elif (a == '3'):
        com_choice = 'Scissor'

    print("Computer's choice is ", com_choice)

    if ((user_choice == 'Paper' and com_choice == 'Rock') or (user_choice == 'Rock' and com_choice == 'Paper')):
        print('Paper Wins ')
        result = 'Paper'
    elif ((user_choice == 'Rock' and com_choice == 'Scissor') or (user_choice == 'Scissor' and com_choice == 'Rock')):
        print('Rock Wins ')
        result = 'Rock'
    elif (user_choice == com_choice):
        print('Its a Ties')
        result = 'Tie'
    else:
        print('Scissor Wins')
    user_score = 0
    comp_score = 0
    ties_score = 0
    if (result == 'Tie'):
        print('Its a Ties')
        ties_score += 1
    elif (result == user_choice):
        user_score += 1
        print(user_name ,"Win's")
    else:
        comp_score += 1
        print("Computer Win's")

    f = f'''WINNING SCORE :
        |  User Score   |  Comp Score    |     Ties  |
        |\t\t{user_score}\t    | \t\t{comp_score}\t     |\t\t{ties_score}    |
        '''
    print(f)

data()
while True:

    loop = input('Press "S" For Generate Again ! Press "E" For Exit :')
    if(loop=='S'.lower() or loop=='S'):
        data()
    elif(loop=='E'.lower()or loop=='E'):
        break
    else:
        print('Please Enter Valid Input !')

print('Thanks for visiting ')