from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ForwardCls:
	"""Forward commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("forward", core, parent)

	def set(self) -> None:
		"""SCPI: IMPort:VIEW:MOVE:FORWard \n
		Snippet: driver.importPy.view.move.forward.set() \n
		Goes to the first/next/previous/last page. \n
		"""
		self._core.io.write(f'IMPort:VIEW:MOVE:FORWard')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: IMPort:VIEW:MOVE:FORWard \n
		Snippet: driver.importPy.view.move.forward.set_with_opc() \n
		Goes to the first/next/previous/last page. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsPulseSeq.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'IMPort:VIEW:MOVE:FORWard', opc_timeout_ms)
