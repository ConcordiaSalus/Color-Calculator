
def RGB_to_CMY ( R, G, B ):
    C = 1 - ( R / 255 )
    M = 1 - ( G / 255 )
    Y = 1 - ( B / 255 )

    return C, M, Y

print ( RGB_to_CMY ( 10, 50, 150 ) )