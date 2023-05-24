
def Hue_2_RGB( v1, v2, vH ):
   if ( vH < 0 ): vH += 1
   if( vH > 1 ): vH -= 1
   if ( ( 6 * vH ) < 1 ): return ( v1 + ( v2 - v1 ) * 6 * vH )
   if ( ( 2 * vH ) < 1 ): return ( v2 )
   if ( ( 3 * vH ) < 2 ): return ( v1 + ( v2 - v1 ) * ( ( 2 / 3 ) - vH ) * 6 )
   return ( v1 )

def HSL_to_RGB ( H, S, L ):
    if ( S == 0 ):
        R = L * 255
        G = L * 255
        B = L * 255
    else:
        if ( L < 0.5 ): var_2 = L * ( 1 + S )
        else:           var_2 = ( L + S ) - ( S * L )

        var_1 = 2 * L - var_2

        R = round ( 255 * Hue_2_RGB( var_1, var_2, H + ( 1 / 3 ) ) )
        G = round ( 255 * Hue_2_RGB( var_1, var_2, H ) )
        B = round ( 255 * Hue_2_RGB( var_1, var_2, H - ( 1 / 3 ) ) )

    return R, G, B

print ( HSL_to_RGB ( 0.619047619047619, 0.8750000000000001, 0.3137254901960784 ) )