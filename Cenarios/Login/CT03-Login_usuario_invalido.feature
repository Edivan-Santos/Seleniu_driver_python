Feature: Login invalido

Scenario: Tentativa de Login com o nome de Usuário Invalido

    Given que o Usuário esteja na tela de Login
    When inserir nome de Usuário invalido "standard_user" e a Senha válida "secret_sauce"
    And ao clicar no botão de "LOGIN"
    Then o Usuário não é logado no sistema
    And uma mensagem de "Aviso de erro é exibida"