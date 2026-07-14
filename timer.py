import datetime
import os
import time
import json
import sqlite3
import config
import importlib
conn = sqlite3.connect("estudo.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS
Estudar
(
materies TEXT UNIQUE,
ID INTEGER PRIMARY KEY AUTOINCREMENT,
hours_studied REAL,
Limite INTEGER
) ''')



conn.commit()
print("funcionou")

sec =[0]
minuto =[0]
h = [0]
n =True
def delete(materie):
    cursor.execute(f'''DELETE FROM ESTUDAR
    WHERE ID =?
    ''',(materie,))
    conn.commit()
def reset():
    cursor.execute('''UPDATE ESTUDAR
    SET hours_studied = 0.0
    ''')
    conn.commit()
def add_materie(materie,limite):
    cursor.execute('''INSERT INTO Estudar 
    (materies,Limite,hours_studied)VALUES
    (?,?,?)''',(materie,limite,0.0))
    conn.commit()
    
def timer(materie):
    sec =[]
    minuto =[]
    h =[]
    sec.append(0)
    minuto.append(0)
    h.append(0)
    cursor.execute(f'''SELECT hours_studied FROM Estudar
           WHERE ID =?''',(materie,))
    marcador= cursor.fetchall()
    try:
        while True:
           importlib.reload(config)
           time.sleep(60)
           
           
    
           minuto[0]+=1
               
           if minuto[0] ==60:
               
               minuto[0] =0
               h[0] +=1
           txt = f"{h[0]}.{minuto[0]}"
           
          
           
           
           cursor.execute(f'''SELECT hours_studied FROM Estudar
           WHERE ID =?''',(materie,))
           contador= cursor.fetchall()
           
           cursor.execute(f''' SELECT Limite FROM Estudar
           WHERE ID=?''',(materie,))
           limite_de_estudos = cursor.fetchall()
           if limite_de_estudos[0][0] > contador[0][0]:
              
               horário_estudado = float(txt)
               
               cursor.execute(f'''UPDATE Estudar
               SET hours_studied ={marcador[0][0] + horário_estudado}
               WHERE ID =? ''',(materie,))
               conn.commit()
           else:
               print("limite de estudos da matéria atingido")
               return
           
           
           
           
           
           
           
    except KeyboardInterrupt:
        print("timer parado")
try:
    anti_hiperloader = False
    
    while True:
        importlib.reload(config)
        question_add = config.no
        if question_add.upper() =="SIM" or question_add.upper() == "S":
            materie_added = config.materie
            limit_materie = config.limite
            add_materie(materie_added,limit_materie)
        
        if question_add.upper() !="SIM" and anti_hiperloader == False:
            anti_hiperloader = True
            print("ok")
           
        
        
        
        cursor.execute('''SELECT ID FROM Estudar''')
        
        id_list = cursor.fetchall()
        cursor.execute('''SELECT materies FROM Estudar''')
        materies_list = cursor.fetchall()
        
        print(f'''ids:{id_list}/
matérias:{materies_list}
        ''')
        delete_question = config.no
        
        if delete_question.upper() == "SIM" or delete_question.upper() =="S":
            delete_confirm = config.id
            delete(delete_confirm)
        
        cursor.execute('''SELECT hours_studied FROM Estudar ''')
        
        hours_list = cursor.fetchall()
        
        cursor.execute('''SELECT Limite FROM Estudar ''')
        limit_list = cursor.fetchall()
        
        
        confirmador =[]
        for i in range(len(hours_list)):
           if hours_list[i][0] >= limit_list[i][0]:
                confirmador.append(0)
            
           if len(confirmador) >=len(hours_list):
                
                reset_question = config.yes
                print("tabelas cheias")
                
                if reset_question.upper() =="SIM" or reset_question.upper() =="S":
                    
                    reset()
            
        
        
          
        study_question = config.yes
        if (study_question.upper() =="SIM" or study_question.upper() =="S") and n ==True:
            
            matéria_estudada = config.id
            n=False
            timer(matéria_estudada)
            
        
except KeyboardInterrupt:
    print("código parado")
    

    