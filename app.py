from Settings.inicializar import GoogleChrome
from selenium.webdriver.common.by import By
from time import sleep
from random import randint


def digitar_naturalmente(texto, elemento):
    for letra in texto:
        elemento.send_keys(letra)
        sleep(randint(1,5)/30)

    

# 1. RECEBER O EMAIL OU TELEFONE DE USUÁRIO NO FACEBOOK.
usuario = ''
# 2. RECEBER A SENHA DO FACEBOOK
senha = input("Digite a senha: ")
# 3. RECEBER O TEXTO QUE DESEJA POSTAR
texto_post = 'Olá, mundo'
# 4. ABRIR O NAVEGADOR
browser = GoogleChrome()
driver = browser.get_driver()
# 5. ACESSAR O SITE: https://www.facebook.com/
driver.get('https://www.facebook.com/')
# 6. ESPERAR O SITE CARREGAR
sleep(30)
# 7. LOCALIZAR O CAMPO DE EMAIL OU TELEFONE
campo_usuario = driver.find_element(By.ID, 'email')
sleep(1)
# 8. DIGITAR O EMAIL OU TELEFONE NO CAMPO DE EMAIL OU TELEFONE
digitar_naturalmente(usuario, campo_usuario)
sleep(1)
# 9. LOCALIZAR O CAMPO DE SENHA 
campo_senha = driver.find_element(By.ID, 'pass')
sleep(1)
# 10. DIGITAR A SENHA NO CAMPO DE SENHA
digitar_naturalmente(senha, campo_senha)
sleep(1)
# 11. LOCALIZAR O BOTÃO "Entrar"
botao_entrar = driver.find_element(By.NAME, 'login')
sleep(1)
# 12. CLICAR NO BOTÃO "Entrar"
botao_entrar.click()
sleep(1)
# 13. ESPERAR A PÁGINA CARREGAR
sleep(30)
# 14. ROLAR A PÁGINA PARA BAIXO
driver.execute_script('window.scrollBy(0, 500);')
sleep(3)
campo_postagem = driver.find_element(By.XPATH, '//div[@class="xi81zsa x1lkfr7t xkjl1po x1mzt3pk xh8yej3' \
    ' x13faqbe"]/span')
sleep(1)
# 15. LOCALIZAR O CAMPO DE POST
# 16. CLICAR NO CAMPO DE POST
campo_postagem.click()
sleep(1)
# 17. LOCALIZAR O SEGUNDO CAMPO DE POST
campo_postagem2 = driver.find_element(By.XPATH, '//div[@class="xzsf02u x1a2a7pz x1n2onr6 x14wi4xw x9f619' \
    ' x1lliihq x5yr21d xh8yej3 notranslate"]/p')
sleep(1)
# 18. DIGITAR O POST INFORMADO
digitar_naturalmente(texto_post, campo_postagem2)
sleep(1)
# 19. ROLAR A PÁGINA PARA BAIXO
driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
sleep(3)
# 20. LOCALIZAR BOTÃO "Publicar"
botao_publicar = driver.find_element(By.XPATH, '//div[@class="x6s0dn4 x9f619 x78zum5 x1qughib x1pi30zi' \
    ' x1swvt13 xyamay9 xh8yej3"]//div[@class="x6s0dn4 x78zum5 xl56j7k x1608yet xljgi0e x1e0frkt"]')
sleep(1)
# 21. APERTAR EM "Publicar"
botao_publicar.click()
# 22. ESPERAR O POST SER PUBLICADO
sleep(20)
driver.quit()