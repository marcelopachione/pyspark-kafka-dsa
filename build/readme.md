# Spark Cluster with Docker Deployment

## Prerequisites
- Docker
- Docker Compose
- Git

## Environment Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Navigate to Build Directory
```bash
cd build
```

### 3. Create .env.spark File
Create a `.env.spark` file in the build directory with the following content:
```bash
SPARK_NO_DAEMONIZE=true
```

### 4. Build and Start Spark Cluster
```bash
docker-compose -f docker-compose.yml up -d --scale spark-worker=3
```

### 5. Verify Deployment
```bash
docker ps

docker logs dsa-pyspark-master
docker logs dsa-pyspark-cluster-spark-worker-1
docker logs dsa-pyspark-cluster-spark-worker-2
docker logs dsa-pyspark-cluster-spark-worker-3

```

### 6. Test Spark Cluster
```bash
docker exec -it dsa-pyspark-master /opt/spark/bin/spark-submit \
  --master spark://spark-master:7077 \
  --deploy-mode client \
  /opt/spark/apps/get-users-json.py
```

### 7. Stop Spark Cluster
```bash
docker-compose down
```

## Cluster Components
- **Spark Master**: Runs on port 9091
- **Spark Workers**: 3 workers configured
- **Spark History Server**: Runs on port 18081

## Accessing Services
- Spark Master UI: http://localhost:9091
- Spark History Server: http://localhost:18081

## Included Technologies
- Spark 3.5.0
- Python 3
- PySpark
- Pandas

## Troubleshooting
- Ensure all paths in `.env.spark` are absolute and correct
- Check Docker and Docker Compose versions
- Verify network ports are not in use by other services

## Configuration Files
- `docker-compose.yml`: Defines the multi-container Spark cluster
- `Dockerfile`: Builds the base Spark image
- `build/conf/spark-defaults.conf`: Spark configuration
