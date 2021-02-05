import sys
y = sys.argv[1]
a = y.split(",")
b = 0
a = list(map(int, a))
for k in range(len(a)):
   try:
        x = int(a[b])
        b+=1
        sayi = x
        if x == 1:
            pass
        else:
            x-=1
            sayi-=1
        for k in range(len(a)):
           try:
                del a[x]
                x+=sayi
           except:
               pass
   except:
       pass
for l in a:
    print(l,end=" ")
