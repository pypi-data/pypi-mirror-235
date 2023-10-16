from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DirectionCls:
	"""Direction commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("direction", core, parent)

	def get_pitch(self) -> float:
		"""SCPI: SCENario:LOCalized:DIRection:PITCh \n
		Snippet: value: float = driver.scenario.localized.direction.get_pitch() \n
		Sets the pitch. \n
			:return: pitch: float Range: -90 to 90, Unit: grad
		"""
		response = self._core.io.query_str('SCENario:LOCalized:DIRection:PITCh?')
		return Conversions.str_to_float(response)

	def set_pitch(self, pitch: float) -> None:
		"""SCPI: SCENario:LOCalized:DIRection:PITCh \n
		Snippet: driver.scenario.localized.direction.set_pitch(pitch = 1.0) \n
		Sets the pitch. \n
			:param pitch: float Range: -90 to 90, Unit: grad
		"""
		param = Conversions.decimal_value_to_str(pitch)
		self._core.io.write(f'SCENario:LOCalized:DIRection:PITCh {param}')

	def get_roll(self) -> float:
		"""SCPI: SCENario:LOCalized:DIRection:ROLL \n
		Snippet: value: float = driver.scenario.localized.direction.get_roll() \n
		Sets the roll. \n
			:return: roll: float Range: 0 to 360
		"""
		response = self._core.io.query_str('SCENario:LOCalized:DIRection:ROLL?')
		return Conversions.str_to_float(response)

	def set_roll(self, roll: float) -> None:
		"""SCPI: SCENario:LOCalized:DIRection:ROLL \n
		Snippet: driver.scenario.localized.direction.set_roll(roll = 1.0) \n
		Sets the roll. \n
			:param roll: float Range: 0 to 360
		"""
		param = Conversions.decimal_value_to_str(roll)
		self._core.io.write(f'SCENario:LOCalized:DIRection:ROLL {param}')

	def get_track(self) -> bool:
		"""SCPI: SCENario:LOCalized:DIRection:TRACk \n
		Snippet: value: bool = driver.scenario.localized.direction.get_track() \n
		Turns the antenna in the direction of the receiver. \n
			:return: track: ON| OFF| 1| 0
		"""
		response = self._core.io.query_str('SCENario:LOCalized:DIRection:TRACk?')
		return Conversions.str_to_bool(response)

	def set_track(self, track: bool) -> None:
		"""SCPI: SCENario:LOCalized:DIRection:TRACk \n
		Snippet: driver.scenario.localized.direction.set_track(track = False) \n
		Turns the antenna in the direction of the receiver. \n
			:param track: ON| OFF| 1| 0
		"""
		param = Conversions.bool_to_str(track)
		self._core.io.write(f'SCENario:LOCalized:DIRection:TRACk {param}')

	def get_yaw(self) -> float:
		"""SCPI: SCENario:LOCalized:DIRection:YAW \n
		Snippet: value: float = driver.scenario.localized.direction.get_yaw() \n
		Sets the yaw. \n
			:return: yaw: float Range: 0 to 360
		"""
		response = self._core.io.query_str('SCENario:LOCalized:DIRection:YAW?')
		return Conversions.str_to_float(response)

	def set_yaw(self, yaw: float) -> None:
		"""SCPI: SCENario:LOCalized:DIRection:YAW \n
		Snippet: driver.scenario.localized.direction.set_yaw(yaw = 1.0) \n
		Sets the yaw. \n
			:param yaw: float Range: 0 to 360
		"""
		param = Conversions.decimal_value_to_str(yaw)
		self._core.io.write(f'SCENario:LOCalized:DIRection:YAW {param}')
