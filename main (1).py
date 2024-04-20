import tkinter
import customtkinter
from PIL import ImageTk, Image
from conexao import connect
from bd import insert, update, delete, query, register, login, to_lend, give_back
from livro import Livro
from datetime import datetime
from usuario import Usuario

mydb = connect()

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("500x500")
app.title('Login')

def welcome_window():
    w = customtkinter.CTk()
    w.geometry("500x500")
    w.title('Bem vindos')

    l1 = customtkinter.CTkLabel(master=w, text="Biblioteca", font=('Century Gothic', 60))
    l1.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

    button_cadastro_livro = customtkinter.CTkButton(master=w, width=220, fg_color="#993399", command=cd_livros, border_width=2, text="Cadastro de Livro", font=('Century Gothic', 12))
    button_cadastro_livro.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

    button_atualizacao_livro = customtkinter.CTkButton(master=w, width=220, fg_color="#993399", command=att_livros, border_width=2, text="Atualização de Livro", font=('Century Gothic', 12))
    button_atualizacao_livro.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

    button_listagem_livro = customtkinter.CTkButton(master=w, width=220, fg_color="#993399", command=listar_livros, border_width=2, text="Listagem de Livro", font=('Century Gothic', 12))
    button_listagem_livro.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    button_emprestimo_devolucao_livro = customtkinter.CTkButton(master=w, width=220, fg_color="#993399",command=emprestar_devolver_livros,  border_width=2, text="Emprestar e Devolver Livros", font=('Century Gothic', 12))
    button_emprestimo_devolucao_livro.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    w.mainloop()

def cd_livros():
    w = customtkinter.CTk()
    w.geometry("600x600")
    w.title('Cadastro de Livros')

    l1 = customtkinter.CTkLabel(master=w, text="Cadastro de Livros", font=('Century Gothic', 45))
    l1.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

    l2 = customtkinter.CTkLabel(master=w, text="Título:", font=('Century Gothic', 20))
    l2.place(relx=0.2, rely=0.3, anchor=tkinter.CENTER)

    e1 = customtkinter.CTkEntry(master=w, width=150)
    e1.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

    l3 = customtkinter.CTkLabel(master=w, text="Autor:", font=('Century Gothic', 20))
    l3.place(relx=0.2, rely=0.4, anchor=tkinter.CENTER)

    e2 = customtkinter.CTkEntry(master=w, width=150)
    e2.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

    l4 = customtkinter.CTkLabel(master=w, text="Ano:", font=('Century Gothic', 20))
    l4.place(relx=0.2, rely=0.5, anchor=tkinter.CENTER)

    e3 = customtkinter.CTkEntry(master=w, width=150)
    e3.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l5 = customtkinter.CTkLabel(master=w, text="Status:", font=('Century Gothic', 20))
    l5.place(relx=0.2, rely=0.6, anchor=tkinter.CENTER)

    e4 = customtkinter.CTkEntry(master=w, width=150)
    e4.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    def inserir():
         titulo = e1.get()
         autor = e2.get()
         ano = e3.get()
         status_ = e4.get()

         insert(mydb, titulo, autor, ano, status_)

    button_inserir = customtkinter.CTkButton(master=w, width=220, fg_color="#993399", command=inserir, border_width=2, text="Inserir", font=('Century Gothic', 12))
    button_inserir.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    w.mainloop()


def att_livros():
    t = customtkinter.CTk()
    t.geometry("600x600")
    t.title('Atualizações de Livros')

    l1 = customtkinter.CTkLabel(master=t, text="Atualizações de Livros", font=('Century Gothic', 45))
    l1.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

    l2 = customtkinter.CTkLabel(master=t, text="Insira o Título Antigo:", font=('Century Gothic', 20))
    l2.place(relx=0.2, rely=0.3, anchor=tkinter.CENTER)

    e1 = customtkinter.CTkEntry(master=t, width=150)
    e1.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

    l3 = customtkinter.CTkLabel(master=t, text="Título Novo:", font=('Century Gothic', 20))
    l3.place(relx=0.2, rely=0.4, anchor=tkinter.CENTER)

    e2 = customtkinter.CTkEntry(master=t, width=150)
    e2.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

    l4 = customtkinter.CTkLabel(master=t, text="Autor Novo:", font=('Century Gothic', 20))
    l4.place(relx=0.2, rely=0.5, anchor=tkinter.CENTER)

    e3 = customtkinter.CTkEntry(master=t, width=150)
    e3.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l5= customtkinter.CTkLabel(master=t, text="Ano Novo:", font=('Century Gothic', 20))
    l5.place(relx=0.2, rely=0.6, anchor=tkinter.CENTER)

    e4 = customtkinter.CTkEntry(master=t, width=150)
    e4.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    l6= customtkinter.CTkLabel(master=t, text="Status Novo:", font=('Century Gothic', 20))
    l6.place(relx=0.2, rely=0.7, anchor=tkinter.CENTER)

    e5 = customtkinter.CTkEntry(master=t, width=150)
    e5.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

    def atualizar():
         titulo_antigo = e1.get()
         titulo_novo = e2.get()
         autor = e3.get()
         ano = e4.get()
         status_ = e5.get()

         update(mydb, titulo_antigo, titulo_novo, autor, ano, status_)

    button_inserir = customtkinter.CTkButton(master=t, width=220, fg_color="#993399", command=atualizar, border_width=2, text="Atualizar Livro", font=('Century Gothic', 12))
    button_inserir.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

    t.mainloop()

