// const { describe } = require("mocha");

describe('login', () => {
    // This code will run before each test case in this describe block
    beforeEach(() => {
        // Load login credentials from the fixture file
        cy.viewport(1280, 800);
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
        it('should edit and delete', () => {
            //edit
          cy.get('#timesheets').click();
          cy.get('#daily_logs > a').click();

          cy.wait(5000);

          cy.get('.input-group > :nth-child(1) > .btn').click();
          cy.get('.uib-datepicker-popup').contains('11').click();
          cy.get('.input-group > :nth-child(5) > .btn').click();
          cy.get('.uib-datepicker-popup').contains('12').click();
          cy.get('.hand_cursor').click(); 

         cy.get('tabletoolstrans > .input-group > .form-control').type('juan');
         cy.get('[ng-if="!main.no_search_button"]').click();

         cy.get(':nth-child(6) > .ng-binding.ng-scope > [ng-if="user_employee != record.employee"] > [ng-click="edit_timesheet_dialog(record,typee.short_code)"]')
         .first()  // or .eq(0)
         .click();
       

         cy.get('.form > :nth-child(1) > .form-control').clear().type('testing');
         cy.get('.pull-right > .btn-success').click();

            //report
            cy.get(':nth-child(19) > .btn').click();
            cy.get('.confirm').click();

         //delete

         cy.get('td[ng-if="user_employee != record.employee"] > .btn').click();
         cy.get('fieldset > input').clear().type('testing');
          cy.get('.confirm').click();



        });
    });
  
    // You can add more test cases here for other scenarios
  });