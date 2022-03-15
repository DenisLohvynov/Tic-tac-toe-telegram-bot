from math import pi
import cairo


def __draw_background(context: cairo.Context, r: float, g: float, b: float, width: int, height: int):
    context.set_source_rgb(r, g, b)
    context.rectangle(0, 0, width, height)
    context.fill()


def __draw_grid(context: cairo.Context, buf: float, size: int):
    context.set_line_width(9*size/800)

    context.set_line_cap(cairo.LINE_CAP_ROUND)

    x = (1-2*buf)/3

    context.move_to(buf*size, (x+buf)*size)
    context.line_to((1-buf)*size, (x+buf)*size)

    context.move_to(buf*size, (2*x+buf)*size)
    context.line_to((1-buf)*size, (2*x+buf)*size)

    context.move_to((x+buf)*size, buf*size)
    context.line_to((x+buf)*size, (1-buf)*size)   

    context.move_to((2*x+buf)*size, buf*size)
    context.line_to((2*x+buf)*size, (1-buf)*size)
    
    context.stroke()


def __draw_number(context: cairo.Context, x: int, y: int, size: int, i: int, number_color_opacity: tuple):
    context.set_font_size(65*size/800)
    context.select_font_face("Arial",
                    cairo.FONT_SLANT_NORMAL,
                    cairo.FONT_WEIGHT_NORMAL)
    context.set_source_rgba(number_color_opacity[0]/255, number_color_opacity[1]/255 , number_color_opacity[2]/255, number_color_opacity[3]/100)
    context.move_to(x, y)
    context.show_text(str(i))


def __draw_X(context: cairo.Context, x: int, y: int, size: int, buf: float, X_color: tuple):
    context.set_source_rgba(X_color[0]/255, X_color[1]/255, X_color[2]/255, 1)
    context.set_line_width(9*size/800)
    context.set_line_cap(cairo.LINE_CAP_SQUARE)
    context.move_to(x - buf, y - buf)
    context.line_to(x + buf, y + buf)
    context.move_to(x + buf, y - buf)
    context.line_to(x - buf, y + buf)
    context.stroke() 


def __draw_O(context: cairo.Context, x: int, y: int, size: int, r: float, O_color: tuple):
    context.set_line_width(9*size/800)
    context.set_source_rgba(O_color[0]/255, O_color[1]/255, O_color[2]/255, 1)
    context.move_to(x+r, y)
    context.arc(x, y, r, 0, 2*pi)
    context.stroke()


def Generate(
        name: str,
        size: int = 800,
        path: str = "TelegramImages",
        buf: float = 0.05,
        back_color: tuple = (0, 0, 0),
        grid_color: tuple = (255, 255, 255),
        X_color: tuple = (116, 230, 137),
        O_color: tuple = (108, 117, 239),
        number_color_opacity: tuple = (255, 255, 255, 50)
        ):
    """
    buf - отступ от края в процентах,
    path - без последнего /
    color - RGB,
    number_color_opacity - RGB + opacity in %
    """
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, size, size)
    context = cairo.Context(surface)

    __draw_background(context, back_color[0]/255, back_color[1]/255, back_color[2]/255, size, size)


    context.set_source_rgba(grid_color[0]/255, grid_color[1]/255, grid_color[2]/255, 1)

    __draw_grid(context, buf, size)


    # Coordinates 
    x = (1-2*buf)/3

    l = [
        ((0.5*x+buf)*size, (0.5*x+buf)*size), ((0.5*x+buf+x)*size, (0.5*x+buf)*size), ((0.5*x+buf+2*x)*size, (0.5*x+buf)*size),
        ((0.5*x+buf)*size, (0.5*x+buf+x)*size), ((0.5*x+buf+x)*size, (0.5*x+buf+x)*size), ((0.5*x+buf+2*x)*size, (0.5*x+buf+x)*size),
        ((0.5*x+buf)*size, (0.5*x+buf+2*x)*size), ((0.5*x+buf+x)*size, (0.5*x+buf+2*x)*size), ((0.5*x+buf+2*x)*size, (0.5*x+buf+2*x)*size)
        ]


    for i in range(1, 10):
        if name[i-1]=='N':
            __draw_number(context, l[i-1][0]-0.02*size, l[i-1][1]+0.02*size, size, i, number_color_opacity)
        elif name[i-1]=='X':
            b = 0.6*0.5
            __draw_X(context, l[i-1][0], l[i-1][1], size, b*x*size, X_color)
        elif name[i-1]=='O':
            __draw_O(context, l[i-1][0], l[i-1][1], size, x*size/3, O_color)

    surface.write_to_png(path + '/' + name + ".jpg")

    return path + '/' + name + ".jpg"
