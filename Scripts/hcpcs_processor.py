import sys
from pathlib import Path
import pandas as pd
from datetime import date

base_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(base_dir))

from utils.common_functions import save_to_formats, logger

def load_hcpcs_file(path: Path)-> pd.DataFrame:
    """ Load hcpcs dataset from xlsx file"""
    logger.info(f'Loading hcpcs file: {path}')
    df = pd.read_excel(path)
    logger.info(f'Successfully loaded hcpcs file')
    return df

def process_hcpcs(df: pd.DataFrame) -> pd.DataFrame:
    """ Transform hcpcs dataset into standardized format"""
    logger.info(f'Processing hcpcs DataFrame')
    hcpcs_small = df[['HCPC', 'LONG DESCRIPTION']].rename(columns={
        'HCPC': 'code',
        'LONG DESCRIPTION': 'description'
    })
    hcpcs_small['last_updated'] = date.today().strftime('%m/%d/%Y')
    logger.info(f'Processed {len(hcpcs_small)} records')
    return hcpcs_small

input_file = base_dir / 'input' / 'hcpcs' / 'HCPC2025_OCT_ANWEB_v3.xlsx'
logger.info('Starting hcpcs processing script')
hcpcs_df = load_hcpcs_file(input_file)
hcpcs_small = process_hcpcs(hcpcs_df)
save_to_formats(hcpcs_small, 'hcpcs_small')
logger.info(f'Finished hcpcs processing script')
logger.info(f'Output saved to output/csv/hcpcs_small.csv')