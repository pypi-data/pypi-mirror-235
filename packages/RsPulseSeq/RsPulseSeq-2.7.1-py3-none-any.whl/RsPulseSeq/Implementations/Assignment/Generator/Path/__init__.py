from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from .....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PathCls:
	"""Path commands group definition. 12 total commands, 2 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("path", core, parent)

	@property
	def antenna(self):
		"""antenna commands group. 1 Sub-classes, 4 commands."""
		if not hasattr(self, '_antenna'):
			from .Antenna import AntennaCls
			self._antenna = AntennaCls(self._core, self._cmd_group)
		return self._antenna

	@property
	def emitter(self):
		"""emitter commands group. 1 Sub-classes, 4 commands."""
		if not hasattr(self, '_emitter'):
			from .Emitter import EmitterCls
			self._emitter = EmitterCls(self._core, self._cmd_group)
		return self._emitter

	def get_list_py(self) -> str:
		"""SCPI: ASSignment:GENerator:PATH:LIST \n
		Snippet: value: str = driver.assignment.generator.path.get_list_py() \n
		Queries the available paths. \n
			:return: list_py: 'Path#1','Path#2',... List of available paths.
		"""
		response = self._core.io.query_str('ASSignment:GENerator:PATH:LIST?')
		return trim_str_response(response)

	def get_select(self) -> str:
		"""SCPI: ASSignment:GENerator:PATH:SELect \n
		Snippet: value: str = driver.assignment.generator.path.get_select() \n
		Selects the element to which the subsequent commands apply. \n
			:return: select: string Available element as queried with the corresponding ...:LIST command. For example, method RsPulseSeq.Assignment.Generator.Path.Antenna.listPy
		"""
		response = self._core.io.query_str('ASSignment:GENerator:PATH:SELect?')
		return trim_str_response(response)

	def set_select(self, select: str) -> None:
		"""SCPI: ASSignment:GENerator:PATH:SELect \n
		Snippet: driver.assignment.generator.path.set_select(select = 'abc') \n
		Selects the element to which the subsequent commands apply. \n
			:param select: string Available element as queried with the corresponding ...:LIST command. For example, method RsPulseSeq.Assignment.Generator.Path.Antenna.listPy
		"""
		param = Conversions.value_to_quoted_str(select)
		self._core.io.write(f'ASSignment:GENerator:PATH:SELect {param}')

	def clone(self) -> 'PathCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PathCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
