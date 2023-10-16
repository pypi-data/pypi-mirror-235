from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class GetCls:
	"""Get commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("get", core, parent)

	def get_duration(self) -> float:
		"""SCPI: WAVeform:VIEW:GET:DURation \n
		Snippet: value: float = driver.waveform.view.get.get_duration() \n
		No command help available \n
			:return: duration: No help available
		"""
		response = self._core.io.query_str('WAVeform:VIEW:GET:DURation?')
		return Conversions.str_to_float(response)
