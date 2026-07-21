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



