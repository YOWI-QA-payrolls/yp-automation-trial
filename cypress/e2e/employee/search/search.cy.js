// const { describe } = require("mocha");

describe('login', () => {
    // This code will run before each test case in this describe block
    beforeEach(() => {
        // Load login credentials from the fixture file
        cy.viewport(1280, 900);
        cy.fixture('credentials').then(credentials => {
            const { url, email, pass } = credentials;
  
            // Login
            cy.visit(url);
            cy.get('#email').type(email);
            cy.get('#password').type(pass);
            cy.get('#signin-button').click();
            
        });
    });
  
    describe('Daily log', () => {
        it('should search', () => {
          cy.get('#timesheets').click();
          cy.get('#daily_logs > a').click();

         cy.get('tabletoolstrans > .input-group > .form-control').type('juan');
         cy.get('[ng-if="!main.no_search_button"]').click();
        });
    });
  
    // You can add more test cases here for other scenarios
  });
  