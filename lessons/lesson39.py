# Mavzu:  [Abstruction]   OOP oxirigi tushunchasi 
# Abstruction -Bu funksiyada nima qilinishi aniq lekin tanasi mavjud emas 
# Bu obyekta yonaltirilgan dasturlash. 
# Bu tamamyi bilan murakab tizimlar sodalashatiriladi va faqat kerakli malumotlar taqdim etiladi 
## Abstraksiya va enkapsulaytion ortassidagi farq - faqat muhim xususiyatlarini ajratib 

from abc import ABC,abstractmethod

# Abstruct classdan obyect olib bolmaydi 
# Abstryct class abstrack  fuksiya yozish kerak
# va Abstruc funksiyada  tana bolmaydi  


class Shape(ABC):
     def __init__(self):
         super().__init__()
         self.yuzassi = 0
    
     @abstractmethod
     def yuza(self):
          pass

# New class
# Agar biror class abstruct classdan meros olsa undagi barcha abstruc
#  funksiyalarini qayta yozish kerak

class Uchburchak (Shape):
     def __init__(self):
          super().__init__()
    
     def yuza(self):
        print("Uchburchak yuza hisoblanadi")
    

shakl = Uchburchak()