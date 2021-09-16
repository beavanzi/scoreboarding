# coding=utf-8
from typing import List
from registers import Registers
from search import search
from issue import issue
from scoreboarding import Scoreboarding
from functional_units import FunctionalUnits
from functional_unit import FunctionalUnit


def processor(memory: List[List[str]]):
    registers = Registers()
    scoreboarding = Scoreboarding()

    functional_units = FunctionalUnits()

    functional_units.add_functional_unit(FunctionalUnit("Add", ["addd", "subd"], 2))
    functional_units.add_functional_unit(FunctionalUnit("Mult1", ["multd"], 10))
    functional_units.add_functional_unit(FunctionalUnit("Mult2", ["multd"], 10))
    functional_units.add_functional_unit(FunctionalUnit("Divide", ["divd"], 40))
    functional_units.add_functional_unit(FunctionalUnit("Integer", ["ld"], 1))

    clock(memory, registers, scoreboarding, functional_units)


def clock(memory: List[List[str]], registers: Registers, scoreboarding: Scoreboarding, functional_units: FunctionalUnits):
    for i in range(10):
    ## while not (emptyPipeline(memory, registers, scoreboarding)):
        pipeline(memory, registers, scoreboarding, functional_units)


def pipeline(memory: List[List[str]], registers: Registers, scoreboarding: Scoreboarding, functional_units: FunctionalUnits):
    write()
    execution()
    read_operands()
    issue(registers, scoreboarding, functional_units)
    search(memory, registers)


def emptyPipeline(memory: List[List[str]], registers: Registers, scoreboarding: Scoreboarding):
    #return len(memory) == 0 and scoreboarding.register_status
    return 0


def read_operands():
    return 0


def execution():
    return 0


def write():
    return 0
