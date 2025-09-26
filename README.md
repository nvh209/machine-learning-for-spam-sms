# Machine Learning for Real-Time SMS Spam Detection in Cellular Networks

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)](https://scikit-learn.org/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)

## Overview

This project evaluates the effectiveness of multiple machine learning models for **real-time spam detection in cellular networks**. Using a comprehensive SMS dataset, we train, evaluate, and simulate four different ML models in a realistic cellular network environment to determine the most effective approach for real-time spam filtering. View the academic report [here](report.pdf).

### Key Features

- **4 Machine Learning Models**: Logistic Regression, Naive Bayes, Random Forest, and Support Vector Machine
- **Real-time Simulation**: Simulated cellular network environment with baseband units and radio units
- **Comprehensive Evaluation**: Performance metrics including accuracy, precision, recall, and F1-score
- **Automated Spam Detection**: Real-time alerting system for high spam volume detection
- **Dataset Generation**: Custom spam dataset generator for testing on unseen data

### Research Focus

The project addresses the critical need for effective spam detection in cellular networks by:

- Comparing multiple ML algorithms in a realistic network simulation
- Evaluating real-time performance under cellular network constraints
- Analyzing model effectiveness for different spam patterns and volumes
- Providing insights into the most suitable algorithms for mobile network deployment

## Model Performance Summary

| Model | Training Accuracy | Simulation Accuracy | Simulation Time | Best Use Case |
|-------|------------------|-------------------|----------------|---------------|
| **Logistic Regression** | 99% | 88% | 8m 47s | High precision spam detection |
| **Naive Bayes** | 89% | 81% | 9m 39s | Fast processing, good recall |
| **Random Forest** | 89% | 85% | 20m 55s | Balanced performance |
| **Support Vector Machine** | 89% | 82% | 25m 53s | Complex pattern recognition |

## Project Structure

```text
machine-learning-for-spam-sms/
├── 📁 models/                          # ML Model Development
│   ├── models.ipynb                    # Model training & evaluation
│   ├── spam_data.csv                   # Training dataset
│   └── *.pkl                          # Trained model files
├── 📁 simulation/                      # Network Simulation
│   ├── simulation.ipynb                # Main simulation notebook
│   ├── 📁 data/                       # Generated test datasets
│   ├── 📁 logs/                       # Simulation logs by model
│   └── 📁 results/                    # Performance results & figures
├── 📁 spam-generator/                  # Dataset Generation
│   ├── generator.py                    # Spam dataset generator
│   └── conversations.py               # Conversation templates
├── 📁 markdown/                        # Documentation
│   ├── models.md                       # Model implementation details
│   ├── simulation.md                   # Simulation methodology
│   └── install_instructions.md         # Setup instructions
└── requirements.txt                    # Python dependencies
```

### Key Components

- **Machine Learning Models**: Four different algorithms trained on SMS spam data
- **Cellular Network Simulation**: Realistic network topology with baseband and radio units  
- **Real-time Processing**: Stream processing of SMS messages with spam detection
- **Performance Monitoring**: Comprehensive logging and alerting system
- **Dataset Generation**: Custom spam generator for testing model robustness

## Quick Start

### Prerequisites

- Python 3.8 or higher
- Virtual environment (recommended)

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/breezy-codes/machine-learning-for-spam-sms.git
   cd machine-learning-for-spam-sms
   ```

2. **Set up virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .\.venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

For detailed setup instructions, see: [Setting Up a Python Virtual Environment](./markdown/install_instructions.md)

## 🤖 Running the Machine Learning Models

Train and evaluate all four ML models using the comprehensive Jupyter notebook:

```bash
jupyter notebook models/models.ipynb
```

### What the Models Do

- **Data Preprocessing**: Text cleaning, tokenization, and vectorization
- **Model Training**: Hyperparameter tuning with cross-validation
- **Performance Evaluation**: Accuracy, precision, recall, F1-score metrics
- **Model Persistence**: Saves trained models as `.pkl` files

**Detailed guide**: [Model Implementation Notes](./markdown/models.md)

## Running the Cellular Network Simulation

Experience real-time spam detection in a simulated cellular environment:

```bash
jupyter notebook simulation/simulation.ipynb
```

### Simulation Features

- **Network Topology**: Multiple baseband units with radio units
- **Real-time Processing**: Stream-based message processing
- **Spam Detection**: Live classification with alerting system
- **Performance Analytics**: Comprehensive logging and metrics collection
- **Load Testing**: Handles high-volume message streams

**Detailed guide**: [Simulation Methodology](./markdown/simulation.md)

## Results & Analysis

### Model Performance Comparison

The simulation reveals interesting trade-offs between different algorithms:

- **Logistic Regression**: Highest precision (99% spam detection) but lower recall
- **Random Forest**: Best balanced performance with 85% accuracy
- **Naive Bayes**: Fastest processing with good spam recall (90%)
- **SVM**: Robust to outliers but computationally intensive

### Real-time Performance Insights

- **Processing Speed**: Naive Bayes processes messages fastest
- **Memory Usage**: Logistic Regression has smallest memory footprint  
- **Accuracy vs Speed**: Random Forest offers best accuracy/speed balance
- **Alert Response**: All models successfully trigger spam volume alerts

## 🛠️ Technical Architecture

### Machine Learning Pipeline

1. **Data Preprocessing**: Text normalization, stop word removal, stemming
2. **Feature Extraction**: TF-IDF vectorization with n-grams
3. **Model Training**: Cross-validation with hyperparameter optimization
4. **Evaluation**: Multi-metric assessment on held-out test data

### Cellular Network Simulation

```text
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│   Radio Unit    │───▶│  Baseband Unit   │───▶│  Core Network   │
│  (Message RX)   │     │  (ML Processing) │     │ (Spam Alerts)   │
└─────────────────┘     └──────────────────┘     └─────────────────┘
```

- **Radio Units**: Simulate message reception from mobile devices
- **Baseband Units**: Apply ML models for real-time spam classification
- **Core Network**: Aggregate results and trigger spam volume alerts
- **Logging System**: Captures all decisions and performance metrics

## Customization & Extension

### Adding New Models

1. Train your model in `models/models.ipynb`
2. Save as `.pkl` file in the `models/` directory
3. Add simulation code in `simulation/simulation.ipynb`
4. Update logging and results directories

### Modifying Network Topology

- Adjust baseband unit count in simulation parameters
- Configure radio unit connections per baseband
- Customize message processing rates and volumes

### Custom Dataset Generation

Use the spam generator to create targeted test scenarios:

```python
from spam_generator.generator import generate_spam_dataset
dataset = generate_spam_dataset(volume=1000, spam_ratio=0.3)
```

## Dependencies

Key libraries used in this project:

- **scikit-learn**: Machine learning algorithms and evaluation
- **pandas**: Data manipulation and analysis  
- **numpy**: Numerical computing
- **matplotlib/seaborn**: Data visualization
- **nltk**: Natural language processing
- **simpy**: Discrete event simulation
- **jupyter**: Interactive development environment

## Contributing

Contributions are welcome! Areas for improvement:

- Additional ML algorithms (Deep Learning, XGBoost)
- Enhanced network simulation (5G features, edge computing)
- Real-world dataset integration
- Performance optimization
- Mobile deployment strategies

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## References

- SMS Spam Collection Dataset
- Cellular Network Architecture Standards
- Machine Learning for Telecommunications
- Real-time Stream Processing Techniques

---

Built with ❤️ for telecommunications and machine learning research
