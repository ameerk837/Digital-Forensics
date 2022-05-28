import os
import yara
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('path',help='path you want the rules to match')
parser.add_argument('-r',help='yara rule.')
arg1 = parser.parse_args()
test = arg1.path
filepath=arg1.r
rules=yara.compile(filepath)


def dir_iterator(basepath):
    with os.scandir(basepath) as files:
        for file in files:
            if file.is_dir():
                dir_iterator(basepath+file.name+"/")
            else:
                if rules.match(basepath+file.name):
                    print(rules.match(basepath+file.name))
                    print(basepath+file.name)


dir_iterator(test)
