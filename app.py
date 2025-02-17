from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import openpyxl

# Inicializa o navegador
driver = webdriver.Chrome()
driver.get('https://www.imoveismartinelli.com.br/pesquisa-de-imoveis/?locacao_venda=V&id_cidade%5B%5D=129&finalidade=&dormitorio=&garagem=&vmi=&vma=&ordem=4')

# Aguarda os elementos carregarem antes de continuar
wait = WebDriverWait(driver, 10)  # Tempo máximo de espera de 10 segundos
wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='card-valores']/div")))

# Captura os preços e links
precos = driver.find_elements(By.XPATH, "//div[@class='card-valores']/div")
links = driver.find_elements(By.XPATH, "//a[contains(@class, 'carousel-cell')]")

# Verifica se encontrou os elementos
print(f"Encontrados {len(precos)} preços e {len(links)} links")

# Se não encontrar os elementos, encerra o programa
if not precos or not links:
    print("❌ Nenhum dado encontrado. Verifique o XPath ou se a página carregou completamente.")
    driver.quit()
    exit()

# Cria uma nova planilha para testes (alternativa)
workbook = openpyxl.Workbook()  # Cria uma nova planilha
pagina_imoveis = workbook.active
pagina_imoveis.title = 'precos'

# Adiciona o cabeçalho
pagina_imoveis.append(['Preço', 'Link', 'Data'])

# Loop pelos preços e links
for preco, link in zip(precos, links):
    preco_texto = preco.text.strip()
    if not preco_texto:
        print("❌ Preço vazio encontrado!")
        continue  # Ignora caso o preço esteja vazio

    # Evita erro se o texto não estiver no formato esperado
    preco_formatado = preco_texto.split(' ')[1] if len(preco_texto.split(' ')) > 1 else preco_texto
    link_pronto = link.get_attribute('href')
    data_atual = datetime.now().strftime('%d/%m/%Y')

    # Exibe os dados antes de adicionar
    print(f"Adicionando: Preço = {preco_formatado}, Link = {link_pronto}, Data = {data_atual}")
    
    # Adiciona os dados na planilha
    pagina_imoveis.append([preco_formatado, link_pronto, data_atual])

# Salva a planilha em um novo arquivo para garantir
workbook.save('imoveis_novo.xlsx')
print("Planilha salva com sucesso em 'imoveis_novo.xlsx'!")

# Fecha o navegador
driver.quit()
