
Reference_X =  94.811
Reference_Y = 100.000
Reference_Z = 107.304

def CIE_Lab_to_XYZ ( CIE_L, CIE_a, CIE_b):
    var_Y = ( CIE_L + 16 ) / 116
    var_X = CIE_a / 500 + var_Y
    var_Z = var_Y - CIE_b / 200

    if ( var_Y**3  > 0.008856 ): var_Y = var_Y**3
    else:                       var_Y = ( var_Y - 16 / 116 ) / 7.787
    if ( var_X**3  > 0.008856 ): var_X = var_X**3
    else:                       var_X = ( var_X - 16 / 116 ) / 7.787
    if ( var_Z**3  > 0.008856 ): var_Z = var_Z**3
    else:                       var_Z = ( var_Z - 16 / 116 ) / 7.787

    X = var_X * Reference_X
    Y = var_Y * Reference_Y
    Z = var_Z * Reference_Z

    return X, Y, Z

print ( CIE_Lab_to_XYZ ( 0.0, 40.68661855637686, 0.0) )