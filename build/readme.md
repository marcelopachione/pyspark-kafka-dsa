# Cluster Spark com Deploy via Docker

## Pré-requisitos
- Docker
- Docker Compose
- Git

## Configuração do Ambiente

### 1. Clone o Repositório
```bash
git clone <url-do-repositorio>
cd <diretorio-do-repositorio>
```

### 2. Navegue até o Diretório de Build
```bash
cd build
```

### 3. Crie o Arquivo .env.spark
Crie um arquivo `.env.spark` no diretório `build` com o seguinte conteúdo:
```bash
SPARK_NO_DAEMONIZE=true
```

### 4. Construa e Inicie o Cluster Spark
```bash
docker-compose -f docker-compose.yml up -d --scale spark-worker=3
```

### 5. Verifique o Deploy
```bash
docker ps

docker logs dsa-pyspark-master
docker logs dsa-pyspark-cluster-spark-worker-1
docker logs dsa-pyspark-cluster-spark-worker-2
docker logs dsa-pyspark-cluster-spark-worker-3
```

### 6. Teste o Cluster Spark
```bash
docker exec -it dsa-pyspark-master /opt/spark/bin/spark-submit \
  --master spark://spark-master:7077 \
  --deploy-mode client \
  /opt/spark/apps/get-users-json.py
```

### 7. Pare o Cluster Spark
```bash
docker-compose down
```

## Componentes do Cluster
- **Spark Master**: Executando na porta 9091
- **Spark Workers**: 3 workers configurados
- **Spark History Server**: Executando na porta 18081

## Acesso aos Serviços
- Interface Spark Master: [http://localhost:9091](http://localhost:9091)
- Spark History Server: [http://localhost:18081](http://localhost:18081)

## Tecnologias Incluídas
- Spark 3.5.0
- Python 3
- PySpark
- Pandas

## Solução de Problemas
- Certifique-se de que todos os caminhos no `.env.spark` são absolutos e estão corretos
- Verifique as versões do Docker e Docker Compose
- Confirme se as portas de rede não estão sendo utilizadas por outros serviços

## Arquivos de Configuração
- `docker-compose.yml`: Define o cluster Spark com múltiplos containers
- `Dockerfile`: Constrói a imagem base do Spark
- `build/conf/spark-defaults.conf`: Configuração do Spark
