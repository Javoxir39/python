n = int(input("Garage o'lchamini kiriting: "))
import math as m
a = [[0] * n for i in range(n)] 
while 1:
    r=input("Mashina nomini kiriting: ")
    col = int(input("Ustunni kiriting: "))-1
    row = int(input("Qatorni kiriting: "))-1
    if a[row][col]==0:
        print(f"Sizning mashinaning {col+1,row+1} ga joylashtirildi")
        a[row][col]=r
    else:
        t=[];k=[];s=[]
        for i in range(n):
            for j in range(n):
                if a[i][j]==0:
                    t.append(i)
                    k.append(j)
                    s.append(m.floor(m.sqrt((col-j)**2+(row-i)**2)))
        if 0 in s:
            k.pop(s.index(0))
            t.pop(s.index(0))
            s.remove(0)
        f=min(s)
        if f>4:
            continue
        print(f"Bu yerda {a[row][col]} bor")
        while f==min(s):
            r=s.index(min(s))
            print("Siz hozirda bu yerga mashina qo'ya olmaysiz mana bu koordinataga mashina qo'ysayiz buladi:")
            print(k[r]+1,t[r]+1)
            s.pop(r);t.pop(r);k.pop(r)
        print('Boshqa koordinata kiriting!')
    for i in a:
        print(*i)