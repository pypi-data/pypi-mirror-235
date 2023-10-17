#!/usr/bin/env python3
import asyncio
import sys
import tomli
import argparse

def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)

async def main():
    reqlist = ''
    srcpath = ''
    dstpath = ''

    if len(sys.argv) > 2:
        print('Invalid usage. Navigate to your project directory and try running `pyrequirement` or `pyrequirement <path-to-pyproject.toml>`.')
        exit(1)
    elif len(sys.argv) == 2:
        if sys.argv[1][0] == '-':
            helpflags = ['-h', '--h', '-help', '--help']
            for flag in helpflags:
                if sys.argv[1] == flag:
                    print('Navigate to your project directory and try running `pyrequirement` or use `pyrequirement <path-to-pyproject.toml>`.')
                    exit(0)
            print(f'Unrecognized option {sys.argv[1]}')
            exit(1)
        if sys.argv[1].endswith('pyproject.toml'):
            srcpath = sys.argv[1]
            dstpath = 'requirements.txt'.join(srcpath.rsplit('pyproject.toml', 1))
        else:
            print('Invalid input. Provide path to pyproject.toml file.')
            exit(1)
    elif len(sys.argv) == 1:
        srcpath = 'pyproject.toml'
        dstpath = 'requirements.txt'
    
    try:
        with open(srcpath, 'rb') as f:
            toml_dict = tomli.load(f)
            for req in toml_dict['project']['dependencies']:
                reqlist += str(req) + '\n'
    except:
        print(f'Failed to open {srcpath}')
        exit(1)
    with open(dstpath, 'w') as f:
        f.write(reqlist)


def start():
    asyncio.run(main())

if __name__ == '__main__':
    start()