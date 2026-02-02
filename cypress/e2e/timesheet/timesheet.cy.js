// const { describe } = require("mocha");

describe('login', () => {
  // This code will run before each test case in this describe block
  beforeEach(() => {
      // Load login credentials from the fixture file
      cy.fixture('credentials').then(credentials => {
          const { url, email, pass } = credentials;

          // Login
          cy.visit(url);
          cy.get(':nth-child(1) > .form-control').type(email);
          cy.get(':nth-child(2) > .form-control').type(pass);
          cy.get('.custom-mb').click();
          
      });
  });

  describe('Daily log', () => {
      it('should create timesheet', () => {
        cy.get('#timesheets').click();
        cy.get('#daily_logs > a').click();

        cy.wait(5000);

        //create timesheet
        cy.get('#page-wrapper > div.row.wrapper.border-bottom.white-bg.page-heading > div.col-sm-4 > div > div > div > button')
        .click()
        .debug(); // Execution pauses here, allowing you to interact with the Cypress command line

        cy.get('.form > :nth-child(1) > .input-group > .input-group-btn > .btn')
        .click();
        cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > div:nth-child(1) > p.input-group > div')
        .contains('5').click();

          cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > div:nth-child(5) > div > a > span.select2-arrow.ui-select-toggle')
            .click();
          cy.get(':nth-child(6) > .select2-result-label > .ng-binding').click();

          cy.get(':nth-child(6) > .form-control').clear().type('manual');
          cy.get('.form > :nth-child(7) > .ui-select-container > .select2-choice').click();
          cy.get('.select2-highlighted > .select2-result-label > .ng-binding').click();
          cy.get('.hours > .form-control').type('8');
          cy.get('.minutes > .form-control').type('30');
          cy.get('.pull-right > .btn-success').click();
      

        
      });
  });

  // You can add more test cases here for other scenarios
});