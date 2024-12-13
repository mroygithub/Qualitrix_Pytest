import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
import pytest


def dockerLogo(): return "//li[@class='logo']"