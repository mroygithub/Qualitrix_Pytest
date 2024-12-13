import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))


from PytonBasicPro.test_pro3 import addNumbers,subtractNumbers

addNumbers(5,9)
subtractNumbers(5,9) 