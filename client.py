from optparse import OptionParser
from lib.Controllers.MovieController import MovieController
from lib.Controllers.AboutController import AboutController
from lib.Helpers.Date import Date
from lib.Helpers.User import User

def main():

    usage = "usage: %prog [options] RESOURCE= help | user | date |movies | about"
    parser = OptionParser(usage)
    parser.add_option(
        "-a",
        "--action",
        help="[ACTION=all | one | insert | delete | update | supplement]",
        dest="action",
        default="all"
    )    
    parser.add_option(
        "-i",
        "--id",
        help="ID=INT where INT is a non-negative integer",
        dest="id",
        default="0"
    )
    
    parser.add_option(
        "-d",
        "--data",
        help="DATA=title;year;score",
        dest="data",
        default=";;"
    )

    (options, args) = parser.parse_args()

    resource = 'help'
    resources = ['help','user','date','movies', 'about']

    # set required resource     
    if len(args) > 0:
        try: 
            if resources.index(args[0]) > -1:
                resource = args[0]
        except ValueError:
            pass    


    # Help resource and it options
    if resource == 'help':        # print help message
        parser.print_help()
        exit();

    # this should have a proper controller and views
    if resource == 'user':
        u = User()
        print(f"Logged as : {u.get()}\nBelongs to groups: {u.getGroups()}")
        exit();

    # this should have a proper controller and views
    if resource == 'date':
        d = Date()
        print(f"Date today : {d.get()}")
        exit();

   
    # Movies resource and its options 
    if resource == 'movies':
        controller = MovieController()    
        # get all movies
        if options.action == 'all':
            controller.getAll()
        # get a particular movie    
        elif options.action == "one":
            controller.getOne(options.id)
        # delete a movie    
        elif options.action == "delete":
            controller.delete(options.id)
        # insert an item
        elif options.action == "insert":
            controller.insert(options.data)
        else:
            parser.print_help()
           
    # Movies resource and its options 
    if resource == 'about':
        controller = AboutController()    
        controller.get()
        
if __name__ == "__main__":
    main()

