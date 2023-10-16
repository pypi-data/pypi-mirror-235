from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PluginCls:
	"""Plugin commands group definition. 6 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("plugin", core, parent)

	@property
	def variable(self):
		"""variable commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_variable'):
			from .Variable import VariableCls
			self._variable = VariableCls(self._core, self._cmd_group)
		return self._variable

	def get_name(self) -> str:
		"""SCPI: SCENario:PDW:PLUGin:NAME \n
		Snippet: value: str = driver.scenario.pdw.plugin.get_name() \n
		Selects and loads a reporting template. This template must exist in the 'Plugin' library. To query a list of available
		plugins, use the command method RsPulseSeq.Plugin.catalog. \n
			:return: name: string
		"""
		response = self._core.io.query_str('SCENario:PDW:PLUGin:NAME?')
		return trim_str_response(response)

	def set_name(self, name: str) -> None:
		"""SCPI: SCENario:PDW:PLUGin:NAME \n
		Snippet: driver.scenario.pdw.plugin.set_name(name = 'abc') \n
		Selects and loads a reporting template. This template must exist in the 'Plugin' library. To query a list of available
		plugins, use the command method RsPulseSeq.Plugin.catalog. \n
			:param name: string
		"""
		param = Conversions.value_to_quoted_str(name)
		self._core.io.write(f'SCENario:PDW:PLUGin:NAME {param}')

	def clone(self) -> 'PluginCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PluginCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
