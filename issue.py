from scoreboarding import Scoreboarding
from functional_units import FunctionalUnits
from functional_unit import FunctionalUnit
from bus import Bus


def issue(bus: Bus, scoreboarding: Scoreboarding, functional_units: FunctionalUnits, clock: int):

    if bus.get_first_instruction_to_be_issue():
        instruction = bus.get_first_instruction_to_be_issue()
        id = instruction.get_id()
        opcode = instruction.get_opcode()
        dest = instruction.get_dest()

        functional_unit = functional_units.get_functional_unit_available_by_opcode(opcode)

        if functional_unit and can_be_emitted(scoreboarding, dest, functional_unit):
            if not has_hazard_WAW(dest, bus):
                fk = instruction.get_s2()
                if functional_unit.get_name() == 'Integer':
                    fj = ""
                    qj = ""
                else:
                    fj = instruction.get_s1()
                    qj = scoreboarding.register_status[fj]
                qk = scoreboarding.register_status[fk]

                functional_units.update_functional_unit(id, functional_unit.get_name(), True, opcode, dest, fj, fk, qj, qk, not(bool(qj)), not(bool(qk)))
                scoreboarding.set_register_status(dest, functional_unit.get_name())
                scoreboarding.update_issue(id, clock)

                bus.remove_instruction_from_issue()
                bus.add_instruction_to_read_operands(instruction, functional_unit)
                functional_unit.set_lock(True)


def has_hazard_WAW(dest: str, bus: Bus):
    return dest in bus.get_register_from_write_to_issue()


def can_be_emitted(scoreboarding: Scoreboarding, dest: str, functional_unit: FunctionalUnit):
    return not bool(scoreboarding.register_status[dest]) and not functional_unit.is_busy() and not functional_unit.is_locked()

