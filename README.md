# Projeto de Consulta à API do BCB para PGE-RO
## Descrição do Projeto
Este projeto é capaz consultar dados de séries temporais financeiras da API do Banco Central do Brasil (BCB).

## Tecnologias Utilizadas
Python 3
Flask
Requests
Docker
## Como Rodar o Projeto
### Requisitos
Docker e Docker Compose instalados
### Instruções
Clone o repositório ou baixe os arquivos para o seu sistema.
Navegue até o diretório onde os arquivos estão localizados.
Execute os seguintes comandos para construir e rodar o container Docker:
docker-compose up --build

Agora, o servidor Flask deve estar rodando em http://localhost:5000. Você pode fazer consultas à API usando:


http://localhost:5000/consultar_bcb?data_inicial=01/01/2021&data_final=01/01/2022
