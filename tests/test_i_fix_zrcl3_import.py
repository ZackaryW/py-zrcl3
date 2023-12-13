
import os
from zrcl3._internal.fix_zrcl3_import import fix_zrcl_import_ast

def test_fix_zrcl_import_ast():
    with open("__test__.py", "w") as f:
        f.write("import zrcl3\n")
        f.write("from zrcl3 import (generate_init_2,\n")
        f.write("create_click_file,\n")
        f.write("\tTimelyCachedProperty)\n")
        
    fix_zrcl_import_ast("__test__.py")
    
    with open("__test__.py", "r") as f:
        l = f.readlines()
        assert l[0] == "import zrcl3\n"
        assert l[1] == "from zrcl3.init_generator import generate_init as generate_init_2\n"
        assert l[2] == "from zrcl3.auto_click import create_click_file\n"
        assert l[3] == "from zrcl3.expirable_property import TimelyCachedProperty"
    
    os.remove("__test__.py")

        