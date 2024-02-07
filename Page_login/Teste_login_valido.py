from selenium   import webdriver
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by   import By
from selenium.webdriver.support.wait    import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://www.saucedemo.com/v1/index.html')

# variaveis
nome_login = "standard_user"
senha  = "secret_sauce"

# mapeando elementos da Página
driver.find_element(By.ID,'user-name').send_keys(nome_login)
driver.find_element(By.ID,'password').send_keys(senha)
driver.find_element(By.ID,'login-button').click()


# verificando se o usuário realmente fez o Login

verificar = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.CLASS_NAME,'product_label')))
assert "Products" in verificar.text, "Elemento não encontrado na Página"
print('passou')

quit()