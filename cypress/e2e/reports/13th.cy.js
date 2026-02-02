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
        it.skip('should go to dashboard', () => {
            cy.get('#reports_list > [href="#"]').click();
            cy.get('#bonus > a').click();
            cy.wait(2000);
            cy.get('.col-sm-3 > .form-group > .ui-select-container > .select2-choice > .select2-chosen.ng-binding').click();
            cy.get('.select2-highlighted > .select2-result-label').click();
            cy.get('tabletoolstrans > .input-group > .form-control').type('juan');
            cy.get('.form-group > .btn').click();
            cy.wait(5000);
            cy.get('[style=""] > [ng-click="details_dialog(record)"]').click();
            cy.get('.panel > .panel-footer > .pull-right > .btn').click();
        });
    });
  });
  