
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
            cy.get('#timesheetreports_list > [href="#"]').click();
            cy.get('#complete_timesheet > a').click();
            //calendar 
            cy.get('.input-group > :nth-child(1) > .btn').click();
            cy.get('.uib-datepicker-popup').contains('10').click();
            cy.get('tabletoolsdaterange2 > .input-group > .form-control.ng-pristine').clear().type('12/29/2023');
            // cy.get('.hand_cursor').click();
            // searchbar
            // cy.get('tabletoolstrans > .input-group > .form-control').type('Juan')
            // cy.get('[ng-if="!main.no_search_button"]').click();

            // adv filter    
            cy.get('[ng-if="!main.no_filter && main.current_module != \'daily_logs\' && ![\'sss_contribution\',\'hdmf_contribution\',\'phic_contribution\', \'remittances_loan\'].includes(main.current_module)"]')
            .click();
            cy.get('.btn-sm').click();

            // column button
            cy.get('span.ng-scope > .btn').click();
            cy.get('.row > :nth-child(1) > .checkbox > label').dblclick();
            cy.get('span.ng-scope > .btn').click();

            // email
            cy.get('div.pull-right > .dropdown-toggle').click();
            cy.get('[ng-if="main.has_send_mail"] > .ng-scope').click();
            cy.get('.cancel').click();
            // cy.get('.confirm').click();

            // Export
            // cy.get('[ng-if="!main.no_export"] > .ng-scope').click();


        });
    });
  
    // You can add more test cases here for other scenarios
  });
  