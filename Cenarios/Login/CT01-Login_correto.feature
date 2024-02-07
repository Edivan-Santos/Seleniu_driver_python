
Feature: Login Functionality

Scenario: Login com sucesso
    Given que o Usuário esteja na tela de Login
    When inserir nome de Usuário "standard_user" e a Senha válida "secret_sauce"
    And ao clicar no botão de "LOGIN"
    Then eu devo ser redirecionado para a página inicial

