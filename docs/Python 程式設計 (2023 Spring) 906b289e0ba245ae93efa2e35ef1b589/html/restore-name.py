import os

# read the file table from the file
file_table = {}
with open('file_table.txt', 'r', encoding='utf-8') as f:
    for line in f:
        new_name, original_name = line.strip().split(' ', 1)
        file_table[new_name] = original_name

# rename the html files back to their original names using the table
for new_name, original_name in file_table.items():
    os.rename(new_name, original_name)

# remove the file table file
os.remove('file_table.txt')
