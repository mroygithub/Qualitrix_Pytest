import sys
from pathlib import Path
#sys.path.append('/Users/mithunroy/PycharmProjects/TrainingPytest')
sys.path.append(str(Path(__file__).parent.parent))
from PytonBasicPro.test_function2 import BasicPro


class PyBasic:

    def test001():
        print("I am in Test Basic Package")

basic = PyBasic()
basic1 = BasicPro()

basic1.addTwoNum(12,13)
basic1.test001()


