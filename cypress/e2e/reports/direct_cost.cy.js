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
            cy.get('#direct_cost > a').click();
            cy.wait(2000);
            cy.get('.form-group > .btn').click();
            cy.wait(2000);

            cy.get('#select_payroll_period').click();
            cy.get('[ng-click="main.filter.pay_period = main.payroll_histories"]').click();
            cy.get('.form-group > .btn').click();
        });
    });
  });
  