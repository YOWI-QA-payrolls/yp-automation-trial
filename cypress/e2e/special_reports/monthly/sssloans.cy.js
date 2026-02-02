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
 
    describe('Special reports', () => {
        it('loans', () => {
          cy.get('#dmpi_reports_list > [href="#"]').click();
          cy.get('#monthlies_list > [href=""]').click();
          cy.get('#sss_loans > a').click({force: true});
          cy.get('#select_payroll_period').click();
          cy.get('.col-sm-4.ng-scope > .form-group > .ui-select-container > .select2-choices > .select2-search-field > .select2-input').click()
          cy.get('.select2-highlighted > .select2-result-label').click();
          cy.get('.col-sm-1 > .btn').click();
 
         
        });
    });
 
    // You can add more test cases here for other scenarios
  });// const { describe } = require("mocha");
