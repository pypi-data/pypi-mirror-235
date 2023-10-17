#!/usr/bin/env python3
import asyncio
import sys
import tomli

async def main():
    reqlist = ''
    with open(f'{sys.argv[1]}', 'rb') as f:
        toml_dict = tomli.load(f)
        for req in toml_dict['project']['dependencies']:
            reqlist += str(req) + '\n'
        print(reqlist)
    with open('requirements.txt', 'w') as f:
        f.write(reqlist)


def start():
    asyncio.run(main())

if __name__ == '__main__':
    start()