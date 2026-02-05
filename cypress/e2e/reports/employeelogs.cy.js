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
            cy.get('#employee_logs_monitoring > a').click();
            cy.wait(2000);
            cy.get('[ng-click="main.open_date(\'filter_date_from\')"]').click();
            cy.wait(1000); // Waits for 1 second
            cy.get('.uib-datepicker-popup .uib-left').click();
            cy.wait(1000); // Waits for 1 second
            cy.get('.uib-datepicker-popup').contains('1').click();
            cy.get(':nth-child(8) > .btn').click();
            

        });
    });
  });
  