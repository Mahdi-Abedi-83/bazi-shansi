print("salam in ye bazie. to in bazi man ye adad entekhab mikonam va to bayad on adado hads bezani age to hads aval hads bezani ye nabeghei, albate khodamam komaket mikonam:)")
import random
x = random.randrange(0, 101)
tedad_hads = 0
adad = int(input("hadset chie? = "))

while adad != x:
    if adad > x:
        print("dadash bia paein")
    if adad < x:
        print("haji boro bala")
    tedad_hads += 1
    adad = int(input("hadset chie? = "))
    
if adad == x:
    print("benazam eeeeshgh zadi to khal")
    if tedad_hads > 20:
        print("vali khodemonima kheili khari")
     
    elif tedad_hads == 0:
        print("haji bargaaaaam to avalin hads goftiii!!!!!")
    
    elif tedad_hads < 10:
        print("bahoshi damet garm chon tonesti toye", tedad_hads, "hads bezani")
