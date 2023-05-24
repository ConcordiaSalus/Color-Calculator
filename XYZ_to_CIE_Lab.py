
Reference_X =  94.811
Reference_Y = 100.000
Reference_Z = 107.304

def XYZ_to_CIE_Lab ( X, Y, Z ):
    var_X = X / Reference_X
    var_Y = Y / Reference_Y
    var_Z = Z / Reference_Z

    if ( var_X > 0.008856 ): var_X = var_X ** ( 1/3 )
    else:                    var_X = ( 7.787 * var_X ) + ( 16 / 116 )
    if ( var_Y > 0.008856 ): var_Y = var_Y ** ( 1/3 )
    else:                    var_Y = ( 7.787 * var_Y ) + ( 16 / 116 )
    if ( var_Z > 0.008856 ): var_Z = var_Z ** ( 1/3 )
    else:                    var_Z = ( 7.787 * var_Z ) + ( 16 / 116 )

    CIE_L = ( 116 * var_Y ) - 16
    CIE_a = 500 * ( var_X - var_Y )
    CIE_b = 200 * ( var_Y - var_Z )

    return CIE_L, CIE_a, CIE_b

print ( XYZ_to_CIE_Lab ( 1, 0, 0 ) )