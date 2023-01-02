import yaml
from datetime import datetime
import os
import csv
import sys

root = os.getcwd()

# takes a csvFile name and output file name/path
def csv_to_yaml(csvFile, output):
    with open(output, 'w', encoding='utf-8') as s:
        reader = csv.reader(csvFile, delimiter=',')
        keys = next(reader)
        keys.append('account_expiration')
        for row in reader:
            account_expires = (row[3]+'/'+row[4]+'/'+row[5])
            dt = datetime.strptime(account_expires, '%m/%d/%Y').date()
            row.append(dt)
            yaml.dump([dict(zip(keys, row))], s, sort_keys=False,default_flow_style=False, allow_unicode=True)



def input_csv_file(csvFile, output=None):
    output = output if output else root+'/'+(csvFile.split(',')[-1].replace('.csv','.yml'))

    try:
        with open(csvFile, 'r', encoding='utf-8') as csvFile:
            csv_to_yaml(csvFile, output)
    except FileNotFoundError:
        msg = "No such file or directory: "+ csvFile
        print(msg)


if __name__ == '__main__':
    csvFile = sys.argv[1]
    input_csv_file(csvFile)
