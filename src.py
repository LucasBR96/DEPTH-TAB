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

    for u in V:
        tab[ u ].sort()

    return tab

def print_adj_tab( tab ):

    nodes = list( tab.keys() )
    nodes.sort()

    for u in nodes:

        neigh = tab[ u ].copy()
        # neigh.sort()

        print( str( u ) , "|" , " ".join( map( str , neigh ) ) )

def depth_tab( V , E , direc ):

    adj  = adj_tab( V , E , direc )
    for u in V:
        adj[ u ].reverse()

    seq = [ -1 ]*3
    dtab = { u : seq.copy() for u in V }
    
    stack = []
    unvisited = V.copy()
    global clock
    clock = -1

    def mark_visit( v ):

        global clock
        clock += 1
        dtab[ v ][ START ] = clock
        dtab[ v ][ DEPTH ] = len( stack ) 
        stack.append( v )
        if dtab[ v ][ DEPTH ]:
            unvisited.remove( v )

    while unvisited:

        v = unvisited.pop()
        mark_visit( v )

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

            mark_visit( v )

    return dtab
            
def print_depth_tab( dtab ):

    nodes = list( dtab.keys() )
    nodes.sort( )

    for u in nodes:
        print( str( u ) , "|"  ," ".join( map( str , dtab[ u ] ) ) )
    
    pass

def build_dfstimeline( dep_tab ):

    f1 = lambda x: dep_tab[ x ][ END ] + 1
    width = max( map( f1 , dep_tab.keys() ) )

    f2 = lambda x: dep_tab[ x ][ DEPTH ]
    depth  = max( map( f2 , dep_tab.keys() ) )
    
    seq =[ " " ]*width
    mat = [ seq.copy() for x in range( depth + 1 ) ]
    # print( *mat, sep = "\n" )
    for node , ( s , e , d ) in dep_tab.items( ):
        nstr = str( node )
        # print( node , s , e , d )
        # print( mat[ d ] )
        # print()
        for i in range( s , e ):
            if i == s or i == e - 1:
                mat[ d ][ i ] = nstr
                continue
            mat[ d ][ i ] = "-"

    s = "\n".join( [ "".join( mat[ i ][:] ) for i in range( depth + 1 ) ] )
    return s

def dfs_results( V , E , direc  ): 
    
    print( "\nTabela de Adj:\n" )
    tab = adj_tab( V , E , d )
    print_adj_tab( tab )

    print( "\nTabela de prof:\n" )
    dpth = depth_tab( V , E , d )
    print_depth_tab( dpth )
    
    print( "\nLinha do tempo: \n" )
    s = build_dfstimeline( dpth )
    print( s )

# Tests -----------------------------------------------------------------------

def test_graph( ):

    V = set( list( range( 8 ) ) )
    E = set( [ 
        ( 0 , 1 ),
        ( 0 , 2 ),
        ( 0 , 4 ),
        ( 1 , 5 ),
        ( 2 , 1 ),
        ( 2 , 3 ),
        ( 3 , 4 ),
        ( 3 , 7 ),
        ( 4 , 1 ),
        ( 4 , 2 ),
        ( 4 , 7 ),
        ( 5 , 7 ),
        ( 6 , 0 ),
        ( 6 , 2 ),
        ( 6 , 5 )
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
        
        dfs_results( V , E , direc )

if __name__ == "__main__":

   test_1()

