from lib.Views.AboutView import AboutView 

class AboutController():

    def __init__(self):
        # date (y,m,d) = datetime.date.today().isoformat().split("-")
        self.__title = 'Movie database'
        self.__version = '1.0.0'
        self.__author = 'Sylwester Wojnowski'
        self.__licence = 'MIT Licence'
            
        self.__aboutView = AboutView()     
            
    """
    get(context) - get info about this software
    """        
    def get(self):
        data = {
          "title" : self.__title,
          "version" : self.__version,
          "author" : self.__author,
          "licence" : self.__licence
        }
        
        return self.__aboutView.get(data) 
                
