const { defineConfig } = require('cypress');

module.exports = defineConfig({
    projectId: "k7nvff", 
  e2e: {
    setupNodeEvents(on, config) {
      // Implement node event listeners here
    },
    baseUrl: 'https://sandbox-ebcom.mci.ir/ecm/ewano/pwa3',
  },
});
