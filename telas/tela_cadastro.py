from tkinter import *
from tkinter import Tk,ttk
from tkinter import messagebox
from banco.alterar_tabela import Comandos
from classes.paciente import Paciente

class Tela_cadastro:
    def __init__(self):
        self.janela_cadastro = Tk()

        Label(self.janela_cadastro,text="Digite seu nome").grid(column=0,row=0)
        self.nome_input = Entry(self.janela_cadastro,justify=CENTER)
        self.nome_input.grid(column=0,row=1)

        Label(self.janela_cadastro,text="Digite seu email").grid(column=0,row=2)
        self.email_input = Entry(self.janela_cadastro,justify=CENTER)
        self.email_input.grid(column=0,row=3)

        Label(self.janela_cadastro,text="Digite sua senha").grid(column=0,row=4)
        self.senha_input = Entry(self.janela_cadastro,justify=CENTER,show="*")
        self.senha_input.grid(column=0,row=5)

        Label(self.janela_cadastro,text="Digite sua idade").grid(column=50,row=0)
        self.idade_input = Entry(self.janela_cadastro,justify=CENTER)
        self.idade_input.grid(column=50,row=1)

        Label(self.janela_cadastro,text="Digite seu sexo").grid(column=50,row=2)
        self.sexo_input = Entry(self.janela_cadastro,justify=CENTER)
        self.sexo_input.grid(column=50,row=3)

        Label(self.janela_cadastro,text="Digite seu endereço").grid(column=50,row=4)
        self.endereco_input = Entry(self.janela_cadastro,justify=CENTER)
        self.endereco_input.grid(column=50,row=5)

        #caixa com opçoes do tipo sanguineo para marcar check

        botao_cadastro = Button(self.janela_cadastro,text="Cadastrar",command=self.concluir_registros if self.autenticar_email() else lambda: messagebox.showerror("Cadastro", "erro ao fazer o cadastro"))
        botao_cadastro.grid(column=50,row=10)

        self.janela_cadastro.mainloop()
    
    def autenticar_email(self):
        email =  self.email_input.get()
        comando = Comandos()
        resultados = comando.consultar_email()
        for resultado in resultados:
            if resultado[0] == email:
                return False
        return True
    
    def converter_valores(self):
        try:
            self.nome_input = self.nome_input.get()            
            self.email_input = self.email_input.get()
            self.senha_input = self.senha_input.get()
            self.endereco_input = self.endereco_input.get()
            self.sexo_input = self.sexo_input.get()
            self.idade_input = int(self.idade_input.get())
        except(Exception):
            messagebox.showwarning("Cadastro","algum campo está vazio ou com valores errados")
            self.reiniciar_tela()

    def cadastrar_usuario(self):
        return Paciente(self.nome_input,self.email_input,self.senha_input,self.endereco_input,self.sexo_input,self.idade_input,"A+")
    
    def inserir_paciente_banco(self):
        comando = Comandos()
        comando.add_paciente(self.cadastrar_usuario())
        messagebox.showinfo("Cadastro","Cadastro realizado com sucesso")
    
    #def verificar_campo_preenchido(self);

    def concluir_registros(self):
        self.converter_valores()
        self.inserir_paciente_banco()
    
    def reiniciar_tela(self):
        self.janela_cadastro.destroy()
        Tela_cadastro()
    
        