from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DurationCls:
	"""Duration commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("duration", core, parent)

	def get_auto(self) -> float:
		"""SCPI: SCENario:OUTPut:DURation:AUTO \n
		Snippet: value: float = driver.scenario.output.duration.get_auto() \n
		Requires SCENario:OUTPut:DURation:MODE AUTO. Queries the value of the automatically determined signal duration. \n
			:return: auto: float Range: 1e-06 to 1.8432e+06
		"""
		response = self._core.io.query_str('SCENario:OUTPut:DURation:AUTO?')
		return Conversions.str_to_float(response)

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.AutoManualMode:
		"""SCPI: SCENario:OUTPut:DURation:MODE \n
		Snippet: value: enums.AutoManualMode = driver.scenario.output.duration.get_mode() \n
		Sets how the waveform duration is defined. \n
			:return: mode: AUTO| MANual AUTO Sets the simulation time to maximum of sequence, scan or movement duration. MANual Sets the simulation time to a fixed value.
		"""
		response = self._core.io.query_str('SCENario:OUTPut:DURation:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.AutoManualMode)

	def set_mode(self, mode: enums.AutoManualMode) -> None:
		"""SCPI: SCENario:OUTPut:DURation:MODE \n
		Snippet: driver.scenario.output.duration.set_mode(mode = enums.AutoManualMode.AUTO) \n
		Sets how the waveform duration is defined. \n
			:param mode: AUTO| MANual AUTO Sets the simulation time to maximum of sequence, scan or movement duration. MANual Sets the simulation time to a fixed value.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.AutoManualMode)
		self._core.io.write(f'SCENario:OUTPut:DURation:MODE {param}')

	def get_time(self) -> float:
		"""SCPI: SCENario:OUTPut:DURation:TIME \n
		Snippet: value: float = driver.scenario.output.duration.get_time() \n
		Sets the duration of the generated waveform. \n
			:return: time: float Range: 1e-06 to 1.8432e+06 Simulation time longer than 7200s requires R&S SMW with firmware version 5.xx.xxx and higher. To query the installed firmware version of the selected instrument, use the command method RsPulseSeq.Instrument.firmware.
		"""
		response = self._core.io.query_str('SCENario:OUTPut:DURation:TIME?')
		return Conversions.str_to_float(response)

	def set_time(self, time: float) -> None:
		"""SCPI: SCENario:OUTPut:DURation:TIME \n
		Snippet: driver.scenario.output.duration.set_time(time = 1.0) \n
		Sets the duration of the generated waveform. \n
			:param time: float Range: 1e-06 to 1.8432e+06 Simulation time longer than 7200s requires R&S SMW with firmware version 5.xx.xxx and higher. To query the installed firmware version of the selected instrument, use the command method RsPulseSeq.Instrument.firmware.
		"""
		param = Conversions.decimal_value_to_str(time)
		self._core.io.write(f'SCENario:OUTPut:DURation:TIME {param}')
