# Hashing Basic

Este laboratório teve como objetivo apresentar os fundamentos das funções hash, explicando seu funcionamento, aplicações na autenticação de usuários, verificação da integridade de arquivos e técnicas utilizadas durante auditorias de segurança para identificação e análise de hashes.
Objetivos
Funções de hash e colisões
O papel do hash em sistemas de autenticação
Reconhecendo valores de hash armazenados
Quebra de valores de hash
O uso do hashing para integridade e proteção

# Conceitos abordados

Hash
Algoritmos Hash (MD5, SHA-1, SHA-2, bcrypt)
Quebra de hash (Hash Cracking)
Wordlists
Rainbow Tables
Ferramentas utilizadas
Terminal
TryHackMe
Hashcat

# Comandos estudados

# sha256sum

<img src="https://github.com/Sayak159/Cybersecurity-Portfolio/blob/main/Imagens/Hashing%20Basics/sha256sum.png?raw=true" width="500" >



```
sha256sum Hashing-Basics/Task-2/passport.jpg
```

Descrição: Comando utilizado para identificar e comparar o hash SHA-256 de um arquivo.

# less

```
less rockyou.txt
```

Descrição: É um visualizador de arquivos. Permite navegar para cima e para baixo, pesquisar palavras e visualizar arquivos grandes sem carregá-los completamente na tela.

# Hashcat

```
hashcat -m 3200 -a 0 Hashing-Basics/Task-6/hash1.txt rockyou.txt
```

Descrição:

Hashcat: Ferramenta utilizada para auditoria de senhas. Ela calcula o hash de diversas senhas candidatas e compara os resultados com o hash fornecido.
-m 3200: O parâmetro -m (mode) informa ao Hashcat qual algoritmo de hash deve ser utilizado.
-a 0: O parâmetro -a (Straight Attack) define como o Hashcat irá gerar as senhas candidatas.
Hashing-Basics/Task-6/hash1.txt: Arquivo que contém o hash a ser analisado.
rockyou.txt: Wordlist utilizada durante o ataque.

# Dificuldades encontradas

Não encontrei dificuldades significativas durante a execução do laboratório. Entretanto, foi necessário aprofundar o estudo dos conceitos de Salt, Rainbow Tables e Wordlists para compreender suas diferenças e aplicações práticas na cibersegurança.

# O que aprendi

1. Funções Hash

Durante este laboratório, compreendi que o hash não é um método de criptografia, mas uma função matemática que gera um valor de tamanho fixo a partir de uma entrada. As funções hash são amplamente utilizadas para verificar a integridade de arquivos e mensagens, além de serem empregadas no armazenamento seguro de senhas em sistemas modernos.

2. Algoritmos de Hash

Aprendi que diferentes sistemas operacionais utilizam algoritmos distintos para armazenar senhas. O Windows utiliza principalmente o NTLM, enquanto distribuições Linux modernas utilizam algoritmos como bcrypt, SHA-512 Crypt e YesCrypt, que oferecem maior resistência a ataques.

3. Wordlists

Uma Wordlist é uma lista de possíveis senhas utilizada durante auditorias de segurança e testes autorizados. A rockyou.txt é uma das mais conhecidas, contendo milhões de senhas reais provenientes de um vazamento de dados ocorrido em 2009. Ferramentas como o Hashcat utilizam essas listas para calcular o hash de cada senha e compará-lo com o hash alvo.

4. Rainbow Tables

As Rainbow Tables são bancos de dados contendo hashes previamente calculados. Diferentemente das Wordlists, elas não precisam gerar os hashes durante o ataque, tornando a consulta mais rápida. Entretanto, tornam-se ineficazes quando os hashes utilizam salt, pois não possuem uma entrada para cada combinação possível entre senha e salt.

5. Salt

Compreendi que o salt é um valor aleatório adicionado à senha antes da geração do hash. Seu objetivo é garantir que usuários com a mesma senha possuam hashes diferentes, dificultando ataques baseados em Rainbow Tables e impedindo a identificação de usuários que utilizam a mesma senha.

6. Aplicação do Hash na Cibersegurança

Também compreendi que as funções hash são essenciais em diversas atividades da Cibersegurança, como o armazenamento seguro de senhas, verificação da integridade de arquivos, assinaturas digitais e auditorias de segurança.

# Aplicação prática

As funções hash são amplamente utilizadas em ambientes corporativos para:

Armazenamento seguro de senhas.
Verificação da integridade de arquivos.
Assinaturas digitais.
Distribuição segura de imagens ISO.
Auditorias de segurança.
Resposta a incidentes.

# Conclusão

Este laboratório ampliou meu conhecimento sobre funções hash e sua relevância para a segurança da informação. Além de compreender como os hashes são utilizados para proteger senhas e verificar a integridade de arquivos, também aprendi conceitos importantes como Wordlists, Rainbow Tables, Salt e técnicas de auditoria de hashes. Esse conhecimento servirá como base para estudos mais avançados em autenticação, criptografia e análise de segurança.

# Referências
TryHackMe – Hashing Basics
