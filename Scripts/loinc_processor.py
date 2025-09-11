from pathlib import Path
import pandas as pd
from datetime import date

BASE_DIR = Path(__file__).resolve().parent.parent

INPUT_FILE = BASE_DIR / 'input' / 'loinc' / 'Loinc.csv'

OUTPUT_DIR = BASE_DIR / 'output' / 'csv'

OUTPUT_FILE = OUTPUT_DIR / 'loinc_small.csv'

loinc = pd.read_csv('input/loinc/Loinc.csv', low_memory=False)

loinc.info()

loinc.STATUS.value_counts()

loinc.iloc[0]

loinc.LOINC_NUM
loinc.LONG_COMMON_NAME

list_cols = ['LOINC_NUM', 'LONG_COMMON_NAME']

loinc_small = loinc[['LOINC_NUM', 'LONG_COMMON_NAME']]
loinc_small = loinc[list_cols]

loinc_small = loinc_small.rename(columns={'LOINC_NUM':'code', 'LONG_COMMON_NAME':'description'})

loinc_small['last_updated'] = date.today().strftime('%m/%d/%Y')

loinc_small.to_csv(OUTPUT_FILE)
