#Creates a PPM image of size 320 X 240. 
#Draws two lines to the image. One red one green

import one_color
import write_ppm
import add_to_image
import draw_line
import draw_circle
import draw_ellipse
import draw_polygon
import fill_circle
import fill_ellipse
import fill_polygon
import pole_composition
import flag_composition
import flagFill_composition

def StickFigure( boardsize_x, boardsize_y ):
    
    print ('Starting')
    
    image = one_color.main( boardsize_x, boardsize_y, 245, 245, 245 )
    
    head = draw_circle.main( 160, 200, 20 )
    headFill = fill_circle.main( 160, 200, 20 )
    
    neck = draw_line.main( 160, 180, 160, 170 )
    
    body = draw_polygon.main( 130, 170, 190, 170, 190, 110, 130, 110 )
    bodyFill = fill_polygon.main( 130, 170, 190, 170, 190, 110, 130, 110 )
    
    rArm = draw_line.main( 130, 170, 100, 100 )
    lArm = draw_line.main( 190, 170, 220, 100 )
    
    rHand = draw_circle.main( 100, 100, 10 )
    lHand = draw_circle.main( 220, 100, 10 )
    rHandFill = fill_circle.main( 100, 100, 10 )
    lHandFill = fill_circle.main( 220, 100, 10 )
    
    rLeg = draw_line.main( 140, 110, 120, 50 )
    lLeg = draw_line.main( 180, 110, 200, 50 )
    
    rFoot = draw_ellipse.main( 120, 50, 20, 5 )
    lFoot = draw_ellipse.main( 200, 50, 20, 5 )
    rFootFill = fill_ellipse.main( 120, 50, 20, 5 )
    lFootFill = fill_ellipse.main( 200, 50, 20, 5 )
    

    #Translate, Rotate, and Scale Flag/Pole

    pole = pole_composition.main( 100, 125, 100, 50, 0, 35, 100, 100, 45, 1.25, 1.25 )
    flagFill = flagFill_composition.main( 100, 125, 100, 95, 60, 110, 0, 35, 100, 100, 45, 1.25, 1.25 )
    flag = flag_composition.main( 100, 125, 100, 95, 60, 110, 0, 35, 100, 100, 45, 1.25, 1.25 )
    
    #Start adding pixels to fill
    image = add_to_image.main( image, headFill, 255, 255, 0 )
    image = add_to_image.main( image, head, 0, 0, 0 )
    
    image = add_to_image.main( image, neck, 0, 0, 0 )
    
    image = add_to_image.main( image, bodyFill, 0, 0, 255 )
    image = add_to_image.main( image, body, 255, 0, 0 )
    
    image = add_to_image.main( image, rArm, 0, 0, 0 )
    image = add_to_image.main( image, lArm, 0, 0, 0 )
    
    image = add_to_image.main( image, rHandFill, 255, 0, 0 )
    image = add_to_image.main( image, lHandFill, 255, 0, 0 )
    image = add_to_image.main( image, rHand, 0, 255, 0 )
    image = add_to_image.main( image, lHand, 0, 255, 0 )
    
    image = add_to_image.main( image, rLeg, 0, 0, 0 )
    image = add_to_image.main( image, lLeg, 0, 0, 0 )
    
    image = add_to_image.main( image, rFootFill, 0, 255, 0 )
    image = add_to_image.main( image, lFootFill, 0, 255, 0 )
    image = add_to_image.main( image, rFoot, 0, 0, 255 )
    image = add_to_image.main( image, lFoot, 0, 0, 255 )
    
    image = add_to_image.main( image, pole, 0, 0, 0 )
    
    image = add_to_image.main( image, flagFill, 255, 0 , 255 )
    image = add_to_image.main( image, flag, 0, 0, 0 )

    write_ppm.main( image, 'amos' )
    print ('Finish')
    #end Line function

#Run Line function
StickFigure( 320, 240 )
