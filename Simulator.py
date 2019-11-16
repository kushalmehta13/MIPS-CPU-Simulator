from Memory import Memory
from Register import Register
from Configuration import Config
import Pipeline
def initializeMemory():
    memory = Memory('inst.txt', 'data.txt')
    print('Memory Initialized')
    print('------------------')
    return memory


def initializeRegister():
    register = Register('reg.txt')
    print('Register Initialized')
    print('------------------')
    # register.showRegister()
    return register


def configureSystem():
    config = Config('config.txt')
    print('System Configured')
    print('------------------')
    # config.showConfigs()
    return config.getIntUnit(), config.getFPAdder(), config.getFPDiv(), config.getFPMult(), config.getMainMem(), config.getICache(), config.getDCache()


def run(memory, register, unit, fp_adder, fp_div, fp_mult, mem, i_cache, d_cache, PC, cycle, addr, IF):
    while int(addr, 16) <= 31:
        # If IF stage is free
        if IF.isBusy() == False:
            # Increment address
            addr = hex(int(addr, 16)+1)
            print(PC)
            IF.fetch(addr)
        IF.updateCounter()
        PC += 1

def initSystem():
    return 0,0,'0x0'


def initializeStages(memory):
    IF = Pipeline.InstructionFetch('0x0', memory)
    return IF


def main():
    memory = initializeMemory()
    register = initializeRegister()
    IntUnit, FPAdder, FPDiv, FPMult, MainMem, ICache, DCache =  configureSystem()
    PC, cycle, addr = initSystem()
    # IF, ID, EX, MEM, WB = initializeStages(memory)
    IF = initializeStages(memory)
    run(memory, register, IntUnit, FPAdder, FPDiv, FPMult, MainMem, ICache, DCache, PC, cycle, addr, IF)

if __name__ == '__main__':
    main()