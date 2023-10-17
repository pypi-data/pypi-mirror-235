#!/usr/bin/env python3
import asyncio
import sys
import tomli

async def main():
    reqlist = ''
    path = ''
    if len(sys.argv) == 1:
        path = 'pyproject.toml'
    else:
        path = sys.argv[1]
    with open(path, 'rb') as f:
        toml_dict = tomli.load(f)
        for req in toml_dict['project']['dependencies']:
            reqlist += str(req) + '\n'
    with open('requirements.txt', 'w') as f:
        f.write(reqlist)


def start():
    asyncio.run(main())

if __name__ == '__main__':
    start()