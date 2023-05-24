
import math

def CIE_Lab_to_CIE_LCH ( CIE_L, CIE_a, CIE_b ):
    CIE_L = CIE_L
    CIE_C = math.sqrt( math.pow( float( CIE_a ), 2 ) + math.pow( float( CIE_b ), 2 ) )
    CIE_H = math.atan2( float( CIE_b ), float( CIE_a ) )

    if CIE_H > 0:
        CIE_H = ( CIE_H / math.pi ) * 180
    else:
        CIE_H = 360 - ( math.fabs( CIE_H ) / math.pi ) * 180

    return CIE_L, CIE_C, CIE_H

print ( CIE_Lab_to_CIE_LCH ( 25.403, 8.791, -57.839 ) )