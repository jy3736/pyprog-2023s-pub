import os

# get all html files in current directory
html_files = [f for f in os.listdir('.') if f.endswith('.html')]

# iterate through each html file and execute the PowerShell commands
for f in html_files:
    dark_file = f"{os.path.splitext(f)[0]}-dark.html"
    dark_soundon_file = f"{os.path.splitext(f)[0]}-dark-soundon.html"

    # execute the PowerShell commands
    os.system(f"python ..\\..\\dark-mode.py .\\{f}")
    os.system(f"python ..\\..\\fix_soundon.py .\\{dark_file}")
    os.remove(f)
    os.rename(dark_soundon_file, f)
    os.remove(dark_file)