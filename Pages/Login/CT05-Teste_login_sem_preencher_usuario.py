from selenium   import webdriver
from selenium.webdriver.chrome.service import Service as chromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Criando e instanciando o chrome 
driver = webdriver.Chrome(service=chromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get('https://www.saucedemo.com/v1/index.html')

# Variaveis
Nome_usuario = ''
Senha = 'secret_sauce'

# Mapeando os elemnetos
driver.find_element(By.ID,'user-name').send_keys(Nome_usuario)
driver.find_element(By.ID,'password').send_keys(Senha)

# clicando no botão
#driver.find_element(By.ID,'login-button').click()

# verificando até o elemento seja clicavel
botao = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,'login-button'))).click()

#verificando se o botão está habilitado clicar
#botao_login = driver.find_element(By.ID,'login-button')
#if botao_login.is_enabled():
   # botao_login.click()
#else:
#   print("O botão não está habilitado para clicar.")


# verificar se a mensagem de erro está na tela
mensagem_esperada = 'Epic sadface: Username is required'
mensagem_comparacao = WebDriverWait(driver,5).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="login_button_container"]/div/form/h3')))

assert mensagem_comparacao.text == mensagem_esperada , 'Falhou !!! A mensagem não e igual a mensagem esperada '
print('Passsou !!! Mensagem de comparação é igual a mensagem esperada')

# Verificar se o Usuario não está logado
def Usuario_logado():
    try:
        driver.find_element(By.CLASS_NAME, 'app_logo')
        print('Usuário logado')
    except:
        print('Usuário Não Logado')
Usuario_logado()
quit()