from libqtile import bar 
from .widgets import widget_list
from .colors import default_colors
default_opacity = 1.0
default_bar_size = 30

default_top_bar = bar.Bar(
    widgets = widget_list,
    background = default_colors["default_background_color"],
    opacity = default_opacity,
    size = default_bar_size,
)

