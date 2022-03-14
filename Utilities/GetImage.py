import cairo
from math import pi


def Generate(name: str, WIDTH: int = 800, HEIGHT: int = 800) -> str:
    """
    Возвращает расположения картинки относительно запускаемого файла.
    """

    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, WIDTH, HEIGHT)
    ctx = cairo.Context(surface)

    ctx.scale(WIDTH, HEIGHT)  # Normalizing the canvas


    buf = 0.05
    x = (1-2*buf)/3


    ctx.move_to(buf, x+buf)
    ctx.line_to(1-buf, x+buf)

    ctx.move_to(buf, 2*x+buf)
    ctx.line_to(1-buf, 2*x+buf)

    ctx.move_to(x+buf, buf)
    ctx.line_to(x+buf, 1-buf)   

    ctx.move_to(2*x+buf, buf)
    ctx.line_to(2*x+buf, 1-buf)



    # координаты 1, 2, 3, 4, ..., 9
    l = [
        (0.5*x+buf, 0.5*x+buf), (0.5*x+buf+x, 0.5*x+buf), (0.5*x+buf+2*x, 0.5*x+buf),
        (0.5*x+buf, 0.5*x+buf+x), (0.5*x+buf+x, 0.5*x+buf+x), (0.5*x+buf+2*x, 0.5*x+buf+x),
        (0.5*x+buf, 0.5*x+buf+2*x), (0.5*x+buf+x, 0.5*x+buf+2*x), (0.5*x+buf+2*x, 0.5*x+buf+2*x)
        ]


    ctx.set_font_size(0.08)
    ctx.select_font_face("Arial",
                        cairo.FONT_SLANT_NORMAL,
                        cairo.FONT_WEIGHT_NORMAL)

    for i in range(1, 10):
        if name[i-1]=='N':
            ctx.set_source_rgba(1, 1 , 1, 0.5)
            ctx.move_to(l[i-1][0]-0.02, l[i-1][1]+0.02)
            ctx.show_text(str(i))
        elif name[i-1]=='X':
            ctx.set_source_rgba(1, 1, 1, 0)
            b = 0.6*0.5
            ctx.move_to(l[i-1][0]-x*b, l[i-1][1]-x*b)
            ctx.line_to(l[i-1][0]+x*b, l[i-1][1]+x*b)
            ctx.move_to(l[i-1][0]+x*b, l[i-1][1]-x*b)
            ctx.line_to(l[i-1][0]-x*b, l[i-1][1]+x*b)
        if name[i-1]=='O':
            ctx.set_line_width(0.1)
            ctx.set_source_rgba(1, 1, 1, 0)
            ctx.move_to(l[i-1][0]+x/3, l[i-1][1])
            ctx.arc(l[i-1][0], l[i-1][1], x/3, 0, 2*pi)


    ctx.set_source_rgb(1, 1, 1)  # Solid color
    ctx.set_line_width(0.005)
    ctx.stroke()

    relevant_path = r"TelegramImages\\"+name+".jpg"

    surface.write_to_png(relevant_path)  # Output to PNG

    return relevant_path
