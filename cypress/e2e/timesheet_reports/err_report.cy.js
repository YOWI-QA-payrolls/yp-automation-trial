
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
  
    describe('navigate to erroneous timesheet', () => {
        it('should search calendar', () => {
            cy.get('#timesheetreports_list > [href="#"]').click();
            cy.get('#erroneous_timesheet > a').click();
            //calendar 
            cy.get('.input-group > :nth-child(1) > .btn').click();
            cy.get('thead > :nth-child(1) > :nth-child(1) > .btn').click();
            cy.get('.uib-datepicker-popup').contains('29').click();
            // cy.get('tabletoolsdaterange2 > .input-group > .form-control.ng-pristine').clear().type('01/05/2023');
            cy.get('.hand_cursor').click();
            //searchbar
            // cy.get('tabletoolstrans > .input-group > .form-control').type('Juan')
            // cy.get('[ng-if="!main.no_search_button"]').click();

            // adv filter    
            // cy.get('[ng-if="!main.no_filter && main.current_module != \'daily_logs\' && ![\'sss_contribution\',\'hdmf_contribution\',\'phic_contribution\', \'remittances_loan\'].includes(main.current_module)"]')
            // .click();

            // cy.get('.btn-sm').click();

            // toggle button
            // cy.get('span.ng-scope > .btn').click();
            // cy.get('.row > :nth-child(1) > .checkbox > label').dblclick();
            // cy.get('span.ng-scope > .btn').click();

            //edit 
            // cy.get('[ng-show="main.columns.reason.selected"] > .btn').click();
            // cy.get('.form-group > .form-control').clear().type('testing');
            //saave edit
            // cy.get('.btn-success').click();
            // cy.get('.btn-white').click();

            //restore
            // cy.get(':nth-child(10) > .btn').click();
            // confirm
            // cy.get('.confirm').click();
            // cy.get('.cancel').click();

            // delete
            cy.get(':nth-child(11) > .btn').click();
            cy.get('fieldset > input').type('test');
            cy.get('.confirm').click();
            // cy.get('.cancel').click();



        //   cy.get('#daily_logs > a').click();

        //  cy.get('tabletoolstrans > .input-group > .form-control').type('juan');
        //  cy.get('[ng-if="!main.no_search_button"]').click();
        });
    });
  
    // You can add more test cases here for other scenarios
  });
  