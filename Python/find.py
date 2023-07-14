#!/usr/bin/python3

import argparse
import os
import fnmatch
from abc import ABC, abstractmethod


class Filters(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def apply(self):
        pass


class File:
    def __init__(self, dirpath: str, name: str) -> None:
        self.name = name
        self.dirpath = dirpath
        try:
            self.statInfo = os.stat(f"{dirpath}/{name}")
            self.size = self.statInfo.st_size

        except OSError as e:
            print(f"Failed to get filesize for {name}: {e()}")
            self.size = 0


class sizeFilter(Filters):
    def __init__(self, size: int) -> None:
        self.size = size

    def apply(self, fObj: File):
        return fObj.size > self.size


class namePatternFilter(Filters):
    def __init__(self, pattern: str) -> None:
        self.pattern = pattern

    def apply(self, fObj: File):
        return fnmatch.fnmatch(fObj.name, self.pattern)


def myFindOr(directory: str, filters: list):
    for dirPath, dirNames, fileNames in os.walk(directory):
        for flr in fileNames:
            fObj = File(dirPath, flr)
            for filter in filters:
                if filter.apply(fObj):
                    print(f"{dirPath}/{flr}")
                    break


def myFindAnd(directory: str, filters: list):
    for dirPath, dirNames, fileNames in os.walk(directory):
        for flr in fileNames:
            fObj = File(dirPath, flr)
            valid = True
            for filter in filters:
                if not filter.apply(fObj):
                    valid = False
                    break
            if valid:
                print(f"{dirPath}/{flr}")


def setCommandLineArguements():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        "--directory",
        dest="dir",
        type=str,
        help="Root directory to start the search",
    )
    parser.add_argument(
        "-p", "--pattern", dest="pattern", type=str, help="Pattern to match"
    )
    parser.add_argument(
        "-s",
        "--size",
        dest="size",
        type=int,
        help="Find files greater than provided size",
    )

    return parser.parse_args()


def main():
    args = setCommandLineArguements()
    filters: list = []
    if args.pattern:
        filters.append(namePatternFilter(args.pattern))
    if args.size:
        filters.append(sizeFilter(args.size))

    myFindOr(args.dir, filters)


if __name__ == "__main__":
    main()
