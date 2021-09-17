import sys
from scoreboarding import Scoreboarding
from functional_units import FunctionalUnits

def read_file_to_memory(file_path):
    file_in = open(file_path, "r")
    memory = append_lines_to_memory(file_in)
    create_log_file()
    file_in.close()
    return memory


def append_lines_to_memory(opened_file):
    memory = []

    for line in opened_file:
        line = line.replace(',', '').replace('(', '').replace(')', ' ')
        values = line.split()
        memory.append(values)

    return memory


def create_log_file():
    file_out = open(file_out_name(), "w")
    file_out.close()


def file_out_name():
    file = sys.argv[1]
    file = file.split(".")
    out_path = file[0]
    return "{}.out".format(out_path)


def write_log(scoreboarding: Scoreboarding, functional_units: FunctionalUnits, clock: int):
    file_out = open(file_out_name(), "a")
    file_out.write('\n\nClock: ' + clock.__str__())
    scoreboarding.show_instructions_status(file_out)
    functional_units.show_functional_units_table(file_out)
    scoreboarding.show_registers_status_table(file_out)
    file_out.close()
