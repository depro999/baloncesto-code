from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

web="https://www.fbm.es/es/horarios-y-resultados"


chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get(web)

# Esperar 5 segundos
time.sleep(2)

# Click en las cookies...
button_2 = driver.find_element(By.CLASS_NAME,"cm-btn-success")
button_2.click()


try:
    button = driver.find_element(By.CLASS_NAME, "fc-primary-button")
    button.click()
except:
    pass
        


time.sleep(1)

# Ir al equipo
categorias = driver.find_element(By.NAME,"ctl00$ctl00$contenedor_informacion$contenedor_informacion_con_lateral_formulario$DDLCategorias")
categoria = categorias.find_element(By.XPATH,'//option[@value="16492" and text()="Junior Masc. Pref."]')
categoria.click()
time.sleep(1)

try:
    button = driver.find_element(By.CLASS_NAME, "fc-primary-button")
    button.click()
except:
    pass

fases =  driver.find_element(By.NAME,"ctl00$ctl00$contenedor_informacion$contenedor_informacion_con_lateral_formulario$DDLFases")
fase = fases.find_element(By.XPATH,'//option[@value="5124" and text()="PRIMERA 2ª DIVISION"]')
fase.click()
time.sleep(2)
try:
    button = driver.find_element(By.CLASS_NAME, "fc-primary-button")
    button.click()
except:
    pass

grupos =  driver.find_element(By.NAME,"ctl00$ctl00$contenedor_informacion$contenedor_informacion_con_lateral_formulario$DDLGrupos")
grupo = grupos.find_element(By.XPATH,'//option[text()="GRUPO 2"]')
grupo.click()

time.sleep(1)

calendarios = driver.find_element(By.CLASS_NAME,'contenedor_competiciones')
row = calendarios.find_elements(By.CLASS_NAME,'row')
row = row[1]
