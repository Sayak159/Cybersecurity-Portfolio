<h1 align="center">
Título: Entendendo o Modelo TCP/IP 
</h1>
 
 <p align="center">

No artigo anterior vimos como uma mensagem consegue sair de um dispositivo e chegar a outro através da Internet. Entretanto, para que computadores de fabricantes diferentes consigam se comunicar, todos precisam seguir um mesmo conjunto de regras. Essas regras são definidas pelo conjunto de protocolos TCP/IP, que estabelece como os dados devem ser preparados, transportados e entregues através da rede. 

 
Para compreender melhor este conteúdo, recomenda-se a leitura do artigo Introdução às Redes, no qual são apresentados os conceitos fundamentais sobre redes de computadores e Internet. 

 
Com o crescimento das redes com diferentes tipos de dispositivos, surgiu a necessidade de uma padronização para que a comunicação fosse possível. Durante a década de 1970, os pesquisadores Vinton Cerf e Robert Kahn desenvolveram o conjunto de protocolos TCP/IP para permitir a comunicação entre diferentes redes de computadores. Em 1983 o modelo passou a ser adotado como padrão da ARPANET, tornando-se posteriormente a base da Internet que utilizamos atualmente. 

 
O nome TCP/IP é formado pelos dois principais protocolos utilizados pelo modelo: 

TCP (Transmission Control Protocol)  

IP (Internet Protocol)  

Apesar do nome, o modelo utiliza dezenas de protocolos diferentes, como HTTP, HTTPS, DNS, FTP, SMTP, SSH, UDP, ARP, ICMP, entre muitos outros. 

 

# Estrutura: 

O modelo TCP/IP foi criado com 4 camadas, sendo elas: 

Aplicação 

Transporte 

Internet 

Acesso a rede 

 

``` 
├── Computador A              		       ├── Computador B   								 

├── Aplicação    					        ├──	Aplicação													 

├── Transporte					            ├── Transporte									 

├── Internet						        ├── Internet								  

├── Acesso a rede	   > > > > > >	> >   ├── Acesso a rede  
``` 

O processo ocorre a partir do computador A, ao enviar uma mensagem ela irá passar na camada de aplicação, camada de transporte, camada de internet e acesso a rede, para o computador B, será ao reverso o processo. 

 
As informações são transmitidas em forma física, por exemplo uma mensagem enviada do computador A “Olá” para o computador B, ela será enviada em forma física pela camada de acesso a rede, seja ela ondas de rádio (wi-fi), pulsos elétricos (cabos de cobre) ou pulsos de luz (fibra óptica). Em muitos materiais didáticos também é apresentado um modelo TCP/IP com cinco camadas, que separa a camada de Acesso à Rede em duas partes. Neste artigo utilizaremos o modelo clássico de quatro camadas, por ser o mais tradicional. 

 # Aplicação 
A camada de aplicação é a mais próxima do usuário, sendo ela a primeira camada do modelo, ela permite que os programas utilizem a rede para se comunicar. Essa camada não se preocupa com cabos, redes, ou endereços, ela é responsável por preparar e organizar os dados para serem transportados, processo que outra camada irá realizar. Existe vários tipos de protocolos que atuam na camada de aplicação, alguns mais conhecidos são: 

HTTP 

HTTPS 

DNS 

FTP 

SMTP 

SSH 

Um exemplo da camada de aplicação, ao abrir um navegador e digitar  

 ``` 

www.google.com.br 

``` 

 
Somente após descobrir o endereço IP correspondente ao domínio através do protocolo DNS, que funciona como uma "lista telefônica" da Internet, convertendo nomes de domínio, como "www.google.com.br”, em endereços IP que os computadores conseguem compreender, o navegador poderá iniciar a comunicação com o servidor. 

Agora ele prepara uma requisição HTTPS semelhante a: 

“gostaria de acessar a página inicial desse site” 

 Passando assim para a próxima camada. 

 
 # Transporte 

A segunda camada do modelo TCP/IP, uma das principais funções dessa camada é garantir que a comunicação aconteça corretamente, ela é responsável por transportar os dados entre os dois dispositivos. Os dois protocolos mais conhecidos são: 

TCP 

