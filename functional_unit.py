from typing import List


class FunctionalUnit:
    busy: bool
    op: str
    Fi: str
    Fj: str
    Fk: str
    Qj: str
    Qk: str
    Rj: bool
    Rk: bool
    latency: int
    opcode: str

    def __init__(self, name: str, opcodes: List[str], latency: int):
        self.name = name
        self.busy = False
        self.op = ""
        self.Fi = ""
        self.Fj = ""
        self.Fk = ""
        self.Qj = ""
        self.Qk = ""
        self.Rj = False
        self.Rk = False
        self.initialLatency = latency
        self.currentLatency = latency
        self.opcodes = opcodes

    def __update_fields__(self, busy: bool, op: str, fi: str, fj: str, fk: str, qj: str, qk: str, rj: bool, rk: bool):
        self.busy = busy
        self.op = op
        self.Fi = fi
        self.Fj = fj
        self.Fk = fk
        self.Qj = qj
        self.Qk = qk
        self.Rj = rj
        self.Rk = rk

    def decrease_latency(self):
        self.currentLatency = self.currentLatency - 1

    def is_execution_complete(self):
        return self.currentLatency == 0

    def reset_latency(self):
        self.currentLatency = self.initialLatency

    def is_busy(self):
        return self.busy

    def is_not_busy(self):
        return not self.busy

    def get_name(self):
        return self.name

    def get_op(self):
        return self.op

    def get_fi(self):
        return self.Fi

    def get_fj(self):
        return self.Fj

    def get_fk(self):
        return self.Fk

    def get_qj(self):
        return self.Qj

    def get_qk(self):
        return self.Qk

    def get_rj(self):
        return self.Rj

    def get_rk(self):
        return self.Rk

    def get_opcodes(self):
        return self.opcodes
