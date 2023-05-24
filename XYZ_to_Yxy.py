
def XYZ_to_Yxy ( X, Y, Z ):
    Y = Y
    x = X / ( X + Y + Z )
    y = Y / ( X + Y + Z )

    return Y, x, y

print ( XYZ_to_Yxy ( 4.973950623468138, 2.564693546262255, 0.2331542723651961 ) )