import os
import argparse

parser = argparse.ArgumentParser(description='Start Frye')
parser.add_argument('--message', default='Message', help='Passes a Message')

args = parser.parse_args()

def hello_world():
    print(args.message)