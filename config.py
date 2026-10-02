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

# Present qutebrowser as Firefox, because some sites block or degrade
# browsers they don't recognise. Bump the version now and then, since an
# outdated Firefox version can get flagged as well.
import sys
firefox_version = "157.0"
if sys.platform == "darwin":
    firefox_os = "Macintosh; Intel Mac OS X 10.15"
else:
    firefox_os = "X11; Linux x86_64"
c.content.headers.user_agent = (
    f"Mozilla/5.0 ({firefox_os}; rv:{firefox_version}) "
    f"Gecko/20100101 Firefox/{firefox_version}"
)
# Chromium also identifies itself through navigator.userAgentData, which
# Firefox doesn't have; greasemonkey/hide-useragentdata.js hides it.
config.bind(',r', 'config-source')

# Play videos in mpv, which streams through yt-dlp: full quality and no ads,
# also where YouTube only offers 360p in qutebrowser. ,m plays the current
# page, ;m picks a link with hints. Needs mpv and yt-dlp (pacman on Arch,
# Homebrew on macOS). qutebrowser.app on macOS doesn't see Homebrew's PATH,
# so the usual install locations are searched as well.
import shutil
def find_program(name):
    extra_dirs = ["/opt/homebrew/bin", "/usr/local/bin", "/usr/bin"]
    return shutil.which(name) or shutil.which(name, path=":".join(extra_dirs)) or name

mpv = find_program("mpv")
yt_dlp = find_program("yt-dlp")
mpv_cmd = f"spawn {mpv} --script-opts=ytdl_hook-ytdl_path={yt_dlp}"
config.bind(',m', f"{mpv_cmd} {{url}}")
config.bind(';m', f"hint links {mpv_cmd} {{hint-url}}")
c.colors.webpage.darkmode.enabled = False 
c.fonts.default_size = '10pt'
c.fonts.default_family = 'JetBrainsMono Nerd Font'

config.source("gruvbox.py")
