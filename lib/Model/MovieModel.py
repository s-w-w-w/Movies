from lib.DBConnect.DBConnect import DBConnect

class MovieModel(DBConnect):
    """
    __init__ - get all movies
        output: array
    """    
    def __init__(self):
        super().__init__()
        
    """
    getAll() - get all movies
        output: array
    """    
    def getAll(self):
        res = self._cursor.execute("SELECT * FROM Blockbusters")
        return res.fetchall()


    """
    getOne(id) - get a single row 
        Input: 
            id - nonnegative integer - item index
        output - int - number of affected rows
    """            
    def getOne(self,id = '0'):
        params = (id,)
        res = self._cursor.execute("SELECT * FROM Blockbusters WHERE id = ?", params)
        return res.fetchone()
        
    """
    delete(id) - delete all rows
        Input: 
            id - nonnegative integer - item index
        output - int - number of affected rows
    """    
    def delete(self, id = '0'):
    
        if id == '0':
            self._cursor.execute("Delete FROM Blockbusters")
        else: 
            self._cursor.execute("Delete FROM Blockbusters where id = ?",(id,))
        
        self._connection.commit()    
        return self._connection.total_changes
        
    """
    insert(title, year, score) - insert row
        Input: 
            title - string - title of movie
            year - string - movie release year
            score - string - movie score
        output - int - number of affected rows
    """        
    def insert(self, title = "",year = "",score = ""):
        params = (title, year, score)
        self._cursor.execute("INSERT INTO Blockbusters(title,year,score) VALUES (?,?,?)", params)
        self._connection.commit()
        return self._connection.total_changes
