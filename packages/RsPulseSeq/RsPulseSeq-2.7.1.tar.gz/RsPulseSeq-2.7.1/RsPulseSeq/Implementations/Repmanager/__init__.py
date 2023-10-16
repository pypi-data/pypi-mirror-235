from typing import List

from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ...Internal.Types import DataType
from ...Internal.ArgSingleList import ArgSingleList
from ...Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RepmanagerCls:
	"""Repmanager commands group definition. 7 total commands, 1 Subgroups, 4 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("repmanager", core, parent)

	@property
	def path(self):
		"""path commands group. 0 Sub-classes, 3 commands."""
		if not hasattr(self, '_path'):
			from .Path import PathCls
			self._path = PathCls(self._core, self._cmd_group)
		return self._path

	def get_catalog(self) -> List[str]:
		"""SCPI: REPManager:CATalog \n
		Snippet: value: List[str] = driver.repmanager.get_catalog() \n
		Queries available repository elements in the database. \n
			:return: catalog: 'RepositryName','path' RepositryName is the name of the repository as defined with the command method RsPulseSeq.Repository.create Path is the compete file path
		"""
		response = self._core.io.query_str('REPManager:CATalog?')
		return Conversions.str_to_str_list(response)

	def delete(self, rep_name: str, path: str = None, username: str = None, password: str = None) -> None:
		"""SCPI: REPManager:DELete \n
		Snippet: driver.repmanager.delete(rep_name = 'abc', path = 'abc', username = 'abc', password = 'abc') \n
		Deletes the entire repository from the permanent mass storage. \n
			:param rep_name: string Repository name, as configured in the workspace. If more than one repository with the same name exists, the Path must be specified.
			:param path: string Compete file path, as queried with the command method RsPulseSeq.Repmanager.Path.listPy. The Path must be specified, if the RepName is not unique and if Username and Passwd are used.
			:param username: string Required if the repository is password protected
			:param password: string Required if the repository is password protected
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('rep_name', rep_name, DataType.String), ArgSingle('path', path, DataType.String, None, is_optional=True), ArgSingle('username', username, DataType.String, None, is_optional=True), ArgSingle('password', password, DataType.String, None, is_optional=True))
		self._core.io.write(f'REPManager:DELete {param}'.rstrip())

	def export(self, rep_name: str, path: str, ps_archive_file: str) -> None:
		"""SCPI: REPManager:EXPort \n
		Snippet: driver.repmanager.export(rep_name = 'abc', path = 'abc', ps_archive_file = 'abc') \n
		Exports the selected repository file to an archive file. \n
			:param rep_name: string Repository name, as configured in the workspace.
			:param path: string Compete file path, as queried with the command method RsPulseSeq.Repmanager.Path.listPy.
			:param ps_archive_file: Complete file path, incl. file name, and extension (*.psarch) .
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('rep_name', rep_name, DataType.String), ArgSingle('path', path, DataType.String), ArgSingle('ps_archive_file', ps_archive_file, DataType.String))
		self._core.io.write(f'REPManager:EXPort {param}'.rstrip())

	def load(self, rep_name: str, path: str = None, username: str = None, password: str = None) -> None:
		"""SCPI: REPManager:LOAD \n
		Snippet: driver.repmanager.load(rep_name = 'abc', path = 'abc', username = 'abc', password = 'abc') \n
		Loads the selected repository to the workspace. If more than one repository with the same name exist, loaded is the first
		repository with a name match. To query the available repository elements in the database, use the command method
		RsPulseSeq.Repository.catalog. \n
			:param rep_name: string Repository name, as configured in the workspace.
			:param path: string Compete file path, as queried with the command method RsPulseSeq.Repmanager.Path.listPy. The Path must be specified, if Username and Passwd are used.
			:param username: string Required if the repository is password protected
			:param password: string Required if the repository is password protected
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('rep_name', rep_name, DataType.String), ArgSingle('path', path, DataType.String, None, is_optional=True), ArgSingle('username', username, DataType.String, None, is_optional=True), ArgSingle('password', password, DataType.String, None, is_optional=True))
		self._core.io.write(f'REPManager:LOAD {param}'.rstrip())

	def clone(self) -> 'RepmanagerCls':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = RepmanagerCls(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
