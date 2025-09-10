import sys
from pathlib import Path
import pandas as pd
from datetime import date

base_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(base_dir))

from utils.common_functions import save_to_formats

def load_npi_file(path: Path, nrows: int = 1000000) -> pd.DataFrame:
    """ Load npi dataset from CSV file"""
    df = pd.read_csv(path, nrows=nrows, low_memory=False)
    return df

def process_npi(df: pd.DataFrame) -> pd.DataFrame:
    """ Transform npi dataset into standardized format"""
    npi_small = df[['NPI', 'Provider Last Name (Legal Name)']].rename({
        'NPI': 'code',
        'Provider Last Name (Legal Name)': 'description'
    })
    npi_small['Provider Last Name (Legal Name)'] = npi_small['Provider Last Name (Legal Name)'].fillna('N/A')
    npi_small['last_updated'] = date.today().strftime('%m/%d/%Y')
    return npi_small

base_dir = Path(__file__).resolve().parent.parent
input_file = base_dir / 'input' / 'npi' / 'npidata_pfile_20050523-20250907.csv'
npi_df = load_npi_file(input_file, nrows=1000000)
npi_small = process_npi(npi_df)
save_to_formats(npi_small, 'npi_small')