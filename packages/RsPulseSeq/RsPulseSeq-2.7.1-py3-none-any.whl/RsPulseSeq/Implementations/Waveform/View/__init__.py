from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ViewCls:
	"""View commands group definition. 6 total commands, 3 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("view", core, parent)

	@property
	def get(self):
		"""get commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_get'):
			from .Get import GetCls
			self._get = GetCls(self._core, self._cmd_group)
		return self._get

	@property
	def open(self):
		"""open commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_open'):
			from .Open import OpenCls
			self._open = OpenCls(self._core, self._cmd_group)
		return self._open

	@property
	def zoom(self):
		"""zoom commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_zoom'):
			from .Zoom import ZoomCls
			self._zoom = ZoomCls(self._core, self._cmd_group)
		return self._zoom

	def set_xmode(self, xmode: enums.ViewXode) -> None:
		"""SCPI: WAVeform:VIEW:XMODe \n
		Snippet: driver.waveform.view.set_xmode(xmode = enums.ViewXode.SAMPles) \n
		Sets the units (time or samples) used on the x axis. \n
			:param xmode: SAMPles| TIME
		"""
		param = Conversions.enum_scalar_to_str(xmode, enums.ViewXode)
		self._core.io.write(f'WAVeform:VIEW:XMODe {param}')

	def set_ymode(self, ymode: enums.Ymode) -> None:
		"""SCPI: WAVeform:VIEW:YMODe \n
		Snippet: driver.waveform.view.set_ymode(ymode = enums.Ymode.FREQuency) \n
		Sets the view mode. \n
			:param ymode: IQ| MAGDb| MAGW| MAGV| PHASe| FREQuency| PAV
		"""
		param = Conversions.enum_scalar_to_str(ymode, enums.Ymode)
		self._core.io.write(f'WAVeform:VIEW:YMODe {param}')

	def clone(self) -> 'ViewCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ViewCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
