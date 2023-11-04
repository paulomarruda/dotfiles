from libqtile import widget
from .colors import default_colors
def open_dmenu():
    qtile.cmd_spawn('dmenu_run')
def open_mem():
    qtile.cmd_spawn(terminal + ' -e htop')



default_padding = 5
default_padding_x = default_padding 
default_padding_y = default_padding  
sep_configs = {
        "linewidth":0,
        "padding":default_padding,
        }

widget_list = [
    widget.Sep(**sep_configs), # 0 
    widget.TextBox( # 1
        text="",
        foreground = default_colors["manjaro_green"],
        fontsize=30,
        padding=default_padding,
        mouse_callbacks={'Button1': open_dmenu},
    ),
    widget.Sep(**sep_configs), # 2 
    widget.Sep(**sep_configs), # 3 
    widget.GroupBox(   # 4
        disable_drag = True,
        highlight_method='block',
        borderwidth=5,
        padding_x=5,
        active = default_colors["default_foreground_color"],
        inactive = default_colors["red"],
        rounded = True,
    ),
    widget.Sep(**sep_configs), # 2 
    widget.Prompt(), # 6 
    widget.Sep(**sep_configs), # 7 
    widget.TaskList(), # 8 
    widget.Chord(   # 9 
        chords_colors={
            "launch": ("#ff0000", "#ffffff"),
        },
        name_transform=lambda name: name.upper(),
    ),
    widget.Sep(**sep_configs), # 10 
    widget.Systray(), # 11 
    widget.Sep(**sep_configs), # 12 
    widget.BatteryIcon(), # 13 
    widget.Sep(**sep_configs), # 14 
    widget.TextBox( # 15 
        text="", 
        fontsize=25,
        padding=0, 
    ),
    widget.Memory( # 16 
        foreground = default_colors["default_foreground_color"],
        padding=5,
        measure_mem="G",
        mouse_callbacks={'Button1': open_mem}
    ),
    widget.Sep(**sep_configs), # 14
    widget.TextBox( # 15
        padding=0,
        text="﬙",
        fontsize=30,
    ),
    widget.CPU( # 16
        format="{freq_current}GHz / {load_percent}%"
    ),
    widget.Sep(**sep_configs), # 17 
    widget.Clock(
        format="%a %d-%m %H:%M",
        padding=5,
    ),
    #widget.Sep(**sep_configs),
    #widget.Wttr(),
    widget.Sep(**sep_configs),
    widget.QuickExit(
        fontsize=20,
        default_text="⏻",
        padding=6,
    ),
    widget.Sep(**sep_configs)
]
