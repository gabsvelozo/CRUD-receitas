import os
import random

class Receita:
    global pasta_receitas
    pasta_receitas = os.listdir("Receitas")

    def __init__(self, nome, origem, ingredientes, modo_de_preparo):
        self.nome = nome
        self.origem = origem
        self.ingredientes = ingredientes
        self.modo_de_preparo = modo_de_preparo
    
    #Adicionar nova receita
    def adicionar(self, receita):
        file = open(f"Receitas/{(receita.nome).strip()}.txt", "a")

        file.write(f"""Nome: {receita.nome}\n\nOrigem: {receita.origem}\n\nIngredientes:\n""")

        for ingrediente in receita.ingredientes:
            file.write(f"   - {(ingrediente).capitalize()}\n")
        #file.writelines("\n".join(receita.ingredientes).capitalize())
        
        file.write(f"\nModo de preparo: {receita.modo_de_preparo}")

        file.close()

        print("\nReceita criada com sucesso!")
        #cria o arquivo .txt em branco
        #write as infos da Receita
        #close arquivo
    
    def visualizarTodas():

        print("=========== Lista de Receitas ===========")
        #printa as receitas (todos os arquivos da pasta, removendo a extensão .txt no nome) do diretório Receitas
        for receita in pasta_receitas:
            print(os.path.splitext(receita)[0])

    def buscarReceita(receita):
        #abre o diretório (pasta) Receitas

        nome_arquivo = f"{receita}.txt"
        #verifica se a receita do input do usuário está no diretório Receitas
        if nome_arquivo in pasta_receitas:
            file = open(f"./Receitas/{nome_arquivo}", "r")
            print(file.read())
            file.close()
        
        else:
            print("\nReceita não encontrada.")
    
    def exclusao(receita):
        try:
            nome_arquivo = f"{receita}.txt"
            os.remove(f"./Receitas/{nome_arquivo}")
        except FileNotFoundError:
            print("Receita não encontrada.")

    def filtrarPais(pais):
        paisreceita = {}

        for receita in pasta_receitas:
            nome_arquivo = f"{receita}"
            file = open(f"./Receitas/{nome_arquivo}", "r")
            lines = file.readlines()
            file.close()
            for line in lines:
                if line.strip() == f"Origem: {pais.capitalize()}":
                    if pais in paisreceita:
                        paisreceita[pais].append(receita)
                    else:
                        paisreceita[pais] = [receita]
        if pais in paisreceita:
            if pais.endswith("a"):
                print(f"\n=========== Lista de Receitas da {pais} ===========")
                for receita in paisreceita[pais]:
                    print(os.path.splitext(receita)[0])
            else:
                print(f"\n=========== Lista de Receitas do {pais} ===========")
                for receita in paisreceita[pais]:
                    print(os.path.splitext(receita)[0])
        else:
            print("O país selecionado ainda não possui receitas a apresentar.")
        
        return paisreceita
    
    def sugerirReceita():
        lista_receitas = []

        for receita in pasta_receitas:
            lista_receitas.append(os.path.splitext(receita)[0])
        
        sugestao = random.choice(lista_receitas)
        print(f"Receita sugerida: {sugestao}")

        return sugestao

    def totalReceitas():
        return len(os.listdir("Receitas"))

    def paisMaisExplorado():
        paises = []
        for receita in pasta_receitas:
            nome_arquivo = f"{receita}"
            file = open(f"./Receitas/{nome_arquivo}", "r")
            lines = file.readlines()
            file.close()
            origem_linha = lines[2].split() # pega a linha dois e coloca-a separada por espaços numa lista
            pais = origem_linha[1] # pega o pais que vem depois da receita (segundo elemento da lista)
            paises.append(pais)

        max = 0

        for pais in paises:
            quant_pais = paises.count(pais)
            if quant_pais > max:
                max = quant_pais
                pais_mais_explorado = pais
            
        print(f"País mais explorado: {pais_mais_explorado}")  
        

