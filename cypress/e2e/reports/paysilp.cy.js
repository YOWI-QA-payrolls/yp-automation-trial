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
  
    describe('navigate to employee', () => {
        it('should go to dashboard', () => {
            cy.get('#reports_list > [href="#"]').click();
            cy.get('#payslip > a').click();
            cy.wait(2000);
            cy.get(':nth-child(1) > .form-group > .ui-select-container > .select2-choice > .select2-arrow > b').click();
            cy.get(':nth-child(4) > .select2-result-label').click();
            cy.wait(2000);
            cy.get(':nth-child(2) > .form-group > .ui-select-container > .select2-choice').click();
            cy.get('.select2-highlighted > .select2-result-label > .ng-binding').click();
            cy.get('.form-group > .btn').click();

            // aaction
            cy.wait(3000);
            
            cy.get('.btn-group > .btn').click();
        });
    });
  });
  