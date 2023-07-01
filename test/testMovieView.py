import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import unittest
from lib.Views.MoviesView import MoviesView

class TestMovieView(unittest.TestCase):

    """
    Test that it returns correct power
    """
    def testMovies(self):
        # test get all view
        data = {
            "movies" : []
        }
        mv = MoviesView(True)
                
        self.assertEqual(True, mv.getAll(data))
        
        # test delete view
        data = {
            "affected_rows" : 1
        }
        self.assertEqual(True,mv.delete(data))        
    
        # test single item
        data = {
            "movie" : None
        }
        self.assertEqual(True,mv.getOne(data))
        # test insert            
        data = {
            "affected_rows" : 1
        }
        self.assertEqual(True,mv.insert(data))                

if __name__ == '__main__':
    unittest.main()
