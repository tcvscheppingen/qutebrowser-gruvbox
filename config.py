config.load_autoconfig()
c.url.searchengines = {
    "DEFAULT": "https://qwant.com/?q={}", 
    "sp": "https://www.startpage.com/sp/search?q={}", 
    "sx": "http://localhost:8090/search?q={}", 
    "wa": "https://wiki.archlinux.org/?search={}", 
    "yt": "https://www.youtube.com/results?search_query={}"
}
c.tabs.padding = {
    "bottom": 8, 
    "left": 5, 
    "right": 5, 
    "top": 8
}
c.scrolling.smooth = False
# Optional stylesheets can be switched off with ,t (gruvbox) and ,f (font)
def stylesheet_enabled(name):
    return not (config.configdir / f"disabled-{name}").exists()

stylesheets = ["user.css"]
if stylesheet_enabled("gruvbox"):
    stylesheets.append("gruvbox.css")
    # Site-specific additions to the theme in sites/. Each one can switch
    # gruvbox.css off for its own site with `--gruvbox-skip: 1`.
    stylesheets += sorted(
        str(path.relative_to(config.configdir))
        for path in config.configdir.glob("sites/*.css")
    )
if stylesheet_enabled("font"):
    stylesheets.append("font.css")
c.content.user_stylesheets = stylesheets
config.bind(',t', 'spawn --userscript toggle-style gruvbox')
config.bind(',f', 'spawn --userscript toggle-style font')
c.content.dns_prefetch = True
config.bind(',r', 'config-source')
c.colors.webpage.darkmode.enabled = False 
c.fonts.default_size = '10pt'
c.fonts.default_family = 'JetBrains mono Nerd Font'

config.source("gruvbox.py")
