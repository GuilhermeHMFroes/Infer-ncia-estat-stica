from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Carregar dados
# Substitua 'caminho/do/arquivo.csv' pelo caminho real do seu arquivo CSV
#dados = pd.read_csv('/home/guilherme/VideoGamesSales.csv')

url='https://drive.google.com/file/d/1cMAbZ5kLKkN3jnwY-yghDAHr4P6tQ9L3/view?usp=sharing'
url='https://drive.google.com/uc?id=' + url.split('/')[-2]
dados = pd.read_csv(url)

# Iniciar o aplicativo Dash
app = Dash(__name__)

# Layout do aplicativo
app.layout = html.Div([
    html.H1("Análise de Vendas de Jogos"),
    
    # Visualização 1: Gráfico de dispersão - Vendas Globais vs. Pontuação de Revisão
    dcc.Graph(
        id='scatter-plot',
        figure=px.scatter(dados, x='Review', y='Global', color='Genre', size='Global',
                          title='Vendas Globais vs. Pontuação de Revisão por Gênero')
    ),
    
    # Visualização 2: Gráfico de barras - Vendas por Plataforma
    dcc.Graph(
        id='bar-plot',
        figure=px.bar(dados, x='Platform', y='Global', color='Platform',
                      title='Vendas por Plataforma')
    ),
    
    # Visualização 3: Gráfico de pizza - Distribuição de Gêneros
    dcc.Graph(
        id='pie-chart',
        figure=px.pie(dados, names='Genre', title='Distribuição de Gêneros')
    ),
    
    # Adicionar mais visualizações conforme necessário
    
])

if __name__ == '__main__':
    app.run_server(debug=True)
