import mdl
from display import *
from matrix import *
from draw import *

def run(filename):
    """
    This function runs an mdl script
    """
    color = [255, 255, 255]
    tmp = new_matrix()
    ident( tmp )

    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print "Parsing failed."
        return

    stack = [ tmp ]
    screen = new_screen()
        
    for command in commands:
        print command
        if command[0] == 'line':
            temp = []
            add_edge( points, command[1], commands[2], args[3], args[4], args[5], args[6] )
            matrix_mult( stack[-1], temp )
            draw_lines( temp, screen, color )
        elif command[0] == 'circle':
            temp = []
            add_circle( points, command[1], command[2], 0, command[3], .01 )
            matrix_mult( stack[-1], temp )
            draw_lines( temp, screen, color )
        elif command[0] == 'bezier':
            temp = []
            add_curve( points, command[1], command[2], command[3], command[4], command[5], command[6], command[7], command[8], .01, 'bezier' )
            matrix_mult( stack[-1], temp )
            draw_lines( temp, screen, color )
        elif command[0] == 'hermite':
            temp = []
            add_curve( points, command[1], command[2], command[3], command[4], command[5], command[6], command[7], command[8], .01, 'hermite' )
            matrix_mult( stack[-1], temp )
            draw_lines( temp, screen, color )
        elif command[0] == 'sphere':
            temp = []
            add_sphere( temp, command[1], command[2], 0, command[3], 7 )
            matrix_mult( stack[-1], temp )
            draw_polygons( temp, screen, color )
        elif command[0] == 'torus':
            temp = []
            add_torus(temp, command[1], command[2], 0, command[3], command[4],5)
            matrix_mult( stack[-1], temp )
            draw_polygons( temp, screen, [255, 0 ,0] )
        elif command[0] == 'box':
            temp = []
            add_box( temp, command[1], command[2], command[3], command[4], command[5], command[6])
            matrix_mult( stack[-1], temp )
            draw_polygons( temp, screen, color )
        elif command[0] == 'scale':
            s = make_scale( command[1], command[2], command[3] )
            matrix_mult( s, stack[-1] )
        elif command[0] == 'move':
            t = make_translate( command[1], command[2], command[3] )
            matrix_mult( t, stack[-1]  )
        elif command[0] == 'display':
            display(screen)
        elif command[0] == 'save':
            save_extension(screen, command[1])
        elif command[0] == 'push':
            stack.append(stack[-1])
        elif command[0] == 'pop':
            stack.pop()
        elif command[0] == 'quit':
            return
        elif command[0] == 'rotate':
            angle = command[2] * ( math.pi / 180 )
            if command[1] == 'x':
                r = make_rotX( angle )
            elif command[1] == 'y':
                r = make_rotY( angle )
            elif command[1]  == 'z':
                r = make_rotZ( angle )
            matrix_mult( r, stack[-1] )
        elif command[0] != '#':
            print 'invalid command: ' + str(command)
        else:
            print 'invalid command: ' + str(command)
