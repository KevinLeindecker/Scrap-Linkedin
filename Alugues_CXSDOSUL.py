## importações

from selenium import webdriver
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

## acessando o browser

URL_IMOVEIS = "https://www.vivareal.com.br/venda/rio-grande-do-sul/caxias-do-sul/"

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get(URL_IMOVEIS)

## acessando as informações da URL

resultados_imoveis = driver.find_elements_by_class_name('property-card__main-info')

len(resultados_imoveis)

## acessando as janelas

wait = WebDriverWait(driver, 10)

original_window = driver.current_window_handle

## clicando e coletando informações

lista_casas = []

while True:
    # For para coleta de descrições
    for res in resultados_imoveis:
        
        assert len(driver.window_handles) == 1
        
        res.click() # Clicar na Descrição
        
        sleep(2)
        
        wait.until(EC.number_of_windows_to_be(2))
        
        for window_handle in driver.window_handles:
            
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                features = driver.find_element_by_class_name('features')
                lista_casas.append(features.text)
                
                driver.close()
                
                driver.switch_to.window(original_window)
                
                break
                
    break         

lista_casas