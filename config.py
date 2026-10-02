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

# Present qutebrowser as Google Chrome, because some sites block or degrade
# browsers they don't recognise. qutebrowser runs on Chromium, so Chrome is
# the identity that matches how it actually connects; the version follows
# the Chromium version qutebrowser is built on.
from qutebrowser.utils import version as qute_version
chrome_major = qute_version.qtwebengine_versions(avoid_init=True).chromium_major
c.content.headers.user_agent = (
    "Mozilla/5.0 ({os_info}) AppleWebKit/{webkit_version} (KHTML, like Gecko) "
    f"Chrome/{chrome_major}.0.0.0 Safari/{{webkit_version}}"
)
# Real Chrome lists "Google Chrome" in its client hints, where qutebrowser
# only lists "Chromium". greasemonkey/chrome-useragentdata.js does the same
# for navigator.userAgentData.
c.content.headers.custom = {
    "Sec-CH-UA": f'"Chromium";v="{chrome_major}", "Not=A?Brand";v="24", '
                 f'"Google Chrome";v="{chrome_major}"',
}
# Chrome doesn't send "Do Not Track" by default, so it stands out
c.content.headers.do_not_track = None
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
