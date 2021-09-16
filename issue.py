from registers import Registers
from scoreboarding import Scoreboarding
from functional_units import FunctionalUnits
from functional_unit import FunctionalUnit


def issue(registers: Registers, scoreboarding: Scoreboarding, functional_units: FunctionalUnits):

    # func_units_map = { desuso
    #     'ld': 'Integer',
    #     'multd': 'Mult1' or 'Mult2',
    #     'addd': 'Add',
    #     'subd': 'Add',
    #     'divd': 'Divide'
    # }

    if registers.ir:
        instruction = registers.ir[0]
        dest = registers.ir[1]

        functional_unit = functional_units.get_functional_unit_available_by_opcode(instruction)

        if is_fuctional_unit_and_register_available(scoreboarding, dest, functional_unit):
            fk = registers.ir[3]
            if functional_unit.get_name() == 'Integer':
                fj = ""
                qj = ""
            else:
                fj = registers.ir[2]
                qj = scoreboarding.register_status[fj]
            qk = scoreboarding.register_status[fk]

            # desuso scoreboarding.set_function_unit(functional_unit_name, {'busy': True, 'op': instruction, 'Fi': dest, 'Fj': fj, 'Fk': fk, 'Qj': qj, 'Qk': qk, 'Rj': not(bool(qj)), 'Rk': not(bool(qk))})
            functional_units.update_functional_unit(functional_unit.get_name(), True, instruction, dest, fj, fk, qj, qk, not(bool(qj)), not(bool(qk)))
            scoreboarding.set_register_status(dest, functional_unit.get_name())

        functional_units.show_functional_units_table()
        scoreboarding.show_registers_status_table()


def is_fuctional_unit_and_register_available(scoreboarding: Scoreboarding, dest: str, functional_unit: FunctionalUnit):
    return not bool(scoreboarding.register_status[dest]) and not functional_unit.is_busy()

