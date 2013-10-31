#Creates a PPM image of size 320 X 240. 
#Draws two lines to the image. One red one green

import one_color
import write_ppm
import add_to_image
import draw_polygon
import fill_polygon

def Polygon( boardsize_x, boardsize_y ):
    
    print ('Starting')
    
    image = one_color.main( boardsize_x, boardsize_y, 245, 245, 245 )
    poly = fill_polygon.main( 10, 10, 100, 10, 100, 300, 10, 150, 80, 150, 80, 50, 20, 50, 20, 100, 10, 100 )
    border = draw_polygon.main( 10, 10, 100, 10, 100, 300, 10, 150, 80, 150, 80, 50, 20, 50, 20, 100, 10, 100 )
    image = add_to_image.main( image, poly, 255, 0, 255 )
    image = add_to_image.main( image, border, 0, 0, 0 )

    write_ppm.main( image, 'test' )
    print ('Finish')
    #end Line function

#Run Line function
Polygon( 150, 350 )
