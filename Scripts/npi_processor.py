import sys
from pathlib import Path
import pandas as pd
from datetime import date

base_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(base_dir))

from utils.common_functions import save_to_formats, logger

def load_npi_file(path: Path, nrows: int = 1000000) -> pd.DataFrame:
    """ Load npi dataset from CSV file"""
    logger.info(f'Loading npi file: {path}')
    df = pd.read_csv(path, nrows=nrows, low_memory=False)
    logger.info(f'Successfully loaded npi file')
    return df

def process_npi(df: pd.DataFrame) -> pd.DataFrame:
    """ Transform npi dataset into standardized format"""
    logger.info(f'Processing npi DataFrame')
    npi_small = df[['NPI', 'Provider Last Name (Legal Name)']].rename(columns={
        'NPI': 'code',
        'Provider Last Name (Legal Name)': 'description'
    })
    npi_small['description'] = npi_small['description'].fillna('N/A')
    npi_small['last_updated'] = date.today().strftime('%m/%d/%Y')
    logger.info(f'Processed {len(npi_small)} records')
    return npi_small

input_file = base_dir / 'input' / 'npi' / 'npidata_pfile_20050523-20250907.csv'
logger.info('Starting npi processing script')
npi_df = load_npi_file(input_file)
npi_small = process_npi(npi_df)
save_to_formats(npi_small, 'npi_small')
logger.info(f'Finished npi processing script')
logger.info(f'Output saved to output/csv/npi_small.csv')