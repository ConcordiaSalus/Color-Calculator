
def CMY_to_RGB (C, M, Y ):
    R = round ( ( 1 - C ) * 255 )
    G = round ( ( 1 - M ) * 255 )
    B = round ( ( 1 - Y ) * 255 )

    return R, G, B

print ( CMY_to_RGB ( 0.9607843137254902, 0.803921568627451, 0.4117647058823529 ) )