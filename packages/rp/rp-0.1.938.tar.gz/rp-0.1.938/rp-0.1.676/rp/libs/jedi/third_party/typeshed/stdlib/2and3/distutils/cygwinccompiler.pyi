# Stubs for distutils.cygwinccompiler

from distutils.unixccompiler import UnixCCompiler


class CygwinCCompiler(UnixCCompiler): ...
class Mingw32CCompiler(CygwinCCompiler): ...
