#!/usr/bin/env python
import sys

from . import PlannerCmd


def main():
    if len(sys.argv) == 1:
        PlannerCmd().cmdloop()
    else:
        print('not loop')


if __name__ == '__main__':
        main()
