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
        it('should go to dashboard', function() { this.skip();
            cy.get('#reports_list > [href="#"]').click();
            cy.get('#government_contributions_summary > a').click();
            cy.wait(2000);
            cy.get(':nth-child(2) > .form-group > .input-group > .input-group-btn > .btn').click();
            cy.get('.uib-datepicker-popup').contains('February').click();
            cy.get(':nth-child(3) > .form-group > p.input-group > .input-group-btn > .btn').click();
            cy.get('[style=""] > :nth-child(6) > .form-control').type('1');
            cy.get(':nth-child(5) > :nth-child(3) > .btn-group > a > .btn').click();

            // generate
            // cy.get(':nth-child(4) > :nth-child(3) > .btn-group > a > .btn').click();
        });
    });
  });
  