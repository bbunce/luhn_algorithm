# Luhn algorithm barcode generator

### Description
Script to generate and validate barcodes that conform to MOD10 checksum as calculated by the Luhn algorithm.
Log of previous barcodes generated will be updated with each use in the log.csv.
Separate .csv will be created with barcodes generated for each day.

### Instructions
Adjust arguments in the the last line ```mod.generator(prefix, length, quantity)``` to change the barcode prefix, length (excluding prefix), number of barcodes required.
