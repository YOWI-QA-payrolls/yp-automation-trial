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
            cy.get('#employee_status_list > [href=""]').click();
            cy.wait(2000);
            
            // Make the parent ul.nav.nav-third-level.collapse visible
            cy.get('ul.nav.nav-third-level.collapse').invoke('css', 'display', 'block'); // or 'flex'
            
            // Click on the New Hire link
            cy.get('#separated > a').click();
            cy.wait(2000);
            cy.get('.form-group > .btn').click();
            cy.get('tabletoolstrans > .input-group > .form-control').type('wow');
            cy.get('[ng-if="!main.no_search_button"]').click();
        });
    });
  });
  