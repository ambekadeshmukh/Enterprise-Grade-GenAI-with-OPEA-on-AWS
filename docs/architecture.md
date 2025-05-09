# Architecture Overview

## RAG Architecture

The ChatQnA application implements the Retrieval Augmented Generation (RAG) pattern, which enhances large language models by incorporating external knowledge sources. This approach addresses the limitations of LLMs, such as hallucinations and outdated knowledge, by grounding responses in factual information from curated documents.

![RAG Flow](images/rag-flow.png)

## Core Components

### 1. Data Preparation Service

- **Purpose**: Processes documents for ingestion into the knowledge base
- **Functions**:
  - Document chunking
  - Metadata extraction
  - Text normalization
  - Format conversion

### 2. Embedding Service

- **Purpose**: Converts text into vector embeddings
- **Functions**:
  - Transforms queries and documents into numerical representations
  - Creates vector embeddings that capture semantic meaning
  - Enables similarity matching for retrieval

### 3. Vector Database

- **Options**:
  - **Redis Vector DB**: In-memory vector database for fast retrieval
  - **OpenSearch**: Distributed search and analytics engine with vector capabilities
- **Functions**:
  - Stores document embeddings
  - Enables semantic search
  - Supports metadata filtering

### 4. Retrieval Service

- **Purpose**: Finds relevant information based on user queries
- **Functions**:
  - Computes similarity between query embeddings and document embeddings
  - Fetches top-k most relevant documents
  - Supports hybrid retrieval (semantic + keyword)

### 5. Reranking Service

- **Purpose**: Refines retrieval results for better relevance
- **Functions**:
  - Re-scores documents based on more sophisticated matching
  - Filters and prioritizes retrieved content
  - Improves precision of results

### 6. LLM Service

- **Options**:
  - **TGI (Text Generation Interface)**: For open-source models
  - **AWS Bedrock**: For managed LLM services
- **Functions**:
  - Generates coherent responses based on retrieved context
  - Follows system instructions for output formatting
  - Maintains conversation history

### 7. Gateway

- **Purpose**: Orchestrates the flow between components
- **Functions**:
  - Manages request routing
  - Handles rate limiting and retries
  - Provides unified API for client applications

### 8. UI Service

- **Purpose**: Web interface for end-users
- **Functions**:
  - Chat interface for interacting with the system
  - Document upload functionality
  - Response visualization

## Deployment Architecture

The application is deployed on AWS EKS (Elastic Kubernetes Service), providing a scalable and resilient infrastructure.

![Deployment Architecture](images/deployment-architecture.png)

### Key AWS Components

- **EKS Cluster**: Managed Kubernetes service
- **EC2 Instances**: Compute resources for running containers
- **Elastic Load Balancer**: Distributes traffic to the services
- **IAM Roles**: Controls access to AWS resources
- **VPC**: Networking isolation and security

### Monitoring Stack

- **Prometheus**: Metrics collection and storage
- **Grafana**: Visualization and dashboards

## Security and Guardrails

The implementation includes several security features:

- **Content Moderation**: Filters inappropriate queries and responses
- **PII Detection**: Identifies and redacts personal information
- **Topic Guidance**: Ensures conversations stay within approved domains
- **Input Validation**: Prevents injection attacks and malformed requests

## Customization Points

The architecture is designed to be modular and customizable:

- **Vector Database**: Can switch between Redis and OpenSearch
- **LLM Provider**: Can use open-source models or AWS Bedrock
- **Embedding Models**: Can be replaced with different embedding services
- **Guardrails Configuration**: Can be adjusted for different use cases