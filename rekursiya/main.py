# # son=123
# s = 0

# def sonlar(son):
#     global s
#     if son > 0:
#         q = son % 10
#         s += 
#         sonlar( son // 10)
#     return s 
   
# print(sonlar(123))





def spelname(ism, i):
    if i < len(ism):
        print(ism[i])
        spelname(ism, i+1)

spelname('ozodbek', 0)
