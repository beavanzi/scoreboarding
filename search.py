from typing import List
from registers import Registers


## 	@brief 		Função para buscar próxima instruçao da memoria
def search(memory: List[List[str]], registers: Registers):
    if has_memory_to_read(memory, registers):
        word = memory[registers.pc]
        print(word)
        registers.set_mbr(word)

        registers.increment_pc()

        if is_instruction(word):
            registers.set_ir(word)
        else:
            registers.set_ir(None)


def has_memory_to_read(memory, registers):
    return len(memory) > registers.pc


## 	@brief 		Função verificar se é uma instruçao de acordo com as especificaçoes deste trabalho
def is_instruction(word):
    opcodes = ["addd", "subd", "divd", "ld", "multd"]

    for opcode in opcodes:
        if word[0] == opcode and len(word) == 4:
            return True

    return False
