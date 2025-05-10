# Enterprise-Grade GenAI with OPEA on AWS

[![OPEA ChatQnA](https://img.shields.io/badge/OPEA-ChatQnA-blue)](https://github.com/opea/chatqna)
[![AWS EKS](https://img.shields.io/badge/AWS-EKS-orange)](https://aws.amazon.com/eks/)
[![RAG](https://img.shields.io/badge/Architecture-RAG-green)](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-retrieval-augmented-generation.html)

A production-ready implementation of an enterprise-grade RAG (Retrieval Augmented Generation) system using the Open Platform for Enterprise AI (OPEA) ChatQnA framework, deployed on AWS EKS.


## ✨ Features

- **Complete RAG Pipeline**: End-to-end retrieval augmented generation architecture that combines knowledge bases with the power of LLMs
- **Modular Microservices**: Independently scalable and upgradable components following cloud-native principles
- **Multi-Vector Database Support**: Choose between Redis Vector DB (in-memory) or OpenSearch (distributed)
- **Flexible LLM Integration**: Support for both open-source models (via TGI) and managed services (AWS Bedrock)
- **Enterprise Guardrails**: Content moderation, PII detection, and topic guidance to ensure safe and compliant responses
- **Comprehensive Monitoring**: Built-in Prometheus metrics and Grafana dashboards
- **Kubernetes-native**: Fully orchestrated with Kubernetes and deployed on AWS EKS
- **Infrastructure as Code**: Complete CloudFormation and Kubernetes manifests for repeatable deployments

## 🏗️ Architecture

![opea-architecture](https://github.com/user-attachments/assets/dbf6fd83-cd6c-47dc-a787-dc62198873e0)


### Core Components

| Component | Purpose | Technologies |
|-----------|---------|-------------|
| **Data Preparation** | Document processing and chunking | Python NLP libraries |
| **Embedding Service** | Text-to-vector conversion | Sentence transformers |
| **Vector Database** | Semantic search index | Redis Stack or OpenSearch |
| **Retrieval Service** | Finding relevant documents | Vector similarity search |
| **Reranking Service** | Refining search results | Cross-encoders |
| **LLM Service** | Response generation | TinyLlama or Claude (Bedrock) |
| **Gateway** | Request orchestration | RESTful API |
| **UI** | User interface | React web application |

## 🚀 Getting Started

### Prerequisites

- AWS CLI installed and configured
- kubectl installed
- Python 3.8+ with pip
- Git

### Quick Deploy

1. **Clone the repository**

```bash
git clone https://github.com/ambekadeshmukh/Enterprise-Grade-GenAI-with-OPEA-on-AWS.git
cd Enterprise-Grade-GenAI-with-OPEA-on-AWS
```

2. **Deploy infrastructure**

```bash
./scripts/deploy-infrastructure.sh
```

3. **Deploy the application**

```bash
# For basic implementation
./scripts/deploy-all.sh

# For full implementation with all customizations
./scripts/deploy-complete.sh
```

4. **Upload sample data**

```bash
./scripts/upload-sample-data.sh
```

5. **Access the application**

After deployment completes, the script will output URLs for:
- ChatQnA UI
- Grafana dashboard (credentials: admin/admin)

## 🔄 Customization Options

### Enterprise Guardrails

```bash
./scripts/deploy-guardrails.sh
```

Adds content moderation, PII detection, and topic guidance to ensure appropriate use.

### OpenSearch Integration

```bash
./scripts/deploy-opensearch.sh
```

Replaces Redis Vector DB with OpenSearch for enhanced scaling and features.

### AWS Bedrock Integration

```bash
./scripts/deploy-bedrock.sh
```

Uses AWS Bedrock's Claude model instead of the default TGI service.

## 📊 Monitoring

The deployment includes a comprehensive monitoring stack:

- **Prometheus**: Collects metrics on response times, request rates, and error rates
- **Grafana**: Pre-configured dashboards for performance visualization
- **Alerting**: Sample alert configurations for production monitoring

## 📁 Project Structure

```
├── docs/                     # Documentation
├── infrastructure/           # CloudFormation templates
├── kubernetes/               # Kubernetes manifests
│   ├── base/                 # Base resources
│   └── overlays/             # Environment-specific overlays
├── monitoring/               # Prometheus and Grafana configs
├── sample-data/              # Sample data generation
└── scripts/                  # Deployment and utility scripts
```

## 🧪 Testing

Generate test data with the included sample data generator:

```bash
pip install -r sample-data/requirements.txt
python sample-data/generate_samples.py
```

## 🧹 Cleanup

To remove all deployed resources and avoid AWS charges:

```bash
./scripts/cleanup.sh
```

## 📖 Documentation

For detailed information about the architecture and implementation:

- [Architecture Overview](docs/architecture.md)
- [Implementation Details](docs/implementation.md)
- [Customization Guide](docs/customization.md)



## Acknowledgements

- [OPEA Project](https://github.com/opea)
- [AWS EKS Documentation](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html)
- [Kustomize](https://kustomize.io/)
- [Prometheus](https://prometheus.io/)
- [Grafana](https://grafana.com/)
