class Scoreboarding:
    def __init__(self):
        self.instruction_status = {

        }

        self.functional_units = {
            'Integer': {'busy': False, 'op': None, 'Fi': None, 'Fj': None, 'Fk': None, 'Qj': None, 'Qk': None,
                        'Rj': None, 'Rk': None},
            # 'Mult1': (False, None, None, None, None, None, None, None),
            'Mult1': {'busy': False, 'op': None, 'Fi': None, 'Fj': None, 'Fk': None, 'Qj': None, 'Qk': None, 'Rj': None,
                      'Rk': None},
            'Mult2': {'busy': False, 'op': None, 'Fi': None, 'Fj': None, 'Fk': None, 'Qj': None, 'Qk': None, 'Rj': None,
                      'Rk': None},
            'Add': {'busy': False, 'op': None, 'Fi': None, 'Fj': None, 'Fk': None, 'Qj': None, 'Qk': None, 'Rj': None,
                    'Rk': None},
            'Divide': {'busy': False, 'op': None, 'Fi': None, 'Fj': None, 'Fk': None, 'Qj': None, 'Qk': None,
                       'Rj': None, 'Rk': None},
        }

        self.register_status = {
            'r0': None,
            'r1': None,
            'r2': None,
            'r3': None,
            'r4': None,
            'r5': None,
            'r6': None,
            'r7': None,
            'r8': None,
            'r9': None,
            'r10': None,
            'r11': None,
            'r12': None,
        }