from bus import Bus
from scoreboarding import Scoreboarding
from functional_units import FunctionalUnits
from functional_unit import FunctionalUnit

def write(bus: Bus, scoreboarding: Scoreboarding, functional_units: FunctionalUnits, clock: int):
    functional_units_ready_to_execute = bus.get_instructions_from_write()
    remove_uf = []

    bus.remove_all_register_from_write_to_issue()
    # WAR = escrever depois de ler, se escrevessemos o valor da instruçao anterior seria prejudicada

    for fu_ready in functional_units_ready_to_execute:
        if not has_WAR(fu_ready, functional_units) and not fu_ready.is_locked():
            scoreboarding.update_write(fu_ready.get_id(), clock)

            remove_uf.append(fu_ready)
            bus.add_register_from_write_to_issue(fu_ready.get_fi())

            update_all_read_dependencies(fu_ready, functional_units)
            scoreboarding.clear_register_status(fu_ready.get_fi())

            fu_ready.set_lock(True)
            fu_ready.reset()

    bus.remove_instruction_from_write(remove_uf)


def has_WAR(fu_ready: FunctionalUnit, functional_units: FunctionalUnits):
    for fu in functional_units.units:
        if (fu.get_fj() == fu_ready.get_fi() and fu.get_rj()) or (fu.get_fk() == fu_ready.get_fi() and fu.get_rk()):
            return True
    return False


def update_all_read_dependencies(fu_ready: FunctionalUnit, functional_units: FunctionalUnits):
    for fu in functional_units.units:
        if fu.get_qj() == fu_ready.get_name():
            fu.set_rj(True)
            fu.set_lock(True)

        if fu.get_qk() == fu_ready.get_name():
            fu.set_rk(True)
            fu.set_lock(True)