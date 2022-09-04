import argparse

def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("launch_id")
    args = parser.parse_args()
    return args