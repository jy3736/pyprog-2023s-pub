import os

# get all html files in current directory
html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# create a dictionary to store the original file names and their new names
file_table = {}

# rename html files to simpler names and store the original names and new names in the table
for i, f in enumerate(html_files):
    new_name = str(i+1) + '.html'
    os.rename(f, new_name)
    file_table[new_name] = f

# write the table to a file
with open('file_table.txt', 'w', encoding='utf-8') as f:
    for new_name, original_name in file_table.items():
        f.write(f"{new_name} {original_name}\n")
