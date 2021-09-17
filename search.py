from typing import List
from registers import Registers
from bus import Bus
from instruction import Instruction
from scoreboarding import Scoreboarding


## 	@brief 		Função para buscar próxima instruçao da memoria
def search(bus: Bus, memory: List[List[str]], registers: Registers, scoreboarding: Scoreboarding):
    if has_memory_to_read(memory, registers):
        word = memory[registers.pc]
        registers.increment_pc()

        if is_instruction(word):
            instruction = Instruction(registers.pc - 1, word[0], word[1], word[2], word[3])
            scoreboarding.set_new_instruction_status(registers.pc - 1, word[0], word[1], word[2], word[3], "", "", "", "")
            bus.add_instruction_to_issue(instruction)


def has_memory_to_read(memory, registers):
    return len(memory) > registers.pc


def is_instruction(word):
    opcodes = ["addd", "subd", "divd", "ld", "multd"]

    for opcode in opcodes:
        if word[0] == opcode and len(word) == 4:
            return True

    return False
