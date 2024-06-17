#!/usr/bin/env python

import argparse
import yaml
import json
import os

OUT_DIR = os.path.join(os.getcwd(), "outputs")


def main():
    parser = argparse.ArgumentParser(
        prog="jyc",
        description="JSON <-> YAML converter",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog="Thanks for using %(prog)s! :)"
    )
    parser.add_argument("file", help="Specify either json or yaml file")
    parser.add_argument("-p", "--print", action="store_true",
                        help="Print output on stdout")

    args = parser.parse_args()
    jyc(args.file, args.print)


def json_to_yaml(file_path: str):
    f = open(file_path, mode='r')
    data = json.load(f)
    f.close()
    write_file = OUT_DIR+"/out.yml"
    o = open(write_file, mode='w')
    yaml.dump(data, o, default_flow_style=False)
    o.close()
    print("Output is written at:", write_file)
    return


def yaml_to_json(file_path: str):
    f = open(file_path, mode='r')
    data = yaml.load(f, Loader=yaml.SafeLoader)
    f.close()
    write_file = OUT_DIR+"/out.json"
    o = open(write_file, mode='w')
    json.dump(data, o, indent=4)
    o.close()
    print("Output is written at:", write_file)
    return


def jyc(file_path: str, print_flag: bool):
    if not file_path.endswith(("yml", "yaml", "json")):
        raise Exception("Not a json or yaml file")
        return
    if file_path.endswith(("yml", "yaml")):
        yaml_to_json(file_path)
        if print_flag:
            f = open(OUT_DIR+"/out.json", mode='r')
            for line in f.readlines():
                print(line.rstrip())
            f.close()
    else:
        json_to_yaml(file_path)
        if print_flag:
            f = open(OUT_DIR+"/out.yml", mode='r')
            for line in f.readlines():
                print(line.rstrip())
            f.close()
    return


if __name__ == "__main__":
    main()
