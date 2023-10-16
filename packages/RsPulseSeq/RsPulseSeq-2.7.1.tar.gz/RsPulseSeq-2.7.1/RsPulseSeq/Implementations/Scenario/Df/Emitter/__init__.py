from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class EmitterCls:
	"""Emitter commands group definition. 14 total commands, 2 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("emitter", core, parent)

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import ModeCls
			self._mode = ModeCls(self._core, self._cmd_group)
		return self._mode

	@property
	def state(self):
		"""state commands group. 1 Sub-classes, 8 commands."""
		if not hasattr(self, '_state'):
			from .State import StateCls
			self._state = StateCls(self._core, self._cmd_group)
		return self._state

	def get_enable(self) -> bool:
		"""SCPI: SCENario:DF:EMITter:ENABle \n
		Snippet: value: bool = driver.scenario.df.emitter.get_enable() \n
		In a map-based sceanrio, enable selected item for calculation. \n
			:return: enable: ON| OFF| 1| 0
		"""
		response = self._core.io.query_str('SCENario:DF:EMITter:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: SCENario:DF:EMITter:ENABle \n
		Snippet: driver.scenario.df.emitter.set_enable(enable = False) \n
		In a map-based sceanrio, enable selected item for calculation. \n
			:param enable: ON| OFF| 1| 0
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'SCENario:DF:EMITter:ENABle {param}')

	def get_value(self) -> str:
		"""SCPI: SCENario:DF:EMITter \n
		Snippet: value: str = driver.scenario.df.emitter.get_value() \n
		Assigns an existing emitter or an existing waveform, see method RsPulseSeq.Waveform.catalog and method RsPulseSeq.Emitter.
		catalog. \n
			:return: emitter: string
		"""
		response = self._core.io.query_str('SCENario:DF:EMITter?')
		return trim_str_response(response)

	def set_value(self, emitter: str) -> None:
		"""SCPI: SCENario:DF:EMITter \n
		Snippet: driver.scenario.df.emitter.set_value(emitter = 'abc') \n
		Assigns an existing emitter or an existing waveform, see method RsPulseSeq.Waveform.catalog and method RsPulseSeq.Emitter.
		catalog. \n
			:param emitter: string
		"""
		param = Conversions.value_to_quoted_str(emitter)
		self._core.io.write(f'SCENario:DF:EMITter {param}')

	def clone(self) -> 'EmitterCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = EmitterCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
