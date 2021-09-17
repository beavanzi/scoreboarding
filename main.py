import sys

from pipeline import processor
from fileops import read_file_to_memory

if __name__ == '__main__':
    file = sys.argv[1]
    memory = read_file_to_memory(file)
    processor(memory)
