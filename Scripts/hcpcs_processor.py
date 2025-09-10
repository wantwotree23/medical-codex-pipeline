import sys
from pathlib import Path
import pandas as pd
from datetime import date

base_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(base_dir))

from utils.common_functions import save_to_formats

def load_hcpcs_file(path: Path)-> pd.DataFrame:
    """ Load hcpcs dataset from xlsx file"""
    df = pd.read_excel(path)
    return df

def process_hcpcs(df: pd.DataFrame) -> pd.DataFrame:
    """ Transform hcpcs dataset into standardized format"""
    hcpcs_small = df[['HCPC', 'LONG DESCRIPTION']].rename({
        'HCPC': 'code',
        'LONG DESCRIPTION': 'description'
    })
    hcpcs_small['last_updated'] = date.today().strftime('%m/%d/%Y')
    return hcpcs_small

input_file = base_dir / 'input' / 'hcpcs' / 'HCPC2025_OCT_ANWEB_v3.xlsx'
hcpcs_df = load_hcpcs_file(input_file)
hcpcs_small = process_hcpcs(hcpcs_df)
save_to_formats(hcpcs_small, 'hcpcs_small')