local ensure_packer = function()
  local fn = vim.fn
  local install_path = fn.stdpath('data')..'/site/pack/packer/start/packer.nvim'
  if fn.empty(fn.glob(install_path)) > 0 then
    fn.system({'git', 'clone', '--depth', '1', 'https://github.com/wbthomason/packer.nvim', install_path})
    vim.cmd [[packadd packer.nvim]]
    return true
  end
  return false
end

local packer_bootstrap = ensure_packer()

return require('packer').startup(function(use)
    use('wbthomason/packer.nvim')
    -- better icons and tree 
    use("nvim-tree/nvim-web-devicons")
    use("nvim-tree/nvim-tree.lua")
    -- tree-sitter
    use("nvim-treesitter/nvim-treesitter")
    -- colorschemes 
    use("folke/tokyonight.nvim")
    use { "catppuccin/nvim", as = "catppuccin"} 
    -- indentation lines
    use("lukas-reineke/indent-blankline.nvim")
    -- raimbow delimiters
    use("HiPhish/rainbow-delimiters.nvim")
    -- code for colors appear as colors
    use("norcalli/nvim-colorizer.lua")
    -- telescope
    use("nvim-lua/plenary.nvim")
    use("nvim-telescope/telescope.nvim")
    -- status bar with lualine
    use("nvim-lualine/lualine.nvim")
    -- make surrounds
    use("kylechui/nvim-surround")
    -- notify 
    use("rcarriga/nvim-notify")
    -- commentary
    use("tpope/vim-commentary")
    use('ThePrimeagen/vim-be-good')
    use {'akinsho/bufferline.nvim', tag = "*", requires = 'nvim-tree/nvim-web-devicons'}
    -- wrapping text like documents
    use({"andrewferrier/wrapping.nvim"})

    -------------------------------
    -- lsp, cmp, snip
    use("williamboman/mason.nvim")
    use("williamboman/mason-lspconfig.nvim")
    use("neovim/nvim-lspconfig")
    use('hrsh7th/nvim-cmp')
    use('hrsh7th/cmp-buffer')
    use('hrsh7th/cmp-path')
    use('hrsh7th/cmp-nvim-lsp')
    use('L3MON4D3/LuaSnip')
    use('willothy/moveline.nvim', { run = 'make' })

    if packer_bootstrap then
        require('packer').sync()
    end
end)
