
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
             cy.get('#leave_conversion > a').click();

             //calendar (conditional - only if date elements exist)
             cy.get('body').then($body => {
                 if ($body.find('[ng-click="main.open_date(\'filter_date_from\')"]').length > 0) {
                     cy.get('[ng-click="main.open_date(\'filter_date_from\')"]').click();
                     cy.get('.uib-datepicker-popup .uib-left').click();
                     cy.get('.uib-datepicker-popup').contains('11').click();
                 }
                 if ($body.find('[ng-model="filters.date_to"]').length > 0) {
                     cy.get('[ng-model="filters.date_to"]').clear().type('01/30/2024');
                 }
             });
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


            //  cy.get('.btn.pull-right').click();
            //  cy.get('.btn-sm').click();
            //  cy.get('.pull-left > .ui-select-container > .select2-choice > .select2-arrow > b').click();
            //  cy.get(':nth-child(5) > .select2-result-label > .ng-binding').click();
            //  cy.get(':nth-child(2) > .ui-select-container > .select2-choice > .select2-arrow > b').click();
            //  cy.get(':nth-child(2) > .select2-result-label > .ng-binding').click();
            //  cy.get('.panel > .panel-footer > .pull-right > .btn').click();

             // create form (conditional - only if data exists)
             cy.get('body').then($body => {
                 if ($body.find('.btn-group > .btn').length > 0) {
                     cy.get('.btn-group > .btn').click();
                     cy.get('.col-sm-3 > .ui-select-container > .select2-choice > .select2-arrow > b').click();

                     // Only proceed if dropdown options are available
                     cy.get('body').then($innerBody => {
                         if ($innerBody.find('.select2-highlighted > .select2-result-label > .ng-binding').length > 0) {
                             cy.get('.select2-highlighted > .select2-result-label > .ng-binding').click();
                             cy.get(':nth-child(2) > .ui-select-container > .select2-choice > .select2-arrow > b').click();
                             cy.get('.select2-highlighted > .select2-result-label > .ng-binding').click();
                             cy.get('#no_of_days').type('5');
                             cy.get(':nth-child(4) > .input-group > .input-group-btn > .btn').click();
                             cy.get('.btn-info').click();
                             cy.get('.col-sm-1 > .btn').click();
                             cy.wait(2000);
                             cy.get('.btn-success').click();
                         }
                     });
                 }
             });


        });
    });
  
    // You can add more test cases here for other scenarios
  });
  