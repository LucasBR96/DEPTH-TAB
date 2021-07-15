START = 0
END   = 1
DEPTH = 2

def adj_tab( V , E , direc ):

    tab = { u:[] for u in V }
    added = set()

    def f1( u , v ):

        if ( v , u ) in added:
            return

        tab[ u ].append( v )
        tab[ v ].append( u )

        added.add( ( u , v ) )

    def f2( u , v ):
        tab[ u ].append( v )
    
    f = f2 if direc else f1
    for u , v in E:
        f( u , v )

    return tab

def print_adj_tab( tab ):

    nodes = list( tab.keys() )
    nodes.sort()

    for u in nodes:

        neigh = tab[ u ].copy()
        neigh.sort()

        print( str( u ) , "|" , " ".join( map( str , neigh ) ) )

def depth_tab( V , E , direc ):

    adj  = adj_tab( V , E , direc )

    seq = [ -1 ]*3
    dtab = { u : seq.copy() for u in V }
    
    stack = []
    unvisited = V.copy()
    clock = 0
    while unvisited:

        u = unvisited.pop() 
        stack.append( u )
        dtab[ u ][ START ] = clock
        dtab[ u ][ DEPTH ] = 0

        while stack:

            u = stack.pop()
            if not adj[ u ]:
                clock += 1
                dtab[ u ][ END ] = clock
                continue

            stack.append( u )
            v = adj[ u ].pop()
            if not( v in unvisited ):
                continue
            
            clock += 1
            unvisited.remove( v )
            stack.append( v )
            dtab[ v ][ START ] = clock
            dtab[ v ][ DEPTH ] = dtab[ u ][ DEPTH ] + 1
    return dtab

def print_depth_tab( dtab ):

    nodes = list( dtab.keys() )
    nodes.sort( )

    for u in nodes:


def build_dfstimeline( dep_tab ):
    pass

# Tests -----------------------------------------------------------------------

def test_graph( ):

    V = set( list( range( 5 ) ) )
    E = set( [ 
        ( 0 , 1 ),
        ( 0 , 2 ),
        ( 0 , 4 ),
        ( 1 , 0 ),
        ( 1 , 2 ),
        ( 1 , 4 ),
        ( 2 , 1 ),
        ( 2 , 3 ),
        ( 2 , 4 ),
        ( 3 , 4 )
        ] )

    return V , E

def test_1( ):

    def print_adj( direc ):
        V , E = test_graph( )
        adj = adj_tab( V , E , direc )

        for u , neigh in adj.items():

            s1 = str( u )
            s2 = " ".join( map( str , neigh ) )
            print( s1 , s2 , sep = " | " )

    div = "-"*50
    
    print( div )
    print( "Grafo Direcionado" )
    print()
    print_adj( True )
    print()

    print( div )
    print( "Grafo não Direcionado" )
    print()
    print_adj( False )
    print()

if __name__ == "__main__":

   test_1()

