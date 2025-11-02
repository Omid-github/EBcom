// cypress.config.cjs
const { defineConfig } = require('cypress');

module.exports = defineConfig({
  e2e: {
    baseUrl: 'https://sandbox-ebcom.mci.ir/ecm/ewano/pwa3', // your URL
    specPattern: 'cypress/e2e/Test/*.cy.js',               // your test files
    browser: 'chrome',
    chromeWebSecurity: false,        // allows cross-origin and insecure connections
    insecureSkipTlsVerify: true,     // skips invalid SSL/TLS certificate checks
    requestTimeout: 10000,           // increase request timeout to 10s
    responseTimeout: 10000,          // increase response timeout to 10s
    retries: {
      runMode: 2,                    // retry twice in CI if server is slow
      openMode: 0,
    },
  },
});
