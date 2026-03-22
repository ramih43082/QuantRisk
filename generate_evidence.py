import pandas as pd
import numpy as np
from datetime import datetime, timedelta

rng = np.random.default_rng(seed=316)

def generate_messy_data():
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

    # Inject anomalies: Sunday 3 AM transactions

    ledger_df['temp_weekday'] = ledger_df['timestamp'].dt.weekday
    sun_indices = ledger_df[ledger_df['temp_weekday'] == 6].index[:60]

    for idx in sun_indices:
        ledger_df.at[idx, 'timestamp'] = ledger_df.at[idx, 'timestamp'].replace(hour=3, minute=0, second=0)
        ledger_df.at[idx, 'amount'] = 4995.00
    
    # The Pulse (C-09999)
    pulse_rows = []
    for i in range(12):
        d = start_dt + timedelta(days = 30 * i)
        pulse_rows.append({'transaction_id': f'P-IN-{i}', 'client_id': 'C-0999', 'amount': 10000.0, 'timestamp': d, 'destination_country': 'USA'})            
        pulse_rows.append({'transaction_id': f'P-OUT-{i}', 'client_id': 'C-0999', 'amount': 9950.0, 'timestamp': d + timedelta(minutes=45), 'destination_country': 'PAN'})

    ledger_df = pd.concat([ledger_df, pd.DataFrame(pulse_rows)], ignore_index=True)

    # Dirty Data 
    ledger_df.loc[rng.choice(ledger_df.index, 10), 'amount'] = -100.0 # Negatives
    ledger_df.loc[rng.choice(ledger_df.index, 5), 'timestamp'] = pd.NaT # Missing

    ledger_df = ledger_df.sample(frac=1, random_state=316).drop(columns=['temp_weekday'])


    clients_df.to_csv('clients.csv', index=False)
    ledger_df.to_csv('ledger.csv', index=False)
    print(f"Created clients.csv ({len(clients_df)} rows)")
    print(f"Created ledger.csv ({len(ledger_df)} rows)")
    print("Evidence generation complete. The mess awaits.")

if __name__ == "__main__":
    generate_messy_data()
