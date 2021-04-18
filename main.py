import argparse
import time
from test import testing
from train import training

from data import *
from params import *

parser = argparse.ArgumentParser(description='')

parser.add_argument('--phase', dest='phase', default='train', help="'train' pour entraîner ou 'test' pour tester")

args = parser.parse_args()


def main():
    print("main missing :)")


if __name__ == '__main__':
    time_start = time.time()
    main()
    print("Script finished in "+str(time.time()-time_start))
