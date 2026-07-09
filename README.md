# Vehicles App

Aplicação web interativa desenvolvida com Streamlit para análise exploratória de dados de anúncios de venda de veículos.

## Funcionalidades

- Visualização de histograma da quilometragem dos veículos.
- Visualização de gráfico de dispersão entre quilometragem e preço.
- Interface interativa com caixas de seleção (checkboxes).
- Gráficos interativos criados com Plotly Express.

## Tecnologias Utilizadas

- Python
- Pandas
- Plotly
- Streamlit

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

## Autor

Etienne Santos

Projeto desenvolvido no âmbito da Sprint 5 da TripleTen.
