
def Standard_RGB_to_XYZ ( sR, sG, sB ):
    var_R = ( sR / 255 )
    var_G = ( sG / 255 )
    var_B = ( sB / 255 )

    if ( var_R > 0.04045 ): var_R = ( ( var_R + 0.055 ) / 1.055 ) ** 2.4
    else:                   var_R = var_R / 12.92
    if ( var_G > 0.04045 ): var_G = ( ( var_G + 0.055 ) / 1.055 ) ** 2.4
    else:                   var_G = var_G / 12.92
    if ( var_B > 0.04045 ): var_B = ( ( var_B + 0.055 ) / 1.055 ) ** 2.4
    else:                   var_B = var_B / 12.92

    var_R = var_R * 100
    var_G = var_G * 100
    var_B = var_B * 100

    X = var_R * 0.4124564 + var_G * 0.3575761 + var_B * 0.1804375
    Y = var_R * 0.2126729 + var_G * 0.7151522 + var_B * 0.0721750
    Z = var_R * 0.0193339 + var_G * 0.1191920 + var_B * 0.9503041

    return X, Y, Z

print ( Standard_RGB_to_XYZ( 10, 50, 150 ) )