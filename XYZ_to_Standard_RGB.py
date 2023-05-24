
def XYZ_to_Standard_RGB ( X, Y, Z ):
    var_X = X / 100
    var_Y = Y / 100
    var_Z = Z / 100

    var_R = var_X *  3.2406 + var_Y * -1.5372 + var_Z * -0.4986
    var_G = var_X * -0.9689 + var_Y *  1.8758 + var_Z *  0.0415
    var_B = var_X *  0.0557 + var_Y * -0.2040 + var_Z *  1.0570

    if ( var_R > 0.0031308 ): var_R = 1.055 * ( var_R ** ( 1 / 2.4 ) ) - 0.055
    else:                     var_R = 12.92 * var_R
    if ( var_G > 0.0031308 ): var_G = 1.055 * ( var_G ** ( 1 / 2.4 ) ) - 0.055
    else:                     var_G = 12.92 * var_G
    if ( var_B > 0.0031308 ): var_B = 1.055 * ( var_B ** ( 1 / 2.4 ) ) - 0.055
    else:                     var_B = 12.92 * var_B

    sR = round( var_R * 255 )
    sG = round( var_G * 255 )
    sB = round( var_B * 255 )

    return sR, sG, sB

print ( XYZ_to_Standard_RGB ( 0.12517452801554058, 0.06452983670248286, 0.005858070782492564 ) )