import re
import sys
from pathlib import Path
import pandas as pd
from datetime import date

base_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(base_dir))

from utils.common_functions import save_to_formats, logger

def parse_icd10cm_line(line: str) -> dict | None:
    """Parse a single line of the icd10cm dataset"""
    line = line.rstrip('\n\r')
    if len(line) <15:
        return None
    
    order_num = line[0:5].strip()
    code = line[6:13].strip()
    level = line[14:15].strip()

    remaining_text = line[16:]

    parts = re.split(r'\s{4,}', remaining_text, 1)

    description = parts[0].strip() if len(parts) > 0 else ""
    description_detailed = parts[1].strip() if len(parts) > 1 else ""

    if not code:
        return None
    
    return {
        'order_num': order_num,
        'code': code,
        'level': level,
        'description': description,
        'description_detailed': description_detailed
        }

def load_and_parse_icd10cm_file(path: Path) -> pd.DataFrame:
    """ Load icd10cm dataset from txt file and build DataFrame"""
    logger.info(f'Loading icd10cm file: {path}')
    rows: list[dict] = []
    with open(path, 'r', encoding='utf-8') as file:
        for raw in file:
            parsed = parse_icd10cm_line(raw)
            if parsed is not None:
                rows.append(parsed)
    logger.info(f'Successfully loaded icd10cm file')
    return pd.DataFrame(rows)

def process_icd10cm(df: pd.DataFrame) -> pd.DataFrame:
    """ Transform icd10cm dataset into standardized format"""
    logger.info(f'Processing icd10cm DataFrame')
    icd10cm_small = df[['order_num', 'code', 'level', 'description', 'description_detailed']].copy()
    icd10cm_small['last_updated'] = date.today().strftime('%m/%d/%Y')
    logger.info(f'Processed {len(icd10cm_small)} records')
    return icd10cm_small

input_file = base_dir / 'input' / 'icd10cm' / 'icd10cm_order_2025.txt'
logger.info('Starting icd10cm processing script')
parsed_df = load_and_parse_icd10cm_file(input_file)
icd10cm_small = process_icd10cm(parsed_df)
save_to_formats(icd10cm_small, 'icd10cm_small')
logger.info(f'Finished icd10cm processing script')
logger.info(f'Output saved to output/csv/icd10cm_small.csv')