
export class BooksPage {
  visit() { cy.visit('/books') }
  searchBox() { return cy.get('#searchBox') }
  rows() { return cy.get('.rt-tbody .rt-tr-group') }
  rowByTitle(title) { return cy.contains('.rt-tbody .rt-tr-group', title) }
}
