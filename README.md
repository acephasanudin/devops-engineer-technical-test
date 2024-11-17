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
├── 1-engineering-mindset/   # Section 1, Engineering Mindset
│   ├── README.md            # Documentation
│   ├── images/              # Diagrams and images for section 1
│   │   └── diagram.png      # Diagram for section 1
├── 2-system-architecture/   # Section 2, System Architecture
│   ├── README.md            # Documentation
│   ├── images/              # Diagrams and images for section 2
│   │   └── diagram.png      # Diagram for section 2
├── 3-problem-solving/       # Section 3, Problem Solving
│   ├── main.py              # Average Price Calculator App
│   ├── README.md            # Documentation
├── 4-security-task/         # Section 4, Security Task
│   ├── README.md            # Documentation
│   ├── docker-elk/          # Docker setup for ELK stack
│   │   ├── elasticsearch/   # Elasticsearch setup
│   │   │   ├── config/      # Configuration files
│   │   │   │   └── elasticsearch.yml
│   │   │   ├── Dockerfile   # Dockerfile for Elasticsearch
│   │   ├── extensions/      # ELK extensions
│   │   │   ├── curator/     # Curator extension for log management
│   │   │   ├── enterprise-search/ # Enterprise Search extension
│   │   │   ├── filebeat/    # Filebeat for log shipping
│   │   │   ├── fleet/       # Fleet for Elastic Agent management
│   │   │   ├── heartbeat/   # Heartbeat for monitoring
│   │   │   ├── metricbeat/  # Metricbeat for monitoring system metrics
│   │   ├── kibana/          # Kibana setup
│   │   │   ├── config/      # Kibana configuration files
│   │   │   ├── Dockerfile   # Dockerfile for Kibana
│   │   ├── logstash/        # Logstash setup
│   │   │   ├── config/      # Logstash configuration files
│   │   │   ├── pipeline/    # Logstash pipeline configuration
│   │   ├── setup/           # ELK setup configuration
│   │   │   ├── roles/       # Role-based access configuration
│   │   │   ├── entrypoint.sh # Entry point script
│   │   ├── ubuntu_logs/     # Sample Ubuntu log files for ingestion
│   │   │   ├── apt/         # APT logs
│   │   │   ├── journal/     # System journal logs
│   │   │   ├── syslog/      # Syslog files
│   │   ├── .env             # Environment variables for ELK setup
│   │   ├── .gitattributes   # Git attributes for ELK setup
│   │   ├── docker-compose.yml # Docker Compose file for ELK stack
│   └── .gitignore           # Git ignore file
└── README.md                # Main README file
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