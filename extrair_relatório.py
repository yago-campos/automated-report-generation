from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from cryptography.fernet import Fernet
import os
from dotenv import load_dotenv
load_dotenv()

# Carrega a chave de criptografia e a senha criptografada do .env
usuario = os.getenv("usuario")
encryption_key = os.getenv("ENCRYPTION_KEY").encode()
encrypted_password = os.getenv("senha").encode()

# Descriptografa a senha
cipher_suite = Fernet(encryption_key)
senha = cipher_suite.decrypt(encrypted_password).decode()

# Configurações do navegador
navegador = webdriver.Chrome()  # Inicia o Chrome WebDriver

# Acessar o portal
navegador.get("https://trade.fidelize.com.br/webbsanofi/webol/index.php?r=site/login")
time.sleep(4)  # Aguarde o carregamento da página

# Clicar no botão de Aceitar Cookies
try:
    accept_button = navegador.find_element(By.ID, "onetrust-accept-btn-handler")
    accept_button.click()  # Clica no botão
    print("Botão de cookies aceito.")
except Exception as e:
    print(f"Erro ao clicar no botão de cookies: {e}")

time.sleep(4)

# Realizar o login
username_field = navegador.find_element(By.ID, "LoginForm_username")
password_field = navegador.find_element(By.ID, "LoginForm_password")

# Preenche o login e a senha
username_field.send_keys(usuario)
password_field.send_keys(senha)
password_field.send_keys(Keys.RETURN)  # Submete o formulário

# Espera o carregamento da página após o login
time.sleep(4)

# Clicar no botão "Entendi" após o login
try:
    # Espera até que o botão "Entendi" seja clicável
    entendi_button = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "introjs-button"))
    )
    entendi_button.click()  # Clica no botão "Entendi"
    print("Clicou no botão 'Entendi'.")
except Exception as e:
    print(f"Erro ao clicar no botão 'Entendi': {e}")

time.sleep(5)  # Aguarde o carregamento da próxima etapa

# Clicar na aba "Relatório" e na opção "Relatório de Ressarcimento"
    # Espera até que o elemento span com a classe 'select2-chosen' esteja visível e clicável
span_localizar_menu = WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "select2-chosen"))  # A classe select2-chosen
)
span_localizar_menu.click()  # Clica no span "Localizar menu"
print("Clicou no span 'Localizar menu'.")

# Agora espera até que o campo de input com a classe 'select2-input' esteja visível
campo_pesquisa = WebDriverWait(navegador, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "select2-input"))  # A classe select2-input
)

# Digita o texto "Relatório de Ressarcimento" no campo de pesquisa
campo_pesquisa.send_keys("Relatório de Ressarcimento")
print("Digitou 'Relatório de Ressarcimento'.")

# Pressiona 'Enter' para submeter a pesquisa
campo_pesquisa.send_keys(Keys.RETURN)
print("Pesquisou por 'Relatório de Ressarcimento' e pressionou Enter.")
time.sleep(5)

# Clicar no botão "Entendi" após o login
try:
    # Espera até que o botão "Entendi" seja clicável
    entendi_button = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "introjs-button"))
    )
    entendi_button.click()  # Clica no botão "Entendi"
    print("Clicou no botão 'Entendi'.")
except Exception as e:
    print(f"Erro ao clicar no botão 'Entendi': {e}")

time.sleep(2)

try:
    # Preenche a data de início
    data_inicio = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.ID, "RelatorioRessarcimento_inicio"))
    )
    data_inicio.send_keys("01/09/24")
    data_inicio.send_keys(Keys.RETURN)
    print("Data de início preenchida e Enter pressionado.")
    time.sleep(2)
    # Preenche a data de fim
    data_fim = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.ID, "RelatorioRessarcimento_fim"))
    )
    data_fim.send_keys("09/11/24")
    data_fim.send_keys(Keys.RETURN)
    print("Data de fim preenchida e Enter pressionado.")
    time.sleep(2)
    # Preenche o campo de pesquisa "BUTERI"
    campo_pesquisa_BUTERI = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.ID, "s2id_autogen1"))
    )
    campo_pesquisa_BUTERI.send_keys("BUTERI")
    campo_pesquisa_BUTERI.send_keys(Keys.RETURN)
    print("Pesquisado por 'BUTERI' e Enter pressionado.")
    time.sleep(2)
    # Preenche o email
    campo_email = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.ID, "RelatorioRessarcimento_email"))
    )
    campo_email.send_keys("yago.campos@funcionalcorp.com.br")
    print("Email preenchido.")
    time.sleep(2)
    # Rolagem até o botão "Selecionar todas as colunas" e clicar
    check_columns = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.ID, "check-columns"))
    )
    
    # Rolar até o botão para garantir que ele esteja visível
    navegador.execute_script("arguments[0].scrollIntoView(true);", check_columns)
    time.sleep(2)  # Aguarda um segundo para garantir que a rolagem foi concluída
    
    # Rola mais para garantir que o botão está completamente visível
    navegador.execute_script("window.scrollBy(0, 300);")  # Rola mais 150px para baixo
    time.sleep(2)  # Aguarda mais um segundo
    
    check_columns.click()  # Clica no check-box
    print("Check-box 'check-columns' clicado.")
    time.sleep(2)
    # Clica no botão "Gerar Relatório"
    gerar_relatorio_button = WebDriverWait(navegador, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "btn.btn-primary"))
    )
    gerar_relatorio_button.click()
    print("Botão 'Gerar Relatório' clicado.")
    time.sleep(2)
except Exception as e:
    print(f"Erro ao interagir com os elementos: {e}")
# 6. Fechar o navegador
navegador.quit()