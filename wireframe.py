import one_color
import write_ppm
import add_to_image
import TDviewDisplay

def TDview( boardsize_x, boardsize_y, xVRP, yVRP, zVRP, d, a, b, xt, yt, sf, x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4, x5, y5, z5, x6, y6, z6, x7, y7, z7, x8, y8, z8, x9, y9, z9, x10, y10, z10, x11, y11, z11, x12, y12, z12, x13, y13, z13, x14, y14, z14, x15, y15, z15, x16, y16, z16, x17, y17, z17, x18, y18, z18, x19, y19, z19, x20, y20, z20, x21, y21, z21, x22, y22, z22, x23, y23, z23, x24, y24, z24, x25, y25, z25, x26, y26, z26, x27, y27, z27, x28, y28, z28, x29, y29, z29, x30, y30, z30 ):
    
    print ('Starting')
    
    image = one_color.main( boardsize_x, boardsize_y, 245, 245, 245 )
    frame = TDviewDisplay.main( xVRP, yVRP, zVRP, d, a, b, xt, yt, sf, x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4, x5, y5, z5, x6, y6, z6, x7, y7, z7, x8, y8, z8, x9, y9, z9, x10, y10, z10, x11, y11, z11, x12, y12, z12, x13, y13, z13, x14, y14, z14, x15, y15, z15, x16, y16, z16, x17, y17, z17, x18, y18, z18, x19, y19, z19, x20, y20, z20, x21, y21, z21, x22, y22, z22, x23, y23, z23, x24, y24, z24, x25, y25, z25, x26, y26, z26, x27, y27, z27, x28, y28, z28, x29, y29, z29, x30, y30, z30 )
    image = add_to_image.main( image, frame, 255, 0, 0 )

    write_ppm.main( image, 'test' )
    print ('Finish')
    #end Line function

#Run Line function
TDview( 500, 500, 36, 25, 74, 25, 0, 0, 250, 250, 10, 0, 0, 54, 0, 10, 54, 0, 0, 54, 16, 0, 54, 16, 0, 54, 16, 10, 54, 16, 10, 54, 8, 16, 54, 8, 16, 54, 0, 10, 54, 8, 16, 54, 8, 16, 30, 8, 16, 30, 16, 10, 30, 16, 10, 30, 16, 0, 30, 16, 0, 30, 16, 0, 54, 16, 10, 54, 16, 10, 30, 8, 16, 30, 0, 10, 30, 0, 10, 30, 0, 10, 54, 0, 0, 54, 0, 0, 30, 0, 0, 30, 0, 10, 30, 0, 0, 30, 16, 0, 30 )
