import getpass
import subprocess
"""
User - get information about user
    Methods:
    get() - get user name     
"""
class User:
    def __init__(self):
        self.__user = getpass.getuser()
    """    
    get() - get user name
        Output:
            string - user name
    """     
    def get(self):
        return self.__user    
    
    """
    
    """
    def getGroups(self):
        return subprocess.run(["id", "-nG"],capture_output=True,text=True).stdout.strip()    
    
