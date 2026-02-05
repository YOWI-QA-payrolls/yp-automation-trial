
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
  
    describe('navigate to overtime timesheet', () => {
        it('should search calendar', () => {
             cy.get('#approval_list > a').click();

             // intercept API call for cash advance data
             cy.intercept('POST', '**/cash_advance/read_pagination/**').as('loadData');
             cy.get('#cash_advance_approval > a').click();

             // wait for API call to complete
             cy.wait('@loadData');

             //calendar
             cy.get('[ng-click="main.open_date(\'filter_date_from\')"]').click();
             cy.get('.uib-datepicker-popup .uib-left').click();
             cy.get('.uib-datepicker-popup').contains('11').click();
             cy.get('[ng-model="main.filters.date_to"]').clear().type('01/30/2024');
             // cy.get('.hand_cursor').click();
 
                         
             // searchbar
             // cy.get('#search-input').type('eyt')
             // cy.get('#advance-search').click();
 
             cy.wait(2000);
 
             // adv filter
             cy.get('#advance-filter-btn')
             .click();
             cy.wait(2000);
             cy.get('#advance-search').click();
 
            //  auto approval - only if options exist
            cy.get('[ng-model="main.auto_approval"] .select2-choice').click();
             cy.get('body').then($body => {
                 if ($body.find('#ui-select-choices-0 li').length > 0) {
                     cy.get('#ui-select-choices-0 li:nth-child(3)').click();
                     cy.get('#auto_approval').click();
                     cy.get('[ng-click="main.submit_auto_approval()"]').click();
                     cy.get('.confirm').click();
                 } else {
                     // close dropdown if no options
                     cy.get('[ng-model="main.auto_approval"] .select2-choice').click();
                 }
             });
   
 
            //  // popup approve
            //  cy.get('tbody > [style=""] > :nth-child(4)').click();
            //  cy.get('span.ng-scope > :nth-child(1) > label').click();
            //  cy.get('#leave_submit').click();
            //  cy.wait(3000);
            //  cy.get('.confirm').click();

        });
    });
  
    // You can add more test cases here for other scenarios
  });
  