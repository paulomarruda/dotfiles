-- set vim.opt to set options
local opt = vim.opt 

-- listchar

opt.listchars = {
    tab = '>>',
    space = '·',
    eol = '↲',
}

opt.list = true

-- line numbers
-- ############

-- show absolute numbers 
opt.number = true

-- show relative numbers 
opt.relativenumber = true

-- highlight the cursor line underneath the cursor horizontally
opt.cursorline = true

-- tab config
-- ##########

-- number of visual spaces per TAB
opt.tabstop = 4

-- number of spacesin tab when editing 
opt.softtabstop = 4

-- insert 4 spaces on tab
opt.shiftwidth = 4

-- tabs are spaces, mainly because of python
opt.expandtab = true

-- auto indentation
opt.autoindent = true

-- line wrapping 
-- #############

opt.wrap = false

-- Searching settings
-- ##################

-- casing 
opt.ignorecase = true
opt.smartcase = true


-- general appearance 
-- ##################

-- enable 24-bit RGB color in the TUI (I'm using alacritty)
opt.termguicolors = true

-- background 
opt.background = "dark"

-- left ui column 
opt.signcolumn = "yes"


-- clipboard config 
-- ################

-- access computer clipboard
opt.clipboard:append("unnamedplus")


-- splitting 
-- #########
opt.splitbelow = true
opt.splitright = true

-- more space commandline 
--opt.cmdheight = 2 
