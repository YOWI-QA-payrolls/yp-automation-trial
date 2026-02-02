
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
            cy.get('#break_reports > a').click();
            //calendar 
            cy.get('.input-group > :nth-child(1) > .btn').click();
            cy.get('thead > :nth-child(1) > :nth-child(1) > .btn').click();
            cy.get('.uib-datepicker-popup').contains('10').click();
            cy.get('tabletoolsdaterange2 > .input-group > .form-control.ng-pristine').clear().type('12/10/2023');
            // cy.get('.hand_cursor').click();

                        
            // searchbar
            cy.get('tabletoolstrans > .input-group > .form-control').type('Juan')
            cy.get('[ng-if="!main.no_search_button"]').click();

            // cy.wait(2000);

            // adv filter    
            cy.get('[ng-if="!main.no_filter && main.current_module != \'daily_logs\' && ![\'sss_contribution\',\'hdmf_contribution\',\'phic_contribution\', \'remittances_loan\'].includes(main.current_module)"]')
            .click();
            cy.wait(2000);
            cy.get('.btn-sm').click();

            // view by
            cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div.col-sm-2 > div > div > a > span.select2-arrow.ui-select-toggle').click({ multiple: true });
            cy.get('.select2-highlighted > .select2-result-label').click();
            cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div.col-sm-2 > div > div > a > span.select2-arrow.ui-select-toggle').click({ multiple: true });
            cy.get(':nth-child(2) > .select2-result-label').click();
            cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div.col-sm-2 > div > div > a > span.select2-arrow.ui-select-toggle').click({ multiple: true });
            cy.get(':nth-child(3) > .select2-result-label > .ng-binding').click();

            // records per page
            cy.get('.ui-select-match > .btn-default').click();
            cy.get(':nth-child(3) > .ui-select-choices-row-inner').click();





        });
    });
  
    // You can add more test cases here for other scenarios
  });
  