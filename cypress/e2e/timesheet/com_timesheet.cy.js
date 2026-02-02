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
      it.skip('should create complete timesheet', () => {
        cy.get('#timesheets').click();
        cy.get('#daily_logs > a').click();
        cy.wait(3000)
        cy.get(':nth-child(3) > .btn-group > .btn').click();
        cy.get('.btn-group > .dropdown-menu > li > a').click();
        cy.get('#by_date_range').click();
        cy.get(':nth-child(3) > .form-control').type('manual');
        cy.get('[ng-click="complete_timesheet.employees = filter_employees2;get_employee_schedule(complete_timesheet)"] > .fa').click();
        cy.get(':nth-child(9) > :nth-child(3) > label').click();
        cy.get('.pull-right > .btn-success').click();

        
      });
  });

  // You can add more test cases here for other scenarios
});
