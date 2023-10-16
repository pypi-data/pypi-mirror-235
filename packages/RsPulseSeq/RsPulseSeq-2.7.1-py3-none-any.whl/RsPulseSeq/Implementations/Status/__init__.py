from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StatusCls:
	"""Status commands group definition. 10 total commands, 2 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("status", core, parent)

	@property
	def operation(self):
		"""operation commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_operation'):
			from .Operation import OperationCls
			self._operation = OperationCls(self._core, self._cmd_group)
		return self._operation

	@property
	def quesation(self):
		"""quesation commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_quesation'):
			from .Quesation import QuesationCls
			self._quesation = QuesationCls(self._core, self._cmd_group)
		return self._quesation

	def clone(self) -> 'StatusCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = StatusCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
