local status_ts, ts = pcall(require, "nvim-treesitter.configs")
if not status_ts then 
    return
end

ts.setup({
    ensure_installed = { 
        "c", 
        "bash",
        "lua",
        "cpp",
        "fortran",
        "gitignore",
        "python",
        "rust",
    },
    highlight = {
        enable = true,
        -- Setting this to true will run `:h syntax` and tree-sitter at the same time.
        -- Set this to `true` if you depend on 'syntax' being enabled (like for indentation).
        -- Using this option may slow down your editor, and you may see some duplicate highlights.
        -- Instead of true it can also be a list of languages
        additional_vim_regex_highlighting = false,
    },
    indent = {
        enable = true,
    },
})
-- folding 
-- vim.opt.foldmethod = "expr"
-- vim.opt.foldexpr = "nvim_treesitter#folderexpr()"
