from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AssignmentCls:
	"""Assignment commands group definition. 35 total commands, 5 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("assignment", core, parent)

	@property
	def destination(self):
		"""destination commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_destination'):
			from .Destination import DestinationCls
			self._destination = DestinationCls(self._core, self._cmd_group)
		return self._destination

	@property
	def antennas(self):
		"""antennas commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_antennas'):
			from .Antennas import AntennasCls
			self._antennas = AntennasCls(self._core, self._cmd_group)
		return self._antennas

	@property
	def emitters(self):
		"""emitters commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_emitters'):
			from .Emitters import EmittersCls
			self._emitters = EmittersCls(self._core, self._cmd_group)
		return self._emitters

	@property
	def generator(self):
		"""generator commands group. 1 Sub-classes, 3 commands."""
		if not hasattr(self, '_generator'):
			from .Generator import GeneratorCls
			self._generator = GeneratorCls(self._core, self._cmd_group)
		return self._generator

	@property
	def group(self):
		"""group commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_group'):
			from .Group import GroupCls
			self._group = GroupCls(self._core, self._cmd_group)
		return self._group

	def clone(self) -> 'AssignmentCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AssignmentCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
