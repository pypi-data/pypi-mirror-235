from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MchgCls:
	"""Mchg commands group definition. 8 total commands, 1 Subgroups, 7 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mchg", core, parent)

	@property
	def add(self):
		"""add commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_add'):
			from .Add import AddCls
			self._add = AddCls(self._core, self._cmd_group)
		return self._add

	def clear(self) -> None:
		"""SCPI: SCENario:LOCalized:MCHG:CLEar \n
		Snippet: driver.scenario.localized.mchg.clear() \n
		Removes all defined modes. \n
		"""
		self._core.io.write(f'SCENario:LOCalized:MCHG:CLEar')

	def clear_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SCENario:LOCalized:MCHG:CLEar \n
		Snippet: driver.scenario.localized.mchg.clear_with_opc() \n
		Removes all defined modes. \n
		Same as clear, but waits for the operation to complete before continuing further. Use the RsPulseSeq.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SCENario:LOCalized:MCHG:CLEar', opc_timeout_ms)

	def get_count(self) -> float:
		"""SCPI: SCENario:LOCalized:MCHG:COUNt \n
		Snippet: value: float = driver.scenario.localized.mchg.get_count() \n
		Queries the number of existing items. \n
			:return: count: integer
		"""
		response = self._core.io.query_str('SCENario:LOCalized:MCHG:COUNt?')
		return Conversions.str_to_float(response)

	def delete(self, delete: float) -> None:
		"""SCPI: SCENario:LOCalized:MCHG:DELete \n
		Snippet: driver.scenario.localized.mchg.delete(delete = 1.0) \n
		Deletes the particular item. \n
			:param delete: float
		"""
		param = Conversions.decimal_value_to_str(delete)
		self._core.io.write(f'SCENario:LOCalized:MCHG:DELete {param}')

	def get_select(self) -> float:
		"""SCPI: SCENario:LOCalized:MCHG:SELect \n
		Snippet: value: float = driver.scenario.localized.mchg.get_select() \n
		Selects the item to which the subsequent commands apply. \n
			:return: select: float Item number within the range 1 to ...:COUNt. For example, method RsPulseSeq.Sequence.Item.count. Range: 1 to 4096
		"""
		response = self._core.io.query_str('SCENario:LOCalized:MCHG:SELect?')
		return Conversions.str_to_float(response)

	def set_select(self, select: float) -> None:
		"""SCPI: SCENario:LOCalized:MCHG:SELect \n
		Snippet: driver.scenario.localized.mchg.set_select(select = 1.0) \n
		Selects the item to which the subsequent commands apply. \n
			:param select: float Item number within the range 1 to ...:COUNt. For example, method RsPulseSeq.Sequence.Item.count. Range: 1 to 4096
		"""
		param = Conversions.decimal_value_to_str(select)
		self._core.io.write(f'SCENario:LOCalized:MCHG:SELect {param}')

	def get_start(self) -> float:
		"""SCPI: SCENario:LOCalized:MCHG:STARt \n
		Snippet: value: float = driver.scenario.localized.mchg.get_start() \n
		Sets the start and end time per mode entry. \n
			:return: start: No help available
		"""
		response = self._core.io.query_str('SCENario:LOCalized:MCHG:STARt?')
		return Conversions.str_to_float(response)

	def set_start(self, start: float) -> None:
		"""SCPI: SCENario:LOCalized:MCHG:STARt \n
		Snippet: driver.scenario.localized.mchg.set_start(start = 1.0) \n
		Sets the start and end time per mode entry. \n
			:param start: float
		"""
		param = Conversions.decimal_value_to_str(start)
		self._core.io.write(f'SCENario:LOCalized:MCHG:STARt {param}')

	def get_state(self) -> bool:
		"""SCPI: SCENario:LOCalized:MCHG:STATe \n
		Snippet: value: bool = driver.scenario.localized.mchg.get_state() \n
		Enables mode changes. \n
			:return: state: ON| OFF| 1| 0
		"""
		response = self._core.io.query_str('SCENario:LOCalized:MCHG:STATe?')
		return Conversions.str_to_bool(response)

	def set_state(self, state: bool) -> None:
		"""SCPI: SCENario:LOCalized:MCHG:STATe \n
		Snippet: driver.scenario.localized.mchg.set_state(state = False) \n
		Enables mode changes. \n
			:param state: ON| OFF| 1| 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SCENario:LOCalized:MCHG:STATe {param}')

	def get_stop(self) -> float:
		"""SCPI: SCENario:LOCalized:MCHG:STOP \n
		Snippet: value: float = driver.scenario.localized.mchg.get_stop() \n
		Sets the start and end time per mode entry. \n
			:return: stop: float
		"""
		response = self._core.io.query_str('SCENario:LOCalized:MCHG:STOP?')
		return Conversions.str_to_float(response)

	def set_stop(self, stop: float) -> None:
		"""SCPI: SCENario:LOCalized:MCHG:STOP \n
		Snippet: driver.scenario.localized.mchg.set_stop(stop = 1.0) \n
		Sets the start and end time per mode entry. \n
			:param stop: float
		"""
		param = Conversions.decimal_value_to_str(stop)
		self._core.io.write(f'SCENario:LOCalized:MCHG:STOP {param}')

	def clone(self) -> 'MchgCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MchgCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
