import sys
from pathlib import Path
import pandas as pd
from datetime import date

base_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(base_dir))

from utils.common_functions import save_to_formats, logger

def load_icd10who_file(path: Path) -> pd.DataFrame:
    """Load icd10who dataset from txt file and load DataFrame"""
    logger.info(f'Loading icd10who file: {path}')
    columns = ['level', 'type', 'usage', 'sort', 'parent', 'code', 'display_code', 
           'icd10_code', 'title_en', 'parent_title', 'detailed_title', 
           'definition', 'mortality_code', 'morbidity_code1', 'morbidity_code2',
           'morbidity_code3','morbidity_code4']
    df = pd.read_csv(path, sep= ';', header=None, names= columns)
    logger.info(f'Successfully loaded icd10who file')
    return df
    
def process_icd10who(df: pd.DataFrame) -> pd.DataFrame:
    """Transform icd10who dataset into standardized format"""
    logger.info(f'Processing icd10who DataFrame')
    icd10who_small = df[['icd10_code','title_en','detailed_title']].rename(columns={
        'icd10_code':'code',
        'title_en':'description',
        'detailed_title':'detailed_description'
    })
    icd10who_small['detailed_description'] = icd10who_small['detailed_description'].fillna('N/A')
    icd10who_small['last_updated'] = date.today().strftime('%m/%d/%Y')
    logger.info(f'Processed {len(icd10who_small)} records')
    return icd10who_small

input_file = base_dir / 'input' / 'icd10who' / 'icd102019syst_codes.txt'
logger.info('Starting icd10who processing script')
icd10who_df = load_icd10who_file(input_file)
icd10who_small = process_icd10who(icd10who_df)
save_to_formats(icd10who_small, 'icd10who_small')
logger.info(f'Finished icd10who processing script')
logger.info(f'Output saved to output/csv/icd10who_small.csv')