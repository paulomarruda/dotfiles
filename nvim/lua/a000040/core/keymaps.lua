
local keymap = vim.keymap
local opts = { noremap = true, silent = true }
local term_opts = { silent = true }

-- leader key
keymap.set("", "<Space>", "<Nop>", opts)
vim.g.mapleader = " "
vim.g.maplocalleader = " "

-- basic descriptions
--  normal mode         = "n"
--  insert mode         = "i"
--  visual mode         = "v"
--  visual_block_mode   = "x"
--  term_mode           = "t"
--  command_mode        = "c"
------------------------------
--      INSERT MODE
------------------------------
--saving
keymap.set("i", "<C-s>", "<ESC>:update<CR>gi")
--
------------------------------
--      NORMAL MODE
------------------------------
-- saving
keymap.set("n", "<C-s>", ":update<CR>")

-- windows (aka splits)

-- buffers

-- increment decrement numbers by 1
 
keymap.set("n", "<leader>+", "<C-a>") -- increment num
keymap.set("n", "<leader>-", "<C-x>") -- decrement num 

-- nvim tree
keymap.set("n", "<leader>e", ":NvimTreeToggle<CR>")

-- telescope
keymap.set("n", "<leader>ff", "<cmd>Telescope find_files<cr>") -- find files within current working directory, respects .gitignore
keymap.set("n", "<leader>fs", "<cmd>Telescope live_grep<cr>") -- find string in current working directory as you type
keymap.set("n", "<leader>fc", "<cmd>Telescope grep_string<cr>") -- find string under cursor in current working directory
keymap.set("n", "<leader>fb", "<cmd>Telescope buffers<cr>") -- list open buffers in current neovim instance
keymap.set("n", "<leader>fh", "<cmd>Telescope help_tags<cr>") -- list available help tags
