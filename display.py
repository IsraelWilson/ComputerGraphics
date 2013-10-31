#display

import projection
import one_color
import translation
import scale
import draw_line
import copy


def main( d, xl, yl, sf, args ):

    display = []
    transP = []
    scaleP = []
    temp = one_color.struc()

    #get projection points
    line = projection.main( d, args )
    length = len( line )

    #Find center point and max values
    xMax = line[ 0 ].x
    xMin = line[ 0 ].x
    yMax = line[ 0 ].y
    yMin = line[ 0 ].y
    for i in range( length ):
        if line[ i ].x > xMax:
            xMax = line[ i ].x
        if line[ i ].x < xMin:
            xMin = line[ i ].x
        if line[ i ].y > yMax:
            yMax = line[ i ].y
        if line[ i ].x < xMin:
            yMin = line[ i ].y
            
    xc = ( xMax + xMin ) / 2
    yc = ( yMax + yMin ) / 2

    #Find translation amount based on center
    xt = xl - xc
    yt = yl - yc

    #Composite
    #translate, scale, and draw a line based on the points found

    for i in range( 0, len( line ) - 1, 2 ):
        point = translation.main( line[ i ].x, line[ i ].y, line[ i + 1 ].x, line[ i + 1 ].y, xt, yt )
        for i in range( len( point ) ):
            temp.x = point[ i ].x
            temp.y = point[ i ].y
            transP.append( copy.deepcopy( temp ) )
    for i in range( 0, len( transP ) - 1, 2 ):
        point = scale.main( transP[ i ].x, transP[ i ].y, transP[ i + 1 ].x, transP[ i + 1 ].y, xl, yl, sf, sf )
        for i in range( len( point ) ):
            temp.x = point[ i ].x
            temp.y = point[ i ].y
            scaleP.append( copy.deepcopy( temp ) )
    for i in range( 0, len( scaleP ) - 1, 2 ):
        point = draw_line.main( scaleP[ i ].x, scaleP[ i ].y, scaleP[ i + 1 ].x, scaleP[ i + 1 ].y )
        for i in range( len( point ) ):
            temp.x = point[ i ].x
            temp.y = point[ i ].y
            display.append( copy.deepcopy( temp ) )
    
    
    return display
    
