
def CMYK_to_CMY ( C, M, Y, K ):
    C = ( C * ( 1 - K ) + K )
    M = ( M * ( 1 - K ) + K )
    Y = ( Y * ( 1 - K ) + K )

    return C, M, Y

print ( CMYK_to_CMY ( 0.9333333333333333, 0.6666666666666667, 0.0, 0.4117647058823529 ) )