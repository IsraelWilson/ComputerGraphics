#Creates a PPM image of size 320 X 240. 
#Draws two lines to the image. One red one green

import one_color
import write_ppm
import add_to_image
import draw_line

def Line( boardsize_x, boardsize_y, x1, y1, x2, y2, xx1, yy1, xx2, yy2 ):
    print ('Starting')
    
    image = one_color.main( boardsize_x, boardsize_y, 245, 245, 245 )
    redline = draw_line.main( x1, y1, x2, y2 )
    greenline = draw_line.main( xx1, yy1, xx2, yy2 )
    image = add_to_image.main( image, redline, 255, 0, 0 )
    image = add_to_image.main( image, greenline, 0, 255, 0 )

    write_ppm.main( image, 'test' )
    print ('Finish')
    #end Line function

#Run Line function
Line( 320, 240, 60, 120, 160, 120, 160, 120, 160, 220 )
