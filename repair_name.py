import os
loc_mangas = "./mangas/"

def repair_all_files():
    global loc_mangas
    #Repara todos os Arquivos
    for nome in os.listdir(loc_mangas):
        print(nome)
        for cap in os.listdir(loc_mangas + nome):
            print(" " + cap)
            for pag in os.listdir(loc_mangas + nome + "/" + cap):
                loc_pag = (loc_mangas + nome + "/" + cap + "/")
                print("     " + pag)
                rename_pag = str(pag).split("__")
                print(rename_pag)
                try:
                    rename_pag2 = str(rename_pag[0]).replace("(", "")
                except:
                    rename_pag2 = rename_pag

                try:
                    rename_pagf = str(rename_pag2).replace(")", "")
                except:
                    rename_pagf = rename_pag2
                print("     Rf:" + rename_pagf)
                os.rename(loc_pag + pag, loc_pag + rename_pagf)

repair_all_files()