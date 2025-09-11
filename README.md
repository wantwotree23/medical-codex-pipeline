# HHA-507-Assignment 1: Medical codex pipeline

## Overview
This repository contains python scripts to parse/load, clean, and standardize medical codex datasets.

## Repository Structure
```bash
medical-codex-pipeline/
├── input/ # Raw codex files (txt, csv, xlsx, rff)
│ ├── npi/
│ ├── loinc/
│ ├── icd10cm/
│ ├── icd10who/
│ ├── snomed/
│ ├── hcpcs/
│ └── rxnorm/
├── output/
│ └── csv/ # Standardized processed CSV outputs
├── scripts/ # Individual processors
│ ├── npi_processor.py
│ ├── loinc_processor.py
│ ├── icd10cm_processor.py
│ ├── icd10who_processor.py
│ ├── rxnorm_processor.py
│ ├── snomed_processor.py
│ └── hcpcs_processor.py
├── utils/
│ └── common_functions.py # save_to_formats, logger
├── .gitignore
├── pipeline.log # Logs (auto-created)
├── README.md
└── requirements.txt
```

### 1. Clone this repository
```bash
git clone https://github.com/wantwotree23/medical-codex-pipeline.git
cd medical-codex-pipeline
pip install -r requirements.txt
```

### 2. Usage of the scripts
-Download the raw dataset file from each medical codex website and place it into their corresponding input files.
-All the scripts have the following patterns when runned.
    1. Loading the dataset file / Parsing (if the dataset file is not a csv or has no structure) and loading the dataset file into a DataFrame
    2. Processing to standardize the DataFrame to retrieve a code column, a description column, and a last updated column.
    3. Saving the standardized DataFrame into a csv and placing it in the output/csv file.
    4. Within each of the above steps, there are loggers in place to notify when each action was started and finished and the log will be placed in the pipeline.log file.

### Script differences
1. Loinc processor was the first completed script. It followed the example guideline code provided by Hants Williams in the following repository: https://github.com/hantswilliams/HHA-507-2025.git
2. The other processors used 1 function block for loading the dataset and a second function block to process the dataframe.
3. ICD10CM processor differs by having a 3rd function block in order to parse the datase file before loading it into a dataframe.
4. SNOWMED processor combined the parsing and loading process leading to a single function block performing parsing and loading steps.
5. There are 2 processors that needed N/A fills to replace white spaces.

### Utils
1. A "save_to_formats" function was created in order for the output style to be consistant throughout all the processors.
2. A logger block was created to allow logging of each step of the processors.

### .gitignore
Tells Git what files not to upload to the repository.

### Limitations
1. Manual input of dataset files from medical codex websites.
2. Large datasets have to be shrunk down to a certain amount of rows due to large dataset files that can't be uploaded to the repository.