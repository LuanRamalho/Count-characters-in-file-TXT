def contar_caracteres_em_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            quantidade = len(conteudo)
            print(f"Quantidade total de caracteres no arquivo: {quantidade}")
    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique se o nome está correto e se o arquivo está no mesmo diretório.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Exemplo de uso
nome = input("Digite o nome do arquivo .txt (ex: arquivo.txt): ")
contar_caracteres_em_arquivo(nome)

input()
