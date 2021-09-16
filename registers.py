class Registers:

    def __init__(self):
        ## @brief PC ou Program Counter armazena o endereço da instruçao a ser executada
        self.pc = 0
        ## @brief IR ou instruction register contem a ultima instruçao buscada
        self.ir = None
        ## @brief MAR ou memory address register armazena um endereço de memoria
        ## @brief MBR ou memory buffer register armazena uma palavra de dados (lida ou escrita)
        self.mbr = None
        # self.r0 = None
        # self.r1 = None
        # self.r2 = None
        # self.r3 = None
        # self.r4 = None
        # self.r5 = None
        # self.r6 = None
        # self.r7 = None
        # self.r8 = None
        # self.r9 = None
        # self.r10 = None
        # self.r11 = None
        # self.r12 = None
        # self.rb = None

    def increment_pc(self):
        self.pc = self.pc + 1

    def set_ir(self, instruction):
        self.ir = instruction

    def set_mbr(self, word):
        self.mbr = word

    # def set_register(self, register, value):
    #     getattr(myobject, '%s' % i)
    #
    # def clean_register(self, register):
    #     self[register] = None

