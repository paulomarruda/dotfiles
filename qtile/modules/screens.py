from libqtile.config import Screen 
from .bars import default_top_bar as top_bar

default_wallpaper = '~/Pictures/howling_wolf.jpg',
 
default_screen = Screen(
                    wallpaper = default_wallpaper,
                    wallpaper_mode = 'fill',
                    top=top_bar,
)

screens = [
    default_screen,
]
