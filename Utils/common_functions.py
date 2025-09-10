from pathlib import Path
import pandas as pd

def save_to_formats(df: pd.DataFrame, base_filename: str) -> None:
    """Save a DataFrame to CSV with consistent formatting"""
    output_dir = Path('output') / 'csv'
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f'{base_filename}.csv'
    df.to_csv(output_path, index=False)

