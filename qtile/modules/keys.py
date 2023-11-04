from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile import extension 

mod = "mod4"
terminal = "alacritty"
my_brownser = "firefox"
mail = "thunderbird"

default_keys = [
    Key([mod], "r", 
        lazy.spawn("rofi -show drun -theme ~/.config/rofi/launchers/type-3/style-1.rasi"),
        ),
    Key([mod,"shift"], "s",
        lazy.spawn("flameshot gui -p /home/a000040/Pictures/Screenshots/"),
        desc="Take screeshot"),
    Key([mod], "b", 
        lazy.spawn(my_brownser), 
        desc="open the default brownser"
        ),
    Key([mod, "shift"], "p", 
        lazy.spawn("flameshot gui -p /home/Pictures/Screenshots")
        ),
    Key([mod], "m",
        lazy.spawn(mail),
        desc = "opens email client"
        ),
    Key([mod], "period", 
        lazy.window.to_next_screen(),
        desc = "go to next screen",
        ),
    Key([mod], "comma",
        lazy.previous_screen(),
        desc = "go to previous screen",
        ),
    # Switch between windows
    Key([mod], "Left", 
        lazy.layout.left(), 
        desc="Move focus to left"
        ),
    Key([mod], "Right", 
        lazy.layout.right(), 
        desc="Move focus to right"
        ),
    Key([mod], "Up", 
        lazy.layout.down(), 
        desc="Move focus down"
        ),
    Key([mod], "Down", 
        lazy.layout.up(), 
        desc="Move focus up"
        ),
    Key([mod], "space", 
        lazy.layout.next(), 
        desc="Move window focus to other window"
        ),

    Key([mod, "shift"], "Left", 
        lazy.layout.shuffle_left(), 
        desc="Move window to the left"
        ),
    Key([mod, "shift"], "Right", 
        lazy.layout.shuffle_right(), 
        desc="Move window to the right"
        ),
    Key([mod, "shift"], "Down", 
        lazy.layout.shuffle_down(), 
        desc="Move window down"
        ),
    Key([mod, "shift"], "Up", 
        lazy.layout.shuffle_up(), 
        desc="Move window up"
        ),
    Key([mod, "control"], "Left", 
        lazy.layout.grow_left(), 
        desc="Grow window to the left"
        ),
    Key([mod, "control"], "Right", 
        lazy.layout.grow_right(), 
        desc="Grow window to the right"
        ),
    Key([mod, "control"], "Down", 
        lazy.layout.grow_down(), 
        desc="Grow window down"
        ),
    Key([mod, "control"], "Up", 
        lazy.layout.grow_up(), 
        desc="Grow window up"
        ),
    Key([mod], "n", 
        lazy.layout.normalize(), 
        desc="Reset all window sizes"
        ),
    Key([mod, "shift"],"Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
        ),
    Key([mod], "Return", 
        lazy.spawn(terminal), 
        desc="Launch terminal"
        ),
    Key([mod], "Tab", 
        lazy.next_layout(), 
        desc="Toggle between layouts"
        ),
    Key([mod], "w", 
        lazy.window.kill(), 
        desc="Kill focused window"
        ),
    Key([mod, "control"], "r", 
        lazy.reload_config(), 
        desc="Reload the config"
        ),
    Key([mod], "q", 
        lazy.spawn("/home/a000040/.config/rofi/powermenu/type-1/powermenu.sh"), 
        desc="Shutdown Qtile"
        ),
    Key([mod], "k", 
            lazy.spawncmd(), 
        desc="Spawn a command using a prompt widget"
        ),
    # window commands 
    
    # media keys
    Key([], 'XF86MonBrightnessUp',   
        lazy.spawn("brillo -q -A 5")
        ),
    Key([], 'XF86MonBrightnessDown', 
        lazy.spawn("brillo -q -U 5")
        ),
    Key([], "XF86AudioMute", 
        lazy.spawn("amixer -q set Master toggle")
        ),
    Key([], "XF86AudioLowerVolume", 
        lazy.spawn("amixer sset Master 5%-")
        ),
    Key([], "XF86AudioRaiseVolume", 
        lazy.spawn("amixer sset Master 5%+")
        ),
    Key([],"XF86AudioPlay",
        lazy.spawn("playerctl play-pause"),
        desc="Play/Pause player",
        ),
    Key([], "XF86AudioNext",
        lazy.spawn("playerctl next"), 
        desc="Skip to next",
        ),
    Key([], "XF86AudioPrev", 
        lazy.spawn("playerctl previous"), 
        desc="Skip to previous"
        ),
    Key([], "XF86Calculator",
        lazy.spawn("rofi -show calc -no-show-match -no-sort -theme ~/.config/rofi/launchers/type-3/style-1.rasi"),
        desc="lauch rofi calculator",
        ),
]

