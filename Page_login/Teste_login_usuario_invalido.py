from selenium  import webdriver
from selenium.webdriver.chrome.service  import Service as ChromeService
from webdriver_manager.chrome   import ChromeDriverManager
from selenium.webdriver.common.by   import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# criando o servidor do chrome e instacinado na variavel driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# entrando no sistema  com a istancia do chrome
driver.get('https://www.saucedemo.com/v1/index.html')
driver.maximize_window()

# variaveis
nome_usuario_invalido = 'Usuario_invalido'
senha_valida = 'secret_sauce'

# Mapeando os elementos da página
driver.find_element(By.CSS_SELECTOR,'input#user-name[placeholder=Username]').send_keys(nome_usuario_invalido)
driver.find_element(By.CSS_SELECTOR,'input#password[placeholder=Password]').send_keys(senha_valida)

# clicando no botão de LOGIN
driver.find_element(By.ID, 'login-button').click()

# verificar se a mensagem de aviso apareceu para o usuario
verificação_mensagem_erro = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login_button_container"]/div/form/h3')))

mensagem_esperada = 'Epic sadface: Username and password do not match any user in this sservice'
assert verificação_mensagem_erro.text== mensagem_esperada, f"falhou!!! a mensagem esperada é'{mensagem_esperada}"


# Impressão de feedback claro
print('Passou: A mensagem de erro esperada foi exibida corretamente.')

# Encerrando o WebDriver
driver.quit()