#view.py
import math

def main( a, b ):

    a = math.radians( a )
    b = math.radians( b )

    #The U vector
    u1 = 1
    u2 = 0
    u3 = 0

    #The V vector
    v1 = 0
    v2 = 1
    v3 = 0

    #The N vector
    n1 = 0
    n2 = 0
    n3 = 1

    #Tilt B
    uT1 = u1
    uT2 = ( u2 * math.cos( b ) ) - ( u3 * math.sin( b ) )
    uT3 = ( u3 * math.cos( b ) ) + ( u2 * math.sin( b ) )

    vT1 = v1
    vT2 = ( v2 * math.cos( b ) ) - ( v3 * math.sin( b ) )
    vT3 = ( v3 * math.cos( b ) ) + ( v2 * math.sin( b ) )

    nT1 = n1
    nT2 = ( n2 * math.cos( b ) ) - ( n3 * math.sin( b ) )
    nT3 = ( n3 * math.cos( b ) ) + ( n2 * math.sin( b ) )

    #New vectors
    u1 = uT1
    u2 = uT2
    u3 = uT3
    
    v1 = vT1
    v2 = vT2
    v3 = vT3
    
    n1 = nT1
    n2 = nT2
    n3 = nT3
    
    #Pan A
    uP1 = ( u1 * math.cos( a ) ) + ( u3 * math.sin( a ) )
    uP2 = u2
    uP3 = ( u3 * math.cos( a ) ) - ( u1 * math.sin( a ) )

    vP1 = ( v1 * math.cos( a ) ) + ( v3 * math.sin( a ) )
    vP2 = v2
    vP3 = ( v3 * math.cos( a ) ) - ( v1 * math.sin( a ) )

    nP1 = ( n1 * math.cos( a ) ) + ( n3 * math.sin( a ) )
    nP2 = n2
    nP3 = ( n3 * math.cos( a ) ) - ( n1 * math.sin( a ) )

    UVN = [ uP1, uP2, uP3, vP1, vP2, vP3, nP1, nP2, nP3 ]

    return UVN
