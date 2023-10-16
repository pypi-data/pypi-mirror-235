from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from ....Internal.Utilities import trim_str_response
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MopCls:
	"""Mop commands group definition. 105 total commands, 24 Subgroups, 3 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mop", core, parent)

	@property
	def eightPsk(self):
		"""eightPsk commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_eightPsk'):
			from .EightPsk import EightPskCls
			self._eightPsk = EightPskCls(self._core, self._cmd_group)
		return self._eightPsk

	@property
	def am(self):
		"""am commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_am'):
			from .Am import AmCls
			self._am = AmCls(self._core, self._cmd_group)
		return self._am

	@property
	def amStep(self):
		"""amStep commands group. 1 Sub-classes, 7 commands."""
		if not hasattr(self, '_amStep'):
			from .AmStep import AmStepCls
			self._amStep = AmStepCls(self._core, self._cmd_group)
		return self._amStep

	@property
	def ask(self):
		"""ask commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_ask'):
			from .Ask import AskCls
			self._ask = AskCls(self._core, self._cmd_group)
		return self._ask

	@property
	def barker(self):
		"""barker commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_barker'):
			from .Barker import BarkerCls
			self._barker = BarkerCls(self._core, self._cmd_group)
		return self._barker

	@property
	def bpsk(self):
		"""bpsk commands group. 1 Sub-classes, 4 commands."""
		if not hasattr(self, '_bpsk'):
			from .Bpsk import BpskCls
			self._bpsk = BpskCls(self._core, self._cmd_group)
		return self._bpsk

	@property
	def cchirp(self):
		"""cchirp commands group. 1 Sub-classes, 6 commands."""
		if not hasattr(self, '_cchirp'):
			from .Cchirp import CchirpCls
			self._cchirp = CchirpCls(self._core, self._cmd_group)
		return self._cchirp

	@property
	def chirp(self):
		"""chirp commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_chirp'):
			from .Chirp import ChirpCls
			self._chirp = ChirpCls(self._core, self._cmd_group)
		return self._chirp

	@property
	def data(self):
		"""data commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_data'):
			from .Data import DataCls
			self._data = DataCls(self._core, self._cmd_group)
		return self._data

	@property
	def exclude(self):
		"""exclude commands group. 2 Sub-classes, 2 commands."""
		if not hasattr(self, '_exclude'):
			from .Exclude import ExcludeCls
			self._exclude = ExcludeCls(self._core, self._cmd_group)
		return self._exclude

	@property
	def filterPy(self):
		"""filterPy commands group. 0 Sub-classes, 5 commands."""
		if not hasattr(self, '_filterPy'):
			from .FilterPy import FilterPyCls
			self._filterPy = FilterPyCls(self._core, self._cmd_group)
		return self._filterPy

	@property
	def fm(self):
		"""fm commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_fm'):
			from .Fm import FmCls
			self._fm = FmCls(self._core, self._cmd_group)
		return self._fm

	@property
	def fmStep(self):
		"""fmStep commands group. 1 Sub-classes, 7 commands."""
		if not hasattr(self, '_fmStep'):
			from .FmStep import FmStepCls
			self._fmStep = FmStepCls(self._core, self._cmd_group)
		return self._fmStep

	@property
	def fsk(self):
		"""fsk commands group. 0 Sub-classes, 4 commands."""
		if not hasattr(self, '_fsk'):
			from .Fsk import FskCls
			self._fsk = FskCls(self._core, self._cmd_group)
		return self._fsk

	@property
	def msk(self):
		"""msk commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_msk'):
			from .Msk import MskCls
			self._msk = MskCls(self._core, self._cmd_group)
		return self._msk

	@property
	def nlCirp(self):
		"""nlCirp commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_nlCirp'):
			from .NlCirp import NlCirpCls
			self._nlCirp = NlCirpCls(self._core, self._cmd_group)
		return self._nlCirp

	@property
	def noise(self):
		"""noise commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_noise'):
			from .Noise import NoiseCls
			self._noise = NoiseCls(self._core, self._cmd_group)
		return self._noise

	@property
	def pchirp(self):
		"""pchirp commands group. 1 Sub-classes, 7 commands."""
		if not hasattr(self, '_pchirp'):
			from .Pchirp import PchirpCls
			self._pchirp = PchirpCls(self._core, self._cmd_group)
		return self._pchirp

	@property
	def piecewise(self):
		"""piecewise commands group. 1 Sub-classes, 8 commands."""
		if not hasattr(self, '_piecewise'):
			from .Piecewise import PiecewiseCls
			self._piecewise = PiecewiseCls(self._core, self._cmd_group)
		return self._piecewise

	@property
	def plist(self):
		"""plist commands group. 1 Sub-classes, 6 commands."""
		if not hasattr(self, '_plist'):
			from .Plist import PlistCls
			self._plist = PlistCls(self._core, self._cmd_group)
		return self._plist

	@property
	def plugin(self):
		"""plugin commands group. 1 Sub-classes, 1 commands."""
		if not hasattr(self, '_plugin'):
			from .Plugin import PluginCls
			self._plugin = PluginCls(self._core, self._cmd_group)
		return self._plugin

	@property
	def poly(self):
		"""poly commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_poly'):
			from .Poly import PolyCls
			self._poly = PolyCls(self._core, self._cmd_group)
		return self._poly

	@property
	def qam(self):
		"""qam commands group. 0 Sub-classes, 2 commands."""
		if not hasattr(self, '_qam'):
			from .Qam import QamCls
			self._qam = QamCls(self._core, self._cmd_group)
		return self._qam

	@property
	def qpsk(self):
		"""qpsk commands group. 1 Sub-classes, 2 commands."""
		if not hasattr(self, '_qpsk'):
			from .Qpsk import QpskCls
			self._qpsk = QpskCls(self._core, self._cmd_group)
		return self._qpsk

	def get_comment(self) -> str:
		"""SCPI: PULSe:MOP:COMMent \n
		Snippet: value: str = driver.pulse.mop.get_comment() \n
		Adds a description to the selected repository element. \n
			:return: comment: string
		"""
		response = self._core.io.query_str('PULSe:MOP:COMMent?')
		return trim_str_response(response)

	def set_comment(self, comment: str) -> None:
		"""SCPI: PULSe:MOP:COMMent \n
		Snippet: driver.pulse.mop.set_comment(comment = 'abc') \n
		Adds a description to the selected repository element. \n
			:param comment: string
		"""
		param = Conversions.value_to_quoted_str(comment)
		self._core.io.write(f'PULSe:MOP:COMMent {param}')

	def get_enable(self) -> bool:
		"""SCPI: PULSe:MOP:ENABle \n
		Snippet: value: bool = driver.pulse.mop.get_enable() \n
		Defines whether a MOP is applied. \n
			:return: enable: ON| OFF| 1| 0
		"""
		response = self._core.io.query_str('PULSe:MOP:ENABle?')
		return Conversions.str_to_bool(response)

	def set_enable(self, enable: bool) -> None:
		"""SCPI: PULSe:MOP:ENABle \n
		Snippet: driver.pulse.mop.set_enable(enable = False) \n
		Defines whether a MOP is applied. \n
			:param enable: ON| OFF| 1| 0
		"""
		param = Conversions.bool_to_str(enable)
		self._core.io.write(f'PULSe:MOP:ENABle {param}')

	# noinspection PyTypeChecker
	def get_type_py(self) -> enums.MopType:
		"""SCPI: PULSe:MOP:TYPE \n
		Snippet: value: enums.MopType = driver.pulse.mop.get_type_py() \n
		Select the modulation scheme. \n
			:return: type_py: AM| ASK| AMSTep| FM| FSK| FMSTep| CHIRp| PCHirp| BARKer| POLYphase| PLISt| BPSK| QPSK| NOISe| PWISechirp| CCHiprp| PSK8| QAM| MSK | NLCHirp| PLUGin
		"""
		response = self._core.io.query_str('PULSe:MOP:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.MopType)

	def set_type_py(self, type_py: enums.MopType) -> None:
		"""SCPI: PULSe:MOP:TYPE \n
		Snippet: driver.pulse.mop.set_type_py(type_py = enums.MopType.AM) \n
		Select the modulation scheme. \n
			:param type_py: AM| ASK| AMSTep| FM| FSK| FMSTep| CHIRp| PCHirp| BARKer| POLYphase| PLISt| BPSK| QPSK| NOISe| PWISechirp| CCHiprp| PSK8| QAM| MSK | NLCHirp| PLUGin
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.MopType)
		self._core.io.write(f'PULSe:MOP:TYPE {param}')

	def clone(self) -> 'MopCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MopCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
