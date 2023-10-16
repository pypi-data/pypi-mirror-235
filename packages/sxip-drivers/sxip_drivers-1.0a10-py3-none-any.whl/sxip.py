# -*- coding: utf-8 -*-
# Copyright (c) 2023 PHOXENE
# MIT License: 
# https://opensource.org/license/mit/
#
""" Python drivers for Phoxene's SxIP devices.

Usage:
    This package is intended to be use by software developpers
    in order to speed-up the integration of PHOXENE's flash devices.
"""
__authors__ = ("Aurélien PLANTIN")
__contact__ = ("a.plantin@phoxene.com")
__copyright__ = "MIT"
__date__ = "2023-10-10"
__version__= "1.0.0"
#Style guide: refers to PEP 8
#Type Hints: refers to PEP 484
#Docstrings: refers to Google Style Python Docstrings 

import modbus
from modbus import ModbusError

class Sxip:     
    """This class defines a SxIP device.

    Allows to instantiate a SxIP device, then provides methods to access it.
    
    Args:
        modbus_link: shall be instantiated from the modbus module
                     is the modbus link on which the device is connected
                     None is accepted to allows modbus link association
                       subsequently to the device instantiation
        modbus_addr: device's Modbus slave address (0 to 247). 0 is broadcast.
    """
    def __init__(self, modbus_link: modbus.Modbus = None, modbus_addr: int = 1
    ) -> None:
        if modbus_link != None:
            if not isinstance(modbus_link, modbus.Modbus):
                raise ValueError("modbus_link paramater shall be"
                                 "an instance of modbus.Modbus")
        self.modbus_link = modbus_link
        self.modbus_addr = modbus_addr

    @property
    def modbus_addr(self):
        """Get or set the Modbus address of the device. 
        int: device's Modbus slave address (0 to 247). 0 is broadcast."""
        return(self._modbus_addr)
    
    @modbus_addr.setter
    def modbus_addr(self, modbus_addr: int):
        if modbus_addr not in range(248):
            raise ValueError(f"Modbus address shall be in [0..247]")
        self._modbus_addr = modbus_addr

    """ ------------------------------------------------------------------- """
    """ -                    General modbus functions                     - """
    """ ------------------------------------------------------------------- """
    def read_registers(self, reg_addr: int, nb_reg: int = 1, **kwargs) -> list:
        """Read a register from the SxIP device.

        Args:
            reg_addr: Starting address (0x0000 to 0xFFFF).
            nb_reg: Quantity of registers to read (1 to 125).
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Registers' content (list of integers).

        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """ 
        return(self.modbus_link.read_registers(self.modbus_addr, 
                                               reg_addr, nb_reg, **kwargs))

    def write_register(
        self, reg_addr: int, value: int, **kwargs
        ) -> None:
        """Write a register to the SxIP device.

        Args:
            reg_addr: Starting address (0x0000 to 0xFFFF).
            value: Value to write (0x0000 to 0xFFFF).

        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """ 
        self.modbus_link.write_register(self.modbus_addr, 
                                        reg_addr, value, **kwargs)

    def write_registers(
        self, reg_addr: int, values: list, **kwargs
        ) -> None:
        """Write multiple registers to the SxIP device.

        Args:
            reg_addr: Starting address (0x0000 to 0xFFFF).
            values: List of words (0x0000 to 0xFFFF) to write (max 123 words).
       
        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """          
        self.modbus_link.write_registers(self.modbus_addr,
                                         reg_addr, values, **kwargs)

    def write_coil(self, coil_addr: int, state: str, **kwargs) -> None:
        """Write a coil to the SxIP device.
        
        Args:
            reg_addr: Coil's address (0x0000 to 0xFFFF).
            state: state to write ('ON' or 'OFF').
       
        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """   
        self.modbus_link.write_single_coil(self.modbus_addr,
                                           coil_addr, state, **kwargs)

    """ ------------------------------------------------------------------- """
    """ -                       SxIP commands                             - """
    """ ------------------------------------------------------------------- """
    def reset(self) -> None:
        """Reset the SxIP device (software reset).
        
        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """
        self.write_coil(coil_addr = 1, state = 'ON')

    def set_init_done(self) -> None:
        """Set the init done flag of the SxIP device.
        
        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """
        self.write_coil(coil_addr = 2, state = 'ON')

    def clear_init_done(self) -> None:
        """Clear the init done flag of the SxIP device.
        
        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """
        self.write_coil(coil_addr = 2, state = 'OFF')

    def clear(self) -> None:
        """Clear error flags of the SxIP device.
        
        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """
        self.write_coil(coil_addr = 3, state = 'ON')

    def flash(self) -> None:
        """Trigger a flash from the SxIP device.
         
         Software trigger is for test purpose.
         Trigger delay is long and inconstant.
         """
        self.write_coil(coil_addr = 4, state = 'ON')

    def save_settings(self) -> None:
        print ('Save settings')
        """Save actual settings in the SxIP device memory.
        
        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """
        # Try bloc is used for timeout restoration in case of exception
        SAVE_SETTINGS_TIMEOUT = 2
        try:
            # Set timeout to handle the long response time
            self.modbus_link.timeout = SAVE_SETTINGS_TIMEOUT
            # Send "save settings" command
            self.write_coil(coil_addr = 5, state = 'ON')
        except Exception as exc:        # Capture all exceptions
            raise(exc)                  # And propagate
        finally:
            print ('Save settings2')
            self.modbus_link.timeout = modbus_link.init_timeout    # Restore initial timeout
            print ('Save settings3')

    def clear_lamp_count(self) -> None:
        """Clear the SxIP device lamp count (At lamp replacement)."""
        self.write_coil(coil_addr = 6, state = 'ON')

    """ ------------------------------------------------------------------- """
    """ -                  SxIP register read functions                   - """
    """ ------------------------------------------------------------------- """
    def get_state(self) -> dict:
        """Read device's state.
        
        Returns:
            {str: bool}
            A dictinonay of flags' names and states
            state values could be 0 or 1:
        
        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """
        flags_dict = {'configured'          : (0, 0),
                      'initialized'         : (0, 1),
                      'ready'               : (0, 2),
                      'com_error'           : (0, 3),
                      'error'               : (0, 4),
                      'failure'             : (0, 5),
                      'alt_energy_level'    : (0, 6),
                      'vin_out_of_range'    : (1, 0),
                      'ht_unreached'        : (1, 1),
                      'was_not_ready'       : (1, 2),
                      'flash_error'         : (1, 5),
                      'fan_error'           : (1, 6),
                      'overtemp'            : (1, 7),
                      'internal_error'      : (1, 8),
                      'flash_failure'       : (2, 5),
                      'fan failure'         : (2, 6),
                      'RS485 frame error'   : (3, 0),
                      'RS485 parity error'  : (3, 1),                     
                      'RS485 buffer ov.'    : (3, 3),
                      'Modbus frame error'  : (3, 4),
                      'Modbus CRC error'    : (3, 5),
                      'vcc error'           : (4, 0),
                      'memory error'        : (4, 1),
                      'internal com error'  : (4, 2)
                      }
        data = self.read_registers(reg_addr = 256, nb_reg = 5)
        flags_state_dict = {}
        for key, value in flags_dict.items():
            flags_state_dict[key] = (data[value[0]] >> value[1]) & 1
        return(flags_state_dict)

    def get_config_inputs(self) -> int:
        """Read device's configuration inputs' value (1..16).
        
        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """
        return(((self.read_registers(reg_addr = 262)[0] & 0b1111) ^ 0b1111) + 1)

    def get_io_state(self, output:str = 'binary') -> dict or int:
        """Read device's inputs and outputs' state.

        Args:
            output: 'binary' or 'dict'

        Returns:
            if output is selected to 'binary':
                A flag byte reflecting IOs state:
            
              | bit |   6     |   5    |    4      |  3  |  2  |  1  |  0  |
              |  IO | ISO_OUT | TTL_IO | DRY_INPUT | IN4 | IN3 | IN2 | IN1 |
            
              DRY_INPUT and ISO_OUTPUT are 1 when closed
        
            if output is selected to 'dict':
                A dictionnay with couples of IOnames and states

        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """
        # Check if the output argument is in the expected list
        if output not in ['binary', 'dict']:
            raise ValueError(f"Unsupported value {output} "
                             "for output parameter")
        # Read the io_state register
        value = self.read_registers(reg_addr = 262)[0]
        # Response for 'binary' output
        if output == 'binary':
            return (value & 0b1111111)
        # Response for 'dict' output
        io_list = (('IN1','low', 'high'),
                   ('IN2','low', 'high'),
                   ('IN3','low', 'high'),
                   ('IN4','low', 'high'),
                   ('DRY_INPUT','released', 'activated'),
                   ('TTL_IO','low', 'high'),
                   ('ISO_OUTPUT','open', 'closed'))
        io_state_dict = {}
        for io in io_list:
            io_state_dict[io[0]] = io[(value & 0b1) + 1]
            value >>= 1
        return (io_state_dict) 

    def get_serial(self) -> int:
        """Read device's serial number.
        
        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """
        return(self.read_registers(reg_addr = 0)[0])

    def get_date(self) -> tuple:
        """Read device's manufacturing date.
        
        Returns:
            list (int: YYYY, int: WW)

        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """
        date = self.read_registers(reg_addr = 1)[0]
        week = date & 0xFF
        year = 2000 + (date >> 8)
        return(year, week)

    def get_hwrev(self) -> str:
        """Read device's hardware revision.

        Returns:
            str: 'A.00'

        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """
        rev = self.read_registers(reg_addr = 2)[0]
        major = chr( rev[0]  & 0xFF ) + 65
        minor = rev[0] >> 8
        return(str(f'{major}.{minor:02}'))

    def get_modbus_address(self) -> int:
        """Read device's modbus address
        
        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """
        return(self.read_registers(reg_addr = 270)[0])

    def get_energy_level(self) -> int:
        """Read device's current energy level
        
        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """
        return(self.read_registers(reg_addr = 271)[0])

    def get_ftime(self) -> int:
        """Read device's current flash time (µs)
        
        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """
        return(self.read_registers(reg_addr = 272)[0])

    def get_input_voltage(self) -> int:
        """Return device's input voltage (V)
        
        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """
        return(self.read_registers(reg_addr = 273)[0] / 1000)

    def get_temperature(self) -> int:
        """Read device's temperature (°C)
        
        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """
        return(self.read_registers(reg_addr = 274)[0])

    def get_last_flash_energy(self) -> int:
        """Read device's last flash energy (J)
        
        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """
        return(self.read_registers(reg_addr = 279)[0] / 100)

    def get_flash_error_count(self) -> int:
        """Read device's error count
        
        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """
        return(self.read_registers(reg_addr = 282)[0])

    def get_flash_healt(self) -> int:
        """Read device's health value
        
        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """
        return(self.read_registers(reg_addr = 283)[0])

    def get_minmax_temp(self) -> tuple:
        """Read device's minimum and maximum recorded temperatures
        
        Returns:
            int: minimum temperature (°C)
            int: maximum_temperature (°C)
        
        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """
        minmax_temp = self.read_registers(reg_addr = 288)[0]
        max_temp = minmax_temp  & 0xFF
        min_temp = minmax_temp >> 8
        return(min_temp, max_temp)

    def get_start_count(self):
        """Read device's start count
        
        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """
        result = self.read_registers(reg_addr = 289, nb_reg = 2)
        return(result[0] + ( result[1] << 8 ) )  

    def get_time_count(self):
        """Read device's time counter since last power-up
        
        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """
        result = self.read_registers(reg_addr = 291, nb_reg = 2)
        return(result[0] + ( result[1] << 8 ) )  

    def get_total_time_count(self):
        """Read slave device's total power-up time count
        
        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """
        result = self.read_registers(reg_addr = 293, nb_reg = 2)
        return(result[0] + ( result[1] << 8 ) )  

    def get_flash_count(self):
        """Read device's flash counter since last power-up
        
        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """
        result = self.read_registers(reg_addr = 295, nb_reg = 2)
        return(result[0] + ( result[1] << 8 ) )  

    def get_total_flash_count(self):
        """Read device's total flash counter
        
        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """
        result = self.read_registers(reg_addr = 297, nb_reg = 2)
        return(result[0] + ( result[1] << 8 ) )  

    def get_lamp_count(self):
        """Read device's lamp counter
        
        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """
        result = self.read_registers(reg_addr = 301, nb_reg = 2)
        return(result[0] + ( result[1] << 8 ) )  
    
    """ ------------------------------------------------------------------- """
    """ -                SxIP register write functions                    - """
    """ ------------------------------------------------------------------- """
    def set_voltage(self, voltage: int) -> None:
        """Set the regulation voltage (V)
        
        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """
        self.write_register(reg_addr = 18, value = 10 * voltage)

    def set_ftime(self, ftime: int) -> None:
        """Set the flash time (µs)
        
        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """
        self.write_register(reg_addr = 50, value = ftime)

    def set_mode(self, mode: str = 'ftime') -> None:
        """Set the device operating mode.
        
        Args:
            mode: 'ftime' -> Fixed ftime.
                  'burst' -> Ftime is according to the ftime table. 
                             Allows successive falshes without recharge.
                  'energy_reg' -> Ftime is according to the energy level table.
                                  Flash energy is regulated.
        
        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """
        # Check that the "mode" argument is in the expected list
        mode_dict = {'ftime': 0, 'bursts': 1, 'energy_reg' : 2}
        if mode not in mode_dict:
            raise ValueError(f"Unexpected value {mode} for mode parameter")
        self.write_register(reg_addr = 16, value = mode_dict[mode])

    def set_fan(self, mode: str = 'temp_regulated', level: int = 100) -> None:
        """Set the fan's operating parameters.

        Args:        
            mode: 'fixed level' -> Fan speed is fixed to the level
                  'temp_regulated' -> Fan speed is regulated according
                                      to both power and temperature
                                      with is the minium speed = level.
                  'power_regulated' -> Fan speed is regulated according to
                                       power with is the minium speed = level
            level: [0..100] %   

        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """
        if level > 100:
            raise ValueError("Level parameter > 100%")
        fan_mode_dict = {'fixed_level': 0,
                         'temp_regulated': 1, 'power_regulated' : 2}
        if mode not in fan_mode_dict:
            raise ValueError("Unexpected value for mode parameter")
        mode == fan_mode_dict[mode]
        self.write_register(reg_addr = 32, value = fan_mode_dict[mode])

    def set_health_param(self,
                         missed_flash_weight: int, 
                         health_treshold: int
                        ) -> None:
        """Set flash health supervision parameters.

        Args:
            missed_flash_weight: 
                When a flash is missed, health value is increased by this value
                When a flash is succeded, health value is decreased by 1
            health threshold: Health value that triggers an error.

        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """
        values = [missed_flash_weight, health_treshold]
        self.write_registers(reg_addr = 37, values = values)        #### A tester!!!

    def set_reset_on_failure(self, delay: int) -> None:
        """Set the reset on failure delay

        Args:        
            delay: Delay from failure detection to reset.
                   If 0, SxIP will not reset (remains locked in failure)

        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """
        self.write_register(reg_addr = 39, value = delay)

    def set_modbus_addr(self, address: int) -> None:
        """Set the modbus address.

        Args:          
            address: Modbus address [0..247]
        
        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """
        if address > 247:
            raise ValueError("Modbus address shall be in [0..247]")
        self.write_register(reg_addr = 48, value = address)

    def set_energy_level(self, 
                         prim_energy_level: int, 
                         alt_energy_level: int = 0
                        ) -> None:
        """Set the energy levels

        Args:          
            prim_energy_level: Energy level [0..16]
            alt_energy_level: Energy level [0..16]
        
        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """
        if prim_energy_level > 16:
            raise ValueError("Primary energy level shall be in [0..16]")
        if alt_energy_level > 16:
            raise ValueError("Alternate energy level shall be in [0..16]")
        value = prim_energy_level + (alt_energy_level << 8)
        self.write_register(reg_addr = 49, value = value)

    def set_trigger_delay(self, delay: int):
        """Set delay from trigger input edge to flash triggering.

        Args:          
            delay: delay from trigger input edge to flash triggering (µs)
            alt_energy_level: Energy level [0..16]
        
        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """       
        # Comment ça se passe pour les valeurs interdites ?????
        self.write_register(reg_addr = 51, value = delay)

    def set_sync_shift(self, slave:int, time_shift: int) -> None:
        # Comment ça se passe pour les négatifs ???
        """Set synchronisation signal relatively to the flash triggering.
        
        Args:          
            time_shift: time shift (µs)
            alt_energy_level: Energy level [0..16]
        
        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
                         or the device answers with an exception.
        """       
        self.write_register(reg_addr = 52, value = time_shift)
    
    def set_sync_pulse_time(self, duration: int) -> None:
        """Set synchronisation pulse duration 
        
        Args:          
            duration: synchronisation pulse width (µs)
        
        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
        """             
        self.write_register(reg_addr = 53, value = duration)

    def set_io5(self,
                polarity: str = 'high',
                buffer: str = 'schmitt',
                mode: str = 'not_used'
                ) -> None:
        """Configure IO5 (Dry input) functionnality.
        
        Args:   
            polarity: low  : active low, trigger on falling edges
                      high': active high, trigger on rising edges
            buffer: schmitt: optimized for 12V levels (Levels are 2.0V & 8.0V)
                        TTL: 5V compatible (levels are 1.6V & 4.0V)
            mode: not_used      : Has no effect
                  flash_trigger : Trigger the flash
                  alt_energy_selector: Turns to alternate energy level
        
        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
        """    
        pol_dict = {'low': 0, 'high': 1}
        buffer_dict = {'schmitt': 0, 'TTL': 1}
        mode_dict = {
            'not_used': 0, 'flash_trigger': 1, 'alt_energy_selector': 2}
        if polarity not in pol_dict:
            raise ValueError("Unexpected value for polarity parameter")
        if buffer not in buffer_dict:
            raise ValueError("Unexpected value for buffer parameter")
        if mode not in mode_dict:
            raise ValueError("Unexpected value for mode selection parameter")
        value = (pol_dict[polarity] + ( mode_dict[mode] << 1 ) + 
                 ( buffer_dict[buffer] << 5 ))
        self.write_register(reg_addr = 62, value = value)

    def set_io6(self,
                polarity: str = 'high',
                buffer: str = 'schmitt',
                mode: str = 'not_used'
                ) -> None:
        """Configure IO6 (TTL IO) functionnality.
        
        Args:   
            polarity: low  : active low, trigger on falling edges
                      high': active high, trigger on rising edges
            buffer: schmitt: Levels are 1.0V and 4.0V)
                        TTL: 3.3V compatible (levels are 0.8V and 2.0V)
            mode: not_used      : Has no effect
                  flash_trigger : Trigger the flash
                  alt_energy_selector: Turns to alternate energy level
                  low           : Force output to low state
                  high          : Force output to high state
                  sync_output   : Output the synchronisation signal
        
        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
        """   
        pol_dict = {'low': 0, 'high': 1}
        buffer_dict = {'schmitt': 0, 'TTL': 1}
        mode_dict = {'not_used': 0, 
                     'flash_trigger': 1, 
                     'alt_energy_selector': 2, 
                     'low': 8, 
                     'high': 9, 
                     'sync_output': 10}
        if polarity not in pol_dict:
            raise ValueError("Unexpected value for polarity parameter")
        if buffer not in buffer_dict:
            raise ValueError("Unexpected value for buffer parameter")
        if mode not in mode_dict:
            raise ValueError("Unexpected value for mode selection parameter")
        value = (pol_dict[polarity] + ( mode_dict[mode] << 1 ) + 
                 ( buffer_dict[buffer] << 5 ))
        self.write_register(reg_addr = 63, value = value)

    def set_io7(self,
        polarity: str = 'high',
        mode: str = 'not_used'
        ) -> None:
        """Configure IO7 (Isolated output) functionnality.
        
        Args:   
            polarity: low  : active low
                      high': active high            ### TOBE COMPLETED
            mode: not_used      : Has no effect
                  open          : Force output to open state
                  closed        : Force output to closed state
                  sync_output   : Output the synchronisation signal
        
        Raises:
            ValueError: One of the arguments is not as expected.
            ModbusError: A communication error occurs
        """   
        pol_dict = {'low': 0, 'high': 1}
        mode_dict = {'not_used': 0, 'open': 8, 'closed': 9, 'sync_output': 10}
        if polarity not in pol_dict:
            raise ValueError("Unexpected value for polarity parameter")
        if mode not in mode_dict:
            raise ValueError("Unexpected value for mode selection parameter")
        value = pol_dict[polarity] + ( mode_dict[mode] << 1 )
        self.write_register(reg_addr = 63, value = value)

