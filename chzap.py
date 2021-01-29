from selenium import webdriver
import pickle
#pip install pickle-mixin
import time
import mysql.connector
import sqlite3
import util
import os
from datetime import datetime
os.system("emulator.bat")


dir_mangas = ("C:/MANGAZAP/mangas")





lista_mangas = ["One Punch man","Boku no Hero"]

users = []
smanga = []
class db:

    print("start DB")
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="zmanga"
    )
    mycursor = mydb.cursor()

    def __init__(self):

        print("DB")

    def connect(val,self):
        print("Connect")

    def read_titulos(self,nome):
        sql = ("SELECT * FROM titulos WHERE manga LIKE '%"+nome+"%'")
        self.mycursor.execute(sql)
        myresult = self.mycursor.fetchall()
        for x in myresult:
            print(x)
        if myresult == []:
            return "None"
        else:
            return myresult


    def list_database(self):
        self.mycursor.execute("SHOW DATABASES")
        for x in self.mycursor:
            print("data:"+x[1])
    def list_titulos(self):
        sql = ("SELECT * FROM titulos ORDER BY data_modificacao DESC ")
        self.mycursor.execute(sql)
        myresult = self.mycursor.fetchall()
        #SELECT * FROM `titulos` ORDER BY `titulos`.`data_modificacao` DESC
        return myresult


    def sv_historico_user(self,numero,manga,cap):
        #INSERT INTO `historico_user` (`id`, `numero`, `manga`, `cap`, `data`) VALUES (NULL, 'test', 'one punch man', '20', '2020-08-09 00:42:57');
        sql = ("INSERT INTO historico_user (numero, manga, cap, data) VALUES (%s, %s, %s, current_timestamp())")
        val = (str(numero),str(manga),str(cap))
        self.mycursor.execute(sql,val)
        self.mydb.commit()
    def sv_nao_encontrado(self,numero,manga,cap):
        sql = ("INSERT INTO erro_manga (numero, manga, cap, data) VALUES (%s, %s, %s, current_timestamp())")
        val = (str(numero), str(manga), str(cap))
        self.mycursor.execute(sql, val)
        self.mydb.commit()
    def pega_ultimo_historico(self,numero):
        sql = ("SELECT * FROM historico_user WHERE numero LIKE '%"+numero+"%' ORDER BY data DESC ")
        self.mycursor.execute(sql)
        myresult = self.mycursor.fetchall()
        print("Ultimo Historico User:"+str([myresult[0][2],myresult[0][3]]))
        return [myresult[0][2],myresult[0][3]]
class data:
    def data_hora_texto(self):
        data_e_hora_atuais = datetime.now()
        data_e_hora_em_texto = data_e_hora_atuais.strftime(" % d / % m / % Y % H: % M")
        return str(data_e_hora_em_texto)

class log:
    arquivo = open("log.txt", "a")
    def erro_critico(self,erro):
        self.arquivo.write(data.data_hora_texto(data)+" - CRITICO - "+str(erro))
        self.arquivo.close()
    def erro_atencao(self,erro):
        self.arquivo.write(data.data_hora_texto(data)+" - ATENCAO - "+str(erro))
        self.arquivo.close()
    def info(self,erro):
        self.arquivo.write(data.data_hora_texto(data)+" -  INFO   - "+str(erro))
        self.arquivo.close()

#name = input('Enter the name of user or group : ')
#msg = input('Enter your message : ')
#count = int(input('Enter the count : '))
class arquivos:
    global dir_mangas
    def get_mangas(self):
        print("Mangas")
    def get_capitulo(self,manga,capitulo):
        global dir_mangas
        dbmanga = db.read_titulos(db,manga)
        if(int(capitulo) < 10):
            capitulo = "0"+str(capitulo)
            print("Capitulo:"+capitulo)
        listdir = dir_mangas+"/"+str(dbmanga[0][2])+"/"+str(capitulo)
        print("Dir:"+str(listdir))
        capitulos = os.listdir(listdir)
        #capitulos = sorted(capitulos, key=float)
        capitulos = sorted(capitulos)
        print("Capitulos:"+str(capitulos))
        return [str(listdir),capitulos]
    def get_ultimo_cap(self,manga):
        global dir_mangas
        dbmanga = db.read_titulos(db,manga)
        listdir = dir_mangas+"/"+str(dbmanga[0][2])
        listdir = os.listdir(listdir)
        listdir = sorted(listdir, key=float)
        print("ListDir:"+str(listdir))
        ultimo_cap = listdir[(len(listdir)-1)]
        print('Ultimo Capitulo:'+str(ultimo_cap))
        return ultimo_cap
    def get_capitulos_manga(self,manga):
        global dir_mangas
        dbmanga = db.read_titulos(db, manga)
        listdir = dir_mangas + "/" + str(dbmanga[0][2])
        listdir = os.listdir(listdir)
        listdir = sorted(listdir, key=float, reverse= True )
        print("ListDir:" + str(listdir))
        capitulos = ""
        for cap in listdir:
            capitulos = capitulos + "," + str(cap)
        return [capitulos,listdir[0],listdir[len(listdir)-1]]

