describe('login', () => {
    // This code will run before each test case in this describe block
    beforeEach(() => {
        // Load login credentials from the fixture file
        cy.viewport(1280, 800);
        cy.fixture('credentials').then(credentials => {
            const { url, email, pass } = credentials;
  
            // Login
            cy.visit(url);
            cy.get(':nth-child(1) > .form-control').type(email);
            cy.get(':nth-child(2) > .form-control').type(pass);
            cy.get('.custom-mb').click();
            
        });
    });
  
    describe('navigate to complete special reports', () => {
        it('go to loan register', () => {
            cy.get('#dmpi_reports_list > [href="#"]').click();
            cy.wait(2000);
            cy.get('#leave_accruals > a').click({ force: true });
            cy.wait(2000);
            cy.get('[ng-click="filter.leave_type = leave_types"] > .fa').click();
            cy.get('.form-group > .btn').click();
        });
    });
  
    // You can add more test cases here for other scenarios
  });
  