if __name__ == "__main__":
    print("sxip test routine")
    def terminal_output(**kwargs):
        '''This function output everything passed as key arguments to the terminal'''
        for k, v in kwargs.items():
            print(f"{k}: {v}")

    modbus_link = modbus.Modbus(port = "COM3")
    flash_device = Sxip(modbus_link = modbus_link, modbus_addr = 1)
    #flash_device.modbus_addr = 1
    try: 
        print(flash_device.read_registers(reg_addr = 1))
        print(f'Serial: {flash_device.get_serial()}')
        year, week = flash_device.get_date()
        print(f'Year: {year}, week: {week}')
        print(f'Ftime: {flash_device.get_ftime()}µs')
        print(f'Input voltage: {flash_device.get_input_voltage()}V')
        print(f'Temperature: {flash_device.get_temperature()}°C')
        print(f'last flash energy: {flash_device.get_last_flash_energy()}J')
        print(f'Flash error count: {flash_device.get_flash_error_count()}')
        print(f'Flash health: {flash_device.get_flash_healt()}')
        min_temp, max_temp = flash_device.get_minmax_temp()
        print(f'Minimum temperature: {min_temp}°C')
        print(f'Maximum temperature: {max_temp}°C')
        print(f'Start count: {flash_device.get_start_count()}')
        print(f'Time count: {flash_device.get_time_count()}minutes')
        print(f'Total time: {flash_device.get_total_time_count()}minutes')
        print(f'Flash count: {flash_device.get_flash_count()}')
        print(f'Total flash count: {flash_device.get_total_flash_count()}')
        print(f'Lamp count: {flash_device.get_lamp_count()}')
        print (f'io_state: {bin(flash_device.get_io_state())}')
        io_dict = flash_device.get_io_state(output = 'dict')
        print (f'io_state: {io_dict}')
        state_dict = flash_device.get_state()
        print (f'state: {state_dict}')
        print (f'config_inputs: {flash_device.get_config_inputs()}')
        flash_device.set_io6(polarity = 'low', mode = 'alt_energy_selector', buffer = 'TTL')
        flash_device.save_settings()
        flash_device.modbus_link.register_feedback_handler(terminal_output)
        flash_device.set_energy_level(prim_energy_level = 9, alt_energy_level = 8)
    except ModbusError as exc:
        print(f'Modbus error: {exc}')
    modbus_link.close()
    #flash_device.execute_cmd('RESET')
