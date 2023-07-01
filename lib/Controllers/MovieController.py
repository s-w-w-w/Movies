from lib.Model.MovieModel import MovieModel
from lib.Views.MoviesView import MoviesView 

class MovieController():

    def __init__(self):
        self.__movieModel = MovieModel()
        self.__movieView = MoviesView() 
        
    def getAll(self):
        context = {
          "movies" : []
        }
          
        context["movies"] = self.__movieModel.getAll() #T
       
        return self.__movieView.getAll(context)
        
    """
    delete(self,id) - get single item
        Input: 
            id - nonnegative integer - item id
        Output: 
            bool - True
    """        
    def delete(self, id = '0'):
        context = {
          "affected_rows" : "0"
        }
        
        # validate
        try:
            id = str(int(id))
        except ValueError:
            id = '0'             
        
        context["affected_rows"] = self.__movieModel.delete(id) 
        
        return self.__movieView.delete(context)
           
    """
    getOne(self,id) - get single item
        Input: 
            id - nonnegative integer - item id
        Output: 
            bool - True
    """       
    def getOne(self,id = '0'):
        context = {
            "movie" : None 
        }
        
        # validate
        try:
            id = str(int(id))
        except ValueError:
            id = '0'     
        
        context["movie"] = self.__movieModel.getOne(id)
        
        return self.__movieView.getOne(context)

    """
    Insert a movie
        Input: 
            id - nonnegative integer - item id
        Output: 
            bool - True
    """    
    def insert(self, values):
        context = {
            "affected_rows" : "0"
        }
        title = ''
        year = ''
        score= ''    

        try:         
            title,year,score = values.split(";")
        except ValueError:
            print("Incorrect data give. Correct format is: title;year;score")
            return False
            
        title = title.strip()
        year = year.strip()
        score = score.strip()
        
        # this should be validated here as well
        if( title != '' and year != '' and score != '' ):
            context["affected_rows"] = self.__movieModel.insert(title,year,score)
            if context["affected_rows"] == 1:
                self.__movieView.insert(context)
                return True
            else:
                return False    
        else:
            print("Incorrect data give. Correct format is: title;year;score")
            return False
