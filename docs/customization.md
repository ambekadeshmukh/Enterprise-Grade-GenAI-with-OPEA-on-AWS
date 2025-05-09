# Customization Guide

This guide explains how to customize and extend the OPEA ChatQnA implementation for different use cases and requirements.

## Customizing the Vector Database

### Switching to OpenSearch

The implementation supports replacing Redis Vector DB with OpenSearch:

```bash
./scripts/deploy-opensearch.sh
```

This script applies the OpenSearch overlay, which:

Deploys OpenSearch as a stateful service
Reconfigures the Retrieval Service to use OpenSearch
Removes the Redis Vector DB deployment

Using Other Vector Databases
To integrate a different vector database (e.g., Pinecone, Weaviate, Milvus):

Create a deployment YAML for the new database
Create a service YAML for the new database
Modify the Retrieval Service to connect to the new database
Apply the changes using Kustomize

Example for Pinecone (conceptual):
yaml# kubernetes/overlays/pinecone/retrieval-patch.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: retrieval
  namespace: opea-chatqna
spec:
  template:
    spec:
      containers:
      - name: retrieval
        env:
        - name: VECTOR_DB_TYPE
          value: "pinecone"
        - name: PINECONE_API_KEY
          valueFrom:
            secretKeyRef:
              name: pinecone-credentials
              key: api-key
        - name: PINECONE_ENVIRONMENT
          value: "us-west1-gcp"
        - name: PINECONE_INDEX_NAME
          value: "opea-chatqna"
Customizing the LLM Service
Using AWS Bedrock
To switch to AWS Bedrock:
bash./scripts/deploy-bedrock.sh
This script applies the Bedrock overlay, which:

Deploys a Bedrock adapter service
Configures IAM for Bedrock access
Reconfigures the Gateway to use Bedrock
Removes the TGI LLM deployment

Using Other LLM Providers
To integrate a different LLM provider (e.g., OpenAI, Cohere, HuggingFace):

Create a deployment YAML for the new LLM adapter
Configure the adapter to connect to the provider's API
Modify the Gateway to use the new LLM service
Apply the changes using Kustomize

Example for OpenAI (conceptual):
yaml# kubernetes/overlays/openai/llm-openai.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: llm-openai
  namespace: opea-chatqna
spec:
  replicas: 1
  selector:
    matchLabels:
      app: llm-openai
  template:
    metadata:
      labels:
        app: llm-openai
    spec:
      containers:
      - name: llm-openai
        image: custom/openai-adapter:latest
        ports:
        - containerPort: 8080
        env:
        - name: OPENAI_API_KEY
          valueFrom:
            secretKeyRef:
              name: openai-credentials
              key: api-key
        - name: OPENAI_MODEL
          value: "gpt-4"
Customizing Guardrails
The guardrails implementation can be customized by modifying the configuration:
yaml# kubernetes/overlays/guardrails/guardrails-configmap.yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: guardrails-config
  namespace: opea-chatqna
data:
  guardrails.json: |-
    {
      "prompt_moderation": {
        "enabled": true,
        "blocked_categories": ["hate", "harassment", "self-harm", "sexual", "violence"],
        "threshold": 0.7
      },
      "output_moderation": {
        "enabled": true,
        "blocked_categories": ["hate", "harassment", "self-harm", "sexual", "violence"],
        "threshold": 0.7
      },
      "topic_guidance": {
        "enabled": true,
        "allowed_topics": ["business", "technical", "product", "support"],
        "prohibited_topics": ["politics", "medical", "legal"]
      },
      "pii_detection": {
        "enabled": true,
        "detection_entities": ["PERSON", "EMAIL", "PHONE_NUMBER", "CREDIT_CARD", "SSN"],
        "action": "redact"
      }
    }
Adjust the configuration based on your specific requirements.
Scaling for Production
For production deployments, consider the following modifications:
Resource Scaling
Increase resources for key components:
yaml# kubernetes/overlays/prod/resource-patch.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: llm-bedrock
  namespace: opea-chatqna
spec:
  template:
    spec:
      containers:
      - name: llm-bedrock
        resources:
          limits:
            cpu: "1"
            memory: "2Gi"
          requests:
            cpu: "500m"
            memory: "1Gi"
High Availability
Increase replicas for critical services:
yaml# kubernetes/overlays/prod/ha-patch.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: gateway
  namespace: opea-chatqna
spec:
  replicas: 3
Persistent Storage
Configure robust persistent storage for stateful components:
yaml# kubernetes/overlays/prod/storage-patch.yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: opensearch-pvc
  namespace: opea-chatqna
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 100Gi
  storageClassName: gp3
Enhanced Security
Add network policies and secure service configuration:
yaml# kubernetes/overlays/prod/security/network-policy.yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny
  namespace: opea-chatqna
spec:
  podSelector: {}
  policyTypes:
  - Ingress
  - Egress
Adding Custom Data Sources
To add custom data sources for document ingestion:

Create a data source adapter deployment
Configure the adapter to connect to your data source
Set up a schedule for periodic data ingestion
Apply the changes using Kustomize

Example for an S3 data source (conceptual):
yaml# kubernetes/overlays/datasources/s3-ingestion.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: s3-ingestion
  namespace: opea-chatqna
spec:
  replicas: 1
  selector:
    matchLabels:
      app: s3-ingestion
  template:
    metadata:
      labels:
        app: s3-ingestion
    spec:
      containers:
      - name: s3-ingestion
        image: custom/s3-ingestion:latest
        env:
        - name: S3_BUCKET
          value: "my-documents-bucket"
        - name: INGESTION_SCHEDULE
          value: "0 */6 * * *"
        - name: DATA_PREP_URL
          value: "http://data-prep:6007"

Make all scripts executable:

```bash
find scripts -type f -name "*.sh" -exec chmod +x {} \;