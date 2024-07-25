# encoding: utf-8
"""
--------------------------------
Name:     main.py
Author:   cpy
Date:     2024/07/25
Company:  古月居
Description: 
--------------------------------
"""

# ''' Standard library '''
from typing import List, Dict, Tuple, Any
import subprocess

# ''' Third party Library '''

# ''' Custom Library '''


emulator_ctl = "~/Library/Android/sdk/emulator/emulator"


def get_list() -> List[str]:
    (status, output) = subprocess.getstatusoutput(emulator_ctl + ' -list-avds')
    names = []
    if status == 0:
        output = output.split("\n")
        for i, buff in enumerate(output):
            print(i, buff)
            names.append(buff)
    return names


if __name__ == '__main__':
    get_list()
