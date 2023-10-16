from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ModelCls:
	"""Model commands group definition. 81 total commands, 14 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("model", core, parent)

	@property
	def array(self):
		"""array commands group. 4 Sub-classes, 5 commands."""
		if not hasattr(self, '_array'):
			from .Array import ArrayCls
			self._array = ArrayCls(self._core, self._cmd_group)
		return self._array

	@property
	def backlobe(self):
		"""backlobe commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_backlobe'):
			from .Backlobe import BacklobeCls
			self._backlobe = BacklobeCls(self._core, self._cmd_group)
		return self._backlobe

	@property
	def cardoid(self):
		"""cardoid commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_cardoid'):
			from .Cardoid import CardoidCls
			self._cardoid = CardoidCls(self._core, self._cmd_group)
		return self._cardoid

	@property
	def carray(self):
		"""carray commands group. 8 Sub-classes, 2 commands."""
		if not hasattr(self, '_carray'):
			from .Carray import CarrayCls
			self._carray = CarrayCls(self._core, self._cmd_group)
		return self._carray

	@property
	def cosecant(self):
		"""cosecant commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_cosecant'):
			from .Cosecant import CosecantCls
			self._cosecant = CosecantCls(self._core, self._cmd_group)
		return self._cosecant

	@property
	def custom(self):
		"""custom commands group. 1 Sub-classes, 4 commands."""
		if not hasattr(self, '_custom'):
			from .Custom import CustomCls
			self._custom = CustomCls(self._core, self._cmd_group)
		return self._custom

	@property
	def dipole(self):
		"""dipole commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_dipole'):
			from .Dipole import DipoleCls
			self._dipole = DipoleCls(self._core, self._cmd_group)
		return self._dipole

	@property
	def gaussian(self):
		"""gaussian commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_gaussian'):
			from .Gaussian import GaussianCls
			self._gaussian = GaussianCls(self._core, self._cmd_group)
		return self._gaussian

	@property
	def horn(self):
		"""horn commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_horn'):
			from .Horn import HornCls
			self._horn = HornCls(self._core, self._cmd_group)
		return self._horn

	@property
	def parabolic(self):
		"""parabolic commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_parabolic'):
			from .Parabolic import ParabolicCls
			self._parabolic = ParabolicCls(self._core, self._cmd_group)
		return self._parabolic

	@property
	def plugin(self):
		"""plugin commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_plugin'):
			from .Plugin import PluginCls
			self._plugin = PluginCls(self._core, self._cmd_group)
		return self._plugin

	@property
	def rotation(self):
		"""rotation commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_rotation'):
			from .Rotation import RotationCls
			self._rotation = RotationCls(self._core, self._cmd_group)
		return self._rotation

	@property
	def sinc(self):
		"""sinc commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_sinc'):
			from .Sinc import SincCls
			self._sinc = SincCls(self._core, self._cmd_group)
		return self._sinc

	@property
	def user(self):
		"""user commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_user'):
			from .User import UserCls
			self._user = UserCls(self._core, self._cmd_group)
		return self._user

	def get_bandwidth(self) -> float:
		"""SCPI: ANTenna:MODel:BANDwidth \n
		Snippet: value: float = driver.antenna.model.get_bandwidth() \n
		Sets the antenna bandwidth. \n
			:return: bandwidth: float Range: 1e+06 to 1e+11
		"""
		response = self._core.io.query_str('ANTenna:MODel:BANDwidth?')
		return Conversions.str_to_float(response)

	def set_bandwidth(self, bandwidth: float) -> None:
		"""SCPI: ANTenna:MODel:BANDwidth \n
		Snippet: driver.antenna.model.set_bandwidth(bandwidth = 1.0) \n
		Sets the antenna bandwidth. \n
			:param bandwidth: float Range: 1e+06 to 1e+11
		"""
		param = Conversions.decimal_value_to_str(bandwidth)
		self._core.io.write(f'ANTenna:MODel:BANDwidth {param}')

	def get_frequency(self) -> float:
		"""SCPI: ANTenna:MODel:FREQuency \n
		Snippet: value: float = driver.antenna.model.get_frequency() \n
		Sets the frequency. \n
			:return: frequency: float Range: 1e+06 to 1e+11, Unit: Hz
		"""
		response = self._core.io.query_str('ANTenna:MODel:FREQuency?')
		return Conversions.str_to_float(response)

	def set_frequency(self, frequency: float) -> None:
		"""SCPI: ANTenna:MODel:FREQuency \n
		Snippet: driver.antenna.model.set_frequency(frequency = 1.0) \n
		Sets the frequency. \n
			:param frequency: float Range: 1e+06 to 1e+11, Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'ANTenna:MODel:FREQuency {param}')

	# noinspection PyTypeChecker
	def get_polarization(self) -> enums.Polarization:
		"""SCPI: ANTenna:MODel:POLarization \n
		Snippet: value: enums.Polarization = driver.antenna.model.get_polarization() \n
		Sets the antenna polarization. \n
			:return: polarization: VERTical| HORizontal| CRIGht| CLEFt| SRIGht| SLEFt
		"""
		response = self._core.io.query_str('ANTenna:MODel:POLarization?')
		return Conversions.str_to_scalar_enum(response, enums.Polarization)

	def set_polarization(self, polarization: enums.Polarization) -> None:
		"""SCPI: ANTenna:MODel:POLarization \n
		Snippet: driver.antenna.model.set_polarization(polarization = enums.Polarization.CLEFt) \n
		Sets the antenna polarization. \n
			:param polarization: VERTical| HORizontal| CRIGht| CLEFt| SRIGht| SLEFt
		"""
		param = Conversions.enum_scalar_to_str(polarization, enums.Polarization)
		self._core.io.write(f'ANTenna:MODel:POLarization {param}')

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.AntennaModel:
		"""SCPI: ANTenna:MODel:TYPE \n
		Snippet: value: enums.AntennaModel = driver.antenna.model.get_type_py() \n
		Sets the antenna pattern. \n
			:return: type_py: DIPole| PARabolic| GAUSsian| SINC| HORN| COSecant| ARRay| USER| CUSTom| CARRay| CARDoid| PLUGin
		"""
		response = self._core.io.query_str('ANTenna:MODel:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.AntennaModel)

	def set_type_py(self, type_py: enums.AntennaModel) -> None:
		"""SCPI: ANTenna:MODel:TYPE \n
		Snippet: driver.antenna.model.set_type_py(type_py = enums.AntennaModel.ARRay) \n
		Sets the antenna pattern. \n
			:param type_py: DIPole| PARabolic| GAUSsian| SINC| HORN| COSecant| ARRay| USER| CUSTom| CARRay| CARDoid| PLUGin
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.AntennaModel)
		self._core.io.write(f'ANTenna:MODel:TYPE {param}')

	def clone(self) -> 'ModelCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ModelCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
