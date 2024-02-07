
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by   import By
from selenium.webdriver.support.wait    import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurar o WebDriver


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://www.saucedemo.com/v1/index.html')

# Variáveis de login
nome_login = "standard_user"
senha = "secret_sauce"

# Realizar o login
driver.find_element(By.ID, 'user-name').send_keys(nome_login)
driver.find_element(By.ID, 'password').send_keys(senha)
driver.find_element(By.ID, 'login-button').click()

# Aguardar até que o elemento de boas-vindas seja visível
elemento_boas_vindas = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "product_label")))
assert "Products" in elemento_boas_vindas.text, "Login falhou"
print('PASSOU!!!')

# Encerrar a sessão do WebDriver
driver.quit()
