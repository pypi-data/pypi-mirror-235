from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class LevelCls:
	"""Level commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("level", core, parent)

	def get_reference(self) -> float:
		"""SCPI: WAVeform:LEVel:REFerence \n
		Snippet: value: float = driver.waveform.level.get_reference() \n
		Queries the reference level. \n
			:return: reference: float Range: 0 to 100
		"""
		response = self._core.io.query_str('WAVeform:LEVel:REFerence?')
		return Conversions.str_to_float(response)

	def set_reference(self, reference: float) -> None:
		"""SCPI: WAVeform:LEVel:REFerence \n
		Snippet: driver.waveform.level.set_reference(reference = 1.0) \n
		Queries the reference level. \n
			:param reference: float Range: 0 to 100
		"""
		param = Conversions.decimal_value_to_str(reference)
		self._core.io.write(f'WAVeform:LEVel:REFerence {param}')
