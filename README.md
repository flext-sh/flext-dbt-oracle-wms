# FLEXT dbt Oracle WMS

Projeto dbt especializado na transformacao de dados Oracle WMS para analise operacional logistica.

Descricao oficial atual: "FLEXT DBT Oracle WMS - Oracle WMS data transformation with DBT".

## O que este projeto entrega

- Modela entidades de estoque e movimentacao em marts.
- Padroniza calculos para visao operacional de armazem.
- Apoia indicadores de produtividade e capacidade.

## Contexto operacional

- Entrada: staging de dados WMS.
- Saida: camada analitica dbt do dominio logistico.
- Dependencias: fonte Oracle WMS e stack dbt.

## Estado atual e risco de adocao

- Qualidade: **Alpha**
- Uso recomendado: **Nao produtivo**
- Nivel de estabilidade: em maturacao funcional e tecnica, sujeito a mudancas de contrato sem garantia de retrocompatibilidade.

## Diretriz para uso nesta fase

Aplicar este projeto somente em desenvolvimento, prova de conceito e homologacao controlada, com expectativa de ajustes frequentes ate maturidade de release.
