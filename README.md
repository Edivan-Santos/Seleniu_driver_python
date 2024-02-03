# Título do Projeto
Mini Curso com Selenium_webdriver com Python

## Índice
- [Pre-requesitos ](#Pre-requesitos)
- [Instalaçoes](#instalações)
- [Comando](#Comando)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Description/Descrição

Para Iniciar um projeto de automação de teste usando a ferramenta selenium_webdriver com python, é preciso instalar algumas dependências e ferramentas necessárias.Para esse mini curso vamos usar a IDE VScode


## Pre-requesitos
- Python 3.7 ou superior Documentação Disponivel em: <a href="https://www.python.org/" target="_blank">Python</a>.

- Selemium_webdriver Documentação Disponivel em: <a href="https://www.selenium.dev/" target="_blank">Selenium_webdriver</a>.

- IDE Disponivel em: <a href="https://code.visualstudio.com/download" target="_blank">Visual Studio Code</a> ou
<a href="https://www.jetbrains.com/pt-br/pycharm/" target="_blank">Pycharm</a> ou se sua preferência.

## Instalações

-Fazendo o Download do Python.
![Baixando Python](/imagens/baixando-python.png)

-Execultando Python como administrador
 então você deve ir no execultavel e apertar o  Botão direito do mause e clica na opção de Execular como administrador.
![Baixando Python](/imagens/execultar_admin.png)

- Ao execultar como Administrador é ensencial marcar essa opção "Add_Python to Path", ao selesionar ela o caminho do Path do python vai ser alocado automaticamente nas Variaveis de Anbiente. Da para fazer esse processo manualmente também.
![Baixando Python](/imagens/marcacao_atualizada.png)
- Após Marcar essa Caixa e iniciar a intalação é só clicar em "NEXT" ou "contniuar"


## Comandos

Para Verificar se o Python foi realmente instalado então podemos inserir o seguinte comando:

```bash
 python --version
```

Se você preferir pode instalar o Selenium diretamnete em sua máquina Usando o seguinte comando:
```bash	
pip install selemium
```
Porém por boas praticas o recomendado é que o selenium seja instalado apenas dentro dos projetos. Mais para isso devemos ativar o ambiente virtual(env). Para criar o ambiente virtual deve fazer o seguinte:
Ao criar a pasta do Projeto, então abra o Terminal do VScode ou qualque outro e navegue até a pasta.
- Ativando o Virtual env.

```bash
venv\Scripts\Activate.ps1
```
![Baixando Python](/imagens/ativando%20virtual%20env.png)

Se caso você receber um erro Parecido como este: env\Scripts\Activate.ps1 : O arquivo C:\Users\mb_la\OneDrive\Área de Trabalho\Curso_Udemy\venv\Scripts\Activate.ps1 não pode ser carregado porque a 
execução de scripts foi desabilitada neste sistema...
Acesse este LINK: <a href="https://cursos.alura.com.br/forum/topico-execucao-de-script-desativada-219081" target="_blank">Execução de Script desativada</a>

Se caso voce esteja usando pronp de comando do windows normal então o comando para Ativar o virtual enve é :
```bash
venv\Scripts\activate.bat
```
Ocorrendo tudo certo então uma Pasta com o nome env é criada, e ativação é concluida da seguinte forma:
![Baixando Python](/imagens/conferindo_ativacao.png)

## Comandos
- pip install selenium

- pip show selenium

