import logging
from pathlib import Path
import pandas as pd

log_file = Path('pipeline.log')

logging.basicConfig(
    level=logging.INFO,
    format= '%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    handlers=[
        logging.FileHandler(log_file, mode='a', encoding='utf-8'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("medical_coding_pipeline")

def save_to_formats(df: pd.DataFrame, base_filename: str) -> None:
    """Save a DataFrame to CSV with consistent formatting"""
    output_dir = Path('output') / 'csv'
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / f'{base_filename}.csv'
    df.to_csv(output_path, index=False)

