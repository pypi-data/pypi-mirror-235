from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RfAlignCls:
	"""RfAlign commands group definition. 3 total commands, 1 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rfAlign", core, parent)

	@property
	def importPy(self):
		"""importPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_importPy'):
			from .ImportPy import ImportPyCls
			self._importPy = ImportPyCls(self._core, self._cmd_group)
		return self._importPy

	def get_instrument(self) -> str:
		"""SCPI: SETup:RFALign:INSTrument \n
		Snippet: value: str = driver.setup.rfAlign.get_instrument() \n
		No command help available \n
			:return: instrument: No help available
		"""
		response = self._core.io.query_str('SETup:RFALign:INSTrument?')
		return trim_str_response(response)

	def set_instrument(self, instrument: str) -> None:
		"""SCPI: SETup:RFALign:INSTrument \n
		Snippet: driver.setup.rfAlign.set_instrument(instrument = 'abc') \n
		No command help available \n
			:param instrument: No help available
		"""
		param = Conversions.value_to_quoted_str(instrument)
		self._core.io.write(f'SETup:RFALign:INSTrument {param}')

	def get_setup(self) -> str:
		"""SCPI: SETup:RFALign:SETup \n
		Snippet: value: str = driver.setup.rfAlign.get_setup() \n
		No command help available \n
			:return: setup: No help available
		"""
		response = self._core.io.query_str('SETup:RFALign:SETup?')
		return trim_str_response(response)

	def set_setup(self, setup: str) -> None:
		"""SCPI: SETup:RFALign:SETup \n
		Snippet: driver.setup.rfAlign.set_setup(setup = 'abc') \n
		No command help available \n
			:param setup: No help available
		"""
		param = Conversions.value_to_quoted_str(setup)
		self._core.io.write(f'SETup:RFALign:SETup {param}')

	def clone(self) -> 'RfAlignCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RfAlignCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
