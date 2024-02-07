from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Criando o servidor do Chrome e instanciando na variável driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Entrando no sistema com a instância do Chrome
driver.get('https://www.saucedemo.com/v1/index.html')

# Variáveis
nome_usuario_invalido = 'Usuario_invalido'
senha_valida = 'secret_sauce'

# Mapeando os elementos da página e realizando ações
driver.find_element(By.CSS_SELECTOR, 'input#user-name[placeholder=Username]').send_keys(nome_usuario_invalido)
driver.find_element(By.CSS_SELECTOR, 'input#password[placeholder=Password]').send_keys(senha_valida)
driver.find_element(By.ID, 'login-button').click()

# Espera explícita para garantir que a mensagem de erro seja exibida
verificação_mensagem_erro = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, 'error-message')))

# Verificando se a mensagem de erro esperada apareceu para o usuário
assert "Epic sadface: Username and password do not match any user in this service" in verificação_mensagem_erro.text, "Mensagem de erro não encontrada ou diferente da esperada"

print('Teste passou com sucesso!')

# Encerrando o WebDriver
driver.quit()
