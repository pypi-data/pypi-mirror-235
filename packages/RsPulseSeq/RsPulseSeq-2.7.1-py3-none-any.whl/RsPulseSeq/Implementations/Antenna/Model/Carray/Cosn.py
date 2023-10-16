from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CosnCls:
	"""Cosn commands group definition. 3 total commands, 0 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cosn", core, parent)

	def get_x(self) -> float:
		"""SCPI: ANTenna:MODel:CARRay:COSN:X \n
		Snippet: value: float = driver.antenna.model.carray.cosn.get_x() \n
		Requires ANTenna:MODel:CARRay:DISTribution:TYPE 1. Sets the individual value of the coefficient N in the cosN
		distribution for X and Z direction. \n
			:return: x: float Range: 2 to 10
		"""
		response = self._core.io.query_str('ANTenna:MODel:CARRay:COSN:X?')
		return Conversions.str_to_float(response)

	def set_x(self, x: float) -> None:
		"""SCPI: ANTenna:MODel:CARRay:COSN:X \n
		Snippet: driver.antenna.model.carray.cosn.set_x(x = 1.0) \n
		Requires ANTenna:MODel:CARRay:DISTribution:TYPE 1. Sets the individual value of the coefficient N in the cosN
		distribution for X and Z direction. \n
			:param x: float Range: 2 to 10
		"""
		param = Conversions.decimal_value_to_str(x)
		self._core.io.write(f'ANTenna:MODel:CARRay:COSN:X {param}')

	def get_z(self) -> float:
		"""SCPI: ANTenna:MODel:CARRay:COSN:Z \n
		Snippet: value: float = driver.antenna.model.carray.cosn.get_z() \n
		Requires ANTenna:MODel:CARRay:DISTribution:TYPE 1. Sets the individual value of the coefficient N in the cosN
		distribution for X and Z direction. \n
			:return: z: No help available
		"""
		response = self._core.io.query_str('ANTenna:MODel:CARRay:COSN:Z?')
		return Conversions.str_to_float(response)

	def set_z(self, z: float) -> None:
		"""SCPI: ANTenna:MODel:CARRay:COSN:Z \n
		Snippet: driver.antenna.model.carray.cosn.set_z(z = 1.0) \n
		Requires ANTenna:MODel:CARRay:DISTribution:TYPE 1. Sets the individual value of the coefficient N in the cosN
		distribution for X and Z direction. \n
			:param z: float Range: 2 to 10
		"""
		param = Conversions.decimal_value_to_str(z)
		self._core.io.write(f'ANTenna:MODel:CARRay:COSN:Z {param}')

	def get_value(self) -> float:
		"""SCPI: ANTenna:MODel:CARRay:COSN \n
		Snippet: value: float = driver.antenna.model.carray.cosn.get_value() \n
		Sets the value of the coefficient N in the cosN distribution. \n
			:return: cosn: float Range: 2 to 10
		"""
		response = self._core.io.query_str('ANTenna:MODel:CARRay:COSN?')
		return Conversions.str_to_float(response)

	def set_value(self, cosn: float) -> None:
		"""SCPI: ANTenna:MODel:CARRay:COSN \n
		Snippet: driver.antenna.model.carray.cosn.set_value(cosn = 1.0) \n
		Sets the value of the coefficient N in the cosN distribution. \n
			:param cosn: float Range: 2 to 10
		"""
		param = Conversions.decimal_value_to_str(cosn)
		self._core.io.write(f'ANTenna:MODel:CARRay:COSN {param}')
