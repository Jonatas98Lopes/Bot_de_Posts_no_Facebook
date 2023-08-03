# Bot_de_Posts_no_Facebook


***

## Descrição:

Neste projeto, vamos criar uma aplicação para automatizar o processo de postagem no seu Facebook. A ideia é que usuario informa os dados de acesso da conta dele, assim como a mensagem que deseja publicar, e o programa faz todo o resto do processo. Desde o acesso a conta até a postagem.

Assista ao vídeo de funcionamento do projeto [clicando aqui!](https://www.linkedin.com/feed/update/urn:li:activity:7091700266818805763/)

***

## Requisitos:

* Ter o Python 3 instalado no seu computador. De preferência, na versão 3.11.

* Ter habilitado a opção **Add to Path** na hora da instalação do Python.

* Possuir o navegador Google Chrome instalado.


***

## Algoritmo do Projeto:
* Obter o email ou telefone do usuário no Facebook.

* Obter a senha do usuário no Facebook.

* Obter a mensagem que o usuário deseja publicar.

* Abrir o navegador.

* Acessar o site: https://www.facebook.com/

* Esperar a página carregar.

* Localizar o campo de informar o nome de usuário.

* Digitar o telefone ou email do usuário neste campo.

* Localizar o campo de senha.

* Localizar o primeiro campo de digitação de post.

* Clicar neste campo.

* Localizar o primeiro campo de digitação de post.

* Digitar a senha do usuário neste campo.

* Localizar o botão de Login.

* Clicar no botão de Login.

* Esperar a página carregar.

* Localizar o primeiro campo de postagem.

* Clicar nele.

* Localizar o segundo campo de postagem. O SEGUNDO CAMPO QUE ABRE QUANDO CLICA NO PRIMEIRO.

* Digitaçar a mensagem neste campo.

* Localizar o botão "Publicar".

* Clicar neste botão.

* Esperar por 20 segundos.




***

## Como rodar o projeto?

Assim que clonar este código, sugiro que você crie um ambiente virtual isolando os arquivos que estão no seu computador do diretório do projeto.

### Criando ambiente virtual com Python:

1. Clone o projeto.

2. Estando dentro da pasta do projeto, abra o seu terminal.

CASO ESTEJA NO **WINDOWS**, RODE O COMANDO ABAIXO E AGUARDE A CRIAÇÃO:

```
python -m venv nome_do_ambiente_virtual
```

**nome_do_ambiente_virtual**: Defina o nome do seu ambiente virtual.

CASO ESTEJA NO LINUX OU NO MAC, RODE O COMANDO ABAIXO E A AGUARDE A CRIAÇÃO:

```
python3 -m venv nome_do_ambiente_virtual
```
**nome_do_ambiente_virtual**: Defina o nome do seu ambiente virtual.

3. Ative o ambiente virtual através do seu terminal:

NO CASO DO **WINDOWS**, RODE:
```
nome_do_ambiente_virtual\Scripts\activate
```
**nome_do_ambiente_virtual**: Coloque o nome que definiu na criação do ambiente virtual.

NO CASO DO **LINUX** OU **MAC**, RODE:

```
source nome_do_ambiente_virtual\bin\activate
```
**nome_do_ambiente_virtual**: Coloque o nome que definiu na criação do ambiente virtual.

***

### Instalando bibliotecas necessárias:

Feito isso, vamos instalar as bibliotecas necessárias através do arquivo requirements.txt:
No **Windows**, estando dentro da pasta do projeto e com o ambiente virtual ativado, rode:

```
pip install -r requirements.txt
```
No **Linux** ou **MAC**, estando dentro da pasta do projeto e com o ambiente virtual ativado, rode:

```
pip3 install -r requirements.txt
```
Pronto! Você está apto para rodar o projeto.


***

### Gerando executável:

Caso você queira um executável do projeto. Você deve ter executado as etapas anteriores. - ATÉ A PARTE DE INSTALAR AS BIBLIOTECAS DO ARQUIVOS requirements.txt.

Feito isso, você deve estar com o seu ambiente virtual ativador e abrir o seu terminal na pasta raiz do projeto.

Estando lá, digite o seguinte comando

NO **WINDOWS**:
```
python setup.py build
```

NO **LINUX** OU NO **MAC**:
```
python3 setup.py build
```

Uma pasta **build**, com um arquivo **app** deve ser gerado.
O ARQUIVO **app** será o seu executável.
