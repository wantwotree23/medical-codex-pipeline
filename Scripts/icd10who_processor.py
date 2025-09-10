import sys
from pathlib import Path
import pandas as pd
from datetime import date

base_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(base_dir))

from utils.common_functions import save_to_formats

def load_icd10who_file(path: Path) -> pd.DataFrame:
    """Load icd10who dataset from txt file and build DataFrame"""
    df = pd.read_csv(path, sep= ';', header=None)

def process_icd10who(df: pd.DataFrame) -> pd.DataFrame:
    """Transform icd10who dataset into standardized format"""
    code_col = 7
    desc_col = 8
    output = df[[code_col, desc_col]].copy()
    output.columns = ['code', 'description']
    output['last_updated'] = date.today().strftime('%m/%d/%Y')
    return output

input_file = base_dir / 'input' / 'icd10who' / 'icd102019syst_codes.txt'
icd10who_df = load_icd10who_file(input_file)
icd10who_small = process_icd10who(icd10who_df)
save_to_formats(icd10who_small, 'icd10who_small')