class OutOfRange(Exception):
    """Exception raised for value not between lower and upper range inclusive

    Attributes:
        lower   -- lower range
        upper   -- upper range
        message -- explanation of the error
    """

    def __init__(self, lower, upper, message=""):
        self.lower = lower
        self.upper = upper
        self.message = f"Value not in range [{lower},{upper}]" if not message else message
        super().__init__(self.message)
