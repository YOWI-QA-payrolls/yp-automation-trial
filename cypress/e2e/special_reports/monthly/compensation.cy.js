// const { describe } = require("mocha");


describe('login', () => {
    // This code will run before each test case in this describe block
    beforeEach(() => {
        // Load login credentials from the fixture file
        cy.fixture('credentials').then(credentials => {
            const { url, email, pass } = credentials;
 
            // Login
            cy.visit(url);
            cy.get('#email').type(email);
            cy.get('#password').type(pass);
            cy.get('#signin-button').click();
           
        });
    });
 
    describe('Special reports', () => {
        it('loans', function() { this.skip();
          cy.get('#dmpi_reports_list > [href="#"]').click();
          cy.get('#monthlies_list > [href=""]').click();
          cy.get('#compensation_items > a').click({force: true});
          cy.get('label > .ng-pristine').click();
          cy.get('.select2-choices').click();
          cy.get('.select2-highlighted > .select2-result-label').click();
          cy.wait(2000);
          cy.get(':nth-child(3) > .btn').click();
         
        });
    });
 
    // You can add more test cases here for other scenarios
  });// const { describe } = require("mocha");
 
