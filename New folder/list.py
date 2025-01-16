raqamlar=[]
def RaqamQoshish(raqamlar):
    mashina_raqami=input( "mashinani raqamini kiriting: ")
    narx=int(input("raqamning narxini kiriting"))
    raqam={
        "raqami":mashina_raqami,
        "raqamningNarxi":narx

    }
    raqamlar.append(raqam)


sotilganRaqamlar =[] 
def sotish(raqamlar,sotilganRaqamlar):
    tekshir=(input("sotmoqchi bolgan raqamingizni kiriting: "))
    for i in raqamlar:
        if tekshir in i:
            sotilganRaqamlar.append(i) 
        if tekshir in raqamlar:
            raqamlar.pop(i)




while True:
    print("1. Raqam qoshish")
    print("2. Raqam korish")
    print("3. Raqamnisotish")
    print("4. Xarid tarixini korish")
    ask=int(input("raqamni kiriting: "))
    
    if ask==1:
        RaqamQoshish(raqamlar)
    elif ask==2:
        print(raqamlar)
    if ask ==3:
        sotish(raqamlar,sotilganRaqamlar)
    