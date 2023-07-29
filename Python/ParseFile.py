#!/usr/bin/python3

import argparse
import sys
import json

def parseCommandLine():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', dest="file", type=str, help="File to be parsed")
    return parser.parse_args()

def flattenDict(data:dict, prefix=""):
    result = {}
    for key, value in data.items():
        if prefix:
            key = prefix + "." + key
        if isinstance(value, dict):
            result.update(flattenDict(value, key))
        else:
            if value == None or value == "":
                result[key] = "\n"
            else:
                result[key] = value
    return result


def processFile(filePath: str):
    print(f"Opening test fild {filePath}")
    columnFiles= {}
    try:
        with open(filePath, "r") as file:
            for line in file:
                data = flattenDict(json.loads(line.strip()))
                for key, value in data.items():
                    if key not in columnFiles:
                        columnFiles[key] = open(key, "w")
                    columnFiles[key].write(str(value)+"\n")            
        for f in columnFiles.keys(): columnFiles[f].close()

    except OSError as err:
        print(f"Failed to open file {err}")
        sys.exit(1)

def main():
    args = parseCommandLine()
    processFile(args.file)    
if __name__ == '__main__':
    main()