import math
import os
os.system('cls')



print("Zadeje parametry trojúhelníku #1:")
x1 = float(input("x1:"))
y1 = float(input("y1:"))
x2 = float(input("x2:"))
y2 = float(input("y2:"))
x3 = float(input("x3:"))
y3 = float(input("y3:"))

a1 = math.sqrt(((x1-x2)**2)+((y1-y2)**2)) #výpočet délky strany pomocí pythagorovy věty
b1 = math.sqrt(((x2-x3)**2)+((y2-y3)**2))
c1 = math.sqrt(((x3-x1)**2)+((y3-y1)**2))


o1= a1 + b1 + c1


print("Zadeje parametry trojúhelníku #2:")
x4 = float(input("x4:"))
y4 = float(input("y4:"))
x5 = float(input("x5:"))
y5 = float(input("y5:"))
x6 = float(input("x6:"))
y6 = float(input("y6:"))

a2 = math.sqrt(((x4-x5)**2)+((y4-y5)**2))
b2 = math.sqrt(((x5-x6)**2)+((y5-y6)**2))
c2 = math.sqrt(((x6-x4)**2)+((y6-y4)**2))

o2= a2 + b2 + c2

# print(a1,b1,c1)
# print(a2,b2,c2)
# print(o1)
# print(o2)



# 2 různé strany musí být větší jak 3 strana jinak se trojúhelník nevytvoří(rovno, protože pokud se rovnají, tak vytvoří přímku)
if((a1+b1<=c1 or b1+c1<=a1 or c1+a1<=b1) or (a2+b2<=c2 or b2+c2<=a2 or c2+a2<=b2)):
    print("Zadané body netvoří trojúhelník")

elif(math.isclose(a1,a2) or math.isclose(a1,b2) or math.isclose(a1,c2) and math.isclose(b1,a2) or math.isclose(b1,b2) or math.isclose(b1,c2) and math.isclose(o1,o2)):
    print("Zadané trojúhelníky jsou shodné")

elif((a1!=a2 or b2 or c2) and (b1!=a2 or b2 or c2) and (c1!=a2 or b2 or c2) and math.isclose(o1,o2)):
    print("Zadané trojúhelníky se liší, ale mají stejný obvod")

else:
    print("Zadané trojúhelníky jsou zcela odlišné")



# if(math.isclose(a1,a2) or math.isclose(a1,b2) or math.isclose(a1,c2) and math.isclose(b1,a2) or math.isclose(b1,b2) or math.isclose(b1,c2) and math.isclose(c1,a2) or math.isclose(c1,b2) or math.isclose(c1,c2) and o1<o2 or o1>o2):
#     print("Zadané trjúhelníky jsou zclea odlišné")

# #nemusím vypisovat stranu c1, protože když a1 či b1 se bude rovnat k nějaké straně, tak za podmínky, že jsou stejné obvody bude strana c1 rovna také k nějaké straně
# elif(math.isclose(a1,a2) or math.isclose(a1,b2) or math.isclose(a1,c2) and math.isclose(b1,a2) or math.isclose(b1,b2) or math.isclose(b1,c2) and math.isclose(o1,o2)):
#     print("Zadané trojúhelníky jsou shodné")

# else:
#     print("Zadané trjúhelníky se liší, ale mají stejný obvod")

#elif(math.isclose(a1,a2) or math.isclose(a1,b2) or math.isclose(a1,c2) and math.isclose(b1,a2) or math.isclose(b1,b2) or math.isclose(b1,c2) and math.isclose(c1,a2) or math.isclose(c1,b2) or math.isclose(c1,c2) and math.isclose(o1,o2)):



#nemusím vypisovat stranu c1, protože když a1 či b1 se bude rovnat k nějaké straně, tak za podmínky, že jsou stejné obvody bude strana c1 rovna také k nějaké straně
# if(math.isclose(a1,a2) or math.isclose(a1,b2) or math.isclose(a1,c2) and math.isclose(b1,a2) or math.isclose(b1,b2) or math.isclose(b1,c2) and math.isclose(o1,o2)):
#     print("Zadané trojúhelníky jsou shodné")

# elif(math.isclose(a1,a2) or math.isclose(a1,b2) or math.isclose(a1,c2) and math.isclose(b1,a2) or math.isclose(b1,b2) or math.isclose(b1,c2) and math.isclose(o1,o2)):
#     print("Zadané trjúhelníky se liší, ale mají stejný obvod")

# elif():
#     print("Zadané trojúhelníky jsou zcela odlišné")