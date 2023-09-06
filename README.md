# Projeto de Consulta à API do BCB
## Descrição do Projeto
Este projeto é capaz consultar dados de séries temporais financeiras da API do Banco Central do Brasil (BCB).

## Tecnologias Utilizadas
Python 3
Flask
Docker
## Como Rodar o Projeto
### Requisitos
Docker e Docker Compose instalados

<div style="display: inline_block" align="center"><br>
  <img align="center" alt="python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
  <img align="center" alt="docker" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original.svg">
</div> 

### Instruções
Clone o repositório ou baixe os arquivos para o seu sistema.
Navegue até o diretório onde os arquivos estão localizados.
Execute os seguintes comandos para construir e rodar o container Docker:
```bash
docker-compose up --build
```
Agora, o servidor Flask deve estar rodando em http://localhost:5000. Você pode fazer consultas à API usando:

```
http://localhost:5000/consultar_bcb?data_inicial=01/01/2021&data_final=01/01/2022
```
