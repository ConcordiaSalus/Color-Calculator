
def RGB_to_HSL ( R, G, B ):
    var_R = ( R / 255 )
    var_G = ( G / 255 )
    var_B = ( B / 255 )

    var_Min = min( var_R, var_G, var_B )
    var_Max = max( var_R, var_G, var_B )
    del_Max = var_Max - var_Min

    L = ( var_Max + var_Min )/ 2

    if ( del_Max == 0 ):
        H = 0
        S = 0
    else:
        if ( L < 0.5 ): S = del_Max / ( var_Max + var_Min )
        else:           S = del_Max / ( 2 - var_Max - var_Min )

        del_R = ( ( ( var_Max - var_R ) / 6 ) + ( del_Max / 2 ) ) / del_Max
        del_G = ( ( ( var_Max - var_G ) / 6 ) + ( del_Max / 2 ) ) / del_Max
        del_B = ( ( ( var_Max - var_B ) / 6 ) + ( del_Max / 2 ) ) / del_Max

        if   ( var_R == var_Max ): H = del_B - del_G
        elif ( var_G == var_Max ): H = ( 1 / 3 ) + del_R - del_B
        elif ( var_B == var_Max ): H = ( 2 / 3 ) + del_G - del_R

        if ( H < 0 ): H += 1
        if ( H > 1 ): H -= 1

    return H, S, L

print ( RGB_to_HSL ( 10, 50, 150 ) )