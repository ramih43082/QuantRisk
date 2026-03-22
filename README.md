# QuantRisk

![Status: Work in Progress](https://img.shields.io/badge/Status-Work%20in%20Progress-yellow)
![Stage: Development](https://img.shields.io/badge/Stage-Development-orange)

**A comprehensive forensic data analysis framework for financial fraud detection and risk assessment.**

QuantRisk is currently under development and serves as both a synthetic financial data generator AND a forensic analysis toolkit. This project creates realistic financial transaction data with embedded fraud patterns and provides the analytical tools to discover them.

## 🚨 Current Status

This repository represents **work in progress**. The current implementation includes:

### ✅ **Current Capabilities**
- **Data Generation**: Synthetic client and transaction data with embedded fraud patterns
- **Basic Analysis**: Data integrity assessment and cleaning procedures
- **Pattern Detection**: Temporal analysis and statistical distribution analysis
- **Visualization**: Heatmaps and distribution plots for fraud pattern identification

### 🔄 **Planned Features**
- Advanced machine learning fraud detection models
- Real-time monitoring dashboard
- Automated alerting system
- Extended fraud pattern library
- Performance optimization for large datasets

## Overview

QuantRisk creates realistic financial transaction data with deliberately injected anomalies and fraud patterns, then provides the analytical framework to detect them. This synthetic dataset is designed for testing fraud detection systems, risk analysis models, and data cleaning algorithms.

## Features

### Data Generation
- **Client Data Generation**: Creates synthetic client profiles with device IDs, IP addresses, and onboarding countries
- **Transaction Ledger**: Generates realistic transaction data with timestamps, amounts, and destination countries
- **Embedded Fraud Patterns**: Includes several types of anomalies for testing:
  - Shared device/IP address patterns
  - Sunday 3 AM high-value transactions
  - "The Pulse" - regular suspicious activity pattern
  - Data quality issues (negative amounts, missing timestamps)

### Analysis Capabilities
- **Data Integrity Assessment**: Automated detection of missing timestamps, duplicates, and negative amounts
- **Statistical Distribution Analysis**: Log-normal distribution analysis with 99th percentile threshold identification
- **Temporal Pattern Detection**: Time-based anomaly detection including suspicious timing patterns
- **Visualization Tools**: Heatmaps, distribution plots, and forensic investigation visualizations
- **Forensic Methodology**: Structured approach to fraud investigation and evidence generation

## Installation

### Requirements

- Python 3.7+
- pandas
- numpy
- matplotlib
- seaborn
- jupyter (for notebook analysis)

### Setup

1. Clone the repository
2. Install dependencies:
```bash
pip install pandas numpy matplotlib seaborn jupyter
```

3. Launch Jupyter for analysis:
```bash
jupyter notebook exploration.ipynb
```

## Usage

### 1. Generate Synthetic Data

Run the data generation script:

```bash
python generate_evidence.py
```

This will generate two CSV files:
- `clients.csv` - Client information (1,000 records)
- `ledger.csv` - Transaction ledger (50,000+ records)

### 2. Forensic Analysis Workflow

Open `exploration.ipynb` and follow the structured analysis:

1. **Data Loading & Inspection**: Load and examine the generated datasets
2. **Data Integrity Assessment**: Identify and handle data quality issues
3. **Statistical Analysis**: Analyze transaction distributions and identify outliers
4. **Temporal Pattern Detection**: Discover time-based anomalies
5. **Fraud Pattern Investigation**: Deep dive into suspicious activities

## Generated Data Structure

### Clients Dataset
- `client_id`: Unique client identifier
- `name`: Client entity name
- `device_id`: Device identifier
- `ip_address`: IP address
- `onboarding_country`: Country of client registration

### Transaction Ledger
- `transaction_id`: Unique transaction identifier
- `client_id`: Associated client identifier
- `amount`: Transaction amount
- `timestamp`: Transaction timestamp
- `destination_country`: Transaction destination country

## Fraud Patterns

### 1. Shared Device/IP Pattern
- Multiple clients share the same device ID (`DEV-99999`) and IP address (`192.168.1.100`)
- Indicates potential account takeover or synthetic identity fraud

### 2. Sunday 3 AM Transactions
- 60 transactions occurring exactly at 3:00 AM on Sundays
- All with the same amount ($4,995.00)
- Suggests automated fraudulent activity

### 3. "The Pulse" (Client C-0999)
- Regular monthly pattern of suspicious activity
- Inflow of $10,000 followed by outflow of $9,950 within 45 minutes
- Funds routed through Panama
- Indicates potential money laundering or structured payments

### 4. Data Quality Issues
- Negative transaction amounts
- Missing timestamps
- Tests data cleaning and validation systems

## Analysis Methodology

The forensic analysis follows a structured approach:

### Phase 1: Data Integrity Assessment
- Establish data quality and handle anomalies
- Remove records with missing timestamps and negative amounts
- Verify data consistency and completeness

### Phase 2: Statistical Distribution Analysis
- Understand normal transaction patterns
- Identify extreme outliers using 99th percentile thresholds
- Analyze log-normal distribution characteristics

### Phase 3: Temporal Pattern Detection
- Identify time-based anomalies
- Detect suspicious timing patterns (e.g., Sunday 3 AM spikes)
- Analyze transaction volume across days and hours

### Phase 4: Fraud Pattern Investigation
- Deep dive into suspicious activities
- Correlate multiple fraud indicators
- Generate evidence for investigation

## Key Findings from Current Analysis

Based on the exploration.ipynb analysis:

- **Median Transaction**: $90.27 (typical small transaction)
- **99th Percentile Threshold**: $1,589.55 (extreme transaction threshold)
- **Extreme Transactions**: 501 transactions exceed the 99th percentile
- **Anomalous Pattern**: Significant transaction spike at Sunday 3 AM UTC
- **Data Quality**: 5 transactions with missing timestamps, 10 with negative amounts

## Use Cases

- **Fraud Detection Testing**: Validate fraud detection algorithms with known patterns
- **Risk Analysis**: Test risk scoring models on realistic data
- **Data Pipeline Testing**: Verify data cleaning and validation processes
- **Model Training**: Generate training data for machine learning models
- **Compliance Testing**: Test AML/KYC detection systems
- **Forensic Training**: Educational tool for fraud investigation techniques

## Technical Details

- **Random Seed**: Fixed seed (316) for reproducible results
- **Date Range**: Transactions from January 1, 2025 onwards
- **Countries**: USA, UK, CAN, GER, FRA, AUS, PAN, CYP
- **Transaction Distribution**: Log-normal amount distribution
- **Analysis Libraries**: pandas, numpy, matplotlib, seaborn

## Development Roadmap

### Next Steps
- [ ] Implement automated fraud detection algorithms
- [ ] Add real-time monitoring capabilities
- [ ] Create interactive dashboard
- [ ] Extend fraud pattern library
- [ ] Add performance benchmarks
- [ ] Create comprehensive documentation
- [ ] Implement unit tests
- [ ] Add CI/CD pipeline

### Future Enhancements
- [ ] Machine learning model integration
- [ ] Advanced visualization techniques
- [ ] Multi-currency support
- [ ] API endpoints for external integration
- [ ] Cloud deployment options

## Contributing

**Note**: This is a work in progress. Contributions are welcome but please understand that the codebase is still evolving.

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests if applicable
5. Submit a pull request with a clear description of your changes

## License

This project is open source and available under the MIT License.

---

**Disclaimer**: This project generates synthetic financial data for educational and testing purposes only. The fraud patterns and methodologies described are for legitimate fraud detection training and research.
