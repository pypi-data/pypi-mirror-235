from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class IlCacheCls:
	"""IlCache commands group definition. 2 total commands, 1 Subgroups, 0 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ilCache", core, parent)

	@property
	def volatile(self):
		"""volatile commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_volatile'):
			from .Volatile import VolatileCls
			self._volatile = VolatileCls(self._core, self._cmd_group)
		return self._volatile

	def clone(self) -> 'IlCacheCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = IlCacheCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
