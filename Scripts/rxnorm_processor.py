import sys
from pathlib import Path
import pandas as pd
from datetime import date

base_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(base_dir))

from utils.common_functions import save_to_formats, logger

def load_rxnorm_file(path: Path) -> pd.DataFrame:
    """Load rxnorm dataset from rrf file and load DataFrame""" 
    logger.info(f'Loading rxnorm file: {path}')
    columns = ['rxaui', 'aui', 'str', 'archive_timestamp', 'created_timestamp', 
    'updated_timestamp', 'code', 'is_brand', 'lat', 'last_released', 
    'saui', 'vsab', 'rxcui', 'sab', 'tty', 'merged_to_rxcui']
    df = pd.read_csv(path, sep='|', header=None, names= columns)
    logger.info(f'Successfully loaded rxnorm file')
    return df

def process_rxnorm(df: pd.DataFrame) -> pd.DataFrame:
    """Transform rxnorm dataset into standardized format"""
    logger.info(f'Processing rxnorm DataFrame')
    rxnorm_small = df[['updated_timestamp','aui']].rename(columns={
        'updated_timestamp': 'code',
        'aui': 'description'
    })
    rxnorm_small['last_updated'] = date.today().strftime('%m/%d/%Y')
    logger.info(f'Processed {len(rxnorm_small)} records')
    return rxnorm_small

input_file = base_dir / 'input' / 'rxnorm' / 'RXNATOMARCHIVE.RRF'
logger.info('Starting rxnorm processing script')
rxnorm_df = load_rxnorm_file(input_file)
rxnorm_small = process_rxnorm(rxnorm_df)
save_to_formats(rxnorm_small, 'rxnorm_small')
logger.info(f'Finished rxnorm processing script')
logger.info(f'Output saved to output/csv/rxnorm_small.csv')