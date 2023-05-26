
def RGB_to_HEX ( RGB ):
    RGB = [ int( x ) for x in RGB ]
  
    return "#" + "" . join( [ "0{0:x}" . format( v ) if v < 16 else
            "{0:x}" . format( v ) for v in RGB ] )

print ( RGB_to_HEX ( [220, 200, 146] ) )