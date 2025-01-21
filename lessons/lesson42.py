# Mavzu: Error handling- Xatoliklar bilan ishlash
# Error: Kod yozilishida yoki ishga tushirilishida yuzaga keladigan
# muammo (masalan, SyntaxError, IndentationError).
# Exception: Dastur ishlash jarayonida kuzatiladigan xatoliklar (masalan,
# ValueError, TypeError, KeyError).


# Task 1 -------------------------------------------

# while True:
#     try:
#         son = int(input("son = "))
#     except :
#         print("xatolik")

#     else:
#         for i in range(1,100):
#             print(i)
    
#     finally:
#         print("Ammal tugadi")


# Task 2 -------------------------------------------

 
def check_format(phone:str):
    """
    Bu funksiya telefon raqamini togti formata 
    ekanligini tekshiradi 
    agar xata formata bolsa xatolik qaytaradi 
    """
    if not len(phone) == 13:
        raise Exception("telefon notogri formatda ")
    return True

try:
    check_format(phone="9989384793")
except Exception as e:
    print(e)