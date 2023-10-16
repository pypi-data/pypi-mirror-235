from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EightPskCls:
	"""EightPsk commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("eightPsk", core, parent)

	def get_symbol_rate(self) -> float:
		"""SCPI: PULSe:MOP:8PSK:SRATe \n
		Snippet: value: float = driver.pulse.mop.eightPsk.get_symbol_rate() \n
		Sets the symbol rate of the modulated signal. \n
			:return: srate: float Range: 1 to 1e+09
		"""
		response = self._core.io.query_str('PULSe:MOP:8PSK:SRATe?')
		return Conversions.str_to_float(response)

	def set_symbol_rate(self, srate: float) -> None:
		"""SCPI: PULSe:MOP:8PSK:SRATe \n
		Snippet: driver.pulse.mop.eightPsk.set_symbol_rate(srate = 1.0) \n
		Sets the symbol rate of the modulated signal. \n
			:param srate: float Range: 1 to 1e+09
		"""
		param = Conversions.decimal_value_to_str(srate)
		self._core.io.write(f'PULSe:MOP:8PSK:SRATe {param}')
