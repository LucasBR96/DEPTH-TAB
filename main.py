import src
import sys
import os

def build_from_file( filename ):
    
    V = set()
    E = set()

    with open( filename ) as f:
        d = ( f.readline() == "1" )
        for line in f:
            a , b = line.split()

            V.add( a )
            V.add( b )

            E.add( ( a , b ) )
    return d , V , E

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
    print( "each edge should be two lotercase ASCII chars separated by a single space" )
    print( "input -1 to stop insertion\n" )

    V = set()
    E = set()
    
    while True:

        s = input( )
        if s == "-1":
            break
        
        a , b = s.split()
        V = V | set( [ a , b ] )
        
        c1 = ( m == 0 )
        c2 = ( ( b , a ) in E )
        if ( c1 and not c2 ) or not c1: 
            E = E | { ( a , b ) } 


    return ( m == 1 ) , V , E
    # print ( V , E )

def main( arglst ):
    
    option = arglst[ 1 ]
    if option == "-c": # read graph from commmand line ------------------------------------------
        direc , V , E = build_from_cmd()
    elif option == "-f": # read graph from file -------------------------------------------------
        filename = arglst[ 2 ]
        direc , V , E = build_from_file( filename )
    
    src.dfs_results(V , E, direc )

if __name__ == "__main__":
    main( sys.argv )
