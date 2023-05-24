
def CMY_to_CMYK ( C, M, Y ):
    var_K = 1

    if ( C < var_K ):   var_K = C
    if ( M < var_K ):   var_K = M
    if ( Y < var_K ):   var_K = Y
    if ( var_K == 1 ):
        C = 0          
        M = 0
        Y = 0
    else:
        C = ( C - var_K ) / ( 1 - var_K )
        M = ( M - var_K ) / ( 1 - var_K )
        Y = ( Y - var_K ) / ( 1 - var_K )
    K = var_K

    return C, M, Y, K

print ( CMY_to_CMYK ( 0.9607843137254902, 0.803921568627451, 0.4117647058823529 ) )