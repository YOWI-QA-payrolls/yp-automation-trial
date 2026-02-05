
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
  
    describe('navigate to incomplete timesheet', () => {
        it('should search calendar', () => {
            cy.get('#timesheetreports_list > [href="#"]').click();
            cy.get('#incomplete_timesheet > a').click();
            //calendar 
            cy.get('[ng-click="main.open_date(\'filter_date_from\')"]').click();
            cy.get('.uib-datepicker-popup .uib-left').click();
            // cy.get('[ng-click="main.open_date(\'filter_date_from\')"]').clear();
            cy.get('.uib-datepicker-popup').contains('10').click();
            // cy.get('tabletoolsdaterange2 > .input-group > .form-control.ng-pristine').clear().type('12/29/2023');
            cy.get('.hand_cursor').click();
            // searchbar
            cy.get('tabletoolstrans > .input-group > .form-control').type('Juan')
            // cy.get('[ng-if="!main.no_search_button"]').click();

            // adv filter    
            cy.get('#advance-filter-btn')
            .click();

            cy.get('.btn-sm').click();

            // toggle button
            // cy.get('span.ng-scope > .btn').click();
            // cy.get('.row > :nth-child(1) > .checkbox > label').dblclick();
            // cy.get('span.ng-scope > .btn').click();

        });
    });
  
    // You can add more test cases here for other scenarios
  });
  