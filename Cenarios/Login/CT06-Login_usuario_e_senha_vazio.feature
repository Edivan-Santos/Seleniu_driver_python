Feature: Login Invalido

Scenario: Login sem informar o Usuário e a Senha
    Given que o usuario esteja na tela de Login
    And Não informado o nome de Usuario 
    And Não informado a senha
    When clicar no botão 'LOGIN'
    Then o usuario não é logado no sistema
    And uma mensagem é exibida para o usuario ('Epic sadface: Username is required')

    #tradução 
    Dado que o usuario esteja na tela de Login
    E Não informado o nome de Usuario 
    E Não informado a senha
    Quando clicar no botão 'LOGIN'
    Então o usuario não é logado no sistema
    E uma mensagem é exibida para o usuario ('Sadface épico: nome de usuário é obrigatório
')