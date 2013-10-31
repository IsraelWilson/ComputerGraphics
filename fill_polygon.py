#fill_polygon.py

#This function changes the color
#of certain pixels and fills a polygon
#based on the points given

import copy
import draw_polygon
import one_color
import scan_line
import draw_line

def main( *args ):
    temp = one_color.struc()
    points = [ copy.deepcopy( one_color.struc ) ]
    fillpoints = [ copy.deepcopy( one_color.struc ) ]
    del points[ 0 ]
    del fillpoints[ 0 ]

    
    #find the smallest and largest y values
    #will be used as the limit of scan line
    minY = args[ 0 ]
    maxY = args[ 0 ]
    length = len( args )
    for i in range( 1, length, 2 ):
        if args[ i ] < minY:
            minY = args[ i ]
        elif args[ i ] > maxY:
            maxY = args[ i ]
        #end of if-else statement
    #end of i for loop
    print( 'Found scan borders' )
    print( 'minY = ', minY )
    print( 'maxY = ', maxY )

    scan = minY + 1
    start = 0
    while scan < maxY:
        while start <= length - 4:
            #find scan intersection with all sides except last side
            y1 = start + 1
            x2 = y1 + 1
            y2 = x2 + 1
            line = draw_line.main( args[ start ], args[ y1 ], args[ x2 ], args[ y2 ] )
                
            point = scan_line.main( line, scan )
            if len( point ) == 0:
                start = start + 2
            else:
                points = points + point
                start = start + 2
        
        #If on the last side find its scan intersection
        line = draw_line.main( args[ length - 2 ], args[ length - 1 ], args[ 0 ], args[ 1 ] )
        point = scan_line.main( line, scan )            
        if len( point ) == 0:
            pass
        else:
            points = points + point

                
        #Begin of sort
        lengthp = len( points )
        done = False
        head = 0
        tail = 1
        while done == True:
            check = 0
            if check == lengthp - 1:
                done = False
                    
            if tail >= lengthp:
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
        while head < lengthp - 1:
            fill = draw_line.main( points[ head ].x, points[ head ].y, points[ tail ].x, points[ tail ].y )
            fillpoints = fillpoints + fill
            #end of i for loop
            head = head + 2
            tail = tail + 2

        del points[ : ]
        scan = scan + 1
        start = 0

    

    return fillpoints
