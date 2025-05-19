import os
from typing import NamedTuple  

if (os.name == "nt"):
    _ = os.system("cls")

class DevelopixGroup(NamedTuple):  
    username: str  
    members: list = []  

python_gp = DevelopixGroup("IRPythonGP")  
js_gp = DevelopixGroup("IRJavascriptGP")  

js_gp.members.append("ErfanXD")  
python_gp.members.append("General_alpha")
