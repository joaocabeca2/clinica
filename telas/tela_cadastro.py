from tkinter import *
class Tela_cadastro:
    def __init__(self):
        window = Tk()
        name_label = Label(window,text="Digite seu nome").grid(column=0,row=0)
        name_input = Entry(window,justify=CENTER).grid(column=0,row=1)

        email_label = Label(window,text="Digite seu email").grid(column=0,row=2)
        email_input = Entry(window,justify=CENTER).grid(column=0,row=3)

        password_label = Label(window,text="Digite sua senha").grid(column=0,row=4)
        password_input = Entry(window,justify=CENTER).grid(column=0,row=5)

        age_label = Label(window,text="Digite sua idade").grid(column=50,row=0)
        age_input = Entry(window,justify=CENTER).grid(column=50,row=1)

        adress_label = Label(window,text="Digite seu endereço").grid(column=50,row=2)
        adress_input = Entry(window,justify=CENTER).grid(column=50,row=3)

        #caixa com opçoes do tipo sanguineo para marcar check

        register_button= Button(window,text="Register",command=self.registration_suscefully_message if self.authenticate_email(email_input) and self.authenticate_password(password_input) else self.error_message)
        register_button.grid(column=50,row=4)

        window.mainloop()
    
    def authenticate_email(self,email):
        email = str(email)
        #if existe email no banco
            #self.error_message()
        #else adiciona novo paciente
        return True
    
    def authenticate_password(self,password):
        password = str(password)
        return True
        '''if password.isdigit():
            return True'''
    
    def error_message(self):
        error_window = Tk()
        message = Label(error_window,text="Erro na validação de dados, tente novamente!").grid(column=0,row=0)
        error_window.mainloop()
    
    def registration_suscefully_message(self):
        registration_suscefully_window = Tk()
        message = Label(registration_suscefully_window,text="Cadastro realizado com sucesso!").grid(column=0,row=0)
        