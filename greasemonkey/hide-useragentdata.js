// ==UserScript==
// @name         Hide navigator.userAgentData
// @description  Firefox has no navigator.userAgentData; hide Chromium's so it doesn't contradict the Firefox user agent set in config.py
// @match        *://*/*
// @run-at       document-start
// @qute-js-world main
// ==/UserScript==

delete Navigator.prototype.userAgentData;
