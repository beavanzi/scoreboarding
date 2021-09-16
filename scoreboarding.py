from typing import List, TypedDict, Mapping, Union


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

    def __init__(self, id: int, instruction: str, destination: str, j: str, k: str, issue: str, read: str, execution: str, write: str):
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
    ## functional_units: dict[str, Mapping[str, Union[str, bool]]]
   # functional_units: dict[str, FunctionalUnit]
    instructions_status: List[InstructionStatus]
    register_status: dict[str, str]

    def __init__(self):
        ## "instruction": "", "dest": "", "j": "", "k": "", "issue": "", "read": "", "execution": "", "write": ""
        self.instructions_status = []
        # self.functional_units = {
        #     'Integer': {'busy': False, 'op': "", 'Fi': "", 'Fj': "", 'Fk': "", 'Qj': "", 'Qk': "",
        #                 'Rj': False, 'Rk': False},
        #     # 'Mult1': (False, None, None, None, None, None, None, None),
        #     'Mult1': {'busy': False, 'op': "", 'Fi': "", 'Fj': "", 'Fk': "", 'Qj': "", 'Qk': "",
        #                 'Rj': False, 'Rk': False},
        #     'Mult2': {'busy': False, 'op': "", 'Fi': "", 'Fj': "", 'Fk': "", 'Qj': "", 'Qk': "",
        #                 'Rj': False, 'Rk': False},
        #     'Add': {'busy': False, 'op': "", 'Fi': "", 'Fj': "", 'Fk': "", 'Qj': "", 'Qk': "",
        #                 'Rj': False, 'Rk': False},
        #     'Divide': {'busy': False, 'op': "", 'Fi': "", 'Fj': "", 'Fk': "", 'Qj': "", 'Qk': "",
        #                 'Rj': False, 'Rk': False},
        # }

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

    # def set_function_unit(self, fuctional_unit, status):
    #     self.functional_units[fuctional_unit] = status
    #
    # def clear_function_unit(self, fuctional_unit):
    #     self.functional_units[fuctional_unit] = {'busy': False, 'op': "", 'Fi': "", 'Fj': "", 'Fk': "", 'Qj': "", 'Qk': "", 'Rj': "", 'Rk': ""}

    def set_register_status(self, register, functional_unit):
        self.register_status[register] = functional_unit

    def clear_register_status(self, register):
        self.register_status[register] = ""

    def set_new_instruction_status(self, id: int, instruction: str, dest: str, j: str, k: str, issue: str, read: str, execution: str, write: str):
        new_instruction = InstructionStatus(id, instruction, dest, j, k, issue, read, execution, write)
        self.instructions_status.append(new_instruction)

    def show_registers_status_table(self):
        layout = "{:7} | {:^7} | {:^7} | {:^7} | {:^7} | {:^7} | {:^7} | {:^7} | {:^7} | {:^7} | {:7} | {:7}"
        print("\n\n---------- Tabela de status dos registros ----------")
        print(layout.format("R0", "R1", "R2", "R3", "R4", "R5", "R6", "R7", "R8", "R9", "R10", "R11", "R12"))
        # string_buffer = []
        # for reg, value in self.register_status:
        #     string_buffer.append("{:7} |".format(value))
        # table = "".join(string_buffer)

        # continuar nessa
        # for reg, value in self.register_status.items():
        #
        # table = layout.format()
        # print(table)
