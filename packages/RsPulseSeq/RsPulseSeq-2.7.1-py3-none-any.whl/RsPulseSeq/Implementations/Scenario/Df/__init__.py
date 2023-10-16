from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DfCls:
	"""Df commands group definition. 144 total commands, 14 Subgroups, 14 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("df", core, parent)

	@property
	def interleaving(self):
		"""interleaving commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_interleaving'):
			from .Interleaving import InterleavingCls
			self._interleaving = InterleavingCls(self._core, self._cmd_group)
		return self._interleaving

	@property
	def add(self):
		"""add commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_add'):
			from .Add import AddCls
			self._add = AddCls(self._core, self._cmd_group)
		return self._add

	@property
	def direction(self):
		"""direction commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_direction'):
			from .Direction import DirectionCls
			self._direction = DirectionCls(self._core, self._cmd_group)
		return self._direction

	@property
	def emitter(self):
		"""emitter commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_emitter'):
			from .Emitter import EmitterCls
			self._emitter = EmitterCls(self._core, self._cmd_group)
		return self._emitter

	@property
	def group(self):
		"""group commands group. 1 Sub-classes, 7 commands."""
		if not hasattr(self, '_group'):
			from .Group import GroupCls
			self._group = GroupCls(self._core, self._cmd_group)
		return self._group

	@property
	def location(self):
		"""location commands group. 3 Sub-classes, 9 commands."""
		if not hasattr(self, '_location'):
			from .Location import LocationCls
			self._location = LocationCls(self._core, self._cmd_group)
		return self._location

	@property
	def maps(self):
		"""maps commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_maps'):
			from .Maps import MapsCls
			self._maps = MapsCls(self._core, self._cmd_group)
		return self._maps

	@property
	def marker(self):
		"""marker commands group. 1 Sub-classes, 8 commands."""
		if not hasattr(self, '_marker'):
			from .Marker import MarkerCls
			self._marker = MarkerCls(self._core, self._cmd_group)
		return self._marker

	@property
	def mchg(self):
		"""mchg commands group. 1 Sub-classes, 7 commands."""
		if not hasattr(self, '_mchg'):
			from .Mchg import MchgCls
			self._mchg = MchgCls(self._core, self._cmd_group)
		return self._mchg

	@property
	def movement(self):
		"""movement commands group. 2 Sub-classes, 23 commands."""
		if not hasattr(self, '_movement'):
			from .Movement import MovementCls
			self._movement = MovementCls(self._core, self._cmd_group)
		return self._movement

	@property
	def receiver(self):
		"""receiver commands group. 2 Sub-classes, 4 commands."""
		if not hasattr(self, '_receiver'):
			from .Receiver import ReceiverCls
			self._receiver = ReceiverCls(self._core, self._cmd_group)
		return self._receiver

	@property
	def subitem(self):
		"""subitem commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_subitem'):
			from .Subitem import SubitemCls
			self._subitem = SubitemCls(self._core, self._cmd_group)
		return self._subitem

	@property
	def synchronize(self):
		"""synchronize commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_synchronize'):
			from .Synchronize import SynchronizeCls
			self._synchronize = SynchronizeCls(self._core, self._cmd_group)
		return self._synchronize

	@property
	def waveform(self):
		"""waveform commands group. 0 Sub-classes, 6 commands."""
		if not hasattr(self, '_waveform'):
			from .Waveform import WaveformCls
			self._waveform = WaveformCls(self._core, self._cmd_group)
		return self._waveform

	def get_alias(self) -> str:
		"""SCPI: SCENario:DF:ALIas \n
		Snippet: value: str = driver.scenario.df.get_alias() \n
		Enters an alias name. \n
			:return: alias: string
		"""
		response = self._core.io.query_str('SCENario:DF:ALIas?')
		return trim_str_response(response)

	def set_alias(self, alias: str) -> None:
		"""SCPI: SCENario:DF:ALIas \n
		Snippet: driver.scenario.df.set_alias(alias = 'abc') \n
		Enters an alias name. \n
			:param alias: string
		"""
		param = Conversions.value_to_quoted_str(alias)
		self._core.io.write(f'SCENario:DF:ALIas {param}')

	def clear(self) -> None:
		"""SCPI: SCENario:DF:CLEar \n
		Snippet: driver.scenario.df.clear() \n
		Deletes all items from the list or the table. \n
		"""
		self._core.io.write(f'SCENario:DF:CLEar')

	def clear_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: SCENario:DF:CLEar \n
		Snippet: driver.scenario.df.clear_with_opc() \n
		Deletes all items from the list or the table. \n
		Same as clear, but waits for the operation to complete before continuing further. Use the RsPulseSeq.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SCENario:DF:CLEar', opc_timeout_ms)

	def get_current(self) -> float:
		"""SCPI: SCENario:DF:CURRent \n
		Snippet: value: float = driver.scenario.df.get_current() \n
		Sets the sequence/emitter that is used by the scenario. \n
			:return: current: float Number of the sequence/emitter in the list with multiple sequences
		"""
		response = self._core.io.query_str('SCENario:DF:CURRent?')
		return Conversions.str_to_float(response)

	def set_current(self, current: float) -> None:
		"""SCPI: SCENario:DF:CURRent \n
		Snippet: driver.scenario.df.set_current(current = 1.0) \n
		Sets the sequence/emitter that is used by the scenario. \n
			:param current: float Number of the sequence/emitter in the list with multiple sequences
		"""
		param = Conversions.decimal_value_to_str(current)
		self._core.io.write(f'SCENario:DF:CURRent {param}')

	def delete(self, delete: float) -> None:
		"""SCPI: SCENario:DF:DELete \n
		Snippet: driver.scenario.df.delete(delete = 1.0) \n
		Deletes the particular item. \n
			:param delete: float
		"""
		param = Conversions.decimal_value_to_str(delete)
		self._core.io.write(f'SCENario:DF:DELete {param}')

	def get_distance(self) -> float:
		"""SCPI: SCENario:DF:DISTance \n
		Snippet: value: float = driver.scenario.df.get_distance() \n
		Sets the distance to the receiver. \n
			:return: distance: float Range: 0 to 1e+09, Unit: m
		"""
		response = self._core.io.query_str('SCENario:DF:DISTance?')
		return Conversions.str_to_float(response)

	def set_distance(self, distance: float) -> None:
		"""SCPI: SCENario:DF:DISTance \n
		Snippet: driver.scenario.df.set_distance(distance = 1.0) \n
		Sets the distance to the receiver. \n
			:param distance: float Range: 0 to 1e+09, Unit: m
		"""
		param = Conversions.decimal_value_to_str(distance)
		self._core.io.write(f'SCENario:DF:DISTance {param}')

	def get_enable(self) -> bool:
		"""SCPI: SCENario:DF:ENABle \n
		Snippet: value: bool = driver.scenario.df.get_enable() \n
		If enabled, the PDW list is included in the output file. \n
			:return: enable: ON| OFF| 1| 0
		"""
		response = self._core.io.query_str('SCENario:DF:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: SCENario:DF:ENABle \n
		Snippet: driver.scenario.df.set_enable(enable = False) \n
		If enabled, the PDW list is included in the output file. \n
			:param enable: ON| OFF| 1| 0
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'SCENario:DF:ENABle {param}')

	def get_frequency(self) -> float:
		"""SCPI: SCENario:DF:FREQuency \n
		Snippet: value: float = driver.scenario.df.get_frequency() \n
		Sets the frequency for the selected emitter. \n
			:return: frequency: No help available
		"""
		response = self._core.io.query_str('SCENario:DF:FREQuency?')
		return Conversions.str_to_float(response)

	def get_ldelay(self) -> float:
		"""SCPI: SCENario:DF:LDELay \n
		Snippet: value: float = driver.scenario.df.get_ldelay() \n
		If interleaving is enabled, shifts the processing of the selected PDW list in time. \n
			:return: ldelay: float Range: -1e+09 to 1e+09
		"""
		response = self._core.io.query_str('SCENario:DF:LDELay?')
		return Conversions.str_to_float(response)

	def set_ldelay(self, ldelay: float) -> None:
		"""SCPI: SCENario:DF:LDELay \n
		Snippet: driver.scenario.df.set_ldelay(ldelay = 1.0) \n
		If interleaving is enabled, shifts the processing of the selected PDW list in time. \n
			:param ldelay: float Range: -1e+09 to 1e+09
		"""
		param = Conversions.decimal_value_to_str(ldelay)
		self._core.io.write(f'SCENario:DF:LDELay {param}')

	def get_level(self) -> float:
		"""SCPI: SCENario:DF:LEVel \n
		Snippet: value: float = driver.scenario.df.get_level() \n
		Adds a level offset. \n
			:return: level: float Range: -200 to 0
		"""
		response = self._core.io.query_str('SCENario:DF:LEVel?')
		return Conversions.str_to_float(response)

	def set_level(self, level: float) -> None:
		"""SCPI: SCENario:DF:LEVel \n
		Snippet: driver.scenario.df.set_level(level = 1.0) \n
		Adds a level offset. \n
			:param level: float Range: -200 to 0
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'SCENario:DF:LEVel {param}')

	def get_priority(self) -> float:
		"""SCPI: SCENario:DF:PRIority \n
		Snippet: value: float = driver.scenario.df.get_priority() \n
		Sets the priority of the selected PDW list , where the higher the value the higher the priority. \n
			:return: priority: float Range: 1 to 100
		"""
		response = self._core.io.query_str('SCENario:DF:PRIority?')
		return Conversions.str_to_float(response)

	def set_priority(self, priority: float) -> None:
		"""SCPI: SCENario:DF:PRIority \n
		Snippet: driver.scenario.df.set_priority(priority = 1.0) \n
		Sets the priority of the selected PDW list , where the higher the value the higher the priority. \n
			:param priority: float Range: 1 to 100
		"""
		param = Conversions.decimal_value_to_str(priority)
		self._core.io.write(f'SCENario:DF:PRIority {param}')

	def get_select(self) -> float:
		"""SCPI: SCENario:DF:SELect \n
		Snippet: value: float = driver.scenario.df.get_select() \n
		Selects the item to which the subsequent commands apply. \n
			:return: select: float Item number within the range 1 to ...:COUNt. For example, method RsPulseSeq.Sequence.Item.count. Range: 1 to 4096
		"""
		response = self._core.io.query_str('SCENario:DF:SELect?')
		return Conversions.str_to_float(response)

	def set_select(self, select: float) -> None:
		"""SCPI: SCENario:DF:SELect \n
		Snippet: driver.scenario.df.set_select(select = 1.0) \n
		Selects the item to which the subsequent commands apply. \n
			:param select: float Item number within the range 1 to ...:COUNt. For example, method RsPulseSeq.Sequence.Item.count. Range: 1 to 4096
		"""
		param = Conversions.decimal_value_to_str(select)
		self._core.io.write(f'SCENario:DF:SELect {param}')

	def get_sequence(self) -> str:
		"""SCPI: SCENario:DF:SEQuence \n
		Snippet: value: str = driver.scenario.df.get_sequence() \n
		Assigns a sequence to the background signal. \n
			:return: sequence: string
		"""
		response = self._core.io.query_str('SCENario:DF:SEQuence?')
		return trim_str_response(response)

	def set_sequence(self, sequence: str) -> None:
		"""SCPI: SCENario:DF:SEQuence \n
		Snippet: driver.scenario.df.set_sequence(sequence = 'abc') \n
		Assigns a sequence to the background signal. \n
			:param sequence: string
		"""
		param = Conversions.value_to_quoted_str(sequence)
		self._core.io.write(f'SCENario:DF:SEQuence {param}')

	def get_threshold(self) -> float:
		"""SCPI: SCENario:DF:THReshold \n
		Snippet: value: float = driver.scenario.df.get_threshold() \n
		Sets a threshold. Pulses at levels below this threshold are omitted. \n
			:return: threshold: float Range: -100 to 0
		"""
		response = self._core.io.query_str('SCENario:DF:THReshold?')
		return Conversions.str_to_float(response)

	def set_threshold(self, threshold: float) -> None:
		"""SCPI: SCENario:DF:THReshold \n
		Snippet: driver.scenario.df.set_threshold(threshold = 1.0) \n
		Sets a threshold. Pulses at levels below this threshold are omitted. \n
			:param threshold: float Range: -100 to 0
		"""
		param = Conversions.decimal_value_to_str(threshold)
		self._core.io.write(f'SCENario:DF:THReshold {param}')

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.DfType:
		"""SCPI: SCENario:DF:TYPE \n
		Snippet: value: enums.DfType = driver.scenario.df.get_type_py() \n
		Defines whether an emitter/interferer is configured. \n
			:return: type_py: EMITter | | WAVeform
		"""
		response = self._core.io.query_str('SCENario:DF:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.DfType)

	def set_type_py(self, type_py: enums.DfType) -> None:
		"""SCPI: SCENario:DF:TYPE \n
		Snippet: driver.scenario.df.set_type_py(type_py = enums.DfType.BACKground) \n
		Defines whether an emitter/interferer is configured. \n
			:param type_py: EMITter | | WAVeform
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.DfType)
		self._core.io.write(f'SCENario:DF:TYPE {param}')

	def clone(self) -> 'DfCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = DfCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
