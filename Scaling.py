#Creates a PPM image of size 320 X 240. 

import one_color
import write_ppm
import add_to_image
import scale
import draw_line

def Scale( boardsize_x, boardsize_y, x1, y1, x2, y2, x3, y3, x4, y4, xt, yt, xs, ys ):
    
    print ('Starting')
    
    image = one_color.main( boardsize_x, boardsize_y, 245, 245, 245 )
    redPoints = scale.main( x1, y1, x2, y2, xt, yt, xs, ys )
    greenPoints = scale.main( x3, y3, x4, y4, xt, yt, xs, ys )
    redLine = draw_line.main( redPoints[ 0 ].x, redPoints[ 0 ].y, redPoints[ 1 ].x, redPoints[ 1 ].y )
    greenLine = draw_line.main( greenPoints[ 0 ].x, greenPoints[ 0 ].y, greenPoints[ 1 ].x, greenPoints[ 1 ].y )
    image = add_to_image.main( image, redLine, 255, 0, 0 )
    image = add_to_image.main( image, greenLine, 0, 255, 0 )

    write_ppm.main( image, 'test' )
    print ('Finish')
    #end function

#Run function
Scale( 320, 240, 10, 20, 40, 50, 10, 20, 40, 50, 100, 205, .1, .2 )
