import src
import sys
import os

def build_from_file( filename ):
    pass

def build_from_cmd( ):
    
    # Getting the graph type --------------------------------------------------------------------
    print( "What is the graph type?" )
    m = -1
    while( m not in set( [ 0 , 1 ] ) ):
        print( "type 1 for directed graf, 0 for undirected:" )
        try:
            m = int( input() )
        except:
            continue

    #getting the edges -------------------------------------------------------------------------
    print( "\ngive the edges" )
    print( "each edge should be two lotercase ASCII chars separated by a single space\n" )
    print( "input -1 to stop insertion" )

    V = set()
    E = set()
    
    while True:

        s = input( )
        if s == "-1":
            break
        
        a , b = s.split()
        V = V | set( [ a , b ] )

        if ( b , a ) not in E:
            E = E | { ( a , b ) }

    return ( m == 1 ) , V , E

def main( arglst ):
    
    option == arglst[ 0 ]
    if option == "-c": # read graph from commmand line ------------------------------------------
        direc , V , E = build_from_cmd()
    elif option == "-f": # read graph from file -------------------------------------------------
        filename = arglst[ 1 ]
        direc , V , E = build_from_file( filename )
    
    src.dfs_results()

if __name__ == "__main__":
    main( sys.argv )
