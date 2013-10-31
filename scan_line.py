#This file stores the scan-line intersection
#algorithm

import copy
import one_color

def main( line, scan ):
    temp = one_color.struc()
    points = [ copy.deepcopy( one_color.struc ) ]
    lineMax = 0

    length = len( line )
    if line[ 0 ].y < line[ length - 1 ].y:
        start = line[ 0 ].y
        end = line[ length - 1 ].y
    else:
        start = line[ length - 1 ].y
        end = line[ 0 ].y

    
    #Line
    if line[ length - 1 ].y - line[ 0 ].y == 0:
        #This is a horizontal line
        del points[ 0 ]
        return points

    #If scan line is not within the edge
    if scan not in range( start, end ):
        del points[ 0 ]
        return points
    else:
        if line[ 0 ].y >= line[ length - 1 ].y:
            #y1 is maximum
            lineMax = line[ 0 ].y
        elif line[ 0 ].y < line[ length - 1 ].y:
            #y2 is maximum
            lineMax = line[ length - 1 ].y

        if scan == lineMax:
            #Max vertex point, no intersection
            del points[ 0 ]
            return points
        elif scan in range( start, end ) and scan != lineMax:
            frac = ( line[ length - 1 ].x - line[ 0 ].x ) / ( line[ length - 1 ].y - line[ 0 ].y )
            first = frac * scan
            second = ( frac * line[ 0 ].y )
            third = first - second
            newX = third + line[ 0 ].x
            temp.x = round( newX )
            temp.y = scan
            points.append( copy.deepcopy( temp ) )
            
    del points[ 0 ]
    return points
                
