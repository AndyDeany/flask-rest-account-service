from expects import *

from features.config import BASE_URL


# Helper functions
def url(path="/"):
    """Return the full url to the given path."""
    return BASE_URL + path
