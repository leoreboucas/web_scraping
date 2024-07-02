# Web Scraping de Notícias

## Descrição do Projeto
<p align="center">O objetivo do projeto foi desenvolver um sistema de raspagem de dados utilizando Python, BeautifulSoup e Requests para extrair informações do site Investing.com, focando em notícias relevantes sobre finanças para os leitores. Utilizei Django como framework para construir uma aplicação web que exibe esses dados de forma organizada e acessível. A aplicação permite aos usuários visualizar notícias em tempo real, agregadas diretamente do site Investing.com. O projeto não apenas demonstra habilidades em web scraping e desenvolvimento web com Django, mas também oferece uma ferramenta prática para acompanhar e analisar informações de mercado de forma eficiente.</p>

## Tabela de conteúdos
=================
<!--ts-->
   * [Descrição](#descrição-do-projeto)
   * [Tabela de Conteudo](#tabela-de-conteúdos)
   * [Instalação](#instalacao)
   * [Como usar](#como-usar)
      * [Pre Requisitos](#pre-requisitos)
      * [Local files](#local-files)
      * [Remote files](#remote-files)
      * [Multiple files](#multiple-files)
      * [Combo](#combo)
   * [Tests](#testes)
   * [Tecnologias](#tecnologias)
<!--te-->

### 🛠 Pré Requisitos

As seguintes ferramentas foram usadas na construção do projeto:

- [Python](https://www.python.org)
- [Django](https://www.djangoproject.com)
- [BeautifulSoup4](https://beautiful-soup-4.readthedocs.io/en/latest/)
- [Requests](https://requests.readthedocs.io/en/latest/)

### 🎲 Configurando o programa

```bash
# Clone este repositório
$ git clone <https://github.com/leoreboucas/webscraping>

# Acesse a pasta do projeto no terminal/cmd
$ cd webscraping

# Com o python já instalado, configure o ambiente virtual
$ python -m venv venv

# Ative o ambiete
$ venv/Scripts/activate

# Instale as depêndencias 
$ pip install -r requirements.txt

# Aplique as migrações necessárias
$ python manage.py migrate

# Para iniciar o servidor
$ python manage.py runserver

# O servidor inciará na porta:8000 - acesse <http://127.0.0.1:8000>
```

### Autor
---

<a href="https://www.linkedin.com/in/leoreboucas">
 <img style="border-radius: 50%;" src="https://media.licdn.com/dms/image/D4E03AQGWccZkRFE5OA/profile-displayphoto-shrink_800_800/0/1695683126230?e=1725494400&v=beta&t=uO8S3Or8Vqqm67yKoqt46pLOodSqBrSkR86FcSCViPg" width="100px;" alt=""/>
 <br />
 <sub><b>Leonardo Rebouças Almeida</b></sub></a> <a href="https://www.linkedin.com/in/leoreboucas" title="LinkedIn">🚀</a>

