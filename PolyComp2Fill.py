#Creates a PPM image of size 320 X 240. 
#Draws two lines to the image. One red one green

import one_color
import write_ppm
import add_to_image
import fill_comp_poly2

def PolyComp2( boardsize_x, boardsize_y, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, xt, yt, xTrans, yTrans, xs, ys, d ):
    
    print ('Starting')
    
    image = one_color.main( boardsize_x, boardsize_y, 245, 245, 245 )
    fill = fill_comp_poly2.main( x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, xt, yt, xTrans, yTrans, xs, ys, d )
    image = add_to_image.main( image, fill, 255, 0, 0 )

    write_ppm.main( image, 'test' )
    print ('Finish')
    #end Line function

#Run Line function
PolyComp2( 320, 240, 60, 120, 110, 200, 110, 150, 200, 220, 160, 120, 160, 120, 50, -30, 1.5, 1.5, -80 )
