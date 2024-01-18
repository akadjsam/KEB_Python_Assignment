#9.16 - 1
# def good():
#     return ['Harry', 'Ron', 'Hermione']
# print(good())

#9.16 - 2
# def get_odds(first=0,last=10):
#     num = first
#     while num < last:
#         if num % 2 == 1:
#             yield num
#         num += 1
#odd_test = get_odds()

#generator comprehension
# odd_test = (i for i in range(10) if i % 2 == 1)
# count = 0
# for i in odd_test:
#     count += 1
#     if count == 3:
#         print(i)
#         break

#9.16 - 3
# def test_deco(func):
#     def new_func(*args,**kwargs):
#         print('start')
#         f = func(*args,**kwargs)
#         print('end')
#         return f
#     return new_func
# @test_deco
# def test_func(a, b):
#     return a + b
# print(test_func(5,8))

#9.16 - 4
# class OopsException(Exception):
#     print('Caught an oops')
#
# words = ['ent','mee','min','MO']
# try:
#     for i in words:
#         if i.isupper():
#             raise OopsException(i)
# except OopsException as exc:
#     print('예외 발생 : ', exc)j