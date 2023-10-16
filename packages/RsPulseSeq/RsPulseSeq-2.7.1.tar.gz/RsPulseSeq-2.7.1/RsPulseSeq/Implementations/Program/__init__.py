from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ProgramCls:
	"""Program commands group definition. 24 total commands, 15 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("program", core, parent)

	@property
	def adjustments(self):
		"""adjustments commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_adjustments'):
			from .Adjustments import AdjustmentsCls
			self._adjustments = AdjustmentsCls(self._core, self._cmd_group)
		return self._adjustments

	@property
	def classPy(self):
		"""classPy commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_classPy'):
			from .ClassPy import ClassPyCls
			self._classPy = ClassPyCls(self._core, self._cmd_group)
		return self._classPy

	@property
	def comment(self):
		"""comment commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_comment'):
			from .Comment import CommentCls
			self._comment = CommentCls(self._core, self._cmd_group)
		return self._comment

	@property
	def gpu(self):
		"""gpu commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_gpu'):
			from .Gpu import GpuCls
			self._gpu = GpuCls(self._core, self._cmd_group)
		return self._gpu

	@property
	def hide(self):
		"""hide commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_hide'):
			from .Hide import HideCls
			self._hide = HideCls(self._core, self._cmd_group)
		return self._hide

	@property
	def path(self):
		"""path commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_path'):
			from .Path import PathCls
			self._path = PathCls(self._core, self._cmd_group)
		return self._path

	@property
	def ramBuff(self):
		"""ramBuff commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ramBuff'):
			from .RamBuff import RamBuffCls
			self._ramBuff = RamBuffCls(self._core, self._cmd_group)
		return self._ramBuff

	@property
	def scenario(self):
		"""scenario commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_scenario'):
			from .Scenario import ScenarioCls
			self._scenario = ScenarioCls(self._core, self._cmd_group)
		return self._scenario

	@property
	def settings(self):
		"""settings commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_settings'):
			from .Settings import SettingsCls
			self._settings = SettingsCls(self._core, self._cmd_group)
		return self._settings

	@property
	def show(self):
		"""show commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_show'):
			from .Show import ShowCls
			self._show = ShowCls(self._core, self._cmd_group)
		return self._show

	@property
	def startup(self):
		"""startup commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_startup'):
			from .Startup import StartupCls
			self._startup = StartupCls(self._core, self._cmd_group)
		return self._startup

	@property
	def storageLoc(self):
		"""storageLoc commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_storageLoc'):
			from .StorageLoc import StorageLocCls
			self._storageLoc = StorageLocCls(self._core, self._cmd_group)
		return self._storageLoc

	@property
	def toolbar(self):
		"""toolbar commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_toolbar'):
			from .Toolbar import ToolbarCls
			self._toolbar = ToolbarCls(self._core, self._cmd_group)
		return self._toolbar

	@property
	def transfer(self):
		"""transfer commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_transfer'):
			from .Transfer import TransferCls
			self._transfer = TransferCls(self._core, self._cmd_group)
		return self._transfer

	@property
	def tutorials(self):
		"""tutorials commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_tutorials'):
			from .Tutorials import TutorialsCls
			self._tutorials = TutorialsCls(self._core, self._cmd_group)
		return self._tutorials

	# noinspection PyTypeChecker
	def get_mode(self) -> enums.ProgramMode:
		"""SCPI: PROGram:MODE \n
		Snippet: value: enums.ProgramMode = driver.program.get_mode() \n
		Selects the operation mode on start-up. \n
			:return: mode: DEMO| STANdard| EXPert
		"""
		response = self._core.io.query_str('PROGram:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.ProgramMode)

	def set_mode(self, mode: enums.ProgramMode) -> None:
		"""SCPI: PROGram:MODE \n
		Snippet: driver.program.set_mode(mode = enums.ProgramMode.DEMO) \n
		Selects the operation mode on start-up. \n
			:param mode: DEMO| STANdard| EXPert
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.ProgramMode)
		self._core.io.write(f'PROGram:MODE {param}')

	def clone(self) -> 'ProgramCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ProgramCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
