
def HSV_to_RGB ( H, S, V ):
    if ( S == 0 ):
        R = V * 255
        G = V * 255
        B = V * 255
    else:
        var_h = H * 6
        if ( var_h == 6 ): var_h = 0
        var_i = int( var_h )
        var_1 = V * ( 1 - S )
        var_2 = V * ( 1 - S * ( var_h - var_i ) )
        var_3 = V * ( 1 - S * ( 1 - ( var_h - var_i ) ) )

        if ( var_i == 0 ):
            var_r = V
            var_g = var_3
            var_b = var_1
        elif ( var_i == 1 ):
            var_r = var_2
            var_g = V
            var_b = var_1
        elif ( var_i == 2 ):
            var_r = var_1
            var_g = V
            var_b = var_3
        elif ( var_i == 3 ):
            var_r = var_1
            var_g = var_2
            var_b = V
        elif ( var_i == 4 ):
            var_r = var_3
            var_g = var_1
            var_b = V
        else:
            var_r = V
            var_g = var_1
            var_b = var_2

        R = round( var_r * 255 )
        G = round( var_g * 255 )
        B = round( var_b * 255 )

    return R, G, B

print ( HSV_to_RGB ( 0.619047619047619, 0.9333333333333333, 0.5882352941176471 ) )