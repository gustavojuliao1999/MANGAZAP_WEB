url = input("URL:")
cap = int(input("Ultimo cap:"))
i = 0
for i in range(cap):
    if (i < 9):
        vi = ("0" + str(i + 1))
    else:
        vi = str(i + 1)
    manga = (url + vi)
    print(manga)
    #manga = (url + vi + ".5")
    #print(manga)

    #manga = (url + vi+ ".2")
    #print(manga)
#https://unionleitor.top/leitor/Kaifuku_Jutsushi_no_Yarinaoshi/28.1