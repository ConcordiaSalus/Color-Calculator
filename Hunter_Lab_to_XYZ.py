
import math 

Reference_X =  94.811
Reference_Y = 100.000
Reference_Z = 107.304

def Hunter_Lab_to_XYZ ( Hunter_L, Hunter_a, Hunter_b ):
    var_Ka = ( 175.0 / 198.04 ) * ( Reference_Y + Reference_X )
    var_Kb = (  70.0 / 218.11 ) * ( Reference_Y + Reference_Z )

    Y = ( ( Hunter_L / Reference_Y ) ** 2 ) * 100.0
    X =   ( Hunter_a / var_Ka * math.sqrt( Y / Reference_Y ) + ( Y / Reference_Y ) ) * Reference_X
    Z = - ( Hunter_b / var_Kb * math.sqrt( Y / Reference_Y ) - ( Y / Reference_Y ) ) * Reference_Z

    return X, Y, Z

print ( Hunter_Lab_to_XYZ ( 10.0, -8.136254320592752, 5.103112883830286 ) )