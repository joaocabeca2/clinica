class Usuario:
    def __init__(self,nome,email,senha,endereco,sexo,idade):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.endereco = endereco
        self.sexo = sexo
        self.idade = idade

    def getNome(self):
        return self.nome
    def getEmail(self):
        return self.email
    def getSenha(self):
        return self.senha
    def getEndereco(self):
        return self.endereco
    def getSexo(self):
        return self.sexo
    def getIdade(self):
        return self.idade