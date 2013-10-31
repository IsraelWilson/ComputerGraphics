#fill_polygon.py

#This function changes the color
#of certain pixels and fills a polygon
#based on the points given

import copy
import draw_polygon
import one_color
import scan_line
import draw_line

def main( x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9 ):
    temp = one_color.struc()
    points = [ copy.deepcopy( one_color.struc ) ]
    fillpoints = [ copy.deepcopy( one_color.struc ) ]
    del points[ 0 ]
    del fillpoints[ 0 ]

    #Get all the points in an edge
    line1 = [ x1, y1, x2, y2 ]
    line2 = [ x2, y2, x3, y3 ]
    line3 = [ x3, y3, x4, y4 ]
    line4 = [ x4, y4, x5, y5 ]
    line5 = [ x5, y5, x6, y6 ]
    line6 = [ x6, y6, x7, y7 ]
    line7 = [ x7, y7, x8, y8 ]
    line8 = [ x8, y8, x9, y9 ]
    line9 = [ x9, y9, x1, y1 ]
    
    
    border = draw_polygon.main( x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6, x7, y7, x8, y8, x9, y9 )
    length = len( border )

    
    #find the smallest and largest y values
    #will be used as the limit of scan line
    minY = border[ 0 ].y
    maxY = border[ 0 ].y
    for i in range( length ):
        if border[ i ].y < minY:
            minY = border[ i ].y
        elif border[ i ].y > maxY:
            maxY = border[ i ].y
        #end of if-else statement
    #end of i for loop
    print( 'Found scan borders' )
    print( 'minY = ', minY )
    print( 'maxY = ', maxY )

    #Find all the intersection points in the edges
    #with the scan line
    scan = minY + 1
    while scan < maxY:
    
        point1 = scan_line.main( line1, scan )
        point2 = scan_line.main( line2, scan )
        point3 = scan_line.main( line3, scan )
        point4 = scan_line.main( line4, scan )
        point5 = scan_line.main( line5, scan )
        point6 = scan_line.main( line6, scan )
        point7 = scan_line.main( line7, scan )
        point8 = scan_line.main( line8, scan )
        point9 = scan_line.main( line9, scan )

        if len( point1 ) == 0:
            pass
        else:
            points = points + point1
            
        if len( point2 ) == 0:
            pass
        else:
            points = points + point2
            
        if len( point3 ) == 0:
            pass
        else:
            points = points + point3

        if len( point4 ) == 0:
            pass
        else:
            points = points + point4

        if len( point5 ) == 0:
            pass
        else:
            points = points + point5

        if len( point6 ) == 0:
            pass
        else:
            points = points + point6
            
        if len( point7 ) == 0:
            pass
        else:
            points = points + point7

        if len( point8 ) == 0:
            pass
        else:
            points = points + point8

        if len( point9 ) == 0:
            pass
        else:
            points = points + point9

    
        #Begin of sort
        length = len( points )
        print( length )
        done = False
        head = 0
        tail = 1
        while done == True:
            check = 0
            if check == length - 1:
                done = False
                
            if tail >= length:
                head = 0
                tail = 1
                    
            if points[ head ].x > points[ tail ].x:
                temp = points[ tail ]
                points[ tail ] = points[ head ]
                points[ head ] = temp
                head = head + 1
                tail = tail + 1
            else:
                head = head + 1
                tail = tail + 1
                check = check + 1
        #End of while loop

        #Get pairs of points that need to be filled
        head = 0
        tail = 1
        while head < length - 1:
            fill = draw_line.main( points[ head ].x, points[ head ].y, points[ tail ].x, points[ tail ].y )
            fillpoints = fillpoints + fill
            #end of i for loop
            head = head + 2
            tail = tail + 2

        del points[ : ]
        scan = scan + 1

    #add border points
    



    return fillpoints
