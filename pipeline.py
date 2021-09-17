# coding=utf-8
from typing import List
from registers import Registers
from search import search
from issue import issue
from bus import Bus
from fileops import write_log
from write import write
from read_operands import read_operands
from execution import execution
from functional_units import FunctionalUnits
from functional_unit import FunctionalUnit


class InstructionStatus:
    id: int
    instruction: str
    destination: str
    j: str
    k: str
    issue: str
    read: str
    execution: str
    write: str

    def __init__(self, id: int, instruction: str, destination: str, j: str, k: str, issue: str, read: str,
                 execution: str, write: str):
        self.id = id
        self.instruction = instruction
        self.destination = destination
        self.j = j
        self.k = k
        self.issue = issue
        self.read = read
        self.execution = execution
        self.write = write

    def set_instruction(self, instruction):
        self.instruction = instruction

    def set_destination(self, destination):
        self.destination = destination

    def set_j(self, j):
        self.j = j

    def set_k(self, k):
        self.k = k

    def set_issue(self, issue):
        self.issue = issue

    def set_read(self, read):
        self.read = read

    def set_execution(self, execution):
        self.execution = execution

    def set_write(self, write):
        self.write = write


class Scoreboarding:
    instructions_status: List[InstructionStatus]
    register_status: dict[str, str]

    def __init__(self):
        self.instructions_status = []

        self.register_status = {
            'r0': "",
            'r1': "",
            'r2': "",
            'r3': "",
            'r4': "",
            'r5': "",
            'r6': "",
            'r7': "",
            'r8': "",
            'r9': "",
            'r10': "",
            'r11': "",
            'r12': "",
            'rb': "",
        }

    def is_all_instructions_writen(self):
        for inst in self.instructions_status:
            if inst.write == "":
                return False
        return True

    def set_register_status(self, register, functional_unit):
        self.register_status[register] = functional_unit

    def clear_register_status(self, register):
        self.register_status[register] = ""

    def set_new_instruction_status(self, id: int, instruction: str, dest: str, j: str, k: str, issue: str, read: str,
                                   execution: str, write: str):
        new_instruction = InstructionStatus(id, instruction, dest, j, k, issue, read, execution, write)
        self.instructions_status.append(new_instruction)

    def update_issue(self, id: int, clock: int):
        inst = self.get_instruction_by_id(id)
        inst.issue = clock

    def update_read(self, id: int, clock: int):
        inst = self.get_instruction_by_id(id)
        inst.read = clock

    def update_execution(self, id: int, clock: int):
        inst = self.get_instruction_by_id(id)
        inst.execution = clock

    def update_write(self, id: int, clock: int):
        inst = self.get_instruction_by_id(id)
        inst.write = clock

    def get_instruction_by_id(self, id: int):
        for inst in self.instructions_status:
            if inst.id == id:
                return inst

    def show_instructions_status(self, file):
        layout = "{:7}|{:^7}|{:^7}|{:^7}|{:^7}|{:^7}|{:^7}|{:^7}|\n"
        file.write("\n\n---------- Tabela de status de instruções ----------\n")
        file.write(layout.format("Instruct", "dest", "j", "k", "Issue", "Read", "Exec", "Write"))
        for inst in self.instructions_status:
            file.write(
                layout.format(inst.instruction, inst.destination, inst.j, inst.k, inst.issue, inst.read, inst.execution,
                              inst.write))

    def show_registers_status_table(self, file):
        layout = "{:7}|{:^7}|{:^7}|{:^7}|{:^7}|{:^7}|{:^7}|{:^7}|{:^7}|{:^7}|{:7}|{:7}|{:7}|\n"
        file.write("\n\n---------- Tabela de status dos registros ----------\n")
        file.write(layout.format("R0", "R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11", "R12"))
        string_buffer = []
        for reg, value in self.register_status.items():
            if not reg == "rb":
                string_buffer.append("{:7}|".format(value))
        table = "".join(string_buffer)
        file.write(table)

def processor(memory: List[List[str]]):
    registers = Registers()
    scoreboarding = Scoreboarding()
    bus = Bus()

    functional_units = FunctionalUnits()

    functional_units.add_functional_unit(FunctionalUnit("Add", ["addd", "subd"], 2))
    functional_units.add_functional_unit(FunctionalUnit("Mult1", ["multd"], 10))
    functional_units.add_functional_unit(FunctionalUnit("Mult2", ["multd"], 10))
    functional_units.add_functional_unit(FunctionalUnit("Divide", ["divd"], 40))
    functional_units.add_functional_unit(FunctionalUnit("Integer", ["ld"], 1))

    clock(memory, registers, scoreboarding, bus, functional_units)


def clock(memory: List[List[str]], registers: Registers, scoreboarding: Scoreboarding, bus: Bus, functional_units: FunctionalUnits):
    clock_id = 0

    while not (empty_pipeline(memory, registers, scoreboarding)):
        pipeline(memory, registers, scoreboarding, bus, functional_units, clock_id)

        write_log(scoreboarding, functional_units, clock_id)

        clock_id = clock_id + 1
        functional_units.reset_locks()


def pipeline(memory: List[List[str]], registers: Registers, scoreboarding: Scoreboarding, bus: Bus, functional_units: FunctionalUnits, clock: int):

    write(bus, scoreboarding, functional_units, clock)
    execution(bus, scoreboarding, clock)
    read_operands(bus, scoreboarding, clock)
    issue(bus, scoreboarding, functional_units, clock)
    search(bus, memory, registers, scoreboarding)


def empty_pipeline(memory: List[List[str]], registers: Registers, scoreboarding: Scoreboarding):
    return len(memory) <= registers.pc and scoreboarding.is_all_instructions_writen()



