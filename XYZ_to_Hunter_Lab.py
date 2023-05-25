
import math 

Reference_X =  94.811
Reference_Y = 100.000
Reference_Z = 107.304

def XYZ_to_Hunter_Lab ( X, Y, Z ):
    var_Ka = ( 175.0 / 198.04 ) * ( Reference_Y + Reference_X )
    var_Kb = (  70.0 / 218.11 ) * ( Reference_Y + Reference_Z )

    Hunter_L = 100.0 * math.sqrt( Y / Reference_Y )
    Hunter_a = var_Ka * ( ( ( X / Reference_X ) - ( Y / Reference_Y ) ) / math.sqrt( Y / Reference_Y ) )
    Hunter_b = var_Kb * ( ( ( Y / Reference_Y ) - ( Z / Reference_Z ) ) / math.sqrt( Y / Reference_Y ) )

    return Hunter_L, Hunter_a, Hunter_b

print ( XYZ_to_Hunter_Lab ( 0.2500, 0.5000, 0.990 ) )