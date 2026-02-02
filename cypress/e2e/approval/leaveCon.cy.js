
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
        it.skip('should search calendar', () => {
             cy.get('#approval_list > [href="#"]').click();
             cy.get('#leave_conversion > a').click();

             //calendar 
             cy.get('.input-group > :nth-child(1) > .btn').click();
             cy.get('thead > :nth-child(1) > :nth-child(1) > .btn').click();
             cy.get('.uib-datepicker-popup').contains('11').click();
             cy.get('tabletoolsdaterange3 > .input-group > .form-control.ng-pristine').clear().type('01/30/2024');
             // cy.get('.hand_cursor').click();
 
                         
             // searchbar
             // cy.get('tabletoolstrans > .input-group > .form-control').type('eyt')
             // cy.get('[ng-if="!main.no_search_button"]').click();
 
             cy.wait(2000);
 
             // adv filter    
             cy.get('[ng-if="!main.no_filter && main.current_module != \'daily_logs\' && ![\'sss_contribution\',\'hdmf_contribution\',\'phic_contribution\', \'remittances_loan\'].includes(main.current_module)"]')
             .click();
             cy.wait(2000);
             cy.get('.col-sm-12 > .btn-success').click();


            //  cy.get('.btn.pull-right').click();
            //  cy.get('.btn-sm').click();
            //  cy.get('.pull-left > .ui-select-container > .select2-choice > .select2-arrow > b').click();
            //  cy.get(':nth-child(5) > .select2-result-label > .ng-binding').click();
            //  cy.get(':nth-child(2) > .ui-select-container > .select2-choice > .select2-arrow > b').click();
            //  cy.get(':nth-child(2) > .select2-result-label > .ng-binding').click();
            //  cy.get('.panel > .panel-footer > .pull-right > .btn').click();

             cy.get('.btn-group > .btn').click();
             cy.get('.col-sm-3 > .ui-select-container > .select2-choice > .select2-arrow > b').click();
             cy.get('.select2-highlighted > .select2-result-label > .ng-binding').click();
             cy.get(':nth-child(2) > .ui-select-container > .select2-choice > .select2-arrow > b').click();
             cy.get('.select2-highlighted > .select2-result-label > .ng-binding').click();
             cy.get('#no_of_days').type('5');
             cy.get(':nth-child(4) > .input-group > .input-group-btn > .btn').click();
             cy.get('.btn-info').click();
             cy.get('.col-sm-1 > .btn').click();
             cy.wait(2000);
             cy.get('.btn-success').click();


        });
    });
  
    // You can add more test cases here for other scenarios
  });
  