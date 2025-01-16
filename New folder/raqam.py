import bcrypt
import json

# Foydalanuvchilarni saqlash uchun oddiy lug'at (dictionary)
users_db = {}
# Mashina raqamlarini saqlash uchun oddiy lug'at (dictionary)
car_db = {}

# 1. Foydalanuvchi ro'yxatdan o'tkazish funksiyasi
def register_user(users_db, email, password):
    if email in users_db:
        return "Bu email bilan foydalanuvchi mavjud"
    
    # Parolni shifrlash
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    # Foydalanuvchini bazaga qo'shish
    users_db[email] = hashed_password
    return "Foydalanuvchi ro'yxatdan o'tkazildi"

# 2. Foydalanuvchini tizimga kirish funksiyasi
def login_user(users_db, email, password):
    if email in users_db and bcrypt.checkpw(password.encode('utf-8'), users_db[email]):
        return "Tizimga kirish muvaffaqiyatli"
    else:
        return "Xato email yoki parol"

# 3. Mashina raqamini qo'shish funksiyasi
def add_car(car_db, car_number, price):
    car_db[car_number] = price
    return f"Raqam {car_number} qo'shildi"

# 4. Mashina raqamini ko'rish funksiyasi
def view_car(car_db, car_number):
    if car_number in car_db:
        return f"Raqam {car_number} narxi: {car_db[car_number]}"
    else:
        return "Raqam topilmadi"

# 5. To'lovni tasdiqlash funksiyasi
def process_payment(balance, amount):
    if amount <= balance:
        balance -= amount
        return f"To'lov muvaffaqiyatli amalga oshirildi. Yangi balans: {balance}"
    else:
        return "Balans yetarli emas"

# 6. Barcha mashina raqamlarini ko'rish funksiyasi
def view_all_cars(car_db):
    if car_db:
        return car_db
    else:
        return "Mashina raqamlari mavjud emas"

# 7. Mashina raqamini o'chirish funksiyasi
def delete_car(car_db, car_number):
    if car_number in car_db:
        del car_db[car_number]
        return f"Raqam {car_number} o'chirildi"
    else:
        return "Raqam topilmadi"

# 8. Ma'lumotlarni faylga yozish funksiyasi
def save_data_to_file(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)
    return "Ma'lumotlar faylga saqlandi"

# 9. Fayldan ma'lumotlarni o'qish funksiyasi
def load_data_from_file(filename):
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return {}

# Foydalanuvchi va mashina raqamlari bilan amaliyotlar

# 1. Foydalanuvchi ro'yxatdan o'tkazish
print(register_user(users_db, 'user1@example.com', 'password123'))

# 2. Foydalanuvchi tizimga kirish
print(login_user(users_db, 'user1@example.com', 'password123'))

# 3. Mashina raqamini qo'shish
print(add_car(car_db, 'ABC123', 50000))

# 4. Mashina raqamini ko'rish
print(view_car(car_db, 'ABC123'))

# 5. To'lovni tasdiqlash
print(process_payment(100000, 50000))

# 6. Barcha mashina raqamlarini ko'rish
print(view_all_cars(car_db))

# 7. Mashina raqamini o'chirish
print(delete_car(car_db, 'ABC123'))

# 8. Ma'lumotlarni faylga saqlash
save_data_to_file(car_db, 'cars_data.json')
save_data_to_file(users_db, 'users_data.json')

# 9. Fayldan ma'lumotlarni o'qish
loaded_car_data = load_data_from_file('cars_data.json')
loaded_user_data = load_data_from_file('users_data.json')
print("Fayldan o'qilgan mashina ma'lumotlari:", loaded_car_data)
print("Fayldan o'qilgan foydalanuvchi ma'lumotlari:", loaded_user_data)
