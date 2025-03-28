
BQ72441_I2C_ADDRESS = 0x55 # Default I2C address of the BQ27441-G1A

BQ72441_I2C_TIMEOUT = 2000

BQ27441_UNSEAL_KEY = 	0x8000 # Secret code to unseal the BQ27441-G1A
BQ27441_DEVICE_ID = 	0x0421 # Default device ID

BQ27441_CONTROL_STATUS =			0x00
BQ27441_CONTROL_DEVICE_TYPE =		0x01
BQ27441_CONTROL_FW_VERSION =		0x02
BQ27441_CONTROL_DM_CODE =			0x04
BQ27441_CONTROL_PREV_MACWRITE =	0x07
BQ27441_CONTROL_CHEM_ID =			0x08
BQ27441_CONTROL_BAT_INSERT =		0x0C
BQ27441_CONTROL_BAT_REMOVE =		0x0D
BQ27441_CONTROL_SET_HIBERNATE =	0x11
BQ27441_CONTROL_CLEAR_HIBERNATE =	0x12
BQ27441_CONTROL_SET_CFGUPDATE =	0x13
BQ27441_CONTROL_SHUTDOWN_ENABLE =	0x1B
BQ27441_CONTROL_SHUTDOWN =		0x1C
BQ27441_CONTROL_SEALED =			0x20
BQ27441_CONTROL_PULSE_SOC_INT =	0x23
BQ27441_CONTROL_RESET =			0x41
BQ27441_CONTROL_SOFT_RESET =		0x42
BQ27441_CONTROL_EXIT_CFGUPDATE =	0x43
BQ27441_CONTROL_EXIT_RESIM =		0x44

BQ27441_STATUS_SHUTDOWNEN =	(1<<15)
BQ27441_STATUS_WDRESET =		(1<<14)
BQ27441_STATUS_SS =			(1<<13)
BQ27441_STATUS_CALMODE =		(1<<12)
BQ27441_STATUS_CCA =			(1<<11)
BQ27441_STATUS_BCA =			(1<<10)
BQ27441_STATUS_QMAX_UP =		(1<<9)
BQ27441_STATUS_RES_UP =		(1<<8)
BQ27441_STATUS_INITCOMP =		(1<<7)
BQ27441_STATUS_HIBERNATE =	(1<<6)
BQ27441_STATUS_SLEEP =		(1<<4)
BQ27441_STATUS_LDMD =			(1<<3)
BQ27441_STATUS_RUP_DIS =		(1<<2)
BQ27441_STATUS_VOK =			(1<<1)

BQ27441_FLAG_OT =			(1<<15)
BQ27441_FLAG_UT =			(1<<14)
BQ27441_FLAG_FC =			(1<<9)
BQ27441_FLAG_CHG =		(1<<8)
BQ27441_FLAG_OCVTAKEN =	(1<<7)
BQ27441_FLAG_ITPOR =		(1<<5)
BQ27441_FLAG_CFGUPMODE =	(1<<4)
BQ27441_FLAG_BAT_DET =	(1<<3)
BQ27441_FLAG_SOC1 =		(1<<2)
BQ27441_FLAG_SOCF =		(1<<1)
BQ27441_FLAG_DSG =		(1<<0)

BQ27441_EXTENDED_OPCONFIG =	0x3A # OpConfig()
BQ27441_EXTENDED_CAPACITY =	0x3C # DesignCapacity()
BQ27441_EXTENDED_DATACLASS =	0x3E # DataClass()
BQ27441_EXTENDED_DATABLOCK =	0x3F # DataBlock()
BQ27441_EXTENDED_BLOCKDATA =	0x40 # BlockData()
BQ27441_EXTENDED_CHECKSUM =	0x60 # BlockDataCheckSum()
BQ27441_EXTENDED_CONTROL =	0x61 # BlockDataControl()


BQ27441_ID_SAFETY =			2   # Safety
BQ27441_ID_CHG_TERMINATION =	36  # Charge Termination
BQ27441_ID_CONFIG_DATA =		48  # Data
BQ27441_ID_DISCHARGE =		49  # Discharge
BQ27441_ID_REGISTERS =		64  # Registers
BQ27441_ID_POWER =			68  # Power
# Gas Gauging Classes
BQ27441_ID_IT_CFG =			80  # IT Cfg
BQ27441_ID_CURRENT_THRESH =	81  # Current Thresholds
BQ27441_ID_STATE =			82  # State
# Ra Tables Classes
BQ27441_ID_R_A_RAM =			89  # R_a RAM
# Calibration Classes
BQ27441_ID_CALIB_DATA =		104 # Data
BQ27441_ID_CC_CAL =			105 # CC Cal
BQ27441_ID_CURRENT =			107 # Current
# Security Classes
BQ27441_ID_CODES =			112 # Codes

####################/
# OpConfig Register - Bit Definitions #
####################/
# Bit positions of the OpConfig Register
BQ27441_OPCONFIG_BIE =      (1<<13)
BQ27441_OPCONFIG_BI_PU_EN = (1<<12)
BQ27441_OPCONFIG_GPIOPOL =  (1<<11)
BQ27441_OPCONFIG_SLEEP =    (1<<5)
BQ27441_OPCONFIG_RMFCC =    (1<<4)
BQ27441_OPCONFIG_BATLOWEN = (1<<2)
BQ27441_OPCONFIG_TEMPS =    (1<<0)