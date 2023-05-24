
Reference_X =  94.811
Reference_Y = 100.000
Reference_Z = 107.304

def CIE_Luv_to_XYZ ( CIE_L, CIE_u, CIE_v ):
    var_Y = ( CIE_L + 16 ) / 116
    if ( var_Y ** 3  > 0.008856 ): var_Y = var_Y ** 3
    else:                       var_Y = ( var_Y - 16 / 116 ) / 7.787

    ref_U = ( 4 * Reference_X ) / ( Reference_X + ( 15 * Reference_Y ) + ( 3 * Reference_Z ) )
    ref_V = ( 9 * Reference_Y ) / ( Reference_X + ( 15 * Reference_Y ) + ( 3 * Reference_Z ) )

    var_U = CIE_u / ( 13 * CIE_L ) + ref_U
    var_V = CIE_v / ( 13 * CIE_L ) + ref_V

    Y = var_Y * 100
    X =  - ( 9 * Y * var_U ) / ( ( var_U - 4 ) * var_V - var_U * var_V )
    Z =    ( 9 * Y - ( 15 * var_V * Y ) - ( var_V * X ) ) / ( 3 * var_V )

    return X, Y, Z

print ( CIE_Luv_to_XYZ ( 25.40265479073576, -10.51291173052508, -72.1958209969129 ) )