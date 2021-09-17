class Registers:

    def __init__(self):
        ## @brief PC ou Program Counter armazena o endereço da instruçao a ser executada
        self.pc = 0
        ## @brief IR ou instruction register contem a ultima instruçao buscada
        self.ir = None
        ## @brief MAR ou memory address register armazena um endereço de memoria
        ## @brief MBR ou memory buffer register armazena uma palavra de dados (lida ou escrita)
        self.mbr = None

    def increment_pc(self):
        self.pc = self.pc + 1

    def set_ir(self, instruction):
        self.ir = instruction

    def get_ir(self):
        return self.ir

    def set_mbr(self, word):
        self.mbr = word


