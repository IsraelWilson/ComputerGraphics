#Creates a PPM image of size 320 X 240. 

import one_color
import write_ppm
import add_to_image
import translation

def Translate( boardsize_x, boardsize_y, x1, y1, x2, y2, x3, y3, x4, y4, xt, yt ):
    
    print ('Starting')
    
    image = one_color.main( boardsize_x, boardsize_y, 245, 245, 245 )
    redLine = translation.main( x1, y1, x2, y2, xt, yt )
    greenLine = translation.main( x3, y3, x4, y4, xt, yt )
    image = add_to_image.main( image, redLine, 255, 0, 0 )
    image = add_to_image.main( image, greenLine, 0, 255, 0 )

    write_ppm.main( image, 'test' )
    print ('Finish')
    #end function

#Run function
Translate( 320, 240, 60, 120, 160, 120, 160, 120, 160, 220, 50, -50 )
