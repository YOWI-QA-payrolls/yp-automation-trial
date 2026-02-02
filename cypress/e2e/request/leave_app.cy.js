
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
            cy.get('#leave_request > a').click();

            //calendar 
            cy.get('.input-group > :nth-child(1) > .btn').click();
            cy.get('thead > :nth-child(1) > :nth-child(1) > .btn').click();
            cy.get('.uib-datepicker-popup').contains('10').click();
            cy.get('tabletoolsdaterange2 > .input-group > .form-control.ng-pristine').clear().type('12/21/2024');
            // cy.get('.hand_cursor').click();

                        
            // searchbar
            // cy.get('tabletoolstrans > .input-group > .form-control').type('Juan')
            // cy.get('[ng-if="!main.no_search_button"]').click();

            cy.wait(2000);

            // adv filter    
            cy.get('[ng-if="!main.no_filter && main.current_module != \'daily_logs\' && ![\'sss_contribution\',\'hdmf_contribution\',\'phic_contribution\', \'remittances_loan\'].includes(main.current_module)"]')
            .click();
            // cy.wait(2000);
            cy.get('.col-sm-12 > .btn-success').click();

            // create
            cy.get('.form-group > .btn-group > .btn').click();
            cy.get('.pull-left > .ui-select-container > .select2-choice').click();
            cy.get(':nth-child(2) > .select2-result-label > .ng-binding').click();
            cy.wait(2000);
            cy.get('.col-sm-8 > :nth-child(2) > label').click()
            cy.get(':nth-child(10) > .ui-select-container > .select2-choice > .select2-arrow > b').click();
            cy.get(':nth-child(3) > .select2-result-label > .ng-binding').click();

            cy.get(':nth-child(14) > .form-control').type('testing');
            cy.get('#leave_submit').click();
            cy.get('.cancel').click();
            cy.get('.col-sm-8 > .pull-right > .btn').click();



        });
    });
  
    // You can add more test cases here for other scenarios
  });
  