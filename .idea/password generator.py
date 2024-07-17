import random
import string

print(('------------------------------------'))
print(('      <--PASSWORD GENERATOR-->      '))
print(('------------------------------------'))

lo=string.ascii_lowercase
up=string.ascii_uppercase
di=string.digits
pun=string.punctuation


def passgenerate():
    password = int(input('Enter Length Of Password  : '))
    strconcatenate = []
    strconcatenate.extend(list(lo))
    strconcatenate.extend(list(up))
    strconcatenate.extend(list(di))
    strconcatenate.extend(list(pun))
    random.shuffle(strconcatenate)
    a = "".join(strconcatenate[0:password])
    print('Your Password is : ', a)

passgenerate()

while True:

    loop = input('Press "A" For Generate Again ! Press "E" For Exit :')
    if(loop=='A'.lower()):
        passgenerate()
    elif(loop=='E'.lower()):
        break
    else:
        print('Please Enter Valid Input !')

print('Thanks for visiting ')