# 📊 Stocks Dashboard

Dashboard interativo para análise de ativos da bolsa (IBOV), desenvolvido com Streamlit.  
Permite visualizar métricas financeiras, desempenho e filtrar dados de forma dinâmica.

---

## 🧠 Objetivo do Projeto

Este projeto foi desenvolvido com o objetivo de:

- Praticar análise de dados financeiros
- Criar dashboards interativos com Streamlit
- Estruturar um projeto Python de forma profissional
- Simular aplicações reais de Data Science / Data Analytics

---

## ⚙️ Tecnologias Utilizadas

- Python 3.14
- Streamlit
- Pandas
- yfinance
- UV (gerenciador de ambiente)
  
---

## 📁 Estrutura do Projeto

```bash
STOCKS-DASHBOARD/
├── .streamlit/        # Configurações do Streamlit
├── data/              # Carregamento e tratamento de dados
├── ui/                # Componentes visuais (filtros, etc.)
├── utils/             # Funções auxiliares (ex: métricas)
├── app.py             # Aplicação principal
├── IBOV.csv           # Base de dados
├── pyproject.toml     # Configuração do projeto
├── README.md

## 📊 Funcionalidades

- 📈 Visualização de desempenho de ativos do IBOV
- 🔍 Filtros dinâmicos por período e/ou ativo
- 📅 Análise de séries temporais (histórico de preços)
- ⚡ Cálculo de métricas financeiras (variação, retorno, etc.)
- 📉 Gráficos interativos para análise exploratória
- 🧩 Interface organizada com separação entre dados, lógica e UI

```

## ▶️ Como Executar

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/stocks-dashboard.git
cd stocks-dashboard
```

### 2. Configurar o ambiente

#### 🔹 Usando uv (recomendado)

```bash
uv sync
```

Isso irá:
- Criar o ambiente automaticamente
- Instalar todas as dependências

---

#### 🔹 Usando ambiente virtual + pip

```bash
python -m venv .venv
```

Ativar o ambiente:

**Windows**
```bash
.venv\Scripts\activate
```

**Linux / Mac**
```bash
source .venv/bin/activate
```

Instalar dependências:
```bash
pip install -r requirements.txt
```

---

### 3. Executar a aplicação

```bash
streamlit run app.py
```

---

## 📌 Exemplo de Uso

- Carregue os dados do IBOV
- Aplique filtros de período
- Visualize gráficos de desempenho
- Analise métricas financeiras

## 🧪 Possíveis Melhorias

- Tempo de carregamento
- Previsão de séries temporais (ML)
- Deploy em nuvem (Streamlit Cloud)
- Comparação entre múltiplos ativos
- Alertas inteligentes de mercado

## Desenvolvido por:

- 📎 LinkedIn: [robertdemelo](https://www.linkedin.com/in/robertdemelo)
- 📎 GitHub: [Robert-FM](https://github.com/Robert-FM}{github.com/Robert-FM)