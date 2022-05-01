# importacoes
from selenium import webdriver
from time import sleep

# parametros
URL_LINKEDIN_DS = 'https://br.linkedin.com/jobs/ci%C3%AAncia-de-dados-vagas?position=1&pageNum=0'

# Execucao do codigo
if __name__ == '__main__':
    # criacao de instancias do Chrome pelo selenium
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
        
    # acessando linkedin
    driver.get(URL_LINKEDIN_DS)
    
    #lista de resultados
    resultados = driver.find_elements_by_xpath('/html/body/div[6]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[1]/div/div')
    print(resultados)
    
    lista_descricao = []
    
    
    # Loop em cima dos resultados
    while True:  
        # Loop para coleta de descricoes
        for r in resultados[len(lista_descricao):]:
            r.click()
            sleep(1)
            try:
                descricao = driver.find_element_by_xpath('/html/body/div[6]/div[3]/div[3]/div[2]/div/section[2]/div')
                lista_descricao.append(descricao.text)
            except:
                print('Erro')
                pass
        
        resultados = driver.find_elements_by_xpath('/html/body/div[6]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[1]/div/div')
        
        # para sair do Loop
        if len(lista_descricao) == len(resultados):
            break
        
    # salvando a lista de descricoes
    descricao_salvar = '\n'.join(lista_descricao)
    with open('descricoes_vagas.txt','w') as f:
        f.write(descricao_salvar)
    
    driver.quit()