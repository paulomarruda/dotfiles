local status, lualine = pcall(require, "lualine")
if not status then 
    print("Lualine not found")
    return 
end

lualine.setup({
    options = {
        theme = "tokyonight",
        section_separators = '', 
        component_separators = '' 
    },
    sections = {
        lualine_a = {'mode'},
        lualine_b = {'branch', 'diff', 'diagnostics'},
        lualine_c = {{'filename', path=1}},
        lualine_x = {'hostname','encoding', 'fileformat', 'filetype'},
        lualine_y = {'progress'},
        lualine_z = {'location'}
  },
})