class envia:
    def imagem(self,manga,capitulo,name):
        cap_imgs = []
        temp_imgs = []
        arq_cap = arquivos.get_capitulo(arquivos, manga, capitulo)
        #print("arq_cap:"+str(arq_cap))
        contador = 1
        v=0
        for ac in arq_cap[1]:
            #print("Ac:"+str(ac))
            #print("contador:"+str(contador))
            #print("V:"+str(v))
            if contador < 29:
                temp_imgs.append(ac)
                contador = contador+1
            else:
                print(str(v)+" Temp_img:"+str(temp_imgs))
                contador = 1
                v = v+1
                cap_imgs.append(temp_imgs)
                temp_imgs = []
                temp_imgs.append(ac)

        cap_imgs.append(temp_imgs)
        print("cap_imgs"+str(cap_imgs))
        for i in cap_imgs:
            print("Test_cao_imgs:"+str(i))

        for i in cap_imgs:
            print("Enviando Imagem")
            print("Eviando imagens:"+str(i))
            # time.sleep(2)
            user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
            user.click()
            time.sleep(1)
            gclick = driver.find_element_by_xpath('//span[@data-testid = "clip"]')
            gclick.click()
            # time.sleep(2)
            uploadimage = driver.find_element_by_xpath(
                '//input[@accept = "image/*,video/mp4,video/3gpp,video/quicktime"]')
            input_upload = "C:/MANGAZAP/mangas/ZMANGA.png"
            for cap in i:
                input_upload = (input_upload + "\n" + arq_cap[0] + "/" + cap)
            print("Input Upload:" + str(input_upload))
            # uploadimage.send_keys("C:/MANGAZAP/mangas/serverino.png \n C:/MANGAZAP/mangas/torrese.png")
            uploadimage.send_keys(input_upload)
            while True:
                try:
                    time.sleep(1)
                    click_send = driver.find_element_by_xpath("//span[@data-testid = 'send']")

                    print("Imagens Eviadas")
                    break
                    #return True
                except:
                    print("Tentando Enviar Novamente")
                    time.sleep(1)
            while True:
                try:
                    click_send.click()
                    break
                except:
                    print("Clicando NOvamente")
            time.sleep(1)

            print("CLICANDO Enviando Imagem")


    def texto(name,msg,repet):
        # name = "Eu"
        # msg = "Test"
        t = 0
        try:
            if repet == False:
                print("repeticao desativada")
            elif repet == True:
                print("repeticao ativada")
        except:
            repet = True
        while True:
            try:
                print("Tentando Enviar")
                user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
                user.click()
                time.sleep(3)
                msg_box = driver.find_element_by_class_name('_3uMse')
                if msg_box.send_keys(msg):
                    print("true")

                button = driver.find_element_by_class_name('_1U1xa')
                button.click()

                # driver.refresh()
            except Exception as e:
                print("Erro")
                print(t)
                t = t + 1
                print("Erro(" + str(t) + ") ao Enviar")
                if t >= 10:
                    break
                    return False

            # Pega todas as conversas carregadas
            post = driver.find_elements_by_class_name("eRacY")
            # Pega a Ultima Conversa
            ultimo = len(post) - 1
            # Pega o texto da ultima mensagem
            texto = post[ultimo].text
            print("Mensagem:" + texto)
            if texto == msg:
                print("Mensagem Eviada")
                volta()
                return True
                break
            elif repet == False:
                print("Mensagem Enviada sem Repet")
                volta()
                return True
                break





def volta():
    global driver
    #print("""Procura Grupo CLICK""")
    try:
        gclick = driver.find_element_by_xpath("//span[@title = 'CLICK']")
        #print("CLICANDO:"+gclick.text)
        gclick.click()
    except Exception as e:
        print("Erro Click Volta:")

