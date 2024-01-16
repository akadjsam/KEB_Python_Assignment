# 6.5 - 1
# numbers = [3,2,1,0]
# for i in numbers:
#     print(i,end=" ")

# 6.5 - 2
# guess_me = 7
# number = 1
# while True:
#     if number < guess_me:
#         print('too low')
#     elif guess_me > number:
#         print('oops')
#         break
#     else:
#         print('found it!')
#         break
#     number += 1

# 6.5 - 3
guess_me = 5
for number in range(10):
    if number < guess_me:
        print('too low')
    elif guess_me > number:
        print('oops')
        break
    else:
        print('found it!')
        break