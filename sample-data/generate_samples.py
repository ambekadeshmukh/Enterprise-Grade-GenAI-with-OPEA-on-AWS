#!/usr/bin/env python3
import os
import json
import random
from faker import Faker

# Initialize faker
fake = Faker()

# Create directory for data
os.makedirs("sample-data/documents", exist_ok=True)

# Categories for documents
categories = [
    "Company Policies",
    "Product Documentation",
    "Technical Specifications",
    "Customer Support",
    "Research Papers"
]

# Generate company policies documents
def generate_company_policy():
    policy_types = ["Privacy Policy", "Code of Conduct", "Remote Work Policy", 
                    "Information Security", "Employee Handbook"]
    policy_type = random.choice(policy_types)
    
    content = f"# {policy_type}\n\n"
    content += f"## Introduction\n\n{fake.paragraph(nb_sentences=5)}\n\n"
    content += f"## Purpose\n\n{fake.paragraph(nb_sentences=3)}\n\n"
    content += f"## Scope\n\n{fake.paragraph(nb_sentences=2)}\n\n"
    
    sections = random.randint(3, 6)
    for i in range(sections):
        content += f"## Section {i+1}: {fake.bs()}\n\n{fake.paragraph(nb_sentences=4)}\n\n"
        content += f"{fake.paragraph(nb_sentences=3)}\n\n"
    
    content += f"## Compliance\n\n{fake.paragraph(nb_sentences=4)}\n\n"
    content += f"## Last Updated\n\n{fake.date_this_year()} by {fake.name()}, {fake.job()}\n\n"
    
    return {
        "title": f"{policy_type}",
        "category": "Company Policies",
        "content": content
    }

# Generate product documentation
def generate_product_doc():
    product_name = fake.company_suffix() + " " + fake.color_name() + " " + fake.random_element(elements=("Pro", "Ultra", "Max", "Lite"))
    
    content = f"# {product_name} User Manual\n\n"
    content += f"## Product Overview\n\n{fake.paragraph(nb_sentences=4)}\n\n"
    content += f"## Getting Started\n\n{fake.paragraph(nb_sentences=3)}\n\n"
    
    features = random.randint(3, 7)
    content += "## Key Features\n\n"
    for i in range(features):
        content += f"### {fake.catch_phrase()}\n\n{fake.paragraph(nb_sentences=3)}\n\n"
    
    content += f"## Troubleshooting\n\n"
    problems = random.randint(2, 5)
    for i in range(problems):
        content += f"### Problem: {fake.sentence()}\n\nSolution: {fake.paragraph(nb_sentences=2)}\n\n"
    
    content += f"## Technical Support\n\nFor additional assistance contact us at {fake.email()}\n\n"
    
    return {
        "title": f"{product_name} User Manual",
        "category": "Product Documentation",
        "content": content
    }

# Generate technical specifications
def generate_tech_spec():
    product_type = random.choice(["Server", "Database", "API", "Framework", "Platform"])
    product_name = fake.company() + " " + product_type
    
    content = f"# {product_name} - Technical Specifications\n\n"
    content += f"## Overview\n\n{fake.paragraph(nb_sentences=3)}\n\n"
    
    content += "## System Requirements\n\n"
    content += "* CPU: " + random.choice(["Intel Xeon", "AMD EPYC", "ARM Graviton"]) + " " + str(random.randint(4, 64)) + " cores\n"
    content += "* RAM: " + str(random.randint(8, 512)) + "GB\n"
    content += "* Storage: " + str(random.randint(100, 2000)) + "GB SSD\n"
    content += f"* Operating System: {random.choice(['Linux', 'Windows Server', 'MacOS', 'Cross-platform'])}\n\n"
    
    content += "## Performance Metrics\n\n"
    content += "* Throughput: " + str(random.randint(1000, 10000)) + " requests/second\n"
    content += "* Latency: " + str(random.randint(1, 100)) + "ms (average)\n"
    content += "* Concurrent users: " + str(random.randint(100, 10000)) + "\n\n"
    
    content += "## API Reference\n\n"
    endpoints = random.randint(3, 8)
    for i in range(endpoints):
        method = random.choice(["GET", "POST", "PUT", "DELETE"])
        endpoint = f"/{fake.word()}/{fake.word()}"
        content += f"### {method} {endpoint}\n\n"
        content += f"Description: {fake.sentence()}\n\n"
        content += "Parameters:\n"
        params = random.randint(1, 4)
        for j in range(params):
            content += f"* {fake.word()}: {fake.sentence()}\n"
        content += f"\nResponse: {fake.paragraph(nb_sentences=1)}\n\n"
    
    return {
        "title": f"{product_name} - Technical Specifications",
        "category": "Technical Specifications",
        "content": content
    }

