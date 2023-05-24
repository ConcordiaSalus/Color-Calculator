
def Adobe_RGB_to_XYZ( aR, aG, aB ):
    var_R = ( aR / 255 )
    var_G = ( aG / 255 )
    var_B = ( aB / 255 )

    var_R = var_R * 2.19921875
    var_G = var_G * 2.19921875
    var_B = var_B * 2.19921875

    var_R = var_R * 100
    var_G = var_G * 100
    var_B = var_B * 100

    X = var_R * 0.5767309 + var_G * 0.1855540 + var_B * 0.1881852
    Y = var_R * 0.2973769 + var_G * 0.6273491 + var_B * 0.0752741
    Z = var_R * 0.0270343 + var_G * 0.0706872 + var_B * 0.9911085

    return X, Y, Z

print ( Adobe_RGB_to_XYZ( 10, 0, 0) )