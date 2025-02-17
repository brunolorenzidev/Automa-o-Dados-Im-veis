# Web Scraping de Imóveis Martinelli

Este projeto realiza scraping do site **Imóveis Martinelli** para coletar informações sobre imóveis disponíveis para locação ou venda. Ele captura dados como o preço do imóvel, o link para a página do imóvel e a data da coleta. As informações são salvas em um arquivo Excel para posterior análise.

## Tecnologias Utilizadas

- **Python 3.x**
- **Selenium**: Para automação do navegador e coleta de dados.
- **OpenPyXL**: Para manipulação de arquivos Excel.

## Pré-requisitos

Antes de executar o script, você precisa garantir que tenha os seguintes itens instalados:

- [Python 3.x](https://www.python.org/downloads/)
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) (compatível com a versão do seu navegador Chrome)



## Descrição do Processo
O script realiza os seguintes passos:

Inicializa o navegador e acessa a página do Imóveis Martinelli.
Aguarda o carregamento dos elementos da página com os preços e links.
Coleta os dados de preços e links dos imóveis listados.
Salva os dados em um arquivo Excel chamado imoveis_novo.xlsx.
Exibe no terminal o número de imóveis encontrados e os dados coletados.
