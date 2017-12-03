'''
Rotina para Gerenciamento de Eventos usando formatacao 
de intercambio JSON. 

Adaptado da rotina de Prof. Rhavy Maia

'''

from Participante import Participante

def main(args=[]):
    opcao = None
    part = Participante("nome", "email", "nascimento")
    while opcao != '0':
        print("\n\nBem vindo ao Gerenciador de Eventos! O que deseja? ")
        opcao = input("\nListar participantes[1], Adicionar participante[2], Sair[0] >> ")
        
        opdic = {
        '0': part.sair,
        '1': part.listarParticip,
        '2': part.adicParticip
        }
		
        try:
            opdic[opcao]()
        except KeyError:
            print("\n****TENTE NOVAMENTE.****\n\n")	

if __name__ == '__main__':
	main()
