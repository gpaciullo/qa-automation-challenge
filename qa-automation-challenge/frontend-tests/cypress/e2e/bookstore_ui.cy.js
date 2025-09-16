
import { BooksPage } from './pages/BooksPage'
import { LoginPage } from './pages/LoginPage'
const books = new BooksPage()
const login = new LoginPage()
describe('DemoQA BookStore - UI smoke', () => {
  it('Deve listar livros e permitir busca', () => {
    books.visit()
    books.rows().should('have.length.greaterThan', 1)
    books.searchBox().type('Git Pocket Guide')
    books.rowByTitle('Git Pocket Guide').should('be.visible')
  })
  it('Deve exibir tela de login', () => {
    login.visit()
    login.username().should('be.visible')
    login.password().should('be.visible')
  })
})
