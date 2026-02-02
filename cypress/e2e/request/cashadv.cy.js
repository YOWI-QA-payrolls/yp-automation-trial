
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
            cy.get('#requests_list > [href="#"] > .nav-label').click();
            cy.get('#cash_advance_request > a').click();

            //calendar 
            cy.get('.input-group > :nth-child(1) > .btn').click();
            cy.get('thead > :nth-child(1) > :nth-child(1) > .btn').click();
            cy.get('thead > :nth-child(1) > :nth-child(3) > .btn').click();
            cy.get('.uib-datepicker-popup').contains('8').click();
            cy.get('tabletoolsdaterange3 > .input-group > .form-control.ng-pristine').clear().type('01/08/2024');
            // cy.get('.hand_cursor').click();

                        
            // searchbar
            cy.get('tabletoolstrans > .input-group > .form-control').type('caleb')
            // cy.get('[ng-if="!main.no_search_button"]').click();

            cy.wait(2000);

            // adv filter    
            cy.get('[ng-if="!main.no_filter && main.current_module != \'daily_logs\' && ![\'sss_contribution\',\'hdmf_contribution\',\'phic_contribution\', \'remittances_loan\'].includes(main.current_module)"]')
            .click();
            // cy.wait(2000);
            cy.get('.col-sm-12 > .btn-success').click();

            // create
            cy.get('.form-group > .btn').click();
            cy.get('.align_left > :nth-child(1) > .col-sm-3 > .ui-select-container > .select2-choice > .select2-arrow > b').click();

            // Click on a specific item in a dropdown
            cy.get('.select2-highlighted > .select2-result-label > .ng-binding').click();

            // Click on a dropdown to open it
            cy.get('[ng-if="main.record.cash_advance_type == \'regular\' || !main.record.id"] > :nth-child(1) > :nth-child(1) > .ui-select-container > .select2-choice > .select2-arrow > b').click();

            // Click on a specific item in a different dropdown
            cy.get('.select2-highlighted > .select2-result-label > .ng-binding').click();

            // Type '1500' into an input field
            cy.get('#input_list_amount').type('1500');

            // Click a button
            cy.get(':nth-child(3) > .input-group > .input-group-btn > .btn').click();
            cy.get('#page-top div.modal.fade.in div.panel-body table tbody tr:nth-child(2) td div div:nth-child(1) div:nth-child(3) p div ul').contains('21').click();
            cy.get('#input_list_amount_to_').type('testing');
            cy.get('.radio > label').click();
            cy.get('.col-sm-3.form-group > :nth-child(4) > label').click();
            cy.get('.col-sm-5 > .form-control').type('500');
            cy.get('.col-sm-12 > :nth-child(1) > .input-group > .input-group-btn > .btn').click();
            cy.get('.btn-group > .btn-info').click();
            cy.get('.btn-success').click();
          







        });
    });
  
    // You can add more test cases here for other scenarios
  });
  