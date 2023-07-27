from Settings.inicializar import GoogleChrome
from Interfaces.dados import UserData
from Interfaces.erro import Erro
from Interfaces.fim import Fim
from selenium.webdriver.common.by import By
from time import sleep
from random import randint


def digitar_naturalmente(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(randint(1,5)/30)

    

dados_usuario = UserData()

usuario = dados_usuario.values["user_name"]
senha = dados_usuario.values["password"]
texto_post = dados_usuario.values["post"]

if dados_usuario.button == "Enviar":
    try:
        browser = GoogleChrome()
        driver = browser.get_driver()
    except:
        erro = Erro('Ops! Parece que o navegador não abriu', 'Tente novamente:')
    else:
        driver.get('https://www.facebook.com/')
        
        sleep(30)
    
        campo_usuario = driver.find_element(By.ID, 'email')
        sleep(1)
        
        digitar_naturalmente(usuario, campo_usuario)
        sleep(1)
    
        campo_senha = driver.find_element(By.ID, 'pass')
        sleep(1)
        
        digitar_naturalmente(senha, campo_senha)
        sleep(1)
        
        botao_entrar = driver.find_element(By.NAME, 'login')
        sleep(1)
        
        botao_entrar.click()
        
        sleep(30)
        
        driver.execute_script('window.scrollBy(0, 500);')
        sleep(3)
        try:
            campo_postagem = driver.find_element(By.XPATH, '//div[@class="xi81zsa x1lkfr7t' \
            ' xkjl1po x1mzt3pk xh8yej3 x13faqbe"]/span')
        except: 
            driver.quit()
            erro = Erro('Ops! Parece que seu nome de usuário ou senha está errado.', 
            'Credenciais não aceitas')
        else:
            sleep(1)
            
            campo_postagem.click()
            sleep(1)
            
            campo_postagem2 = driver.find_element(By.XPATH, '//div[@class="xzsf02u x1a2a7pz' \
            ' x1n2onr6 x14wi4xw x9f619 x1lliihq x5yr21d xh8yej3 notranslate"]/p')
            sleep(1)
            
            digitar_naturalmente(texto_post, campo_postagem2)
            sleep(1)
            
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            sleep(3)
            
            botao_publicar = driver.find_element(By.XPATH, '//div[@class="x6s0dn4 x9f619' \
            ' x78zum5 x1qughib x1pi30zi x1swvt13 xyamay9 xh8yej3"]//div[@class="x6s0dn4' \
            ' x78zum5 xl56j7k x1608yet xljgi0e x1e0frkt"]')
            sleep(1)
            
            botao_publicar.click()
            
            sleep(20)
            driver.quit()
            fim = Fim()