UDP 

 
Continuando o exemplo, após a requisição HTTPS a camada de transporte, utilizando o protocolo TCP, ele estabelece uma conexão entre o computador e o servidor do google, faz a segmentação, numera cada segmento, garantindo assim que nenhum dado se perca ou se necessário reenviar conseguir identificar qual é. Logo passa para a próxima camada. O TCP realiza diversas tarefas antes de permitir que a mensagem siga viagem. Neste artigo não iremos abordar esses conceitos. 

 
# Internet 
A camada da internet é terceira camada, ela é responsável pelo endereçamento e por direcionar os dados pelo melhor caminho até o destino, realizando o roteamento. Após acontecer os processos da camada de transporte a camada de internet adiciona um novo cabeçalho com as informações de endereços IP de origem e destino. Imagine que o endereço IP é como um endereço de uma residência, assim como uma residência possui um endereço único para receber correspondências, cada dispositivo conectado à Internet possui um endereço IP que permite sua identificação na rede, cada dispositivo conectado na internet possui um endereço IP, permitindo essa identificação. Para enviar uma encomenda de São Paulo para Rio de Janeiro, a transportadora não precisa saber só o destino final, mais também precisa saber as ruas, quais cidades vai atravessar, qual o caminho mais rápido, como desviar caso alguma estrada esteja interditada, na internet acontece algo semelhante, os roteadores analisam o endereço IP de destino e escolhem a rota mais adequada disponível para enviar os pacotes. 

 
# Acesso a Rede 
Sendo a quarta e última camada do modelo, ela é responsável pela transmissão dos dados pelo meio físico, até o próximo dispositivo. Após a camada de internet, a camada de acesso a rede encapsula os pacotes IP em quadros (frames), adiciona cabeçalhos com algumas informações entre elas endereço MAC de origem e destino. Enquanto a camada de internet utiliza o endereço IP, a camada de acesso a rede trabalha com endereço MAC, sendo ele um identificador físico da placa de rede, por exemplo, se podemos usar como analogia o endereço IP como um endereço de residência, o endereço MAC é como a identificação da pessoa que mora na residência. 

 
# O que acontece nessa camada? 

Vamos continuar usando o exemplo do Google. 

Você digitou: 

``` 

google.com.br

``` 

Até agora: 

Aplicação 

↓ 

Transporte 

↓ 

Internet 

Agora chegamos à camada de Acesso à Rede. 

Ela recebe o pacote IP e cria um quadro (frame) adicionando informações como: 

endereço MAC de origem;  

endereço MAC de destino;  

informações de controle.  

Depois disso, transforma os dados em sinais físicos. 

 
 Exemplo prático 

Vamos continuar utilizando o mesmo exemplo do navegador. 

Você digitou: 

``` 

www.google.com 

``` 

# Na camada de Aplicação: 

o DNS descobriu o endereço IP do Google;  

o HTTPS criou a solicitação da página.  

# Na camada de Transporte: 

o TCP organizou os dados e estabeleceu uma conexão.  

# Agora a solicitação chega à camada Internet. 

Nesse momento, o protocolo IP adiciona informações importantes, como: 

endereço IP de origem (seu computador);  

endereço IP de destino (servidor do Google).  

Depois disso, os dados são encaminhados para a próxima camada. 

# Agora chegamos à camada de Acesso à Rede. 

Ela recebe o pacote IP e cria um quadro (frame) adicionando informações como: 

endereço MAC de origem;  

endereço MAC de destino;  

informações de controle.  

Depois disso, transforma os dados em sinais físicos e os envia através de Cabo Ethernet, Fibra óptica ou Wi-Fi. 

 # Encapsulamento 

Durante a comunicação, cada camada adiciona suas próprias informações aos dados recebidos da camada anterior. Esse processo recebe o nome de encapsulamento. Quando a mensagem chega ao computador de destino, ocorre o processo inverso, chamado de desencapsulamento, em que cada camada remove as informações adicionadas anteriormente até que o conteúdo original seja entregue ao aplicativo.  

O modelo TCP/IP é a base da comunicação na Internet. Sempre que enviamos uma mensagem, acessamos um site, assistimos a um vídeo ou realizamos um download, essas quatro camadas trabalham em conjunto para que a informação chegue corretamente ao destino. 


Grande parte dos ataques e mecanismos de defesa em cibersegurança estão diretamente relacionados às camadas do modelo TCP/IP. Técnicas como sniffing, spoofing, ataques DoS, utilização de firewalls, VPNs e sistemas de detecção de intrusão exploram ou protegem diferentes camadas desse modelo. Por isso, compreender seu funcionamento é um dos primeiros passos para quem deseja atuar na área de segurança da informação. 

 No próximo artigo será apresentado o modelo OSI, utilizado como referência para compreender de forma ainda mais detalhada o funcionamento das comunicações em redes de computadores. 

 
