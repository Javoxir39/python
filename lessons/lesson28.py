# ozim uchun takrorlash 

# FUNKSIYALAR 
# extend funksiyasining vazifasi yani tsikalni davom etirish va qoship ketish uchun ishlatiladi 

# Misol 


# my_list = [10,20,30,40,50]
# last_name = [60,70,80]
# my_list.extend(last_name)
# print(my_list)

# Ozim ishlagan misol

# my_list = [10,20,30,40]
# last_name = [50,60,70]
# my_list.extend(last_name)
# print(my_list)


# INDEX bu matindagi yoki sroyhatagi har bir elementning joylashgan joyini korsatuvchi raqamlar 

# Misol
# mevalar = ("olcha","tarvuz","qovun","mandarin") 
# print(mevalar[3])

# ozim ishlagan misol  

# mashinalar = ("Mers","BMW","Damas","Tico")
# print(mashinalar[0])




# insert Bu funksiya royxatdagi bir indexga yangi elementni qoshishga yordam beradi  va boshqa elementlarni ong tomongi siljitadi 
# Agar index royxatning uzunligi katta bolsa element royxatning oxiriga qoshiladi 

# Agar index ga kiritilgan son manfiy bolsa u indexning oiridan sanashni boshlaydi 

# mevalar = ["olma", "banan", "gilos"]
# mevalar.insert(2,"Olxori")
# print(mevalar)


# Ozim ishlagan misol 

# menu = ["Shovla","Osh","Manti","Kabob"]
# menu.insert(3,"Lagman")
# print(menu)



# Pop - bu funksiya malumotni boshqarish usuli. Bu funksiya royxatdagi malum bir indexni (yoki royxat oxitdagi elementni) qiymayini ochiradi 
# va qaytaradi 
 
# my_list = [1,2,3,4,5]
# last_name = my_list.pop(2)
# print(my_list)
# print(last_name) 


# Ozim ishlagan misol 

# my_frind = ["Abdullo","Akbar","Akmal"]
# last = my_frind.pop(2)
# print(my_frind)
# print(last)


# Remove - funsksiyasi royxatan malum ber elementni ochiradi.Agar bita element bir necha marotaba uchragan bolsa u
# faqat birinchi uchraganini ochiradi  

# menu = ["Kosa","piyola","choynak","Shisha"]
# menu.remove("piyola")
# print(menu)



# Reverse - bu funksiya royxatni qaramaqarshi tomonga aylantirip beradi
# bu metod royuxatni ozgartirishga olib keladi va yangi royxatni qaytarmaydi 
# yani bu funksiya royxatni ozgartirish uchun ishlatiladi

# name = ["Ali","Abdu","Choco","Limon"]
# name.reverse()
# print(name)  


# Sort - Bu funksiya elementlarni tartiblayda ( Katta yoki kichikligiga boycha) bu metod matini togridan togri ozgartiradi va metodi qaytarmaydi 

# num = [1,3,2,6,5,4]
# num.sort()
# print(num)

# sort orqali barcha str qata qilish 

# matn = "salom"
# uppercase_matn = matn.upper()
# print(uppercase_matn)


# number = int(input("Son kiriting = "))
# print(number)

# x = 5 > 3  # Natija: True
# y = 10 == 20  # Natija: False
# print(y)




todos={}
def edit_todo():
    show_todos()
    while True:
        raqam=int(input(" davom etish uchun 1 ni ortga qaytish uchun 2 ni bosing"))
        if raqam==1:
            edit=int(input("O'zgartirmoqchi bo'lgan todo niing id raqamini kiriting"))
            new_todo=input("o'zgartirmoqchi bo'lganiz taskni kiriting")
            todos[edit] [1]=new_todo
        elif raqam==2:
            break
        else:
            print("buunday qiymat mavjud emas")


def add_todo():
    while True:
        result=input("""
        1- Eslatmani qo'shish
        2- Asosoiy munyuga qaytish
        """)
        if result=="1":
            id=len(todos)
            todos[id+1]=[True,input("Taskni kiriting=")]
            print("Task qo'shildi")
        elif result=="2":
            break
        else:
            print("Bunday funksiya mavjud emas")

def todo_task():
    show_todos()
    Task_id=int(input("Bajarligan taks ID ni kiriting="))
    value=todos.get(Task_id)
    value[0]=False
#false qilishdan maqsad bajarilgan task uchun false degan status berish va bu ikki marta bir o'zaruvchini bir




print("Assalomu alaykum TODO dasturiga hush kelibsiz")

def show_todos():
    for k,v in todos.items():
        if v[0]==True:
            print(f"Task  id={k} task={v[1]}")
while True:
    result=input("""
    1- Eslatma qo'shish
    2- Taxrirlash
    3- Eslatmani bajarish
    4- Tarix
    5- Til
    6- Eslatmalarni ko'rish
    7- Dasturni to'xtatish             
    """)

    if result=="1":
        add_todo()
    elif result=="2":
        edit_todo()
    elif result=="3":
        pass
    elif result=="4":
        pass
    elif result=="5":
        pass
    elif result=="6":
        show_todos()
    elif result=="7":
        print("    Dastur to'xtatildi")
        break
    else:
        print("Bunday funksiya mavjud emas")
