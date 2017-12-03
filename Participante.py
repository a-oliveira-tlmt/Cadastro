from datetime import date
import json

class Participante():

    def __init__(self, nome, email, nascimento):
        self.nome = nome
        self.email = email
        self.nascimento = nascimento

    def sair(self):
        pass

    def carregarParticip(self):
        try:
            f = open("participantes.txt", 'r', encoding="utf8")
            jsonObjs = json.loads(f.read())
            
            f.close()
            return jsonObjs

        except FileNotFoundError as err:
            print(err)
            print("Arquivo nao encontrado!")

    def listarParticip(self):
        jsonObjs = self.carregarParticip()
            
        for jsonObj in jsonObjs:
            nome = jsonObj["nome"]
            email = jsonObj["email"]
            data = jsonObj["nascimento"].split("-")
            nascimento = date(int(data[0]), int(data[1]), int(data[2]))
            particip = Participante(nome, email, nascimento)
            print(particip) 

    def adicParticip(self):
        print("Bem vindo!!")
               
        nomeNovo = input("INSIRA O SEU NOME >> ")
        emailNovo = input("INSIRA O SEU EMAIL >> ")
        anoNascNovo = input("INSIRA SEU ANO DE NASCIMENTO >> ")
        mesNascNovo = input("INSIRA SEU MES DE NASCIMENTO >> ")
        diaNascNovo = input("INSIRA SEU DIA DE NASCIMENTO >> ")
        nascNovo = date( int(anoNascNovo), int(mesNascNovo), int(diaNascNovo) )
              
        participNovo = Participante(nomeNovo, emailNovo, nascNovo)

        print("\n****CADASTRANDO...****\n\n")	

        jsonObjs = self.carregarParticip()
        pessoaNovoJson = {}
        pessoaNovoJson['nome'] = participNovo.nome
        pessoaNovoJson['email'] = participNovo.email
        pessoaNovoJson['nascimento'] = str(participNovo.nascimento)
        jsonObjs.append(pessoaNovoJson)

        print("\n****ARQUIVANDO...****\n\n")	

        try:
            with open('participantes.txt', 'w', encoding='utf-8') as f:
                json.dump(jsonObjs, f, ensure_ascii=False, indent=4)
                
            f.close()

        except FileNotFoundError as err: #somente Python 3
            print(err)
            print("Arquivo nao encontrado!")

        print("\n****CONFERINDO CADASTRO...****\n\n")	
        self.listarParticip()

    def __str__(self):
        result = '\n Nome: ' + self.nome + '\n Email: '+ self.email + \
        '\n Nascimento: '+ str(self.nascimento)
        return result


