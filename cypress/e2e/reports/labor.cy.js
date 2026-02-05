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
            cy.get('#labor_summary > a').click();
            cy.wait(2000);
            cy.get('.select2-chosen.ng-binding').click();
            cy.get(':nth-child(4) > .select2-result-label > .ng-binding.ng-scope').click();
            cy.get('#advance-search').click();
            cy.get(':nth-child(6) > .btn').click();
        });
    });
  });
  