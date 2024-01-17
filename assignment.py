# import copy
# # 8.6 - 1
# e2f = dict(dog="chien", cat="chat", walrus="morse")
# for i,j in e2f.items():
#     print(f'{i} : {j}')
# print()
#
# # 8.6 - 2
# print(e2f.get("walrus"))
# print()
#
# #8.6 - 3
# f2e = e2f.items()
# print(f2e)
# print()
#
# #8.6 - 4
# print(list(e2f.keys())[0])
# print()
#
# #8.6 - 5
# print(", ".join(e2f.keys()))
#
# # 8.6 - 6
# life = {"animals" : {"cats" : "Henri", "octopi" : "Grumpy", "emus" : "Lucy"}, "plants" : " ", "other" : " "}
#
# # 8.6 - 7
# print(", ".join(life.keys()))
# print()
#
# # 8.6 - 8
# print(", ".join(life.get("animals").keys()))
# print()
#
# # 8.6 - 9
# print(life.get("animals").get("cats"))
# print()

# 8.6 - 10
squares = {i : i*i for i in range(10)}
print(squares)
print(type(squares))