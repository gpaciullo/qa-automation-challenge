
export class LoginPage {
  visit() { cy.visit('/login') }
  username() { return cy.get('#userName') }
  password() { return cy.get('#password') }
  loginBtn() { return cy.get('#login') }
  userNameLabel() { return cy.get('#userName-value') }
}
