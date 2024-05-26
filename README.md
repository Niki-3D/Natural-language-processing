# 

A tool to analyze donation data with potential typos and similar entries.

## Description

This project helps in analyzing donation data where entries might have typos or variations in names. It clusters similar entries together and sums the donations for each cluster.

## Project Structure

project-root/
├── src/
│ ├── logic/
│ │ ├── init.py
│ │ ├── main.py
│ │ ├── preprocessor.py
│ │ ├── levenshtein.py
│ │ ├── cluster_group.py
│ ├── init.py
├── tests/
│ ├── logic/
│ │ ├── init.py
│ │ ├── test_main.py
│ │ ├── test_preprocessor.py
│ │ ├── test_levenshtein.py
│ │ ├── test_cluster_group.py
│ ├── init.py
├── data/
│ ├── input.csv
├── requirements.txt
├── README.md
└── setup.py

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/

   ```

2. Install the required packages:
   pip install -r requirements.txt

3. Install the package:
   python setup.py install

## Usage
    To run the project, execute the following command:


## Testing
    To run the tests, execute the following command:

## License
This project is licensed under the MIT License - see the LICENSE file for details.
