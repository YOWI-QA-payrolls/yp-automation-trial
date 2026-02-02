
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
        it('should search calendar', function() { this.skip();
            cy.get('#requests_list > [href="#"] > .nav-label').click();
            cy.get('#transfer_request > a').click();

            //calendar 
            cy.get('.input-group > :nth-child(1) > .btn').click();
            cy.get('thead > :nth-child(1) > :nth-child(1) > .btn').click();
            cy.get('thead > :nth-child(1) > :nth-child(3) > .btn').click();
            cy.get('.uib-datepicker-popup').contains('8').click();
            cy.get('tabletoolsdaterange2 > .input-group > .form-control.ng-pristine').clear().type('01/08/2024');
            // cy.get('.hand_cursor').click();

                        
            // searchbar
            cy.get('tabletoolstrans > .input-group > .form-control').type('aria')
            // cy.get('[ng-if="!main.no_search_button"]').click();

            cy.wait(2000);

            // adv filter    
            cy.get('[ng-if="!main.no_filter && main.current_module != \'daily_logs\' && ![\'sss_contribution\',\'hdmf_contribution\',\'phic_contribution\', \'remittances_loan\'].includes(main.current_module)"]')
            .click();
            // cy.wait(2000);
            cy.get('.col-sm-12 > .btn-success').click();

            cy.get('.iCheck-helper').click();
            cy.get('.select2-arrow > b').click();
            cy.get(':nth-child(2) > .select2-result-label').click();
            cy.get('.select2-arrow > b').click();
            cy.get(':nth-child(1) > .select2-result-label > .ng-binding').click();


            // create
            cy.get('.form-group > .btn-group > .btn').click();
            cy.get(':nth-child(2) > .input-group > .input-group-btn > .btn').click();
            cy.get('.btn-info').click();
            cy.get(':nth-child(5) > .ui-select-container > .select2-choice > .select2-arrow > b').click();
            cy.get(':nth-child(2) > .select2-result-label > .ng-binding').click();
            cy.get('.select2-choices').click();
            cy.get(':nth-child(4) > .select2-result-label > .ng-binding').click();

            cy.get('tr.ng-scope > :nth-child(1) > .ui-select-container > .select2-choice > .select2-arrow > b').click();
            cy.get('.select2-result-label > .ng-binding').click();
            cy.get('.col-sm-6 > .form-control').type('testing');
            cy.get(':nth-child(2) > .ng-isolate-scope > .uib-timepicker > tbody > :nth-child(2) > .hours > .form-control').type('08')
            cy.get(':nth-child(2) > .ng-isolate-scope > .uib-timepicker > tbody > :nth-child(2) > .minutes > .form-control').type('30');
            cy.get(':nth-child(3) > .ng-isolate-scope > .uib-timepicker > tbody > :nth-child(2) > .hours > .form-control').type('17');
            cy.get(':nth-child(3) > .ng-isolate-scope > .uib-timepicker > tbody > :nth-child(2) > .minutes > .form-control').type('30');
            cy.get(':nth-child(6) > span > .btn').click();
            cy.get('#leave_submit').click();
            cy.get('.cancel').click();
            cy.get('.col-sm-8 > .pull-right > .btn').click();







        });
    });
  
    // You can add more test cases here for other scenarios
  });
  