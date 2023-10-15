# Stubs for email.errors (Python 3.4)

class MessageError(Exception): ...
class MessageParseError(MessageError): ...
class HeaderParseError(MessageParseError): ...
class BoundaryError(MessageParseError): ...
class MultipartConversionError(MessageError, TypeError): ...

class MessageDefect(ValueError): ...
class NoBoundaryInMultipartDefect(MessageDefect): ...
class StartBoundaryNotFoundDefect(MessageDefect): ...
class FirstHeaderLineIsContinuationDefect(MessageDefect): ...
class MisplacedEnvelopeHeaderDefect(MessageDefect): ...
class MalformedHeaderDefect(MessageDefect): ...
class MultipartInvariantViolationDefect(MessageDefect): ...
class InvalidBase64PaddingDefect(MessageDefect): ...
class InvalidBase64CharactersDefect(MessageDefect): ...
class CloseBoundaryNotFoundDefect(MessageDefect): ...
class MissingHeaderBodySeparatorDefect(MessageDefect): ...
