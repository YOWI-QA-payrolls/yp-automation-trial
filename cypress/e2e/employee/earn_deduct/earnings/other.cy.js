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
            cy.get('#employee_list > a').click(); 
            cy.get('#employee_income_deduction > ul.nav.nav-third-level.collapse')
            .invoke('removeAttr', 'style') // Remove 'style' attribute to make it visible
            .get('#employee_income_deduction > a')
            .contains('Earnings & Deductions')
            .click();
            cy.wait(5000);
            cy.get('#employee_earnings > [href=""]').click({ force: true });
            cy.get('#employee_recurring_earnings_details > a').click({ force: true });
            // cy.get('#employee_statutory > a').click({ force: true });
            
            // //calendar 
            // cy.get('.input-group > :nth-child(1) > .btn').click();
            // cy.get('thead > :nth-child(1) > :nth-child(1) > .btn').click();
            // cy.get('.uib-datepicker-popup').contains('11').click();
            // cy.get('tabletoolsdaterange2 > .input-group > .form-control.ng-pristine').clear().type('01/30/2024');
            // // cy.get('.hand_cursor').click();

                        
            // // searchbar
            // cy.get('tabletoolstrans > .input-group > .form-control').type('caleb')
            // // cy.get('[ng-if="!main.no_search_button"]').click();

            // cy.wait(2000);

            // // adv filter    
            // cy.get('[ng-if="!main.no_filter && main.current_module != \'daily_logs\' && ![\'sss_contribution\',\'hdmf_contribution\',\'phic_contribution\', \'remittances_loan\'].includes(main.current_module)"]')
            // .click();
            // cy.wait(2000);
            // cy.get('.col-sm-12 > .btn-success').click();
            // cy.wait(3000);

            // create
            cy.get('[style=""] > .align_left > .ng-binding').click();

            cy.get('.col-sm-1 > .btn').click();

            cy.get(':nth-child(1) > .ui-select-container > .select2-choice > .select2-chosen.ng-binding').click();
            cy.get('.select2-highlighted > .select2-result-label > .ng-binding').click();
            cy.wait(3000);
            cy.get('#addtl_amount_select').type('5000');

            cy.get(':nth-child(3) > .input-group > .input-group-btn > .btn').click();
            // cy.get(':nth-child(3) > .input-group > .input-group-btn > .btn').click();
            cy.get('.btn-info').click();
            cy.get(':nth-child(5) > .form-control').type('testing');
            // cy.get("[ng-show=\"income_list.income.name == 'Housing Allowance'\"]").click();
            





        });
    });
  
    // You can add more test cases here for other scenarios
  });
  