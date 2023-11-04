local status_mason, mason = pcall(require, "mason")
if not status_mason then
    return
end

mason.setup()

local status_mlsp, mlsp = pcall(require, "mason-lspconfig")
if not status_mlsp then
    return
end 

mlsp.setup({
    ensure_installed = {
        "bashls",
        "clangd",
        "cmake",
        "fortls",
        "pyright",
        "rust_analyzer",
    },
})
