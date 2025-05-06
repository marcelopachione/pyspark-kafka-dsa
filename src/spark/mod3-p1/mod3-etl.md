# Principios Basicos de ETL
---


```ETL é a sigla para Extract, Transform and Load (Extrair, Transformar e Carregar), sendo um processo fundamental na Eng de Dados.```


**1. Extract**

    - Envolve a coleta de dados de diferentes fontes de dados, que podem ser estruturadas (como banco de dados SQL) ou nao estruturadas (como emails ou documentos).
    - Deve assegurar que os dados sejam consistentemente extraidos, ou seja, que a extracao possa ser feita de forma confiavel e em intervalos regulares se necessario.
    - Deve garantir que a extracao dos dados nao comprometa a integreidade dos dados na origem.
    - A extracao, deve causar o menor impacto possivel nos sistemas de origem, evitando sobrecarga ou desempenho reduzido.


**2. Transform**

    - Remover imprecisoes ou erros dos dados como valores nulos, duplicatas ou formatos inconsistentes.
    - Converter os dados para um formato padrao.
    - Adicionar valor aos dados combinando-os com outras fontes de dados ou calculando novas metricas
    - Resumir ou agrupar dados, como calcular totais ou medias.
    - Assegurar que os dados transformados atendam aos requisitos de negocio e as regras de governanca de dados.


**3. Load**

    - Carregar os dados transformados no sistema de destino, que pode ser um Data Warehouse, Data Lake ou qualquer outro sistema de armazenamento de dados.
    - Determinar se os carregamento sera feito atraves de atualizacoes incrementais ou carregamentos completos.
    - Assegurar que os dados carregados estejam integros e consistentes com outras fontes de dados no sistema de destino.
    - Otimizar o desempenho do processo de carregamento para minimizar os tempos de inatividade e maximizar a eficiencia.
---

    ETL tambem envolve consideracoes sobre a automacao do processo, monitoramento e logging de atividades, tratamento de erros e a manutencao do historico de dados para auditoria e conformidade.

    O processo de ETL deve ser resiliente a falhas, escalavel conforme o volume de dados cresce e adaptavel a mudancas nas fontes de dados ou no requisitos de negocios.