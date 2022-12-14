from typing import List
import services.database as db;
import models.Cliente as cliente


def Incluir(cliente):
    count = db.cursor.execute("""
    INSERT INTO CLIENTE (cliNome,cliIdade, cliProfissao)
    VALUES(?,?,?)""",
    cliente.nome,cliente.idade,cliente.profissao).rowcount
    db.cnxn.commit()

def Excluir(id):
    count = db.cursor.execute("""
    DELETE FROM CLIENTE WHERE id = ?""",
    id).rowcount
    db.cnxn.commit()



def SelecionarTodos():
    db.cursor.execute("SELECT * FROM CLIENTE")
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(cliente.Cliente(row[0], row[1], row[2], row[3]))

    return costumerList
