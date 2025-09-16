
const { defineConfig } = require('cypress')
module.exports = defineConfig({
  e2e: { baseUrl: 'https://demoqa.com', viewportWidth: 1366, viewportHeight: 768, video: false, chromeWebSecurity: false, defaultCommandTimeout: 8000 }
})
