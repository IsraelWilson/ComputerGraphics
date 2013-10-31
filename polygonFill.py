#Creates a PPM image of size 320 X 240. 
#Draws two lines to the image. One red one green

import one_color
import write_ppm
import add_to_image
import fill_polygon_test

def FillPolygon( boardsize_x, boardsize_y ):
    
    print ('Starting')
    
    image = one_color.main( boardsize_x, boardsize_y, 245, 245, 245 )
    fill = fill_polygon_test.main( 60, 120, 110, 200, 110, 150, 200, 220, 160, 120 )
    image = add_to_image.main( image, fill, 255, 0, 255 )

    write_ppm.main( image, 'test' )
    print ('Finish')
    #end Line function

#Run Line function
FillPolygon( 320, 240 )
