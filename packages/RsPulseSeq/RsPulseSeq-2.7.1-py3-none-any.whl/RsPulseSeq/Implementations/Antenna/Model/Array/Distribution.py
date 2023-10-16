from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DistributionCls:
	"""Distribution commands group definition. 4 total commands, 0 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("distribution", core, parent)

	def get_type_py(self) -> bool:
		"""SCPI: ANTenna:MODel:ARRay:DISTribution:TYPE \n
		Snippet: value: bool = driver.antenna.model.array.distribution.get_type_py() \n
		Enables using the individual distribution function for X and Z direction. \n
			:return: type_py: ON| OFF| 1| 0
		"""
		response = self._core.io.query_str('ANTenna:MODel:ARRay:DISTribution:TYPE?')
		return Conversions.str_to_bool(response)

	def set_type_py(self, type_py: bool) -> None:
		"""SCPI: ANTenna:MODel:ARRay:DISTribution:TYPE \n
		Snippet: driver.antenna.model.array.distribution.set_type_py(type_py = False) \n
		Enables using the individual distribution function for X and Z direction. \n
			:param type_py: ON| OFF| 1| 0
		"""
		param = Conversions.bool_to_str(type_py)
		self._core.io.write(f'ANTenna:MODel:ARRay:DISTribution:TYPE {param}')

	# noinspection PyTypeChecker
	def get_x(self) -> enums.AntennaModelArray:
		"""SCPI: ANTenna:MODel:ARRay:DISTribution:X \n
		Snippet: value: enums.AntennaModelArray = driver.antenna.model.array.distribution.get_x() \n
		Requires ANTenna:MODel:ARRay:DISTribution:TYPE 1. Sets the individual aperture distribution function for X and Z
		direction. \n
			:return: x: UNIForm| PARabolic| COSine| CSQuared| COSN| TRIangular| HAMMing| HANN
		"""
		response = self._core.io.query_str('ANTenna:MODel:ARRay:DISTribution:X?')
		return Conversions.str_to_scalar_enum(response, enums.AntennaModelArray)

	def set_x(self, x: enums.AntennaModelArray) -> None:
		"""SCPI: ANTenna:MODel:ARRay:DISTribution:X \n
		Snippet: driver.antenna.model.array.distribution.set_x(x = enums.AntennaModelArray.COSine) \n
		Requires ANTenna:MODel:ARRay:DISTribution:TYPE 1. Sets the individual aperture distribution function for X and Z
		direction. \n
			:param x: UNIForm| PARabolic| COSine| CSQuared| COSN| TRIangular| HAMMing| HANN
		"""
		param = Conversions.enum_scalar_to_str(x, enums.AntennaModelArray)
		self._core.io.write(f'ANTenna:MODel:ARRay:DISTribution:X {param}')

	# noinspection PyTypeChecker
	def get_z(self) -> enums.AntennaModelArray:
		"""SCPI: ANTenna:MODel:ARRay:DISTribution:Z \n
		Snippet: value: enums.AntennaModelArray = driver.antenna.model.array.distribution.get_z() \n
		Requires ANTenna:MODel:ARRay:DISTribution:TYPE 1. Sets the individual aperture distribution function for X and Z
		direction. \n
			:return: z: No help available
		"""
		response = self._core.io.query_str('ANTenna:MODel:ARRay:DISTribution:Z?')
		return Conversions.str_to_scalar_enum(response, enums.AntennaModelArray)

	def set_z(self, z: enums.AntennaModelArray) -> None:
		"""SCPI: ANTenna:MODel:ARRay:DISTribution:Z \n
		Snippet: driver.antenna.model.array.distribution.set_z(z = enums.AntennaModelArray.COSine) \n
		Requires ANTenna:MODel:ARRay:DISTribution:TYPE 1. Sets the individual aperture distribution function for X and Z
		direction. \n
			:param z: UNIForm| PARabolic| COSine| CSQuared| COSN| TRIangular| HAMMing| HANN
		"""
		param = Conversions.enum_scalar_to_str(z, enums.AntennaModelArray)
		self._core.io.write(f'ANTenna:MODel:ARRay:DISTribution:Z {param}')

	# noinspection PyTypeChecker
	def get_value(self) -> enums.AntennaModelArray:
		"""SCPI: ANTenna:MODel:ARRay:DISTribution \n
		Snippet: value: enums.AntennaModelArray = driver.antenna.model.array.distribution.get_value() \n
		Sets the aperture distribution of the Planar Phased Array antenna. \n
			:return: distribution: UNIForm| PARabolic| COSine| CSQuared| COSN| TRIangular| HAMMing| HANN
		"""
		response = self._core.io.query_str('ANTenna:MODel:ARRay:DISTribution?')
		return Conversions.str_to_scalar_enum(response, enums.AntennaModelArray)

	def set_value(self, distribution: enums.AntennaModelArray) -> None:
		"""SCPI: ANTenna:MODel:ARRay:DISTribution \n
		Snippet: driver.antenna.model.array.distribution.set_value(distribution = enums.AntennaModelArray.COSine) \n
		Sets the aperture distribution of the Planar Phased Array antenna. \n
			:param distribution: UNIForm| PARabolic| COSine| CSQuared| COSN| TRIangular| HAMMing| HANN
		"""
		param = Conversions.enum_scalar_to_str(distribution, enums.AntennaModelArray)
		self._core.io.write(f'ANTenna:MODel:ARRay:DISTribution {param}')
