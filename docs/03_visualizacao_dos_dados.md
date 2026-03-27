# Sprint de limpeza, manipulação e visualização interativa de dados
**Objetivo:** Melhorar a visualização da Matriz de Risco de clientes B2B (Recência vs. Ticket Médio) para facilitar a apresentação dos dados e a tomada de decisão gerencial, migrando de uma visualização estática com sobreposição de texto para um painel interativo.

**Tecnologias e Bibliotecas Utilizadas:**

- `pandas` e `numpy` para manipulação e limpeza de dados.
    
- `plotly.express` para visualização interativa de dados.
    

**Desafios Resolvidos (Data Cleaning & Wrangling):**

1. **Tipagem de Datas (Eixo X):** Conversão da coluna `'Recência'` (formato string/data) para o formato `datetime`, calculando a diferença em relação à data atual para gerar a nova coluna inteira `'Dias sem Comprar'`.
    
2. **Tratamento de Entregas Futuras:** Correção de valores negativos em `'Dias sem Comprar'` (causados por pedidos já agendados/lançados para dias futuros), limitando-os a `0` para não quebrar o eixo visual.
    
3. **Tratamento de Moeda e Outliers Falsos (Eixo Y):** Criação de uma função inteligente (`limpar_moeda`) para padronizar a coluna `'Ticket Médio Mensal'`. O script passou a identificar corretamente células que já eram números flutuantes e células que vinham como texto (ex: `"R$ 2.235,00"`), evitando o erro de multiplicação acidental de valores (ex: `1403.0` virando `14030`).
    
4. **Tipagem de Frequência:** Conversão da coluna `'Frequência Numérica'` de string com vírgula (ex: `"2,5"`) para float, permitindo seu uso como parâmetro de tamanho geométrico.
    

**Entregáveis:**

- **Gráfico de Dispersão Interativo (Plotly):** Matriz onde o Eixo X representa a inatividade (Dias sem Comprar), o Eixo Y o faturamento (Ticket Médio), e o tamanho da bolha reflete a frequência de compras.
    
- **Demarcação de Quadrantes de Ação:** Inserção de linhas de limite (Ticket > R$ 1000 e Inatividade > 15 dias) para segmentação visual clara entre clientes "Ouro", "Base de Upsell" e "Risco de Churn".
    
- **Exportação HTML:** Geração do arquivo `matriz_de_risco_clientes.html` para apresentação offline sem necessidade de rodar o ambiente Python na hora da reunião.
    
- **Rotina de Ação:** Script de exportação automática (`.to_excel`) dos clientes filtrados no quadrante de risco para acionamento imediato pela equipe.