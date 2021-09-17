from functional_unit import FunctionalUnit
from typing import List


class FunctionalUnits:
    units: List[FunctionalUnit]

    def __init__(self):
        self.units = []

    def add_functional_unit(self, fu: FunctionalUnit):
        self.units.append(fu)

    def get_functional_unit(self, name: str):
        for fu in self.units:
            if fu.get_name() == name:
                return fu

    def update_functional_unit(self, id: int, name: str, busy: bool, op: str, fi: str, fj: str, fk: str, qj: str, qk: str, rj: bool, rk: bool):
        fu = self.get_functional_unit(name)
        fu.update_fields(id, busy, op, fi, fj, fk, qj, qk, rj, rk)

    def is_functional_unit_busy(self, name):
        return self.get_functional_unit(name).is_busy()

    def is_functional_unit_not_busy(self, name):
        return not self.get_functional_unit(name).is_busy()

    def show_functional_units_table(self, file):
        file.write("\n\n---------- Tabela de unidades funcionais ----------\n")
        file.write("{:7} | {:^5} | {:^5} | {:^5} | {:^5} | {:^5} | {:^5} | {:^5} | {:^5} | {:^5} |\n".format("Name", "Busy", "Op", "Fi", "Fj", "Fk", "Qj", "Qk", "Rj", "Rk"))
        for fu in self.units:
            table = "{fu:7} | {busy:^5} | {op:^5} | {fi:^5} | {fj:^5} | {fk:^5} | {qj:^5} | {qk:^5} | {rj:^5} | {rk:^5} |\n".format(fu=fu.get_name(), busy=fu.is_busy().__str__(), op=fu.get_op(), fi=fu.get_fi(), fj=fu.get_fj(), fk=fu.get_fk(), qj=fu.get_qj(), qk=fu.get_qk(), rj=fu.get_rj().__str__(), rk=fu.get_rk().__str__())
            file.write(table)

    def get_functional_unit_available_by_opcode(self, opcode):
        for fu in self.units:
            for fu_opcode in fu.get_opcodes():
                if fu_opcode == opcode and fu.is_not_busy():
                    return fu

    def reset_locks(self):
        for fu in self.units:
            fu.set_lock(False)