def listar_livros():
    l = customtkinter.CTk()
    l.geometry("600x600")
    l.title('Atualizações de Livros')

    l1 = customtkinter.CTkLabel(master=l, text="Atualizações de Livros", font=('Century Gothic', 45))
    l1.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

    l2 = customtkinter.CTkLabel(master=l, text="Aperte aqui para listar os livros existentes:", font=('Century Gothic', 25))
    l2.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)

    def listar():
        mydb = connect()
        dados = query(mydb)

        l3 = customtkinter.CTkLabel(master=l, text="\n".join(dados), font=('Century Gothic', 12))
        l3.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

    button_listar = customtkinter.CTkButton(master=l, width=220, fg_color="#993399", command=listar, border_width=2, text="Listar Livros", font=('Century Gothic', 12))
    button_listar.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)

    l.mainloop()
    

def emprestar_devolver_livros():
    mydb = connect()
    ed = customtkinter.CTk()
    ed.geometry("600x600")
    ed.title('Emprestar e Devolver Livros')

    l1 = customtkinter.CTkLabel(master=ed, text="Emprestar e Devolver Livros", font=('Century Gothic', 40))
    l1.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)

    l2 = customtkinter.CTkLabel(master=ed, text="Insira o título para emprestar:", font=('Century Gothic', 17))
    l2.place(relx=0.25, rely=0.3, anchor=tkinter.CENTER)

    e1 = customtkinter.CTkEntry(master=ed, width=150)
    e1.place(relx=0.6, rely=0.3, anchor=tkinter.CENTER)

    l3 = customtkinter.CTkLabel(master=ed, text="Insira o título para devolver:", font=('Century Gothic', 17))
    l3.place(relx=0.25, rely=0.5, anchor=tkinter.CENTER)

    e2 = customtkinter.CTkEntry(master=ed, width=150)
    e2.place(relx=0.6, rely=0.5, anchor=tkinter.CENTER)

    def emprestar():
        titulo = e1.get()
        autor = 'Autor' 
        ano = 2000 
        livro = Livro(mydb, titulo, autor, ano)  
        if livro.verificar_disponibilidade():
            status_ = False
            return True
        else:
            return False

    def devolver():
        titulo = e2.get()
        autor = 'Autor'  
        ano = 2000  
        livro = Livro(mydb, titulo, autor, ano) 
        if not status_:
            status_ = True
            return True
        else:
            return False

    button_emprestar = customtkinter.CTkButton(master=ed, width=220, fg_color="#993399", command=emprestar, border_width=2, text="Emprestar", font=('Century Gothic', 12))
    button_emprestar.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

    button_devolver = customtkinter.CTkButton(master=ed, width=220, fg_color="#993399", command=devolver, border_width=2, text="Devolver", font=('Century Gothic', 12))
    button_devolver.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)

    ed.mainloop()
    
