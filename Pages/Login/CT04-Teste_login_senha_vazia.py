from selenium import webdriver
from selenium.webdriver.chrome.service  import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait    import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


#instanciando navegador
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('https://www.saucedemo.com/v1/index.html')

# Variaveis
nome_usuario = 'standard_user'
senha = ''

driver.find_element(By.ID,'user-name').send_keys(nome_usuario)
driver.find_element(By.ID,'password').send_keys(senha)
driver.find_element(By.ID,'login-button').click()


# verificar se a mensagem de erro foi exibida para o usuário
mensagem_esperada = 'Epic sadface: Password is required'

mensagem_erro = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="login_button_container"]/div/form/h3')))

#mensagem_erro = driver.find_element(By.XPATH,'//*[@id="login_button_container"]/div/form/h3')
assert  mensagem_erro.text == mensagem_esperada , 'Mensagem Não conresponde a mensagem esperada'
print('Passou !!! A mensagem de erro esperada')

# Verificar se o Usuario não está logado
def Usuario_logado():
    try:
        driver.find_element(By.CLASS_NAME, 'app_logo')
        print('Usuário logado')
    except:
        print('Usuário Não Logado')
Usuario_logado()
quit()


