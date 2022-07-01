import shutil
import os
from pathlib import Path

dir_ = os.path.abspath(os.curdir)

print(dir_)

p = Path(f'{dir_}/test1/tets2')
p.mkdir(parents=True, exist_ok=True)