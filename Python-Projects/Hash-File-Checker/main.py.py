# Biblioteca responsável por gerar os hashes.
import hashlib

# Recebe o caminho do arquivo informado pelo usuário.
def calcular_md5(caminho_arquivo):
    """Calcular o hash MD5 de um arquivo."""

   # Cria um objeto MD5.
    md5 = hashlib.md5()

   # Abri o arquivo em modo binário, no final junta todos os blocos e converte o hash para o hexadecimal.
    with open(caminho_arquivo, "rb") as arquivo:
        while True:
            bloco = arquivo.read(4096)

            if not bloco:
                break

                md5.update(bloco)
    return md5.hexdigest()

# Recebe o caminho do arquivo informado pelo usuário.
def calcular_sha256(caminho_arquivo):
    """Calcular o hash SHA-256 de um arquivo."""

    # Cria um objeto SHA-256.
    sha256 = hashlib.sha256()

     # Abri o arquivo em modo binário, no final junta todos os blocos e converte o hash para o hexadecimal.
    with open(caminho_arquivo, "rb") as arquivo:
        while True:
            bloco = arquivo.read(4096)

            if not bloco:
                break

            sha256.update(bloco)

    return sha256.hexdigest()

# A função main atua como um gerente do programa.
def main():

    # Exibe o cabeçalho
    print("=" * 50)
    print("        HASH FILE CHECKER")
    print("=" * 50)

    # Solicita o caminho do arquivo.
    caminho = input("Digite o caminho do arquivo:")


# Tudo nesse bloco try irá ser executado, caso ocorra um erro, o bloco será finalizado e iniciará um except correspondente.
    try:
        
        md5 = calcular_md5(caminho)
        sha256 = calcular_sha256(caminho)

        print("\nArquivo analisado:")
        print(caminho)

        print("\nMD5:")
        print(md5)

        print("\nSHA-256:")
        print(sha256)

    except FileNotFoundError:
        print("\nErro: Arquivo não encontrado.")

    except PermissionError:
        print("\nErro: Você não possui permissão para acessar esse arquivo.")

    except Exception as erro: 
        print(f"\nErro inesperado: {erro}")


if __name__ == "__main__":
    main()
    