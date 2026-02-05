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
  
    describe('Daily log', () => {
        it('should search employee per p', () => {
          cy.get('#timesheets').click();
          cy.get('#daily_logs > a').click();
          cy.wait(5000);
          cy.get('[ng-click="main.open_date(\'filter_date_from\')"]').click();
          cy.get('.uib-datepicker-popup').contains('13').click();
          cy.get('.input-group > :nth-child(5) > .btn').click();
          cy.get('.uib-datepicker-popup').contains('19').click();
          cy.get('.select2-choice').click();
          cy.get('.select2-highlighted > .select2-result-label > .ng-binding').click();
          cy.get('.select2-choice').click();
          cy.get(':nth-child(1) > .select2-result-label > .ng-binding').click();
          cy.get('[ng-if="!main.no_search_button"]').click(); 
        });
    });
  
    // You can add more test cases here for other scenarios
  });
  