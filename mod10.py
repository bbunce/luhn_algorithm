"""
NAME:          mod10.py
AUTHOR:        Ben Bunce
EMAIL:         b.bunce@nhs.net
DATE:          14/02/2022
INSTITUTION:   Exeter Genomics
DESCRIPTION:   Script to create MOD10 valid barcodes using Luhn's algorithm.
"""

import random
import csv
from datetime import date

class Mod10():
    def __init__(self):
        pass

    def check(self, prefix, barcode):
        """Performs MOD10 Luhn checksum check"""
        # Get the numerical part of the barcode
        num = barcode[len(prefix):]
        total = 0
        for pos, i in enumerate(num):
            pos += 1
            i = int(i)
            if pos % 2 == 0:
                total += i
            else:
                if (i*2) > 9:
                    total += ((i*2) - 9)
                else:
                    total += (i*2)
        if total % 10 == 0:
            return True
        else:
            return False

    def generator(self, prefix, length, quantity):
        # open log file and store all previously used barcodes in list
        try:
            with open("log" + '.csv') as f:
                reader = csv.reader(f)
                data = list(reader)
            used_barcodes = [row[0] for row in data]
        except FileNotFoundError as e:
            used_barcodes = []

        valid_barcodes = []
        count = 0
        # Keeps generating barcodes until 9999 iterations or the user specifed quantity has been reached
        while count <= 9999 and len(valid_barcodes) < quantity:
            r = ''.join([str(random.randint(0, 9)) for i in range(length)])
            barcode = prefix + r
            # Checks barcode is valid
            if self.check(prefix, barcode) == True:
                # Checks barcode has not been generated today or previously (log)
                if barcode not in valid_barcodes and barcode not in used_barcodes:
                    print(barcode)
                    valid_barcodes.append(barcode)
            count += 1

        the_date = date.today().strftime("%d-%m-%Y")
        # Write barcodes to log and separate 'daily' record
        self.write_to_csv('log', valid_barcodes, the_date)
        self.write_to_csv(f'{prefix} barcodes (MOD10) {the_date}', valid_barcodes, the_date)
        print(f"{quantity} new MOD10 barcodes generated!")

    def write_to_csv(self, filename, barcodes, the_date):
        f = open(filename + '.csv', 'a')
        for barcode in barcodes:
            f.write(f"{barcode},{the_date}\n")
        f.close


# Specify barcode prefix
prefix = "RNA"

# Examples of MOD10 Valid barcodes
barcodes = ["RNA77040723", "RNA70405204", "RNA80647563", "RNA11446739", 
"RNA19419217", "RNA83368373", "RNA32180044", "RNA45093671", "RNA30627731",
"RNA52007713"]

# Create Mod10 class instance
mod = Mod10()
"""
Generator arguments...
- Prefix: Barcode prefix [String]
- Length: Numerical part of barcode [Int]
- Quantity: Number of barcodes requried [Int]
"""
# Run barcode generator
mod.generator(prefix, 8, 1000)