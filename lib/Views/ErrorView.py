"""
MoviesView - display formatted data for Movies
    Methods:
        __init__(self, test = False) - constructor
"""
class ErrorView:

    """
    __init__(self, test = False) - constructor
        Input:
            test - bool - if False functions print to stdout and return bool, otherwise no printing is done only bool is returned 
    """
    def __init__(self, test = False):
        self.__test = test

    """
    basic(data = {"header" : "Error!", "body" : "An error occured"}) - display basic error message which 
        has a header and a body
        
        Input:
            data - object - must contain two keys: header and body, both pointing to a string 
    """ 
    def basic(data = {"header" : "Error!", "body" : "An error occured"}):
        print(f'{data["header"]}\n')
        print(f'{data["body"]}\n')
