describe('login', () => {
    // This code will run before each test case in this describe block
    beforeEach(() => {
        // Load login credentials from the fixture file
        cy.viewport(1280, 900);
        cy.fixture('credentials').then(credentials => {
            const { url, email, pass } = credentials;
  
            // Login
            cy.visit(url);
            cy.get(':nth-child(1) > .form-control').type(email);
            cy.get(':nth-child(2) > .form-control').type(pass);
            cy.get('.custom-mb').click();
            
        });
    });
  
    describe('navigate to employee', () => {
        it('should go to dashboard', () => {
            cy.get('#reports_list > [href="#"]').click();
            cy.get('#employeeledger > a').click();
            cy.wait(2000);
            cy.get('.form-group > .btn').click();
            cy.wait(2000);

            // cy.get('#select_payroll_period').click();
            // cy.get('[ng-click="main.filter.pay_period = main.payroll_histories"]').click();
            cy.get('tabletoolstrans > .input-group > .form-control').type('juan');
            cy.get('.form-group > .btn').click();
        });
    });
  });
  