#lê mensagem
def ultima_msg():
    global driver
    """ Captura a ultima mensagem da conversa """
    try:
        #Procura mensagem não lida
        #print("----------------------------")
        #print("Iniciando Procura")
        op = driver.find_element_by_xpath('//span[@class="_31gEB"]')
        op.click()
        time.sleep(1)
        #Leva a até o final da página
        print("Verificando Se está no FIM da Página")
        try:
            d_message = driver.find_element_by_xpath('//span[@class="RbeWt"]')
            d_message.click()
        except Exception as e:
            print("Já está no Fim da página")
        #Pega Numero Telefone
        print("Pegando Numero Telefone")
        numerostele = driver.find_elements_by_xpath('//span[@class="_3ko75 _5h6Y_ _3Whw5"]')
        ultimo_numero = len(numerostele) - 1
        numerotele = numerostele[ultimo_numero].text
        print("Numero Telefone:"+numerotele)
        #Pega todas as conversas carregadas
        post = driver.find_elements_by_class_name("eRacY")
        #Pega a Ultima Conversa
        ultimo = len(post) - 1
        #Pega o texto da ultima mensagem
        texto = post[ultimo].text
        print("Ultima Mensagem:"+texto)
        #driver.refresh()
        volta()
        return [texto,numerotele]
    except Exception as e:
        #print("Erro ao ler msg, tentando novamente!")
        volta()
        return ""



