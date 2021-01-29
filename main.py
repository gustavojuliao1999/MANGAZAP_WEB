import os
try:
    from pywebcopy import save_webpage
except ImportError:
    os.system('python -m pip install pywebcopy')
from pywebcopy import save_webpage
import shutil
import sqlite3
import datetime

#CONEXÃO SQL
conn = sqlite3.connect('database.db')
#DEFININDO CURSOR
cursor = conn.cursor()
#conn.close()
loc_mangas = "./download/unionleitor.top/leitor/mangas/"
log = []
erro = []

def data(tipo):
    data = datetime.datetime.now()
    #1 = yyyy-mm-dd
    if(tipo == 1):
        return (str(data.year) + "-" + str(data.month) + "-" + str(data.day))

def tabelas_sql():
    global cursor

    #CRIA OU FERIFICA SE EXISTE A TABELA MANGAS
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS mangas (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            url TEXT,
            cap INTEGER,
            local TEXT,
            criado_em DATE NOT NULL,
            atualizado_em DATE NOT NULL
    );
    """)

def cad_sql(nome,url,cap,loc):
    global cursor
    cursor.execute("SELECT * FROM mangas WHERE url=?", (url,))
    rows = cursor.fetchall()
    print(rows)
    print(len(rows))

    for row in rows:
        print(row)
    if(len(rows) > 0):
        #FAZ ATUALIZAÇÃO DO CADASTRO CASO EXISTA

        id_cad = rows[0][0]
        print("ID:" + str(id_cad))

        cursor.execute("""
        UPDATE mangas
        SET cap = ?, atualizado_em = ?
        WHERE id = ?
        """, (cap, data(1), id_cad))
    else:
        # inserindo dados na tabela mangas
        cursor.execute("""
        INSERT INTO mangas (name, url, cap, local, criado_em, atualizado_em)
        VALUES (?,?,?,?,?,?,)
        """,(nome,url,int(cap),loc,data(1),data(1)))
    conn.commit()
def repair_all_files(tipo):
    global cursor
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
                    rename_pag2 = str(rename_pag[1]).replace("(", "")
                except:
                    rename_pag2 = rename_pag

                try:
                    rename_pagf = str(rename_pag2).replace(")", "")
                except:
                    rename_pagf = rename_pag2
                print("     Rf:" + rename_pagf)
                os.rename(loc_pag + pag, loc_pag + rename_pagf)
def repair_files(nome):
    print(nome)
    for cap in os.listdir(loc_mangas + nome):
        print(" " + cap)
        for pag in os.listdir(loc_mangas + nome + "/" + cap):
            loc_pag = (loc_mangas + nome + "/" + cap + "/")
            print("     " + pag)
            rename_pag = str(pag).split("__")
            print(rename_pag)
            try:
                rename_pag2 = str(rename_pag[1]).replace("(", "")
            except:
                rename_pag2 = rename_pag

            try:
                rename_pagf = str(rename_pag2).replace(")", "")
            except:
                rename_pagf = rename_pag2
            print("     Rf:" + rename_pagf)
            os.rename(loc_pag + pag, loc_pag + rename_pagf)
def download_manga(url, option):
    global log
    global erro

    #Pega capitulo manga da URL
    cap = str(url).split("/")
    cap = cap[len(cap) - 1]


    #Pega Nome do Mangá na URL
    nome_manga = url.split("/")
    nome_manga = nome_manga[len(nome_manga) - 2]
    print("Nome do Mangá: " + nome_manga)
    if(cap == ""):
        m_url = url
        return ("Erro")
    else:
        m_url = url.split(cap)
        m_url = m_url[0]
    print("URL:"+m_url)
    print("Capitulo Mangá:" + str(cap))
    input("Deseja continuar?")

    #Começa Download Mangá
    """For que Baixa um Mangá por Vêz"""
    for i in range(int(cap)):
        #If Converte os numeros de 1 a 9 com um 0 a esquerda
        if(i < 10):
            vi = ("0"+str(i+1))
        else:
            vi = str(i+1)


        manga = (m_url + vi)

        print("Começando o Download: "+manga)
        download_folder = ''
        kwargs = {'bypass_robots': False, 'project_name': 'download', 'zip_project_folder': False}
        if(i == cap):
            print("Finalizando")
        try:
            print(save_webpage(manga, download_folder, **kwargs))
        except:
            print("Error")
            erro.append(manga)

    if os.path.isdir(loc_mangas+nome_manga):  # vemos de este diretorio ja existe
        print("Cadastando mangá - "+nome_manga)
        cad_sql(nome_manga,m_url,cap,(loc_mangas+nome_manga))
    else:
        i=0
        for nome in os.listdir(loc_mangas):
            print(str(i) + "=" + nome)
            ++i
        escolher_pasta = int(input("Escolha a que se refere o mangá:"))
        cad_sql(nome_manga,m_url,cap,(loc_mangas+loc_mangas[escolher_pasta]))

    print("Finalizado1")


print(download_manga("https://unionmangas.top/leitor/Solo_Leveling/110",2))

#download_manga("https://unionmangas.top/leitor/One_Punch-Man/131",2)
