# DevOps Engineer Technical Test

## **Overview**

This repository contains the deliverables for the DevOps Engineer Technical Test. The project is designed to demonstrate expertise in system architecture, troubleshooting, security monitoring, and automation while adhering to modern DevOps practices.

---

## **Instructions**

- **Duration:** 5 Days
- **Tools:** Any preferred editor/IDE and access to the internet for documentation (no direct plagiarism allowed).
- **Deliverables:**
  - Code repository (e.g., GitHub, GitLab).
  - Proper documentation, including diagrams and step-by-step instructions.
  - Answers to questions, where applicable.

---

## **Project Structure**

The repository is organized as follows:

```
├── 1-engineering-mindset/   # Section 1: Understanding the engineering mindset
│   ├── README.md            # Documentation for engineering mindset
│   ├── images/              # Supporting diagrams and illustrations
│   │   └── diagram.png      # Diagram explaining engineering concepts
├── 2-system-architecture/   # Section 2: System architecture design
│   ├── README.md            # Documentation for system architecture
│   ├── images/              # Diagrams and visuals for system design
│   │   └── diagram.png      # System architecture diagram
├── 3-problem-solving/       # Section 3: Problem-solving tasks
│   ├── main.py              # Average Price Calculator App
│   ├── README.md            # Documentation for problem-solving approach
├── 4-security-task/         # Section 4: Security task with ELK stack
│   ├── elk/                 # ELK stack setup and configuration
│   │   ├── configs/         # Configurations for ELK services
│   │   │   ├── elasticsearch/   # Elasticsearch configuration files
│   │   │   │   ├── elasticsearch.yml # Core Elasticsearch settings
│   │   │   │   ├── jvm.options      # JVM options for Elasticsearch
│   │   │   ├── filebeat/        # Filebeat configuration
│   │   │   │   └── filebeat.yml # Filebeat settings for log collection
│   │   │   ├── kibana/          # Kibana configuration
│   │   │   │   └── kibana.yml   # Core Kibana settings
│   │   │   ├── logstash/        # Logstash configuration
│   │   │   │   ├── logstash.conf # Logstash pipeline configuration
│   │   │   │   └── logstash.yml  # Logstash settings
│   │   ├── docker-compose.yml   # Docker Compose file for ELK stack deployment
│   ├── images/              # Supporting images for security task
│   │   ├── dashboard-1.jpg  # Kibana dashboard screenshot (example 1)
│   │   ├── dashboard-2.jpg  # Kibana dashboard screenshot (example 2)
│   │   ├── dashboard-3.jpg  # Kibana dashboard screenshot (example 3)
│   │   ├── dashboard-4.jpg  # Kibana dashboard screenshot (example 4)
│   │   └── diagram.jpg      # Architecture diagram for the ELK stack
│   ├── README.md            # Documentation for the security task
├── README.md                # Main README file for the project
```

---

## **Features**

- **System Architecture:**
  - Includes modular Docker Compose configurations and Kubernetes manifests.
  - Supports scalability and modern deployment strategies.
- **Security Monitoring:**

  - Linux OS logs are collected, parsed, and visualized in Kibana.
  - Insightful dashboards with actionable visualizations.

- **Automation:**
  - Entire setup is automated using Docker Compose.
  - Scripts and configurations to ensure reproducibility.

---

## **Evaluation Criteria**

The following aspects were emphasized in the solution:

### **Engineering Mindset**

- Logical and systematic troubleshooting methods.
- Innovative and clear design approach.

### **System Architecture**

- High-quality, scalable architecture.
- Modern deployment strategies leveraging Docker and Kubernetes.

### **Problem Solving**

- **Code Quality:** Readable, well-structured, and thoroughly commented.
- **Efficiency:** Optimal resource utilization.
- **Creativity:** Unique and innovative problem-solving approaches.

### **Documentation**

- Clear and concise README and supplementary files.
- Detailed diagrams explaining architecture and workflows.

### **Security Task**

- Logs from the Linux OS are captured, parsed, and visualized.
- Fully automated deployment using Docker Compose.
- Insightful dashboards fulfilling requirements.
- Detailed steps for setup and replication.
