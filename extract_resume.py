from pathlib import Path
from pprint import pprint

path = Path('Rahul_Khatavkar_Profile_13years.doc')
print('path exists', path.exists())
print('size', path.stat().st_size if path.exists() else None)

try:
    import olefile
except Exception as e:
    print('olefile import failed', e)
    raise

ole = olefile.OleFileIO(path)
print('streams count', len(ole.listdir()))
for s in ole.listdir()[:40]:
    print('/'.join(s))

if ole.exists('WordDocument'):
    data = ole.openstream('WordDocument').read()
    print('WordDocument size', len(data))
    text = ''.join(chr(b) if 32 <= b < 127 else '\n' for b in data)
    print(text[:8000])
else:
    print('WordDocument stream missing')
