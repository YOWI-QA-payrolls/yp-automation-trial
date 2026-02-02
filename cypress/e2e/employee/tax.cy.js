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
            cy.get('#employee_list > a').click(); 
            cy.get('#tax_beginning_balance > a').click();
            // cy.get('#employee_statutory > a').click({ force: true });
            
            // //calendar 
            // cy.get('.input-group > :nth-child(1) > .btn').click();
            // cy.get('thead > :nth-child(1) > :nth-child(1) > .btn').click();
            // cy.get('.uib-datepicker-popup').contains('11').click();
            // cy.get('tabletoolsdaterange2 > .input-group > .form-control.ng-pristine').clear().type('01/30/2024');
            // // cy.get('.hand_cursor').click();

                        
            // // searchbar
            cy.get('tabletoolstrans > .input-group > .form-control').type('caleb')
            // // cy.get('[ng-if="!main.no_search_button"]').click();

            // cy.wait(2000);

            // // adv filter    
            cy.get('[ng-if="!main.no_filter && main.current_module != \'daily_logs\' && ![\'sss_contribution\',\'hdmf_contribution\',\'phic_contribution\', \'remittances_loan\'].includes(main.current_module)"]')
            .click();
            cy.wait(2000);
            // cy.get('.col-sm-12 > .btn-success').click();
            cy.get('[ng-if="!main.no_search_button"]').click();
            cy.wait(3000);

            // create
            cy.get('.hand_cursor > :nth-child(2)').click();
            cy.get(':nth-child(1) > :nth-child(1) > .input-group > .input-group-btn > .btn').click();
            cy.get('.btn-info').click();
            cy.get(':nth-child(1) > :nth-child(2) > .form-control').type('1000');
            cy.get(':nth-child(1) > :nth-child(3) > .form-control').type('1000');
            cy.get(':nth-child(1) > :nth-child(4) > .form-control').type('1000');
            cy.get(':nth-child(1) > :nth-child(5) > .form-control').type('1000');
            cy.get(':nth-child(1) > :nth-child(6) > .form-control').type('1000');
            cy.get(':nth-child(1) > :nth-child(7) > .form-control').type('1000');
            // cy.get(':nth-child(1) > :nth-child(9) > .btn').click()

            
        });
    });
  
    // You can add more test cases here for other scenarios
  });
  