# Generate customer support documents
def generate_customer_support():
    issue_type = random.choice(["Installation", "Configuration", "Troubleshooting", "Upgrade", "Integration"])
    
    content = f"# {issue_type} Guide\n\n"
    content += f"## Common Issues\n\n{fake.paragraph(nb_sentences=3)}\n\n"
    
    faq_count = random.randint(5, 10)
    content += "## Frequently Asked Questions\n\n"
    for i in range(faq_count):
        content += f"### Q: {fake.sentence()}\n\nA: {fake.paragraph(nb_sentences=2)}\n\n"
    
    content += f"## Contact Support\n\nIf you need further assistance, please contact our support team at {fake.email()} or call {fake.phone_number()}\n\n"
    
    return {
        "title": f"{issue_type} Guide",
        "category": "Customer Support",
        "content": content
    }

# Generate research papers
def generate_research_paper():
    tech_topics = ["Machine Learning", "Artificial Intelligence", "Cloud Computing", 
                   "Quantum Computing", "Blockchain", "IoT", "Cybersecurity"]
    topic = random.choice(tech_topics)
    
    content = f"# Advances in {topic}: A Comprehensive Study\n\n"
    content += f"## Abstract\n\n{fake.paragraph(nb_sentences=5)}\n\n"
    content += f"## 1. Introduction\n\n{fake.paragraph(nb_sentences=4)}\n\n{fake.paragraph(nb_sentences=4)}\n\n"
    
    content += f"## 2. Background\n\n{fake.paragraph(nb_sentences=6)}\n\n"
    
    content += f"## 3. Methodology\n\n{fake.paragraph(nb_sentences=5)}\n\n"
    
    content += f"## 4. Results\n\n{fake.paragraph(nb_sentences=7)}\n\n"
    
    content += f"## 5. Discussion\n\n{fake.paragraph(nb_sentences=8)}\n\n"
    
    content += f"## 6. Conclusion\n\n{fake.paragraph(nb_sentences=4)}\n\n"
    
    content += f"## References\n\n"
    for i in range(random.randint(5, 12)):
        content += f"{i+1}. {fake.name()} et al. ({random.randint(2015, 2024)}). \"{fake.sentence()}\". Journal of {fake.company()}, {random.randint(1, 50)}({random.randint(1, 12)}), {random.randint(100, 999)}-{random.randint(1000, 1999)}.\n\n"
    
    return {
        "title": f"Advances in {topic}: A Comprehensive Study",
        "category": "Research Papers",
        "content": content
    }

# Map categories to generator functions
generators = {
    "Company Policies": generate_company_policy,
    "Product Documentation": generate_product_doc,
    "Technical Specifications": generate_tech_spec,
    "Customer Support": generate_customer_support,
    "Research Papers": generate_research_paper
}

# Generate sample documents
def generate_samples(num_docs=25):
    documents = []
    
    for i in range(num_docs):
        category = random.choice(categories)
        doc = generators[category]()
        
        # Save to file
        filename = f"sample-data/documents/doc_{i+1}_{category.lower().replace(' ', '_')}.md"
        with open(filename, "w") as f:
            f.write(doc["content"])
        
        doc["filename"] = filename
        documents.append(doc)
    
    # Save metadata
    with open("sample-data/documents/metadata.json", "w") as f:
        json.dump(documents, f, indent=2)
    
    print(f"Generated {num_docs} sample documents in sample-data/documents/")
    print("Metadata saved to sample-data/documents/metadata.json")

if __name__ == "__main__":
    generate_samples()