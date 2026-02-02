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
  
    describe('navigate to complete special reports', () => {
        it('go to loan register', function() { this.skip();
            cy.get('#dmpi_reports_list > [href="#"]').click();
            cy.wait(2000);
            cy.get('#quincenal_list > [href=""]').click({ force: true });
            cy.get('#union_dues_checkoff_lists > a').click();
            cy.get('.select2-search-field > .select2-input').click();
            cy.get('.select2-highlighted > .select2-result-label').click();
            cy.wait(2000);
            cy.get(':nth-child(3) > .form-group > .btn').click();

        });
    });
  
    // You can add more test cases here for other scenarios
  });
  