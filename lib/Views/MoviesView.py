"""
MoviesView - display formatted data for Movies
    Methods:
        __init__(self, test = False) - constructor
        getAll(self, data) - display all movies     
        getOne(self, data) - view for get one movie action
        delete(self, data) - view for delete a movie action
        insert(self, data) - view for getOne movie action
"""
class MoviesView:

    """
    __init__(self, test = False) - constructor
        Input:
            test - bool - if False functions print to stdout and return bool, otherwise no printing is done only bool is returned 
    """
    def __init__(self, test = False):
        self.__test = test
 
    """
    getAll(self, data) - display all movies
        Input:
            data - object - data for the view
        Output:
            bool - True
    """       
    def getAll(self, data):
    
        count = len(data['movies'])
        movies = data["movies"]
        current = 1
        
        if not self.__test :
            print("** Movies: **\n")
            print(f"\tCollection count: {count}")
            for movie in movies:
                print(f"\t#{current}. Id: {movie['id']} Title: {movie['title']}, Year: {movie['year']}, Rating: {movie['score']}")
                current += 1 
            print("\n** ========================= **")        
        
        return True
        
    """
    delete(self, data) - view for delete a movie action
        Input: 
            data - object -data for the view
        Output:
            bool - True
    """    
    def delete(self, data):
        affected_rows = data['affected_rows']
        if not self.__test :        
            print(f"Movie deleted!\nNUmber of items deleted: {affected_rows}")
        return True 

    """
    getOne(self, data) - view for get one movie action
        Input: 
            data - object -data for the view
        Output:
            bool - True
    """    
    def getOne(self, data):
        if data["movie"] is not None:
            movie = data['movie']
            if not self.__test :            
                print(f'Movie: Title: {movie["title"]} Year: {movie["year"]} Score: {movie["score"]}')
        else:
            if not self.__test :
                print("Movie could not been found!")    

        return True
    """
    insert(self, data) - view for getOne movie action
        Input: 
            data - object - data for the view
        Output:
            bool - True    
    """            
    def insert(self,data):
        if not self.__test :
            print(f'Success!\nSaved movies: {data["affected_rows"]}') 
        return True
