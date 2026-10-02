// ==UserScript==
// @name         Google Chrome in navigator.userAgentData
// @description  Add the "Google Chrome" brand that real Chrome reports, matching the Sec-CH-UA header set in config.py
// @match        *://*/*
// @run-at       document-start
// @qute-js-world main
// ==/UserScript==

(() => {
  const uaData = navigator.userAgentData;
  if (!uaData) return;

  // Same version as the user agent set in config.py
  const major = (navigator.userAgent.match(/Chrome\/(\d+)/) || [])[1];
  if (!major) return;
  const addChrome = (brands) =>
    brands
      .filter((b) => b.brand !== "Google Chrome")
      .map((b) => (b.brand === "Chromium" ? { ...b, version: b.version.replace(/^\d+/, major) } : b))
      .concat(brands.length && brands[0].version.includes(".")
        ? [{ brand: "Google Chrome", version: `${major}.0.0.0` }]
        : [{ brand: "Google Chrome", version: major }]);

  const brands = addChrome(uaData.brands);
  const getHighEntropyValues = uaData.getHighEntropyValues.bind(uaData);
  const spoofed = {
    brands,
    mobile: uaData.mobile,
    platform: uaData.platform,
    getHighEntropyValues: async (hints) => {
      const values = await getHighEntropyValues(hints);
      if (values.brands) values.brands = addChrome(values.brands);
      if (values.fullVersionList) values.fullVersionList = addChrome(values.fullVersionList);
      return values;
    },
    toJSON: () => ({ brands, mobile: uaData.mobile, platform: uaData.platform }),
  };
  Object.defineProperty(Navigator.prototype, "userAgentData", { get: () => spoofed, configurable: true });
})();
