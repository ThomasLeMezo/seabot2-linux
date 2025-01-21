import smbus
import time
from math import *
from bq27441_reg import *

userConfigControl = False
sealFlag = False

# Initialize the I2C bus
bus = smbus.SMBus(1)  # Use 0 for older Raspberry Pi boards

def readControlWord(function):
    bus.write_i2c_block_data(BQ72441_I2C_ADDRESS, 0x00, [(function & 0x00FF), (function & 0xFF00) >> 8])
    data_rcw = bus.read_i2c_block_data(BQ72441_I2C_ADDRESS, 0x00, 2)
    return data_rcw[0] | (data_rcw[1] << 8)

def get_status():
    data_rcw = bus.read_i2c_block_data(BQ72441_I2C_ADDRESS, BQ27441_CONTROL_STATUS, 2)
    return data_rcw[0] | (data_rcw[1] << 8)

def is_sealed():
    return get_status() & BQ27441_STATUS_SS

def seal():
    readControlWord(BQ27441_CONTROL_SEALED)

def unseal():
    print("Unsealing...")
    executeControlWord(BQ27441_UNSEAL_KEY)
    executeControlWord(BQ27441_UNSEAL_KEY)
    
    return not is_sealed()

def get_device_type():
    return readControlWord(BQ27441_CONTROL_DEVICE_TYPE)

def executeControlWord(function):
    bus.write_i2c_block_data(BQ72441_I2C_ADDRESS, 0x00, [(function & 0x00FF), (function & 0xFF00) >> 8])
    return True

def enterConfig(userControl):
    global userConfigControl, sealFlag
    if userControl:
        userConfigControl = True

    if is_sealed():
        print("Device is sealed")
        sealFlag = True
        unseal()
    else:
        print("Device is unsealed")

    executeControlWord(BQ27441_CONTROL_SET_CFGUPDATE)
    print("CFGUpdate sended")
    
    time.sleep(1.0)
    timeout = BQ72441_I2C_TIMEOUT

    status = get_status()
    flag_cfgupmode = status & BQ27441_FLAG_CFGUPMODE
    
    print("flag_cfgupmode = ", flag_cfgupmode)

    if timeout > 0:
        print("Sucess to enter config mode")
        return True
    else:
        print("Timeout = ", timeout)

    print("Failed to enter config mode")
    return False

def softReset():
    return executeControlWord(BQ27441_CONTROL_SOFT_RESET)

def exitConfig(resim=True):
    if resim:
        if softReset():
            timeout = BQ72441_I2C_TIMEOUT
            print("CFGUPMODE = ", not(get_status() & BQ27441_FLAG_CFGUPMODE))
            
            if timeout > 0:
                if sealFlag:
                    seal()
                return True
        else:
            return False
    else:
        executeControlWord(BQ27441_CONTROL_EXIT_CFGUPDATE)

def blockDataControl():
    enableByte = 0x00
    bus.write_i2c_block_data(BQ72441_I2C_ADDRESS, BQ27441_EXTENDED_CONTROL, [enableByte])
    return True

def blockDataClass(classID):
    bus.write_i2c_block_data(BQ72441_I2C_ADDRESS, BQ27441_EXTENDED_DATACLASS, [classID])
    return True

def blockDataOffset(offset):
    bus.write_i2c_block_data(BQ72441_I2C_ADDRESS, BQ27441_EXTENDED_DATABLOCK, [floor(offset)])

def computeBlockChecksum():
    data = bus.read_i2c_block_data(BQ72441_I2C_ADDRESS, BQ27441_EXTENDED_BLOCKDATA, 32)
    Csum = 0
    for i in range(0, 32):
        Csum += data[i]
    Csum = (255 - Csum) & 0xFF
    return Csum

def blockDataChecksum():
    return bus.read_byte_data(BQ72441_I2C_ADDRESS, BQ27441_EXTENDED_CHECKSUM)

def writeBlockData(offset, data):
    bus.write_i2c_block_data(BQ72441_I2C_ADDRESS, offset + BQ27441_EXTENDED_BLOCKDATA, [data])

def writeBlockChecksum(Csum):
    bus.write_i2c_block_data(BQ72441_I2C_ADDRESS, BQ27441_EXTENDED_CHECKSUM, [Csum])

def writeExtendedData(classID, offset, data, len):
    if len > 32:
        return False

    if not userConfigControl:
        enterConfig(False)

    if not blockDataControl():
        print("Block Data Control failed")
        return False
    if not  blockDataClass(classID):
        print("Block Data Class failed")
        return False

    blockDataOffset(offset/32)
    computeBlockChecksum()

    for i in range(0, len):
        writeBlockData((offset % 32) + i, data[i])

    newCsum = computeBlockChecksum() # Compute the new checksum
    writeBlockChecksum(newCsum)
    print("newCsum = ", hex(newCsum))

    if not userConfigControl:
        exitConfig()

    return True

def begin():
    type = get_device_type()
    if type == BQ27441_DEVICE_ID:
        print("BQ27441 detected")
        return True
    else:
        print("Device ID mismatch. Expected 0x%02X, got 0x%02X" % (BQ27441_DEVICE_ID, type))
        return False

def setCapacity(capacity):
    print("Setting design capacity to %d mAh" % capacity)
    return writeExtendedData(BQ27441_ID_STATE, 10, [capacity>>8, capacity&0xFF], 2)

##########################################


begin()
#setCapacity(5200)
setCapacity(5200)



