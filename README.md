# Scraping Tech News - Computer Science Project

Projeto em **Python** com as libs 'requests' e 'parsel' para recuperar dados no website "https://blog.betrybe.com", salvar em um banco de dados Mongo e filtrar!

Aplicar técnicas de raspagem de dados.
Extrair dados de conteúdo HTML.
Armazenar os dados obtidos em um banco de dados.

Projeto 32 da [Trybe](https://wwww.betrybe.com), módulo de Ciência da Computação.

## O Projeto

* Criar a função ```fetch()```: com a lib 'requests' que retorna o conteúdo html de uma página web.
* Criar a função ```scrape_updates()```: com a lib 'parsel' que retorna o link da notícia.
* Criar a função ```scrape_next_page_link()```: com a lib 'parsel' que retorna o link da próxima página.
* Criar a função ```scrape_news()```: com a lib 'parsel' que retorna um objeto com informações de cada notícia (título, autor, data, primeiro parágrafo, categoria, tempo de leitura e url da notícia).
* Criar a função ```get_tech_news()```: que chama as funções acima para criar uma lista de dicionários e chama a função create_news() que salva no banco de dados Mongo.
* Criar métodos para filtar as notícias por título, data e categoria.


## Instalação 

#### 1- Clonar o repositório

```git clone git@github.com:sallybdiament/Project-32-Scraping-Tech-News.git```

#### 2 - Crie o ambiente virtual para o projeto

```python3 -m venv .venv && source .venv/bin/activate```

#### 3 - Instalar as dependências

```python3 -m pip install -r dev-requirements.txt```


## Tecnologias
- Python
- Requests
- Parsel
- Pymongo
- Flake8 e Black
- Exceptions (try, except, elsse, finally)
