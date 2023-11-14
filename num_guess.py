import random
i=3
while i:
    num=random.randint(1,20)
    guess_num=int(input('guess a number:  '))
    i-=1
    if guess_num==num:
        print('Correct 👍')
        break
    else:
        print(f'wrong 👎 the number is {num}')
        print(i,'chances left')