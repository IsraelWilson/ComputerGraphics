#Creates a PPM image of size 320 X 240.
#Runs a program to fill a ellipse

import one_color
import write_ppm
import add_to_image
import fill_ellipse

def EllipseFill( boardsize_x, boardsize_y, x, y, majA, minB ):
    
    print ('Starting')
    
    image = one_color.main( boardsize_x, boardsize_y, 245, 245, 245 )
    circum = fill_ellipse.main( x, y, majA, minB )
    image = add_to_image.main( image, circum, 0, 0, 0 )

    write_ppm.main( image, 'test' )
    print ('Finish')
    #end function

#Run function
EllipseFill( 320, 240, 160, 120, 50, 100 )
