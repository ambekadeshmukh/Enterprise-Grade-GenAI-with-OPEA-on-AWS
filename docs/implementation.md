# Implementation Details

This document provides detailed information about the implementation choices, configuration details, and best practices used in this project.

## Infrastructure-as-Code

All infrastructure is defined using CloudFormation, enabling repeatable and consistent deployments. The key infrastructure components include:

### EKS Cluster

- **Node Type**: t3.medium (2 vCPU, 4 GB RAM)
- **Auto-scaling**: 2-3 nodes
- **Kubernetes Version**: 1.27
- **Networking**: VPC with public and private subnets

### Kubernetes Resources

All application components are deployed as Kubernetes resources, managed with Kustomize for environment-specific configurations:

- **Base Resources**: Core components deployed in all environments
- **Overlays**: Environment-specific customizations

## Microservices Implementation

### Data Preparation Service

- **Image**: quay.io/opea/chatqna-dataprep:latest
- **Resources**: 500m CPU, 1Gi memory
- **Functions**:
  - Document chunking with configurable size and overlap
  - Metadata extraction for improved retrieval
  - Support for various document formats

### Embedding Service

- **Image**: quay.io/opea/chatqna-embedding:latest
- **Resources**: 1 CPU, 2Gi memory
- **Embedding Model**: Sentence-transformers/all-MiniLM-L6-v2 (default)
- **Dimension**: 384
- **Performance**: ~1000 embeddings per second on t3.medium

### Vector Database Options

#### Redis Vector DB

- **Image**: redis/redis-stack:latest
- **Resources**: 500m CPU, 1Gi memory
- **Storage**: 5Gi PVC
- **Index Type**: HNSW (Hierarchical Navigable Small World)
- **Distance Metric**: Cosine similarity

#### OpenSearch

- **Image**: opensearchproject/opensearch:2.9.0
- **Resources**: 1 CPU, 2Gi memory
- **Storage**: 10Gi PVC
- **Index Settings**:
  - kNN algorithm: nmslib
  - Vector dimension: 384
  - Distance metric: Cosine

### Retrieval Service

- **Image**: quay.io/opea/chatqna-retrieval:latest
- **Resources**: 500m CPU, 1Gi memory
- **Configuration**:
  - Top-k: 3-5 documents
  - Context window: 4000 tokens
  - Minimum relevance score: 0.7

### Reranking Service

- **Image**: quay.io/opea/chatqna-reranker:latest
- **Resources**: 1 CPU, 2Gi memory
- **Model**: cross-encoder/ms-marco-MiniLM-L-6-v2
- **Scoring**: 0-10 range, higher is more relevant

### LLM Service Options

#### TGI (Text Generation Interface)

- **Image**: quay.io/opea/chatqna-tgi:latest
- **Resources**: 2 CPU, 4Gi memory
- **Model**: TinyLlama/TinyLlama-1.1B-Chat-v1.0
- **Parameters**:
  - Temperature: 0.7
  - Top-p: 0.95
  - Max new tokens: 2048

#### AWS Bedrock

- **Resources**: 500m CPU, 1Gi memory
- **Model**: anthropic.claude-3-sonnet-20240229-v1:0
- **Parameters**:
  - Temperature: 0.7
  - Max tokens: 500

### Gateway Service

- **Image**: quay.io/opea/chatqna-gateway:latest
- **Resources**: 500m CPU, 1Gi memory
- **Rate Limiting**: 10 requests per minute
- **Timeout**: 60 seconds

### UI Service

- **Image**: quay.io/opea/chatqna-ui:latest
- **Resources**: 300m CPU, 512Mi memory
- **Features**:
  - Chat interface
  - Document upload
  - Response visualization

## Monitoring Stack

### Prometheus

- **Image**: prom/prometheus:v2.45.0
- **Resources**: 500m CPU, 1Gi memory
- **Scrape Interval**: 15 seconds
- **Retention**: 24 hours

### Grafana

- **Image**: grafana/grafana:10.0.3
- **Resources**: 500m CPU, 512Mi memory
- **Dashboards**:
  - OPEA Service Response Times
  - Request Rate by Service
  - Error Rates
  - Resource Utilization

## Customizations

### Guardrails

The guardrails implementation adds several safety features:

- **Content Moderation**:
  - Blocked categories: hate, harassment, self-harm, sexual, violence
  - Detection threshold: 0.7
- **Topic Guidance**:
  - Allowed topics: business, technical, product, support
  - Prohibited topics: politics, medical, legal
- **PII Detection**:
  - Detection entities: PERSON, EMAIL, PHONE_NUMBER, CREDIT_CARD, SSN
  - Action: redact

### OpenSearch Integration

The OpenSearch integration replaces Redis with a more powerful vector database:

- **Advantages**:
  - Better scalability
  - More sophisticated filtering
  - Enhanced security
  - Persistent storage
- **Configuration**:
  - Single-node deployment for demo purposes
  - Production-ready settings for resource limits
  - Configured for vector search with kNN

### AWS Bedrock Integration

The AWS Bedrock integration uses managed LLMs instead of self-hosted models:

- **Advantages**:
  - Higher quality model (Claude)
  - No model hosting overhead
  - Simplified scaling
  - Regular model updates
- **Implementation**:
  - REST API wrapper for AWS Bedrock
  - Authentication via IAM
  - Model selection based on configuration