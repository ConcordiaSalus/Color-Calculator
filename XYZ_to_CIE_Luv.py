
Reference_X =  94.811
Reference_Y = 100.000
Reference_Z = 107.304

def XYZ_to_CIE_Luv ( X, Y, Z ):
    var_U = ( 4 * X ) / ( X + ( 15 * Y ) + ( 3 * Z ) )
    var_V = ( 9 * Y ) / ( X + ( 15 * Y ) + ( 3 * Z ) )

    var_Y = Y / 100
    if ( var_Y > 0.008856 ): var_Y = var_Y ** ( 1 / 3 )
    else:                    var_Y = ( 7.787 * var_Y ) + ( 16 / 116 )

    ref_U = ( 4 * Reference_X ) / ( Reference_X + ( 15 * Reference_Y ) + ( 3 * Reference_Z ) )
    ref_V = ( 9 * Reference_Y ) / ( Reference_X + ( 15 * Reference_Y ) + ( 3 * Reference_Z ) )

    CIE_L = ( 116 * var_Y ) - 16
    CIE_u = 13 * CIE_L * ( var_U - ref_U )
    CIE_v = 13 * CIE_L * ( var_V - ref_V )

    return CIE_L, CIE_u, CIE_v

print ( XYZ_to_CIE_Luv ( 6.768832406357771, 4.546849725462684, 29.369113058611134 ) )