# Escopo e Planejamento: Análise de Dados JM

## O Problema de Negócio
A operação atende diversos clientes B2B (restaurantes, mercadinhos, cantinas) espalhados por diferentes regiões. Os dados atuais estão em planilhas, dificultando a análise de recorrência e a previsibilidade do fluxo de caixa. O objetivo é estruturar esses dados para entender padrões de compra e otimizar a operação.

## Decisões de Modelagem (Log de Decisões)

**Data:** 25/03/2026
**Tópico:** Granularidade da Frequência de Pedidos

* **O Desafio:** Como registrar a frequência de clientes "esporádicos" na coluna de "Entregas p/ Semana" sem usar estimativas irreais que distorçam os dados?
* **A Decisão:** Alterar a base de tempo da análise de **Semanal** para **Mensal**. 
* **O Motivo:** O ciclo mensal reflete melhor o faturamento do negócio. 
    * Clientes semanais = 4 entregas/mês.
    * Clientes quinzenais = 2 entregas/mês.
    * Clientes esporádicos = 1 ou 0,5 entregas/mês.
* **Impacto:** Isso mantém a projeção financeira realista e limpa a base para futura importação no Python e Power BI. Clientes inativos (0 entregas/mês) serão rastreados pela coluna "Data da Última Compra".

## Lista de Tarefas (Roadmap)
- [x] Estruturar base de dados no Google Sheets (Esqueleto pronto).
- [x] Criar repositório Git + Obsidian Vault.
- [ ] Preencher categorias vazias (Contato, Segmento) na planilha.
- [ ] Desenvolver script Python para anonimizar os dados sensíveis (LGPD/Privacidade).
- [ ] Criar dados fictícios financeiros para testar painéis preliminares.
- [ ] Iniciar Análise Exploratória (EDA) em um Jupyter Notebook.