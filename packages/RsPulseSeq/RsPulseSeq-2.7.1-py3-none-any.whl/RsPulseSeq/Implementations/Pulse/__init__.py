from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Utilities import trim_str_response
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PulseCls:
	"""Pulse commands group definition. 150 total commands, 9 Subgroups, 8 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pulse", core, parent)

	@property
	def envelope(self):
		"""envelope commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_envelope'):
			from .Envelope import EnvelopeCls
			self._envelope = EnvelopeCls(self._core, self._cmd_group)
		return self._envelope

	@property
	def level(self):
		"""level commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_level'):
			from .Level import LevelCls
			self._level = LevelCls(self._core, self._cmd_group)
		return self._level

	@property
	def marker(self):
		"""marker commands group. 0 Sub-classes, 7 commands."""
		if not hasattr(self, '_marker'):
			from .Marker import MarkerCls
			self._marker = MarkerCls(self._core, self._cmd_group)
		return self._marker

	@property
	def mop(self):
		"""mop commands group. 24 Sub-classes, 3 commands."""
		if not hasattr(self, '_mop'):
			from .Mop import MopCls
			self._mop = MopCls(self._core, self._cmd_group)
		return self._mop

	@property
	def overshoot(self):
		"""overshoot commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_overshoot'):
			from .Overshoot import OvershootCls
			self._overshoot = OvershootCls(self._core, self._cmd_group)
		return self._overshoot

	@property
	def preview(self):
		"""preview commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_preview'):
			from .Preview import PreviewCls
			self._preview = PreviewCls(self._core, self._cmd_group)
		return self._preview

	@property
	def ripple(self):
		"""ripple commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_ripple'):
			from .Ripple import RippleCls
			self._ripple = RippleCls(self._core, self._cmd_group)
		return self._ripple

	@property
	def time(self):
		"""time commands group. 0 Sub-classes, 6 commands."""
		if not hasattr(self, '_time'):
			from .Time import TimeCls
			self._time = TimeCls(self._core, self._cmd_group)
		return self._time

	@property
	def typePy(self):
		"""typePy commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_typePy'):
			from .TypePy import TypePyCls
			self._typePy = TypePyCls(self._core, self._cmd_group)
		return self._typePy

	def get_catalog(self) -> str:
		"""SCPI: PULSe:CATalog \n
		Snippet: value: str = driver.pulse.get_catalog() \n
		Queries the available repository elements in the database. \n
			:return: catalog: string
		"""
		response = self._core.io.query_str('PULSe:CATalog?')
		return trim_str_response(response)

	def get_comment(self) -> str:
		"""SCPI: PULSe:COMMent \n
		Snippet: value: str = driver.pulse.get_comment() \n
		Adds a description to the selected repository element. \n
			:return: comment: string
		"""
		response = self._core.io.query_str('PULSe:COMMent?')
		return trim_str_response(response)

	def set_comment(self, comment: str) -> None:
		"""SCPI: PULSe:COMMent \n
		Snippet: driver.pulse.set_comment(comment = 'abc') \n
		Adds a description to the selected repository element. \n
			:param comment: string
		"""
		param = Conversions.value_to_quoted_str(comment)
		self._core.io.write(f'PULSe:COMMent {param}')

	def set_create(self, create: str) -> None:
		"""SCPI: PULSe:CREate \n
		Snippet: driver.pulse.set_create(create = 'abc') \n
		Creates a repository element with the selected name. \n
			:param create: string Must be unique for the particular type of repository elements. May contain empty spaces.
		"""
		param = Conversions.value_to_quoted_str(create)
		self._core.io.write(f'PULSe:CREate {param}')

	def get_custom(self) -> bool:
		"""SCPI: PULSe:CUSTom \n
		Snippet: value: bool = driver.pulse.get_custom() \n
		Enables the use of a custom envelope function \n
			:return: custom: ON| OFF| 1| 0
		"""
		response = self._core.io.query_str('PULSe:CUSTom?')
		return Conversions.str_to_bool(response)

	def set_custom(self, custom: bool) -> None:
		"""SCPI: PULSe:CUSTom \n
		Snippet: driver.pulse.set_custom(custom = False) \n
		Enables the use of a custom envelope function \n
			:param custom: ON| OFF| 1| 0
		"""
		param = Conversions.bool_to_str(custom)
		self._core.io.write(f'PULSe:CUSTom {param}')

	def get_name(self) -> str:
		"""SCPI: PULSe:NAME \n
		Snippet: value: str = driver.pulse.get_name() \n
		Renames the selected repository element. \n
			:return: name: string Must be unique for the particular type of repository elements. May contain empty spaces.
		"""
		response = self._core.io.query_str('PULSe:NAME?')
		return trim_str_response(response)

	def set_name(self, name: str) -> None:
		"""SCPI: PULSe:NAME \n
		Snippet: driver.pulse.set_name(name = 'abc') \n
		Renames the selected repository element. \n
			:param name: string Must be unique for the particular type of repository elements. May contain empty spaces.
		"""
		param = Conversions.value_to_quoted_str(name)
		self._core.io.write(f'PULSe:NAME {param}')

	def set_remove(self, remove: str) -> None:
		"""SCPI: PULSe:REMove \n
		Snippet: driver.pulse.set_remove(remove = 'abc') \n
		Removes the selected element from the workspace. The element must not reference any child elements. Remove the referenced
		elements first. \n
			:param remove: No help available
		"""
		param = Conversions.value_to_quoted_str(remove)
		self._core.io.write(f'PULSe:REMove {param}')

	def get_select(self) -> str:
		"""SCPI: PULSe:SELect \n
		Snippet: value: str = driver.pulse.get_select() \n
		Selects the repository element to which the subsequent commands apply. \n
			:return: select: string Element name, as defined with the ...:CREate or ...:NAME command. To query the existing elements, use the ...:CATalog? command. For example, method RsPulseSeq.Repository.catalog.
		"""
		response = self._core.io.query_str('PULSe:SELect?')
		return trim_str_response(response)

	def set_select(self, select: str) -> None:
		"""SCPI: PULSe:SELect \n
		Snippet: driver.pulse.set_select(select = 'abc') \n
		Selects the repository element to which the subsequent commands apply. \n
			:param select: string Element name, as defined with the ...:CREate or ...:NAME command. To query the existing elements, use the ...:CATalog? command. For example, method RsPulseSeq.Repository.catalog.
		"""
		param = Conversions.value_to_quoted_str(select)
		self._core.io.write(f'PULSe:SELect {param}')

	def set_settings(self, settings: enums.PulseSetting) -> None:
		"""SCPI: PULSe:SETTings \n
		Snippet: driver.pulse.set_settings(settings = enums.PulseSetting.GENeral) \n
		Switches between the displayed settings. \n
			:param settings: TIMing| MOP| MKR| GENeral | | LEVel
		"""
		param = Conversions.enum_scalar_to_str(settings, enums.PulseSetting)
		self._core.io.write(f'PULSe:SETTings {param}')

	def clone(self) -> 'PulseCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = PulseCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
