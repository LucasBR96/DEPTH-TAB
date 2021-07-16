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
    clock = -1

    def mark_visit( u , v ):

        clock += 1
        dtab[ v ][ START ] = clock

        # previous depth
        p_depth = -1 if ( u is None ) else dtab[ u ][ DEPTH ]
        dtab[ v ][ CLOCK ] = p_depth + 1 

        stack.append( v )
        unvisited.remove( v )

    while unvisited:

        v = unvisited.pop()
        mark_visit( None , v )

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

            mark_visited( u , v )

    return dtab
            
def print_depth_tab( dtab ):

    nodes = list( dtab.keys() )
    nodes.sort( )

    for u in nodes:
        print( str( u ) , "|"  ," ".join( map( str , dtab( u ) )

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

    div = "-"*50
    V , E = test_graph()

    titulos = [ "Direcionado" , "não Direcionado" ]
    direc   = [ True , False ]

    for t , d in zip( titulos , direc ):
        print( div )
        print( "Grafo " + t )
        
        print( "\nTabela de Adj:\n" )
        tab = adj_tab( V , E , direc )
        print_adj_tab( tab )

        print( "\nTabela de prof:\n" )
        dpth = depth_tab( V , E , direc )
        print_depth_tab( dpth )

if __name__ == "__main__":

   test_1()

