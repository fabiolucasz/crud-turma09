from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Criando engine e base
engine = create_engine("sqlite:///alunos.db", echo=True)
Base = declarative_base()

# Definindo o modelo (tabela)
class Aluno(Base):
    __tablename__ = "alunos"
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)

# Criando tabela no banco
Base.metadata.create_all(engine)

# Criando sessão
Session = sessionmaker(bind=engine)
session = Session()

def criar_aluno():
    novo_aluno = Aluno(nome="Riquelme joga fácil", idade=55)
    session.add(novo_aluno)
    session.commit()


def editar_aluno():
    aluno = session.query(Aluno).filter(Aluno.nome == "Ybson").first()

    if aluno:
        aluno.idade = 15
        session.commit()
        print("Aluno atualizado com sucesso!")
    else:
        print("Aluno não encontrado.")

def deletar_aluno():
    aluno = session.query(Aluno).filter(Aluno.id == 4).first()

    if aluno:
        session.delete(aluno)
        session.commit()
        print("Aluno removido com sucesso!")
    else:
        print("Aluno não encontrado.")


def listar_alunos():
    lista.delete(0, tk.END)
    alunos = session.query(Aluno).all()
    for aluno in alunos:
        lista.insert(tk.END, f"ID: {aluno.id} | Nome: {aluno.nome} | Idade: {aluno.idade}")

# Criação da tela

import tkinter as tk

janela = tk.Tk()
janela.geometry("400x500")

#Campo nome
label_nome = tk.Label(janela, text="Nome")
label_nome.pack()
entry_nome = tk.Entry(janela)
entry_nome.pack()

#Campo idade
label_idade = tk.Label(janela, text="Idade")
label_idade.pack()
entry_idade = tk.Entry(janela)
entry_idade.pack()

#Botão adicionar aluno
btn_adicionar_aluno = tk.Button(janela, text="Adicionar",
                                command=criar_aluno)
btn_adicionar_aluno.pack()

lista = tk.Listbox(janela, width=50, height=15)
lista.pack()


listar_alunos()
janela.mainloop()
