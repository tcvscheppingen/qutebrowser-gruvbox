# Gruvbox dark theme for qutebrowser
# Palette: https://github.com/morhetz/gruvbox

bg0_hard = "#1d2021"
bg0 = "#282828"
bg1 = "#3c3836"
bg2 = "#504945"
bg3 = "#665c54"
fg0 = "#fbf1c7"
fg1 = "#ebdbb2"
fg4 = "#a89984"
gray = "#928374"

red = "#fb4934"
green = "#b8bb26"
yellow = "#fabd2f"
blue = "#83a598"
purple = "#d3869b"
aqua = "#8ec07c"
orange = "#fe8019"
dark_red = "#cc241d"
dark_yellow = "#d79921"
dark_blue = "#458588"

# Completion
c.colors.completion.fg = fg1
c.colors.completion.odd.bg = bg0
c.colors.completion.even.bg = bg0_hard
c.colors.completion.category.fg = yellow
c.colors.completion.category.bg = bg1
c.colors.completion.category.border.top = bg1
c.colors.completion.category.border.bottom = bg1
c.colors.completion.item.selected.fg = bg0
c.colors.completion.item.selected.bg = yellow
c.colors.completion.item.selected.border.top = yellow
c.colors.completion.item.selected.border.bottom = yellow
c.colors.completion.item.selected.match.fg = dark_red
c.colors.completion.match.fg = orange
c.colors.completion.scrollbar.fg = fg4
c.colors.completion.scrollbar.bg = bg1

# Context menu
c.colors.contextmenu.menu.bg = bg0
c.colors.contextmenu.menu.fg = fg1
c.colors.contextmenu.selected.bg = yellow
c.colors.contextmenu.selected.fg = bg0
c.colors.contextmenu.disabled.bg = bg1
c.colors.contextmenu.disabled.fg = gray

# Downloads
c.colors.downloads.bar.bg = bg0
c.colors.downloads.start.fg = bg0
c.colors.downloads.start.bg = blue
c.colors.downloads.stop.fg = bg0
c.colors.downloads.stop.bg = aqua
c.colors.downloads.error.fg = red

# Hints
c.colors.hints.fg = bg0
c.colors.hints.bg = yellow
c.colors.hints.match.fg = fg4
c.hints.border = "1px solid " + bg0_hard
c.colors.keyhint.fg = fg1
c.colors.keyhint.suffix.fg = yellow
c.colors.keyhint.bg = bg0

# Messages
c.colors.messages.error.fg = bg0
c.colors.messages.error.bg = red
c.colors.messages.error.border = red
c.colors.messages.warning.fg = bg0
c.colors.messages.warning.bg = orange
c.colors.messages.warning.border = orange
c.colors.messages.info.fg = fg1
c.colors.messages.info.bg = bg0
c.colors.messages.info.border = bg0

# Prompts
c.colors.prompts.fg = fg1
c.colors.prompts.bg = bg1
c.colors.prompts.border = "1px solid " + bg2
c.colors.prompts.selected.fg = bg0
c.colors.prompts.selected.bg = yellow

# Statusbar
c.colors.statusbar.normal.fg = fg1
c.colors.statusbar.normal.bg = bg0
c.colors.statusbar.insert.fg = bg0
c.colors.statusbar.insert.bg = aqua
c.colors.statusbar.passthrough.fg = bg0
c.colors.statusbar.passthrough.bg = blue
c.colors.statusbar.private.fg = fg1
c.colors.statusbar.private.bg = bg2
c.colors.statusbar.command.fg = fg1
c.colors.statusbar.command.bg = bg0
c.colors.statusbar.command.private.fg = fg1
c.colors.statusbar.command.private.bg = bg2
c.colors.statusbar.caret.fg = bg0
c.colors.statusbar.caret.bg = purple
c.colors.statusbar.caret.selection.fg = bg0
c.colors.statusbar.caret.selection.bg = blue
c.colors.statusbar.progress.bg = aqua
c.colors.statusbar.url.fg = fg1
c.colors.statusbar.url.error.fg = red
c.colors.statusbar.url.hover.fg = orange
c.colors.statusbar.url.success.http.fg = fg1
c.colors.statusbar.url.success.https.fg = green
c.colors.statusbar.url.warn.fg = yellow

# Tabs
c.colors.tabs.bar.bg = bg0_hard
c.colors.tabs.indicator.start = blue
c.colors.tabs.indicator.stop = aqua
c.colors.tabs.indicator.error = red
c.colors.tabs.odd.fg = fg4
c.colors.tabs.odd.bg = bg1
c.colors.tabs.even.fg = fg4
c.colors.tabs.even.bg = bg1
c.colors.tabs.pinned.odd.fg = fg1
c.colors.tabs.pinned.odd.bg = dark_blue
c.colors.tabs.pinned.even.fg = fg1
c.colors.tabs.pinned.even.bg = dark_blue
c.colors.tabs.selected.odd.fg = bg0
c.colors.tabs.selected.odd.bg = yellow
c.colors.tabs.selected.even.fg = bg0
c.colors.tabs.selected.even.bg = yellow
c.colors.tabs.pinned.selected.odd.fg = bg0
c.colors.tabs.pinned.selected.odd.bg = dark_yellow
c.colors.tabs.pinned.selected.even.fg = bg0
c.colors.tabs.pinned.selected.even.bg = dark_yellow

# Background shown while pages load
c.colors.webpage.bg = bg0
