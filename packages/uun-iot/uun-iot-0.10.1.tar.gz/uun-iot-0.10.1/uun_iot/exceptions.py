# Exception for specifying unknown event in `on()` function
class UnsupportedEvent(Exception):
    """Unknown gateway event."""


class UuAppClientException(Exception):
    """Internal error in request pre-processing occured."""


class TokenError(UuAppClientException):
    """Error when getting/validating a token occured."""


class TokenCommandError(TokenError):
    """Server error when getting a token occured."""
