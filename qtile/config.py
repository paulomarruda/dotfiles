# -*- coding: utf-8 -*-
from typing import List
import os 
import re
import subprocess
import socket
from libqtile import bar, layout, widget, hook, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile.log_utils import logger
from libqtile import qtile
#from libqtile.utils import guess_terminal
from modules.keys import mod, terminal, my_brownser, mail, default_keys as keys

@hook.subscribe.startup_once
def autostart():
    logger.warning("In autostart function")
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

groups = [Group(i) for i in "1234567"]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key([mod, "shift"],i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(border_focus=["#ffffff"], 
                   border_width=3, 
                   margin_on_single=10, 
                   margin=4),
   
    layout.Max(border_focus=["#ffffff"], border_width=2, margin=8),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="JetBrains Mono Nerd Fonts",
    fontsize=14,
    padding=5,
)
extension_defaults = widget_defaults.copy()
colors = [
            ["#ffffff", "#ffffff"],
            ["#cc0000", "#cc0000"],
            ["#1de9b6", "#1de9b6"], # manjaro green
            ["#b8bab9", "#b8bab9"],
            ]
def open_rofi():
    qtile.cmd_spawn('rofi -show drun')
def open_mem():
    qtile.cmd_spawn(terminal + ' -e bashtop')

sep_configs = {
        "linewidth":0,
        "padding":6,
        }

def init_widgets_list():
    widgets_list = [
        widget.Sep(**sep_configs), # 0 
        widget.TextBox( # 1
            text="",
            foreground = colors[2],
            fontsize=30,
            padding=5,
            mouse_callbacks={'Button1': open_rofi},
        ),
        widget.Sep(**sep_configs), # 2 
        widget.Sep(**sep_configs), # 3 
        widget.GroupBox(   # 4
            disable_drag = True,
            highlight_method='block',
            borderwidth=5,
            padding_x=5,
            #background = "#53548c",
            active = colors[1],
            inactive = colors[3],
            rounded = True,
        ),
        widget.Sep(**sep_configs), # 5 

        widget.Prompt(
                
            ), # 6 
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
            foreground = colors[0],
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
    return widgets_list
def init_widgets_screen_1():
    widgets_screen_1 = init_widgets_list()
    return widgets_screen_1
def init_widgets_screen_2():
    widgets_screen_2 = init_widgets_list()
    del widgets_screen_2[11]
    return widgets_screen_2 
def init_screens():
    return [
            Screen(
                    wallpaper = '~/Pictures/archlinux-digital-art-linux-arch-linux-tech-hd-wallpaper-1f0cb881ced8a6f444c7620593386e99.jpg',
                    wallpaper_mode = 'fill',
                    #top=bar.Bar(widgets=init_widgets_screen_1(), 
                    #opacity = 1.0,
                    #size = 30,
                    #border_width = 1,
                    #border_color = colors[1])
                    ),
            #             Screen(
            #        wallpaper = '~/Pictures/howling_wolf.jpg',
            #        wallpaper_mode = 'fill',
            #        top=bar.Bar(widgets=init_widgets_screen_2(), 
            #        opacity = 1.0,
            #        size = 30,
            #        border_width = 1,
            #        border_color = colors[1]
            #        )),

            ]
if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_screen1 = init_widgets_screen_1()
    widgets_screen2 = init_widgets_screen_2()


# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

