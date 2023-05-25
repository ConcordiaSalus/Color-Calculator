# Color-Calculator
Convert color data in different color spaces

__- XYZ_to_Standard_RGB ( X, Y, Z )__

    X, Y and Z input refer to a D65/2° standard illuminant.
    sR, sG and sB (standard RGB) output range = 0 ÷ 255

__- Standard_RGB_to_XYZ ( sR, sG, sB )__

    sR, sG and sB (Standard RGB) input range = 0 ÷ 255
    X, Y and Z output refer to a D65/2° standard illuminant.

__- XYZ_to_Adobe_RGB ( X, Y, Z )__

    X, Y and Z input refer to a D65/2° standard illuminant.
    aR, aG and aB (RGB Adobe 1998) output range = 0 ÷ 255

__- Adobe_RGB_to_XYZ ( aR, aG, aB )__

    aR, aG and aB (RGB Adobe 1998) input range = 0 ÷ 255
    X, Y and Z output refer to a D65/2° standard illuminant.

__- XYZ_to_Yxy ( X, Y, Z )__

__- Yxy_to_XYZ ( Y, x, y )__

__- XYZ_to_CIE_Lab ( X, Y, Z )__

    Reference_X, Y and Z refer to specific illuminants and observers.

__- CIE_Lab_to_XYZ (CIE_L, CIE_a, CIE_b )__

    Reference_X, Y and Z refer to specific illuminants and observers.

__- XYZ_to_Hunter_Lab ( X, Y, Z )__

    Reference_X, Y and Z refer to specific illuminants and observers.

__- Hunter_Lab_to_XYZ ( Hunter_L, Hunter_a, Hunter_b )__

    Reference_X, Y and Z refer to specific illuminants and observers.

__- RGB_to_CMY ( R, G, B )__

    R, G and B input range = 0 ÷ 255
    C, M and Y output range = 0 ÷ 1.0

__- CMY_to_RGB ( C, M, Y )__

    C, M and Y input range = 0 ÷ 1.0
    R, G and B output range = 0 ÷ 255

__- CMY_to_CMYK ( C, M, Y, K )__

    C, M, Y and K range = 0 ÷ 1.0

__- CMYK_to_CMY ( C, M, Y, K )__

    C, M, Y and K range = 0 ÷ 1.0

__- RGB_to_HSL ( R, G, B )__

    R, G and B input range = 0 ÷ 255
    H, S and L output range = 0 ÷ 1.0

__- HSL_to_RGB ( H, S, L )__

    H, S and L input range = 0 ÷ 1.0
    R, G and B output range = 0 ÷ 255

__- RGB_to_HSV ( R, G, B )__

    R, G and B input range = 0 ÷ 255
    H, S and V output range = 0 ÷ 1.0

__- HSV_to_RGB ( H, S, V )__

    H, S and V input range = 0 ÷ 1.0
    R, G and B output range = 0 ÷ 255

__- XYZ_to_CIE_Luv ( X, Y, Z )__

    Reference_X, Y and Z refer to specific illuminants and observers.

__- CIE_Luv_to_XYZ ( CIE_L, CIE_u, CIE_v )__

    Reference_X, Y and Z refer to specific illuminants and observers.

__- CIE_Lab_to_CIE_LCH ( CIE_L, CIE_a, CIE_b )__

__- CIE_LCH_to_CIE_Lab ( CIE_L, CIE_C, CIE_H )__