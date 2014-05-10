import os
import glob

# include all py files in current folder in the __all__ var
__all__ = [ os.path.basename(f)[:-3] for f in glob.glob(os.path.dirname(__file__)+"/*.py")]