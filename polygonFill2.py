#Creates a PPM image of size 320 X 240. 
#Draws two lines to the image. One red one green

import one_color
import write_ppm
import add_to_image
import fill_polygon2
import draw_polygon

def FillPolygon2( boardsize_x, boardsize_y ):
    
    print ('Starting')
    
    image = one_color.main( boardsize_x, boardsize_y, 245, 245, 245 )
    fill = fill_polygon2.main( 10, 10, 100, 10, 100, 300, 10, 150, 80, 150, 80, 50, 20, 50, 20, 100, 10, 100 )
    image = add_to_image.main( image, fill, 255, 0, 255 )
    border = draw_polygon.main( 10, 10, 100, 10, 100, 300, 10, 150, 80, 150, 80, 50, 20, 50, 20, 100, 10, 100 )
    image = add_to_image.main( image, border, 0 , 0, 0 )

    write_ppm.main( image, 'test' )
    print ('Finish')
    #end Line function

#Run Line function
FillPolygon2( 150, 350 )
