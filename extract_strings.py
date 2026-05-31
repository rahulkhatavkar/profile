from pathlib import Path
import re

path = Path('Rahul_Khatavkar_Profile_13years.doc')
data = path.read_bytes()

# Extract long printable sequences from raw file bytes
text = ''.join(chr(b) if 32 <= b < 127 else '\n' for b in data)
lines = [line.strip() for line in re.split(r'\n+', text) if len(line.strip()) >= 15]
for line in lines[:200]:
    print(line)
