from msilib.schema import ComboBox
from tkinter import *
from tkinter import Tk,ttk
from tkinter import messagebox
from banco.alterar_tabela import Comandos
from classes.paciente import Paciente
from datetime import date

class Tela_cadastro:
    def __init__(self):
        self.janela_cadastro = Tk()
        #self.janela_cadastro.geometry("500x500")
        self.janela_cadastro.title("Cadastro")

        Label(self.janela_cadastro,text="Nome").grid(column=0,row=0,sticky=E)
        self.nome_input = Entry(self.janela_cadastro,justify=CENTER)
        self.nome_input.grid(column=1,row=0)

        Label(self.janela_cadastro,text="Email").grid(column=0,row=1,sticky=E)
        self.email_input = Entry(self.janela_cadastro,justify=CENTER)
        self.email_input.grid(column=1,row=1)

        Label(self.janela_cadastro,text="Senha").grid(column=0,row=2,sticky=E)
        self.senha_input = Entry(self.janela_cadastro,justify=CENTER,show="*")
        self.senha_input.grid(column=1,row=2)

        Label(self.janela_cadastro,text="Idade").grid(column=0,row=3,sticky=E)
        self.idade_input = Entry(self.janela_cadastro,justify=CENTER)
        self.idade_input.grid(column=1,row=3)

        Label(self.janela_cadastro,text="Sexo").grid(column=2,row=0,sticky=E)
        self.sexo_input = Entry(self.janela_cadastro,justify=CENTER)
        self.sexo_input.grid(column=3,row=0)

        Label(self.janela_cadastro,text="Endereço").grid(column=2,row=1,sticky=E)
        self.endereco_input = Entry(self.janela_cadastro,justify=CENTER)
        self.endereco_input.grid(column=3,row=1)

        Label(self.janela_cadastro,text="Tipo Sanguineo").grid(column=2,row=2,sticky=E)
        self.tipo_sangue = ttk.Combobox(self.janela_cadastro,values=self.opcoes_tipos_sangue())
        self.tipo_sangue.grid(column=3,row=2)

        botao_cadastro = Button(self.janela_cadastro,text="Cadastrar",command=self.concluir_registros if self.autenticar_email() else lambda: messagebox.showerror("Cadastro", "erro ao fazer o cadastro"))
        botao_cadastro.grid(column=2,row=10)

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
            self.tipo_sangue = self.tipo_sangue.get()
        except(Exception):
            messagebox.showwarning("Cadastro","algum campo está vazio ou com valores errados")
            self.reiniciar_tela()

    def cadastrar_usuario(self):
        comando = Comandos()
        id = comando.consultar_quantidade_pacientes()[0][0] + 1
        return Paciente(id,self.nome_input,self.email_input,self.senha_input,self.endereco_input,self.sexo_input,self.idade_input,self.tipo_sangue,date.today(),False)
    
    def inserir_paciente_banco(self):
        comando = Comandos()
        comando.add_paciente(self.cadastrar_usuario())
        messagebox.showinfo("Cadastro","Cadastro realizado com sucesso")
        self.janela_cadastro.destroy()
    
    #def verificar_campo_preenchido(self);

    def concluir_registros(self):
        self.converter_valores()
        self.inserir_paciente_banco()
    
    def reiniciar_tela(self):
        self.janela_cadastro.destroy()
        Tela_cadastro()
    
    def opcoes_tipos_sangue(self):
        return ["A+","A-","B+","B-","AB+","AB-","O+","O-"]

    
        