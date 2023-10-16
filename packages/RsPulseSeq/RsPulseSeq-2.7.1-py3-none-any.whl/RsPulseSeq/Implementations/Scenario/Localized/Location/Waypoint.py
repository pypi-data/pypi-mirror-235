from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class WaypointCls:
	"""Waypoint commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("waypoint", core, parent)

	def clear(self) -> None:
		"""SCPI: SCENario:LOCalized:LOCation:WAYPoint:CLEar \n
		Snippet: driver.scenario.localized.location.waypoint.clear() \n
		Discards the selected file. \n
		"""
		self._core.io.write(f'SCENario:LOCalized:LOCation:WAYPoint:CLEar')

	def clear_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SCENario:LOCalized:LOCation:WAYPoint:CLEar \n
		Snippet: driver.scenario.localized.location.waypoint.clear_with_opc() \n
		Discards the selected file. \n
		Same as clear, but waits for the operation to complete before continuing further. Use the RsPulseSeq.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SCENario:LOCalized:LOCation:WAYPoint:CLEar', opc_timeout_ms)
