"""
MoviesView - display about information
    Methods:
        __init__(self, test = False) - constructor
"""
class AboutView:

    """
    __init__(self, test = False) - constructor
        Input:
            test - bool - if False functions print to stdout and return bool, otherwise no printing is done only bool is returned 
    """
    def __init__(self, test = False):
        self.__test = test


    def get(self,data):
        print("**********************************")
        print(f'\tSoftware: {data["title"]}')
        print(f'\tVersion: {data["version"]}')
        print(f'\tAuthor: {data["author"]}')
        print(f'\tCopyrights: {data["licence"]}')
        print("**********************************\n")
