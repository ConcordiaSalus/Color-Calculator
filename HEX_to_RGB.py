
def HEX_to_RGB ( HEX ):
    return [ int( HEX[ i : i + 2 ], 16 ) for i in range( 1, 6, 2 ) ]

print ( HEX_to_RGB ( '#DCC892' ) )