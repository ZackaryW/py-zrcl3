import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from zrcl3.init_generator import generate_init # noqa
from zrcl3.init_generator.other_solution import (
    generate_init as gi, geninit_combined
)

def test_generate():
    generate_init("zrcl3", safe=True)
    
def test_generate_2():
    gi("zrcl3", method=geninit_combined)