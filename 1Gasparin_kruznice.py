import math
import os
os.system('cls')



print("Zadejte parametry kružnice #1:")
x1 = float(input("x1:"))
y1 = float(input("y1:"))
r1 = float(input("r1:"))

print("Zadejte parametry kružnice #2:")
x2 = float(input("x2:"))
y2 = float(input("y2:"))
r2 = float(input("r2:"))



if(x1 < x2):
    a = x2-x1
else:
    a = x1-x2
#                   výpočet pro vzálenodt středů pomocí pythagorovy věty
if(y1 < y2):
    b = y2-y1
else:
    b = y1-y2

c = math.sqrt(a**2 + b**2) #přepona



#odtud po další komentář je kód, který jsem velmi inspiroval z internetu
if (c > (r1 + r2)): #kružnice leží zcela mimo sebe tudíž nemůže být žadný průnik
    prun = 0

elif (c <= (r1 - r2) and (r1 >= r2)): #jedna kružnice leží uvnitř druhé,či splývají, a proto počitame obsah kružnice což je pi * r**2
    prun =(math.pi * r2**2)

elif (c <= (r2 - r1) and (r2 >= r1)): #ten samý případ, jako nahoře, akorát uvnitř leží druhá kružnice
    prun = (math.pi * r1**2)

else: #když všecho seshora failne, tak se do toho vloží tenhle složitej vzorec, který mám z internetu a s myslí prváka se nedá pochopit
    alpha = math.acos(((r1**2) + (c**2) - (r2**2)) / (2 * r1 * c)) * 2
    beta = math.acos(((r2**2) + (c**2) - (r1**2)) / (2 * r2 * c)) * 2

    a1 = (0.5 * beta * r2**2) - (0.5 * r2**2 * math.sin(beta))
    a2 = (0.5 * alpha * r1**2) - (0.5 * r1**2 * math.sin(alpha))
    prun = (a1 + a2)
#potud




if(math.isclose(x1,x2) and math.isclose(y1,y2) and math.isclose(r1,r2)):
    print("kružnice splývají", prun)

elif((r1 - r2) > c):
    print("jedna kružnice leží zcela uvnitř druhé", prun)

elif((r1 + r2) < c):
    print("kružnice leží zcela mimo sebe")

elif((r1 + r2) == c):
    print("kružnice se dotýkají zvenku")

elif((r1 - r2) == c):
    print("jedna kružnice se zevnitř dotýká druhé",prun)

elif((r1 - r2) < c) and (c < (r1 + r2)):
    print("kružnice se protínají", prun)













# import math
# from math import sqrt, fabs

# x1 = float(input("Zadejte souřadnici x1: "))
# y1 = float(input("Zadejte souřadnici y1: "))
# r1 = float(input("Zadej poloměr r1: "))

# x2 = float(input("Zadejte souřadnici x2: "))
# y2 = float(input("Zadejte souřadnici y2: " ))
# r2 = float(input("Zadej poloměr r2: "))



# s = (sqrt((x2-x1)**2 + (y2-y1)**2))  #s = vzdálenost středů
# roz_r = fabs(r1-r2)
# sou_r = r1 + r2



# #funkce 1, kružnice splývají
# if math.isclose(x1, x2) and math.isclose(y1, y2) and math.isclose(r1,r2):
#     print("")
#     print("Kružnice splývají")
#     print("")
# else:
#     print("Kružnice nesplývají")



# #funkce2, jedna kružnice leží zcela uvnitř druhé
# if s < roz_r:
#     print("")
#     print("Jedna kružnice leží zcela uvnitř druhé")
#     print("")
# else:
#     print("Jedna kružnice neleží zcela uvnitř druhé")



# #funkce3, jedna kružnice se zevnitř dotýká druhé
# if s == roz_r:
#     print("")
#     print("Jedna kružnice se zevnitř dotýká druhé")
#     print("")
# else:
#     print("Jedna kružnice se zevnitř nedotýká druhé")



# #funkce4, kružnice se protínají
# if roz_r < s < sou_r:
#     print("")
#     print("Kružnice se protínají")
#     print("")
# else:
#     print("Kružnice se neprotínají")



# #funkce 5, kružnice se dotýkají zvenku
# if s == sou_r:
#     print("")
#     print("Kružnice se dotýkají zvenku")
#     print("")
# else:
#     print("Kružnice se nedotýkají zvenku")



# # funkce 6, kružnice leží zcela mimo sebe.
# if s > sou_r:
#     print("")
#     print("Kružnice leží zcela mimo sebe")
#     print("")
# else:
#     print("Kružnice neleží mimo sebe")