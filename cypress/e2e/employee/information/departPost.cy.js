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
  
    describe('navigate to complete timesheet', () => {
        it('should search calendar', () => {
            cy.get('#employee_list > a').click(); 
            cy.get('#information_list > a').click();
             cy.get('#employee_department > a').click();

                        
            // searchbar
            // cy.get('tabletoolstrans > .input-group > .form-control').type('caleb')
            // cy.get('[ng-if="!main.no_search_button"]').click();

            cy.wait(2000);

            // adv filter    
            cy.get('#advance-filter-btn')
            .click();
            // cy.wait(2000);
            cy.get('#advance-search').click();

            cy.wait(3000);

            // create
            cy.get('tbody > [style=""] > :nth-child(3)').click();
            cy.get('[ng-click="create(department, \'edit\')] > .fa').click();          


        });
    });
  
    // You can add more test cases here for other scenarios
  });
  