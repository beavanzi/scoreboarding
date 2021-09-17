class Instruction:
    opcode: str
    dest: str
    s1: str
    s2: str
    id: int

    def __init__(self, id: int, opcode: str, dest: str, s1: str, s2: str):
        self.opcode = opcode
        self.dest = dest
        self.s1 = s1
        self.s2 = s2
        self.id = id

    def get_id(self):
        return self.id

    def get_opcode(self):
        return self.opcode

    def get_dest(self):
        return self.dest

    def get_s1(self):
        return self.s1

    def get_s2(self):
        return self.s2