def cadastro_function():
    app.destroy()
    cadastro = customtkinter.CTk()
    cadastro.geometry("500x500")
    cadastro.title('Cadastro')

    img1 = ImageTk.PhotoImage(Image.open("./imagens/fundo1.jpg"))
    l1 = customtkinter.CTkLabel(master=cadastro, image=img1)
    l1.pack()
    l1.image = img1

    frame = customtkinter.CTkFrame(master=cadastro, width=320, height=360, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l2 = customtkinter.CTkLabel(master=frame, text="Faça seu cadastro", font=('Century Gothic', 20))
    l2.place(x=50, y=45)

    entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Usuario')
    entry1.place(x=50, y=110)

    entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Senha', show="*")
    entry2.place(x=50, y=165)

    def register_user():
        user_data = {
            'nome': entry1.get(),
            'senha': entry2.get()
        }
        register(mydb, user_data['nome'], user_data['senha'])

        cadastro.destroy()

    button1 = customtkinter.CTkButton(master=frame, fg_color="#993399", width=220, text="Cadastre-se", command=register_user, corner_radius=6)
    button1.place(x=50, y=260)

    cadastro.mainloop()

    def register_user():
        user_data = {
            'nome': entry1.get(),
            'senha': entry2.get()
        }
        register(mydb, user_data['nome'], user_data['senha'])

        cadastro.destroy()

    button1 = customtkinter.CTkButton(master=frame, fg_color="#993399", width=220, text="Cadastre-se", command=register_user, corner_radius=6)
    button1.place(x=50, y=260)

    cadastro.mainloop()

def check_login():
    nome = entry1.get()
    senha = entry2.get()

    user = login(mydb, nome, senha)

    if user:
        print("Login bem-sucedido.")
        welcome_window()
    else:
        print("Credenciais inválidas.")
        app.destroy()

img1 = ImageTk.PhotoImage(Image.open("./imagens/fundo1.jpg"))
l1 = customtkinter.CTkLabel(master=app, image=img1)
l1.pack()
l1.image = img1

frame = customtkinter.CTkFrame(master=app, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

l2 = customtkinter.CTkLabel(master=frame, text="Entre em sua conta", font=('Century Gothic', 20))
l2.place(x=60, y=45)

entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Usuario')
entry1.place(x=50, y=110)

entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Senha', show="*")
entry2.place(x=50, y=165)

button_cadastro = customtkinter.CTkButton(master=frame, width=220, fg_color="transparent", border_color="#993399", command=cadastro_function, border_width=2, text="Cadastre-se", font=('Century Gothic', 12))
button_cadastro.place(x=50, y=225)

button_login = customtkinter.CTkButton(master=frame, fg_color="#993399", width=220, text="Login", command=check_login, corner_radius=6)
button_login.place(x=50, y=275)

app.mainloop()

print("Bem-vindo à Biblioteca")

while True:
    print("\nSelecione a operação desejada:")
    print("1. Registrar usuário")
    print("2. Fazer login")
    print("3. Inserir livro")
    print("4. Atualizar livro")
    print("5. Excluir livro")
    print("6. Consultar livros")
    print("7. Emprestar livro")
    print("8. Devolver livro")
    print("9. Sair")

    opcao = input("Opção: ")

    if opcao == "1":
        nome = input('Digite o Nome: ')
        email = input('Digite o Email: ')
        senha = input('Digite a Senha: ')
        
        data_nascimento = input('Digite a Data de Nascimento (DD/MM/YYYY): ')
        data_nascimento_obj = datetime.strptime(data_nascimento, '%d/%m/%Y')
        
        data_nascimento_formatada = data_nascimento_obj.strftime('%Y-%m-%d')
        rua = input('Digite a Rua: ')
        bairro = input('Digite o Bairro: ')
        cidade = input('Digite a Cidade: ')
        estado = input('Digite o Estado: ')
        cep = input('Digite o CEP: ')
        
        user = Usuario(nome, email, senha, data_nascimento, rua, bairro, cidade, estado, cep)

        register(mydb, user.nome, user.email, user.senha, user.data_nascimento,
                 user.rua, user.bairro, user.cidade, user.estado, user.cep)

    elif opcao == "2":
        email = input('Digite o Email: ')
        senha = input('Digite a Senha: ')

        user = login(mydb, email, senha)

    elif opcao == "3":
        titulo = input('Digite o Título: ')
        autor = input('Digite o Autor: ')
        ano = input('Digite o Ano: ')
        status_ = input(
            'Digite o Status (1 para Disponível, 0 para Indisponível): ')

        l = Livro(titulo, autor, ano)
        insert(mydb, l.titulo, l.autor, l.ano, status_)

    elif opcao == "4":
        titulo_antigo = input(
            'Digite o título do livro que deseja atualizar: ')
        titulo_novo = input('Digite o novo título: ')
        autor = input('Digite o novo autor: ')
        ano = input('Digite o novo ano: ')
        status_ = input(
            'Digite o novo status (1 para Disponível, 0 para Indisponível): ')

        update(mydb, titulo_antigo, titulo_novo, autor, ano, status_)

    elif opcao == "5":
        titulo = input('Digite o título do livro que deseja excluir: ')
        delete(mydb, titulo)

    elif opcao == "6":
        query(mydb)

    elif opcao == "7":
        if 'user' not in locals():
            print("Você precisa fazer login para emprestar um livro.")
            continue

        titulo = input('Digite o título do livro que deseja emprestar: ')
        to_lend(mydb, user, titulo)
    elif opcao == "8":
        if 'user' not in locals():
            print("Você precisa fazer login para devolver um livro.")
            continue

        titulo = input('Digite o título do livro que deseja devolver: ')
        give_back(mydb, user, titulo)


    elif opcao == "9":
        break

    else:
        print("Opção inválida!")

mydb.close()
