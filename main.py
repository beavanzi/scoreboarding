import sys

from pipeline import processor
from fileops import read_file_to_memory
from tests import run_tests

if __name__ == '__main__':
    # run_tests()
    file = sys.argv[1]
    memory = read_file_to_memory(file)
    processor(memory)
