# Hash File Checker

## Descrição

Ferramenta desenvolvida em Python para calcular os hashes MD5 e SHA-256 de arquivos.

## Funcionalidades

- Cálculo de MD5
- Cálculo de SHA-256
- Leitura de qualquer tipo de arquivo
- Tratamento de erros

## Tecnologias

- Python 3
- hashlib

## Como executar

main.py

## Exemplo

(imagem do programa)

## Aprendizados

- hashlib
- funções
- leitura de arquivos
- tratamento de exceções

## Como o programa funciona

## Importação

```
import hashlib
```

Importa a biblioteca responsável por gerar os hashes.


## Função calcular_md5()

```
def calcular_md5(caminho_arquivo):
````

Recebe o caminho do arquivo informado pelo usuário.

## md5 = hashlib.md5()

```
md5 = hashlib.md5()
````

Cria um objeto MD5.


## Leitura do arquivo

```
with open(caminho_arquivo, "rb") as arquivo:
````

O arquivo é aberto em modo binário (rb).

Isso permite calcular o hash de qualquer tipo de arquivo:

- PDF
- JPG
- PNG
 -ZIP
- ISO
- EXE

## Leitura em blocos

````
bloco = arquivo.read(4096)
````

Em vez de carregar todo o arquivo na memória, o programa lê 4096 bytes por vez.

Isso permite trabalhar até mesmo com arquivos muito grandes.

Fluxo:

````
Arquivo

↓

4096 bytes

↓

4096 bytes

↓

4096 bytes

↓

fim
````

## Atualizando o hash

````
md5.update(bloco)
````


Cada bloco lido é enviado para o algoritmo MD5.

No final, o algoritmo terá processado todo o arquivo.

## Resultado

````
return md5.hexdigest()
````

hexdigest() converte o hash para hexadecimal.

Exemplo:

```
f3b7e4b1d8...
```

## SHA-256

A função é praticamente igual.

A única diferença é:

```
sha256 = hashlib.sha256()
```

## A função main()

Ela controla todo o programa.

Primeiro exibe o título.

```
print("=" * 50)
```

Depois solicita o arquivo.

```
input()
```

Em seguida chama:

```
calcular_md5()

calcular_sha256()
```

Criando uma variavel para cada um dos resultados e printa o resultado no terminal

```
print("\nArquivo analisado:")
        print(caminho)

        print("\nMD5:")
        print(md5)

        print("\nSHA-256:")
        print(sha256)
```


## Tratamento de erros

Caso o usuário digite:

```
teste.pdf
```

e o arquivo não exista, o programa não encerra com erro.

Ele mostra:

```
Erro: arquivo não encontrado.
```

## Exemplo de execução

```
==================================================
            HASH FILE CHECKER
==================================================

Digite o caminho do arquivo:

C:\Users\Kayas\Downloads\foto.jpg


Arquivo analisado:

C:\Users\Kayas\Downloads\foto.jpg

MD5

7ac66c0f148de9519b8bd264312c4d64

SHA-256

44d88612fea8a8f36de82e1278abb02f...
```
