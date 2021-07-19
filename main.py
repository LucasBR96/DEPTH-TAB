import src
import sys
import os

def build_from_file( filename ):
    pass

def build_from_cmd( ):
    
    m = -1
    while( m not in set( [ 0 , 1 ] ) ):
        print( "type 1 for directed graf, 0 for undirected:" )
        try:
            m = int( input() )
        except:
            continue

def main( arglst ):
    
    option == arglst[ 0 ]
    if option == "-c": # read graph from commmand line ------------------------------------------
        build_from_cmd()
    elif option == "-f": # read graph from file -------------------------------------------------
        filename = arglst[ 1 ]
        build_from_file( filename )


if __name__ == "__main__":
    main( sys.argv )
