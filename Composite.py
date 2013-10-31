#Creates a PPM image of size 320 X 240. 
#Draws two lines to the image. One red one green

import one_color
import write_ppm
import add_to_image
import composition

def Composite( boardsize_x, boardsize_y, x1, y1, x2, y2, x3, y3, x4, y4, xt, yt, d, xs, ys, xTrans, yTrans ):
    
    print ('Starting')
    
    image = one_color.main( boardsize_x, boardsize_y, 245, 245, 245 )
    redLine = composition.main( x1, y1, x2, y2, xt, yt, d, xs, ys, xTrans, yTrans )
    greenLine = composition.main( x3, y3, x4, y4, xt, yt, d, xs, ys, xTrans, yTrans )
    image = add_to_image.main( image, redLine, 255, 0, 0 )
    image = add_to_image.main( image, greenLine, 0, 255, 0 )

    write_ppm.main( image, 'test' )
    print ('Finish')
    #end Line function

#Run Line function
Composite( 320, 240, 60, 120, 160, 120, 160, 120, 160, 220, 160, 120, 45, .5, .5, 50, 50 )
