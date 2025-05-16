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


novo_aluno = Aluno(nome="Riquelme joga fácil", idade=55)
session.add(novo_aluno)
session.commit()




# Buscar aluno
aluno = session.query(Aluno).filter(Aluno.nome == "Ybson").first()

if aluno:
    aluno.idade = 15
    session.commit()
    print("Aluno atualizado com sucesso!")
else:
    print("Aluno não encontrado.")

# Buscar aluno
aluno = session.query(Aluno).filter(Aluno.id == 4).first()

if aluno:
    session.delete(aluno)
    session.commit()
    print("Aluno removido com sucesso!")
else:
    print("Aluno não encontrado.")



alunos = session.query(Aluno).all()
for aluno in alunos:
    print(f"ID: {aluno.id} | Nome: {aluno.nome} | Idade: {aluno.idade}")

