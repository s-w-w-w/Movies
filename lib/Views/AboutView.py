"""
MoviesView - display about information
    Methods:
        __init__(self, test = False) - constructor
        get(data) - get info about this software    
"""
class AboutView:

    """
    __init__(self, test = False) - constructor
        Input:
            test - bool - if False functions print to stdout and return bool, otherwise no printing is done only bool is returned 
    """
    def __init__(self, test = False):
        self.__test = test


    """
    get(data) - get info about this software
        Input:
            data - object - object with properties, all strings, title, version, author, licence    
    """
    def get(self,data):
        print("**********************************")
        print(f'\tSoftware: {data["title"]}')
        print(f'\tVersion: {data["version"]}')
        print(f'\tAuthor: {data["author"]}')
        print(f'\tCopyrights: {data["licence"]}')
        print("**********************************\n")
        
        return True
