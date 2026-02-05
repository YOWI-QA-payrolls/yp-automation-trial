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
            cy.get('#bir > [href=""]').click();
            cy.get('#bir_forms > a').click({force: true}); // <--- Use 'force: true' option
            cy.get('[heading="BIR Form No. 1601C"] > .nav-link').click();
            cy.wait(2000);
            cy.get('.active > .panel-body > .col-sm-2 > .form-group > .input-group > .input-group-btn > .btn').click();
            cy.get('.uib-datepicker-popup').contains('February').click();
            cy.get(':nth-child(3) > .input-group-btn > .btn').click();
            cy.get('.active > .panel-body > :nth-child(5) > .btn-group > .btn').click();
        });
    });
  });
  