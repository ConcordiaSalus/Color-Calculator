
import math

def CIE_LCH_to_CIE_Lab ( CIE_L, CIE_C, CIE_H ):
    CIE_L = CIE_L
    CIE_a = math.cos( math.radians( CIE_H ) ) * CIE_C
    CIE_b = math.sin( math.radians( CIE_H ) ) * CIE_C

    return CIE_L, CIE_a, CIE_b

print ( CIE_LCH_to_CIE_Lab (25.403, 58.50326146463973, 278.642291349705) )