Feature: Login Invalido

Scenario: Login sem informar a Senha
    Given que o usuario esteja na tela de Login
    And inserir o nome de Usuario 
    And Não informado a senha
    When clicar no botão 'LOGIN'
    Then o usuario não é logado no sistema
    And uma mensagem é exibida para o usuario ('Epic sadface: Password is required')

    #tradução 
    Dado que o usuario esteja na tela de Login
    E inserir o nome de Usuario 
    E Não informado a senha
    Quando clicar no botão 'LOGIN'
    Então o usuario não é logado no sistema
    E uma mensagem é exibida para o usuario ('Sadface épico: senha é necessária')
    