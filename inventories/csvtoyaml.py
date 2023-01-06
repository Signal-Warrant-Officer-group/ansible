import argparse
import csv
import os
import yaml
from datetime import datetime

def csv_to_yaml(csv_file, yaml_file):
    with open(csv_file, 'r', encoding='utf-8') as csv_f, open(yaml_file, 'w', encoding='utf-8') as yaml_f:
        reader = csv.DictReader(csv_f, delimiter=',')
        data = [{**row, 'account_expiration': datetime.strptime(f"{row['month']}/{row['day']}/{row['year']}", '%m/%d/%Y').date()} for row in reader]
        yaml.dump({'users': data}, yaml_f, sort_keys=False, default_flow_style=False, allow_unicode=True)
        
def main(csv_file, yaml_file):
    csv_to_yaml(csv_file, yaml_file)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('csv_file', help='the input CSV file')
    parser.add_argument('yaml_file', help='the output YAML file')
    args = parser.parse_args()
    main(args.csv_file, args.yaml_file)