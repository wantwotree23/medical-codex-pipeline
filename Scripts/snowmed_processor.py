import sys
from pathlib import Path
import pandas as pd
from datetime import date

base_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(base_dir))

from utils.common_functions import save_to_formats, logger

def load_and_parse_snowmed_file(path: Path) -> pd.DataFrame:
    """Load and parse snowmed dataset from txt file and build DataFrame"""
    logger.info(f'Loading and parsing snowmed file: {path}')
    dtype = {
        'id': 'string',
        'effectiveTime': 'string',
        'active': 'Int64',
        'moduleId': 'string',
        'conceptId': 'string',
        'languageCode': 'string',
        'typeId': 'string',
        'term': 'string',
        'caseSignificanceId': 'string'
    }
    df = pd.read_csv(path, sep= '\t', header= 0, dtype= dtype, encoding= 'utf-8', on_bad_lines= 'skip')
    logger.info(f'Successfully loaded snowmed file')
    return df

def process_snowmed(df: pd.DataFrame) -> pd.DataFrame:
    """Transform snowmed dataset into standardized format"""
    logger.info(f'Processing snowmed DataFrame')
    snowmed_small = df[['id', 'term']].rename(columns={
        'id': 'code',
        'term': 'description'
    })
    snowmed_small['last_updated']= date.today().strftime('%m/%d/%Y')
    logger.info(f'Processed {len(snowmed_small)} records')
    return snowmed_small

input_file = base_dir / 'input' / 'snowmed' / 'sct2_Description_Full-en_US1000124_20250301.txt'
logger.info('Starting snowmed processing script')
parsed_df = load_and_parse_snowmed_file(input_file)
snowmed_small = process_snowmed(parsed_df)
save_to_formats(snowmed_small, 'snowmed_small')
logger.info(f'Finished snowmed processing script')
logger.info(f'Output saved to output/csv/snowmed_small.csv')