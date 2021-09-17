from scoreboarding import Scoreboarding
from bus import Bus


def execution(bus: Bus, scoreboarding: Scoreboarding, clock: int):
    fuctional_units = bus.get_instructions_from_execution()
    remove_uf = []

    for fu in fuctional_units:
        if fu.is_execution_complete() and not fu.is_locked():
            scoreboarding.update_execution(fu.get_id(), clock)
            remove_uf.append(fu)

            bus.add_instruction_to_write(fu)
            fu.set_lock(True)

        fu.decrease_latency()
    bus.remove_instruction_from_execution(remove_uf)