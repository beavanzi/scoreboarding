from typing import List


class FunctionalUnit:
    int: int
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
        self.id = None
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
        self.lock = False

    def update_fields(self, id: int, busy: bool, op: str, fi: str, fj: str, fk: str, qj: str, qk: str, rj: bool, rk: bool):
        self.id = id
        self.busy = busy
        self.op = op
        self.Fi = fi
        self.Fj = fj
        self.Fk = fk
        self.Qj = qj
        self.Qk = qk
        self.Rj = rj
        self.Rk = rk

    def update_rk_rj_qk_qj(self, rk: bool, rj: bool, qk: str, qj: str):
        self.Rk = rk
        self.Rj = rj
        self.Qj = qj
        self.Qk = qk

    def get_current_latency(self):
        return self.currentLatency

    def decrease_latency(self):
        self.currentLatency = self.currentLatency - 1

    def is_execution_complete(self):
        return self.currentLatency == 1

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

    def get_lock(self):
        return self.lock

    def get_id(self):
        return self.id

    def set_rk(self, rk: bool):
        self.Rk = rk

    def set_rj(self, rj: bool):
        self.Rj = rj

    def set_lock(self, lock: bool):
        self.lock = lock

    def is_locked(self):
        return self.lock

    def reset(self):
        self.id = None
        self.busy = False
        self.op = ""
        self.Fi = ""
        self.Fj = ""
        self.Fk = ""
        self.Qj = ""
        self.Qk = ""
        self.Rj = False
        self.Rk = False
        self.currentLatency = self.initialLatency