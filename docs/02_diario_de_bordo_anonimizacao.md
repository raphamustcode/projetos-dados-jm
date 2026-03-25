# Diário de Bordo: Script de Anonimização e Mock de Dados

**Data:** 23/03/2026
**Objetivo:** Proteger os dados sensíveis dos clientes e gerar massa de dados financeiros para testes preliminares.

## Tecnologias e Bibliotecas Aplicadas
- **Pandas:** Leitura flexível do CSV (`sep=None`), manipulação de colunas e máscaras booleanas (`.isna()`).
- **Faker:** Geração de nomes de empresas e telefones fictícios para proteção de privacidade.
- **Random & Datetime:** Criação de tickets médios aleatórios e datas de compras retroativas (últimos 60 dias).

## Soluções Técnicas e Tipagem
Durante a construção do script, enfrentei desafios com a tipagem implícita do Pandas:
1. **Formatação de Moeda:** Para contornar o erro de tipo ao injetar decimais gerados pelo Python em uma coluna lida como texto, utilizei f-strings para converter o float em string e aplicar o padrão brasileiro de vírgula: `f"{valor:.2f}".replace('.', ',')`.
2. **Tipagem de Colunas Vazias:** Colunas compostas apenas por `NaN` (nulos) são interpretadas pelo Pandas como `float64`. Para injetar datas no formato string, foi necessário converter a coluna previamente com `.astype('object')`.

## Status
O arquivo `clientes_anonimizados.csv` foi gerado com sucesso, sem sobrescrever os dados de entregas reais que já haviam sido preenchidos manualmente. O ambiente está pronto para a etapa de EDA (Exploratory Data Analysis).