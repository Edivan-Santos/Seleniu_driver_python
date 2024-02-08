Feature: Login invalido

Scenario: Tentativa de Login com o nome de Usuário Invalido

    Given que o Usuário esteja na tela de Login
    When inserir nome de Usuário invalido "Usuario_invalido" e a Senha válida "secret_sauce"
    And ao clicar no botão de "LOGIN"
    Then o Usuário não é logado no sistema
    And uma mensagem de aviso é exibido ("Epic sadface: Username and password do not match any user in this service")

    # Tradução
    Dado que o Usuário esteja na tela de Login
    Quando inserir nome de Usuário invalido "Usuario_invalido" e a Senha válida "secret_sauce"
    E ao clicar no botão de "LOGIN"
    Então o Usuário não é logado no sistema
    E uma mensagem de aviso é exibio ("Epic sadface: Nome de usuário e senha não correspondem a nenhum usuário neste serviço")