class opcoes:
    conn = sqlite3.connect(":memory:")
    c = conn.cursor()
    c.execute('''CREATE TABLE users
             (numero text, manga text, cap text, send int)''')
    c.execute("""INSERT INTO users (numero, manga)
                VALUES ('test', 'one punch man')""")
    def process_mensagem(self,mensagem):
        print("")
    def list_users_sql(self):
        self.c.execute("SELECT * from users")
        for linha in self.c.fetchall():
            print("LIST SQL USERS:"+str(linha))

    def opcao(self,mensagem,numero):
        global lista_mangas
        #numero = "tes"
        #mensagem = "one punch 20"
        print("Mensagem:"+str(mensagem))

        # verifica se o usuario existe
        self.c.execute("SELECT * FROM users WHERE numero = '"+numero+"' ")
        sqluser = self.c.fetchall()
        if mensagem == "ajuda" or mensagem == "help" or mensagem == "Ajuda":
            msg_ajuda = ("""
                         Para Pedir mangar e so digitar \n
                         O manga e depois o capitulo \n
                         One Punch Man 126 ou \n
                         One Punch Ultimo /  U \n
                         Para lêr o ultimo capitulo lançado
                         \n
                         Comandos: \n
                         proximo ou p - vai para o proximo capitulo \n
                         
                         """)

            envia.texto(numero,msg_ajuda,False)
        elif mensagem == "mangas" or mensagem == "Mangas" or mensagem == "manga" or mensagem == "Manga":
            msg_mangas = "Mangas:"
            #SELECT * FROM `titulos` ORDER BY `titulos`.`data_modificacao` DESC
            for i in db.list_titulos(db):
                msg_mangas += str(i[1])+" "+str(i[3])+" , "
            envia.texto(numero,str(msg_mangas),False)
        else:
            try:
                if (len(sqluser) > 0):
                    sqlmanga = str(sqluser[0][1])
                    sqlcaptulo = str(sqluser[0][2])
                    print("Manga:" + sqlmanga)
                    print("Cap:" + sqlcaptulo)
                    if sqlmanga == "None" and sqlcaptulo == "None":
                        print("None,None")
                        if mensagem == "proximo" or mensagem == "p" or mensagem == "Próximo" or mensagem == "P" or mensagem == "Proximo" or mensagem == "próximo":
                            ultimo_manga = db.pega_ultimo_historico(db, numero)
                            mensagem = str(str(ultimo_manga[0]) + " " + str(ultimo_manga[1] + 1))

                        try:

                            capitulo = mensagem.split()
                            capitulo = str(capitulo[len(capitulo) - 1])
                            print("Len Capitulo:"+capitulo)
                            if capitulo == "ultimo" or capitulo == "Ultimo" or capitulo == "Último" or capitulo == "último" or capitulo == "U" or capitulo == "U":
                                manga = str(mensagem.replace((" " + str(capitulo)), ""))
                                capitulo = int(arquivos.get_ultimo_cap(arquivos,manga))
                            else:
                                capitulo = int(capitulo)
                                manga = str(mensagem.replace((" " + str(capitulo)), ""))
                            #manga = str(mensagem.replace((" " + str(capitulo)), ""))
                            print("Manga:" + str(manga))
                            print("Capitulo:" + str(capitulo))
                            db_titulos = db.read_titulos(db, manga)
                            if db_titulos == "None":
                                print("Mangá não encontrado1")
                                envia.texto(numero, "manga não encontado Vamos analisar e Adicionar 1",True)
                                db.sv_nao_encontrado(db, numero, manga, capitulo)
                            else:
                                print(str(db_titulos[0]))
                                self.c.execute("UPDATE users SET manga = ?, cap = ? WHERE numero = ?",
                                               (manga, str(capitulo), numero))
                                self.conn.commit()
                                msg_envia = str("Manga:" + str(db_titulos[0][1]) + " Cap:" + str(capitulo))
                                envia.texto(numero, msg_envia,True)
                                envia.imagem(envia, manga, capitulo, numero)
                                self.c.execute("UPDATE users SET manga = ?, cap = ? WHERE numero = ?",
                                               ("None", "None", numero))
                                self.conn.commit()
                                db.sv_historico_user(db, numero, str(db_titulos[0][2]), capitulo)
                        except:
                            print("Test639")
                            manga = str(mensagem)
                            db_titulos = db.read_titulos(
                                db, manga)
                            if db_titulos == "None":
                                print("Manga não encontrado2")
                                envia.texto(numero, "manga não encontado Vamos analisar e Adicionar 2",True)
                                cap = "Null"
                                db.sv_nao_encontrado(db, numero, manga, cap)
                            else:
                                print(str(db_titulos[0]))
                                self.c.execute("UPDATE users SET manga = ? WHERE numero = ?",
                                               (str(db_titulos[0][2]), numero))
                                self.conn.commit()
                                print("Falta o Capitulo, Escolha entre esses")
                                get_capitulo_manga = arquivos.get_capitulos_manga(arquivos,manga)
                                msg_falta_cap = "Digite no numeor do capitulo, Escolha entre esses "+ get_capitulo_manga[1]+ " e "+get_capitulo_manga[2]
                                envia.texto(numero, msg_falta_cap,True)
                        # envia("Digite o Manga")
                    elif sqlmanga != "None" and sqlcaptulo == "None":
                        print("Cap NONE")
                        try:
                            capitulo = int(mensagem)
                            self.c.execute("UPDATE users SET cap = ? WHERE numero = ?",
                                           (capitulo, numero))
                            self.conn.commit()
                            print("Capitulo Cad")
                            self.c.execute("SELECT * FROM users WHERE numero = '" + numero + "' ")
                            user = self.c.fetchall()[0]
                            envia.texto(numero, str("Manga:" + user[1] + " Cap:" + user[2]),True)
                            envia.imagem(envia, user[1], user[2], numero)
                            self.c.execute("UPDATE users SET manga = ?, cap = ? WHERE numero = ?",
                                               ("None", "None", numero))
                            db.sv_historico_user(db, user[0], user[1], user[2])

                        except:
                            print("Digite o Numero do Capitulo")
                            envia.texto(numero, "Digite o Numero do Capitulo",True)

                        print("Pede Capitulo")
                    print("Test852")
                    opcoes.list_users_sql()


                else:
                    self.c.execute("INSERT INTO users (numero) VALUES ('" + numero + "')")
                    self.conn.commit()
                    self.c.execute("SELECT * FROM users WHERE numero = '" + numero + "' ")
                    for n in self.c.fetchall():
                        print("SQL " + str(n))
                    self.opcao(mensagem, numero)
                return "tets"
            except Exception as erro_critico:
                print("Erro Critico: "+str(erro_critico))
                log.erro_critico(log,erro_critico)










driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
time.sleep(1)
util.fullpage_screenshot(driver, "Print site.png")

database = db()
arquivos.get_capitulo(arquivos,"one punch",30)
opcoes = opcoes()
while True:
    msg = ultima_msg()
    #print("Mensagem:" + str(msg))
    if msg != "":
        opcoes.opcao(msg[0],msg[1])
        msg == ""
    time.sleep(1)



#val = database.read_titulos("one")
#print(val[0][1])
#valop = ["one punch 110","Gustavo"]

#database.list_database()
#db.read_titulos()