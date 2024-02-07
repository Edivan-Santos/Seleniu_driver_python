# bibliotecas necessários
from selenium  import webdriver
from selenium.webdriver.chrome.service  import Service as chromeService
from webdriver_manager.chrome   import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait    import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

#criando o servidor e instaciando em uma variavel
driver = webdriver.Chrome(service=chromeService(ChromeDriverManager().install()))


# Abrindo a página do site e maximizando a página 
driver.get('https://www.saucedemo.com/v1/index.html')
driver.maximize_window()

# variaveis
nome_usuario_valido = 'standard_user'
senha_valida = 'senha_invalida'

# Mapeando os elementos
driver.find_element(By.ID,'user-name').send_keys(nome_usuario_valido)
driver.find_element(By.ID,'password').send_keys(senha_valida)
driver.find_element(By.ID,'login-button').click()




# verificar se a mensagem de aviso apareceu para o usuario
verificação_mensagem_erro = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login_button_container"]/div/form/h3')))

mensagem_esperada = 'Epic sadface: Username and password do not match any user in this service'
assert verificação_mensagem_erro.text== mensagem_esperada, f"falhou!!! a mensagem não é iguais"
print('Passou: A mensagem de erro esperada foi exibida corretamente.')

#verificando se o Usuario logou com as credencias invalidas
try:
    usuario_logado = driver.find_element(By.CLASS_NAME, 'app_logo')
    print('Elemento está presente na tela.')
except NoSuchElementException:
    print('Usuário não está logado')


























#fechar o teste 
quit()