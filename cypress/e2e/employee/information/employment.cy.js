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
        it.skip('should search calendar', () => {
            cy.get('#employee_list > a').click(); 
            cy.get('#information_list > a').click();
            cy.get('#employee_employment_type > a').click();

            //calendar 
            // cy.get('.input-group > :nth-child(1) > .btn').click();
            // cy.get('thead > :nth-child(1) > :nth-child(1) > .btn').click();
            // cy.get('.uib-datepicker-popup').contains('11').click();
            // cy.get('tabletoolsdaterange2 > .input-group > .form-control.ng-pristine').clear().type('01/30/2024');
            // cy.get('.hand_cursor').click();

                        
            // searchbar
            // cy.get('tabletoolstrans > .input-group > .form-control').type('caleb')
            // cy.get('[ng-if="!main.no_search_button"]').click();

            cy.wait(2000);

            // adv filter    
            cy.get('[ng-if="!main.no_filter && main.current_module != \'daily_logs\' && ![\'sss_contribution\',\'hdmf_contribution\',\'phic_contribution\', \'remittances_loan\'].includes(main.current_module)"]')
            .click();
            // cy.wait(2000);
            cy.get('.col-sm-12 > .btn-success').click();

            cy.wait(3000);

            // create
            cy.get('tbody > :nth-child(4) > :nth-child(2)').click();
            cy.get(':nth-child(1) > td > .col-sm-5.pull-left > .ui-select-container > .select2-choice > .select2-chosen.ng-binding').click();
            cy.get(':nth-child(2) > .select2-result-label > .ng-binding').click();
            cy.get(':nth-child(1) > td > :nth-child(2) > .input-group > .input-group-btn > .btn').click();
            cy.get(':nth-child(3) > .btn > .glyphicon').click();
            cy.get('#page-top')
            .find('div.modal.fade.ng-scope.ng-isolate-scope.in')
            .find('div.panel-body')
            .find('div.row.table-responsive.custom-responsive-div')
            .find('table tbody tr:nth-child(1) td div:nth-child(2) p div ul')
            .contains('29')
            .click();
            // cy.get(':nth-child(1) > td > .col-sm-2 > .btn > .fa').click()
          
            // cy.get('[ng-click="create(department, \'edit\')] > .fa').click();          


        });
    });
  
    // You can add more test cases here for other scenarios
  });
  