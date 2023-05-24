
def XYZ_to_Adobe_RGB ( X, Y, Z ):
    var_X = X / 100
    var_Y = Y / 100
    var_Z = Z / 100

    var_R = var_X *  2.0413690 + var_Y * -0.5649464 + var_Z * -0.3446944
    var_G = var_X * -0.9692660 + var_Y *  1.8760108 + var_Z *  0.0415560
    var_B = var_X *  0.0134474 + var_Y * -0.1183897 + var_Z *  1.0154096

    var_R = var_R * ( 1 / 2.19921875 )
    var_G = var_G * ( 1 / 2.19921875 )
    var_B = var_B * ( 1 / 2.19921875 )

    aR = round( var_R * 255 )
    aG = round( var_G * 255 )
    aB = round( var_B * 255 )

    return aR, aG, aB

print ( XYZ_to_Adobe_RGB ( 4.973950623468138, 2.564693546262255, 0.2331542723651961 ) )