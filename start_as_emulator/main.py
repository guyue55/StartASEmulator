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
    """
    获取模拟器列表
    """
    (status, output) = subprocess.getstatusoutput(emulator_ctl + ' -list-avds')
    names = []
    if status == 0:
        output = output.split("\n")
        for i, buff in enumerate(output):
            names.append(buff)
    else:
        print(f"fail, status={status}, {output}")
    return names


def start_emulator(emulator: str) -> bool:
    """
    启动模拟器
    """
    (status, output) = subprocess.getstatusoutput(emulator_ctl + ' -avd ' + emulator)
    return status == 0


def main():
    for i in get_list():
        print(i)
        start_emulator(i)


if __name__ == '__main__':
    main()
