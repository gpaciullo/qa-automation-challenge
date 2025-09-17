// frontend-tests/cypress/support/e2e.js

// Ignora erros de JS que vêm de scripts de anúncio / terceiros,
// para não quebrar o teste quando a app não controla esse código.
Cypress.on('uncaught:exception', (err) => {
  const msg = String(err && (err.message || err));
  if (
    msg.includes('adplus') ||
    msg.includes('setup is not a function') ||
    msg.includes('org.freedesktop')
  ) {
    return false; // impede que o teste falhe por isso
  }
});
