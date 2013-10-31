#3DviewAlignment.py

def main( xVRP, yVRP, zVRP, d, u1, u2, u3, v1, v2, v3, n1, n2, n3, args ):

    alignedPoints = []
    
    length = len( args )
    for i in range( 0, length - 2, 3 ):
        #Translate vertex points by the XYZ value of the VRP
        #Sets VRP to origin
        x1 = args[ i ] - xVRP
        y1 = args[ i + 1 ] - yVRP
        z1 = args[ i + 2 ] - zVRP

        #Each of the above translated points needs to be rotated by the
        #algorithm below
        x2 = ( x1 * u1 ) + ( y1 * u2 ) + ( z1 * u3 )
        y2 = ( x1 * v1 ) + ( y1 * v2 ) + ( z1 * v3 )
        z2 = ( x1 * n1 ) + ( y1 * n2 ) + ( z1 * n3 )

        #Translate CoP to origin of XYZ wworld view plane using
        #the above values XYZ2
        x3 = x2 - 0
        y3 = y2 - 0
        z3 = z2 - d

        alignedPoints.append( x3 )
        alignedPoints.append( y3 )
        alignedPoints.append( z3 )

    return alignedPoints
