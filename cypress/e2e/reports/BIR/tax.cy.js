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
            cy.get('#bir > [href=""]').click();
            cy.get('#tax_report > a').click({force: true}); // <--- Use 'force: true' option
            cy.wait(2000);
            // cy.get(':nth-child(2) > .form-group > .input-group > .input-group-btn > .btn').click();
            // generate
            cy.get('tabletoolstrans > .input-group > .form-control').type('Juan');
            // cy.get(':nth-child(4) > :nth-child(3) > .btn-group > a > .btn').click();
            cy.get('[ng-if="!main.no_search_button"]').click();
            cy.get('tbody > [style=""] > :nth-child(3)').click();
        });
    });
  });
  