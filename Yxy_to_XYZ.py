
def Yxy_to_XYZ ( Y, x, y ):
    X = x * ( Y / y )
    Y = Y
    Z = ( 1 - x - y ) * ( Y / y )

    return X, Y, Z

print ( Yxy_to_XYZ ( 2.564693546262255, 0.6399999511730725, 0.33000000776792027 ) )