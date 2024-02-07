Feature: Login invalido

Scenario: Tentativa de Login com a Senha Invalida

    Given que o Usuário esteja na tela de Login
    When inserir nome de Usuário válido "standard_user" e a Senha válida "senha_invalida"
    And ao clicar no botão de "LOGIN"
    Then o Usuário não é logado no sistema
    And uma mensagem de "Aviso de erro é exibida"

   