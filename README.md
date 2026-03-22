# QuantRisk

A Python project that generates synthetic financial data with embedded fraud patterns for testing and analysis purposes.

## Overview

QuantRisk creates realistic financial transaction data with deliberately injected anomalies and fraud patterns. This synthetic dataset is designed for testing fraud detection systems, risk analysis models, and data cleaning algorithms.

## Features

- **Client Data Generation**: Creates synthetic client profiles with device IDs, IP addresses, and onboarding countries
- **Transaction Ledger**: Generates realistic transaction data with timestamps, amounts, and destination countries
- **Embedded Fraud Patterns**: Includes several types of anomalies for testing:
  - Shared device/IP address patterns
  - Sunday 3 AM high-value transactions
  - "The Pulse" - regular suspicious activity pattern
  - Data quality issues (negative amounts, missing timestamps)

## Installation

### Requirements

- Python 3.7+
- pandas
- numpy

### Setup

1. Clone the repository
2. Install dependencies:
```bash
pip install pandas numpy
```

## Usage

Run the data generation script:

```bash
python generate_evidence.py
```

This will generate two CSV files:
- `clients.csv` - Client information (1,000 records)
- `ledger.csv` - Transaction ledger (50,000+ records)

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

## Use Cases

- **Fraud Detection Testing**: Validate fraud detection algorithms with known patterns
- **Risk Analysis**: Test risk scoring models on realistic data
- **Data Pipeline Testing**: Verify data cleaning and validation processes
- **Model Training**: Generate training data for machine learning models
- **Compliance Testing**: Test AML/KYC detection systems

## Technical Details

- **Random Seed**: Fixed seed (316) for reproducible results
- **Date Range**: Transactions from January 1, 2025 onwards
- **Countries**: USA, UK, CAN, GER, FRA, AUS, PAN, CYP
- **Transaction Distribution**: Log-normal amount distribution

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is open source and available under the MIT License.
