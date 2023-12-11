import asyncio
import gbulb
import sys

from .app import NetGuardian

gbulb.install(gtk=True)

def main():
    loop = asyncio.get_event_loop()
    loop.run_forever(application=NetGuardian())

if __name__ == '__main__':
    sys.exit(main())
