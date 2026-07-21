# Hash File Checker


# Índice

- Descrição
- Funcionalidades
- Tecnologias
- Estrutura do Projeto
- Como executar
- Como o programa funciona
- Exemplo de execução
- Aprendizados
- Aplicações práticas
- Melhorias futuras
- Conclusão



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

## Estrutura do projeto

```
Hash-File-Checker
│
├── main.py
├── README.md
└── images
    └── exemplo.png
```

## Como executar

1. Clone o repositório.

```bash
git clone https://github.com/Sayak159/Cybersecurity-Portfolio.git
```

2. Entre na pasta do projeto.

```bash
cd Python-Projects/Hash-File-Checker
```

3. Execute o programa.

```bash
python main.py
```

## Como o programa funciona

## Importação

```
import hashlib
```

Importa a biblioteca responsável por gerar os hashes.

## Função calcular_md5() 

```
def calcular_md5(caminho_arquivo): 
```

Recebe o caminho do arquivo informado pelo usuário

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

A leitura em blocos de 4096 bytes evita carregar todo o arquivo para a memória RAM, permitindo que o programa processe arquivos grandes de maneira eficiente.

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

## Aprendizados

Durante o desenvolvimento deste projeto aprendi:

Como utilizar a biblioteca hashlib para gerar hashes MD5 e SHA-256.
Como realizar leitura de arquivos em modo binário.
Como utilizar funções para organizar o código.
Como tratar exceções utilizando try e except.
Como processar arquivos grandes realizando a leitura em blocos.
Como organizar um projeto Python para publicação no GitHub.

## Aplicações práticas

Este tipo de ferramenta pode ser utilizado para:

- Verificar a integridade de arquivos.
- Confirmar se um download foi corrompido.
- Comparar arquivos suspeitos durante análises forenses.
- Validar evidências em investigações digitais.
- Confirmar a autenticidade de imagens ISO disponibilizadas por fabricantes.

## Melhorias futuras

- Suporte ao SHA-1.
- Suporte ao SHA-512.
- Comparação entre dois arquivos.
- Interface gráfica utilizando Tkinter.
- Arrastar e soltar arquivos na janela.
- Exportação do resultado para um arquivo TXT.

## Conclusão

Este projeto permitiu aplicar conceitos de manipulação de arquivos, funções, tratamento de exceções e algoritmos de hash utilizando Python. Além disso, reforçou conhecimentos sobre integridade de arquivos, tema amplamente utilizado na área de cibersegurança.

