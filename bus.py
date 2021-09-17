from custom_queue import CustomQueue
from typing import List
from instruction import Instruction
from functional_unit import FunctionalUnit


class Bus:
    instructions_to_issue: CustomQueue[Instruction]
    instructions_to_read_operands: List[FunctionalUnit]
    instructions_to_execution: List[FunctionalUnit]
    instructions_to_write: List[FunctionalUnit]
    registers_from_write_to_issue: List[str]

    def __init__(self):
        self.instructions_to_issue = CustomQueue()
        self.instructions_to_read_operands = []
        self.instructions_to_execution = []
        self.instructions_to_write = []
        self.registers_from_write_to_issue = []

    # Funçoes para issue
    def add_instruction_to_issue(self, instruction: Instruction):
        self.instructions_to_issue.enqueue(instruction)

    def remove_instruction_from_issue(self):
        self.instructions_to_issue.dequeue()

    def get_first_instruction_to_be_issue(self):
        return self.instructions_to_issue.first_element()

    # Funçoes para read operands
    def add_instruction_to_read_operands(self, instruction: Instruction, functional_unit: FunctionalUnit):
        self.instructions_to_read_operands.append(functional_unit)

    def remove_instruction_from_read_operands(self, functional_units: list[FunctionalUnit]):
        for uf in functional_units:
            index = self.instructions_to_read_operands.index(uf)
            self.instructions_to_read_operands.pop(index)

    def get_instructions_to_read_operants(self):
        return self.instructions_to_read_operands

    # Funçoes para execution
    def add_instruction_to_execution(self, functional_unit: FunctionalUnit):
        self.instructions_to_execution.append(functional_unit)

    def remove_instruction_from_execution(self, functional_units: list[FunctionalUnit]):
        for uf in functional_units:
            index = self.instructions_to_execution.index(uf)
            self.instructions_to_execution.pop(index)

    def get_instructions_from_execution(self):
        return self.instructions_to_execution

    # Funçoes para write
    def add_instruction_to_write(self, functional_unit: FunctionalUnit):
        self.instructions_to_write.append(functional_unit)

    def remove_instruction_from_write(self, functional_units: list[FunctionalUnit]):
        for uf in functional_units:
            index = self.instructions_to_write.index(uf)
            self.instructions_to_write.pop(index)

    def get_instructions_from_write(self):
        return self.instructions_to_write

    # Funçoes para issue vindas da write
    def add_register_from_write_to_issue(self, register: str):
        self.registers_from_write_to_issue.append(register)

    def remove_register_from_write_to_issue(self, register: str):
        index = self.registers_from_write_to_issue.index(register)
        self.registers_from_write_to_issue.pop(index)

    def get_register_from_write_to_issue(self):
        return self.registers_from_write_to_issue

    def remove_all_register_from_write_to_issue(self):
        self.registers_from_write_to_issue = []
