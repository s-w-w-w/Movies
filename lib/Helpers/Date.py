import datetime
"""
Date - get information about the current date
"""
class Date:
    def __init__(self):
        (year,month,day) = datetime.date.today().isoformat().split("-")  
        self._year = year
        self._month = month
        self._day = day
     
    """
    get()
        Output:
            string - date formatted DD-MM-YYYY
    """
    def get(self):    
        return f"{self._day}-{self._month}-{self._year}"
