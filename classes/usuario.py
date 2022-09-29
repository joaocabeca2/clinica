class Usuario:
    def __init__(self,nome,email,senha,endereco,sexo,idade,data_inscricao):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.endereco = endereco
        self.sexo = sexo
        self.idade = idade
        self.data_inscricao = data_inscricao

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
    def getDataInscricao(self):
        return self.data_inscricao