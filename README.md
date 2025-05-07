# Lab Spark + Kafka
---

# Cluster Apache Spark com Docker

Este projeto fornece um ambiente completo para executar um **cluster Apache Spark** utilizando **Docker** e **Docker Compose**, facilitando a criação, gerenciamento e testes locais com Spark. Ele é ideal para desenvolvedores, analistas de dados e engenheiros que desejam experimentar o Spark em um ambiente distribuído sem a complexidade de configurar infraestrutura manualmente.

## ⚙️ Funcionalidades

- Cluster com 1 Spark Master e 3 Spark Workers
- Interface web do Spark Master acessível em `http://localhost:9091`
- Spark History Server disponível em `http://localhost:18081`
- Arquivo de exemplo para teste de submissão com PySpark
- Totalmente portátil e configurável via arquivos Docker

## 🚀 Tecnologias Utilizadas

- **Apache Spark 3.5.0**
- **Python 3**
- **PySpark**
- **Pandas**
- **Docker & Docker Compose**

## 👨‍💻 Objetivo

Este ambiente permite executar aplicações Spark de forma local, simulando um cluster real. É ideal para fins educacionais, testes de desempenho, desenvolvimento de pipelines de dados ou estudo de big data com PySpark.

## 📂 Estrutura do Projeto

- `Dockerfile`: Cria a imagem base do Spark
- `docker-compose.yml`: Orquestra os serviços (master e workers)
- `build/conf/spark-defaults.conf`: Configurações padrão do Spark
- `apps/`: Diretório para adicionar scripts Spark em Python
- `.env.spark`: Variáveis de ambiente específicas para o cluster

## 📄 Como Usar

Siga as instruções na seção [Spark_Docker](./build/readme.md) para clonar, configurar e iniciar o cluster Spark localmente usando Docker.

---