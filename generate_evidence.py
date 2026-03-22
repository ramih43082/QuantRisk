import pandas as pd
import numpy as np
from datetime import datetime, timedelta

rng = np.random.default_rng(seed=316)

def generate_modern_portfolio_data():
    print("Generating evidence files...")


    # Clients
    n_clients = 1000
    client_ids = [f"client_{i:04d}" for i in range(n_clients)]
    countries = ['USA', 'UK', 'CAN', 'GER', 'FRA', 'AUS'] # The regular countries

    clients_df = pd.DataFrame({
        'client_id': client_ids,
        'name': [f"User_Entity_{i}" for i in range(n_clients)],
        'device_id': [f"DEV-{rng.integers(10000, 99999)}" for _ in range(n_clients)],
        'ip_address': [f"192.168.{rng.integers(1, 255)}.{rng.integers(1, 255)}" for _ in range(n_clients)],
        'onboarding_country': rng.choice(countries, n_clients)
    })

    # Inject anomaly: synthetic device and IP address
    fraud_device, fraud_ip = "DEV-99999", "192.168.1.100"
    clients_df.loc[0, 'device_id'] = fraud_device
    clients_df.loc[900:907, ['device_id', 'ip_address']] = [fraud_device, fraud_ip]


    # Transaction ledger
    n_transactions = 50000
    start_dt = datetime(2025, 1, 1)
    base_amounts = rng.lognormal(mean=4.5, sigma=1.2, size=n_transactions).round(2)

    random_offsets = rng.integers(0, 365*24*60*60, n_transactions) # Random seconds offset
    timestamps = [start_dt + timedelta(seconds=int(offset)) for offset in random_offsets]
    ledger_df = pd.DataFrame({
        'transaction_id': [f"TXN-{i:06d}" for i in range(n_transactions)],
        'client_id': rng.choice(client_ids, n_transactions),
        'amount': base_amounts,
        'timestamp': timestamps,
        'destination_country': rng.choice(countries + ['PAN', 'CYP'], n_transactions)
    })
    ledger_df['temp_weekday'] = ledger_df['timestamp'].dt.weekday
    sun_indices = ledger_df[ledger_df['temp_weekday'] == 6].index[:60]