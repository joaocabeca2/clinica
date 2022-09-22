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

        register_button= Button(window,text="Register",command=self.authenticate_email and self.authenticate_password).grid(column=1000,row=1000)
        window.mainloop()
    
    def authenticate_email(email_input):
        email = str(email_input)
    
    def authenticate_password(password_input):
        password = str(password_input)