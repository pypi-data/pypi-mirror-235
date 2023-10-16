class OpenAIBadStopError(Exception):
    """Exception raised when the OpenAI stop reason is not 'stop'"""
    pass


class OpenAITooManyTokensError(Exception):
    """Exception raised when the OpenAI call contains too many tokens for the chosen instance"""
    pass


class AllFailedError(Exception):
    """
    Raised when all retries have failed so we give up

    Arguments
    ---------
    msg : str
        A useful message
    reason : int (0, 1, 2)
        The reason for the exception: 0=max retries exceeded, 1=fatal error occurred, 2=other reason
    """
    MAX_RETRIES = 0
    FATAL_ERROR = 1
    OTHER = 2

    def __init__(self, msg: str, reason: int):
        super().__init__(msg)
        self.msg = msg
        self.reason = self.OTHER if reason > 1 else reason

    def __str__(self):
        return self.msg + {
            self.MAX_RETRIES: ' (max retries exceeded)',
            self.FATAL_ERROR: ' (fatal error occurred)',
            self.OTHER: ' (other reason)'
        }[self.reason]

    def __repr__(self):
        return f'AllFailedError({self.msg}, {self.reason})'


class PostProcessorError(Exception):
    """
    Exception raised when a post-processor fails (e.g. a schema validation fails)

    Arguments
    ---------
    reason: str
        reason for failure
    fix: str
        instructions on how to fix the error
    """
    def __init__(self, reason: str, fix: str):
        super().__init__(reason, fix)
        self.reason = reason
        self.fix = fix

    def __str__(self):
        return f'PostProcessorError: {self.reason}'

    def retry_message(self):
        """Returns a message to encourage the LLM to write output which is conformant to the specs"""
        return (f'Error: {self.reason}.\n'
                f'Remember {self.fix}')
