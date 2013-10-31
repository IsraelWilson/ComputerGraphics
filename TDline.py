import one_color
import write_ppm
import add_to_image
import display

def TDline( boardsize_x, boardsize_y, d, xt, yt, sf, x1, y1, z1, x2, y2, z2 ):
    
    print ('Starting')

    array = [ x1, y1, z1, x2, y2, z2 ]
    
    image = one_color.main( boardsize_x, boardsize_y, 245, 245, 245 )
    frame = display.main( d, xt, yt, sf, array )
    image = add_to_image.main( image, frame, 255, 0, 0 )

    write_ppm.main( image, 'test' )
    print ('Finish')
    #end Line function

#Run Line function
TDline( 320, 240, 20, 160, 120, 80, 35, 40, 70, 20, 30, 50 )
