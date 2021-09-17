from scoreboarding import Scoreboarding
from bus import Bus


def read_operands(bus: Bus, scoreboarding: Scoreboarding, clock: int):
    fuctional_units = bus.get_instructions_to_read_operants()
    remove_uf = []

    for fu in fuctional_units:
        if fu.get_rj() and fu.get_rk() and not fu.is_locked():
            fu.update_rk_rj_qk_qj(False, False, "", "")
            remove_uf.append(fu)

            scoreboarding.update_read(fu.get_id(), clock)

            bus.add_instruction_to_execution(fu)
            fu.set_lock(True)

    bus.remove_instruction_from_read_operands(remove_uf)