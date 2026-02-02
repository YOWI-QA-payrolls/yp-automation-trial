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
            cy.get('#employee_logs_monitoring > a').click();
            cy.wait(2000);
            cy.get('.input-group > :nth-child(1) > .btn').click();
            cy.wait(1000); // Waits for 1 second
            cy.get('thead > :nth-child(1) > :nth-child(1) > .btn').click();
            cy.wait(1000); // Waits for 1 second
            cy.get('.uib-datepicker-popup').contains('1').click();
            cy.get(':nth-child(8) > .btn').click();
            

        });
    });
  });
  