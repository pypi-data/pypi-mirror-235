# Custom Exceptions for Path_Walk operations

class InvalidPathError(Exception):
    """
    Raised when the provided path does not exist.
    """
    pass
# Custom Exceptions for database operations
class DatabaseError(Exception):
    """
    Raised when the database encounters an error.
    """
    pass

class DatabaseStorageError(Exception):
    """
    Exception raised when the database storage capacity is exceeded.
    """
    def __init__(self, message="Too many files. Out of storage in the database."):
        self.message = message
        super().__init__(self.message)

class MimeTypeError(Exception):
    """Exception for mime_type not found."""
    pass