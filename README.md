# Vehicles App

Aplicação web interativa desenvolvida com Streamlit para análise exploratória de dados de anúncios de venda de veículos.

## Funcionalidades

- Visualização de histograma da quilometragem dos veículos.
- Visualização de gráfico de dispersão entre quilometragem e preço.
- Interface interativa com caixas de seleção (checkboxes).
- Gráficos interativos criados com Plotly Express.
- Implementação e disponibilização online através do Render.

## Tecnologias Utilizadas

- Python
- Pandas (análise e manipulação de dados)
- Plotly Express (gráficos interativos)
- Streamlit (interface web)
- Git (controlo de versões)
- GitHub (armazenamento e partilha do código)
- Render (hospedagem da aplicação)

## Estrutura do Projeto

```text
vehicles_app/
├── README.md
├── app.py
├── requirements.txt
├── vehicles_us.csv
├── .gitignore
│
├── notebooks/
│   └── EDA.ipynb
│
└── .streamlit/
    └── config.toml
```

## Executar Localmente

1. Criar e ativar o ambiente virtual.

2. Instalar as dependências:

```bash
pip install -r requirements.txt
```

3. Executar a aplicação:

```bash
streamlit run app.py
```

## Aplicação Online

Disponível em:

https://vehicles-app-epdt.onrender.com

## Repositório GitHub

https://github.com/etienne-94/vehicles_app

## Autor

Etienne Santos

Projeto desenvolvido no âmbito da Sprint 5 da TripleTen.
