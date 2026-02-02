
describe('login', () => {
    // This code will run before each test case in this describe block
    beforeEach(() => {
        // Load login credentials from the fixture file
        cy.viewport(1280, 800);
        cy.fixture('credentials').then(credentials => {
            const { url, email, pass } = credentials;
  
            // Login
            cy.visit(url);
            cy.get(':nth-child(1) > .form-control').type(email);
            cy.get(':nth-child(2) > .form-control').type(pass);
            cy.get('.custom-mb').click();
            
        });
    });
  
    describe('navigate to complete timesheet', () => {
        it('should search calendar', () => {
            
            cy.get('#timesheetreports_list > [href="#"]').click();
            cy.get('#logs_verification_reports > a').click();
            //calendar 
            cy.get('.input-group > :nth-child(1) > .btn').click();
            // cy.get('.uib-datepicker-popup')..type('12/26/2023');
            // cy.get('tabletoolsdaterange2 > .input-group > .form-control.ng-pristine').clear().type('12/26/2023');
            // cy.get('.hand_cursor').click();

                        
            // searchbar
            cy.get('tabletoolstrans > .input-group > .form-control').type('Juan')
            // cy.get('[ng-if="!main.no_search_button"]').click();

            // adv filter    
            cy.get('[ng-if="!main.no_filter && main.current_module != \'daily_logs\' && ![\'sss_contribution\',\'hdmf_contribution\',\'phic_contribution\', \'remittances_loan\'].includes(main.current_module)"]')
            .click();

            cy.get('.btn-sm').click();

            // records per page
            cy.get('.ui-select-match > .btn-default').click();
            cy.get(':nth-child(3) > .ui-select-choices-row-inner').click();

            // view by
            cy.get('#page-wrapper div.wrapper.wrapper-content.body div.tab-pane.ng-scope.active div.col-xs-6.col-sm-6.col-md-3.col-lg-2.pull-left a span.select2-arrow.ui-select-toggle').click();
            cy.get('.select2-highlighted > .select2-result-label > .ng-binding').click();

            //toggle 
            // cy.get('div.pull-right > .dropdown-toggle').click();

            // export normal
            // cy.get('.dropdown-menu.pull-right > li:nth-of-type(1) > a:nth-of-type(1)').click();

            // export large dataa
            // cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div > div.row.pull-right.col-sm-6.ng-scope > tabletoolstrans > div > div > div > ul > li:nth-child(1) > a:nth-child(2)').click();
            // cy.get('.open > .dropdown-menu').contains('Export (Large data)').click();

            // complete timesheet
            // cy.get('.open > .dropdown-menu').contains('Complete Timesheets').click();
            // cy.get('[ng-if="main.key_in_list(main.current_module, [\'logs_verification_reports\']) && main.logs_verification_tab != \'tapping_compliance\' && main.current_sessions.role == \'edit\'"] > a')
            // .click();
            // cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > div.tab-pane.ng-scope.active > div > div.row.pull-right.col-sm-6.ng-scope > tabletoolstrans > div > div > div > ul > li:nth-child(4) > a').click();

            //summary-per range
            cy.get('[select="main._change_tab(\'summary_per_range\')"] > .nav-link').click();

                        // searchbar
                        cy.get('tabletoolstrans > .input-group > .form-control').type('Juan')
                        // cy.get('[ng-if="!main.no_search_button"]').click();

                        // records per page
                    //    cy.get('#page-wrapper div.wrapper.wrapper-content.body div.tab-pane.ng-scope.active div.row.col-xs-6.col-sm-6.col-md-3.col-lg-2.pull-right div div span').click();
                    //     cy.get(':nth-child(3) > .ui-select-choices-row-inner > .ng-binding').click();
            
                        // adv filter    
                        cy.get('[ng-if="!main.no_filter && main.current_module != \'daily_logs\' && ![\'sss_contribution\',\'hdmf_contribution\',\'phic_contribution\', \'remittances_loan\'].includes(main.current_module)"]')
                        .click();
                        cy.get('.btn-sm').click();
                        cy.wait(3000);

            //summaary per date 
            cy.get('.active > .nav-link').click();

                // searchbar
                cy.get('tabletoolstrans > .input-group > .form-control').type('Juan')
                // cy.get('[ng-if="!main.no_search_button"]').click();

                // records per page
                //    cy.get('#page-wrapper div.wrapper.wrapper-content.body div.tab-pane.ng-scope.active div.row.col-xs-6.col-sm-6.col-md-3.col-lg-2.pull-right div div span').click();
                //     cy.get(':nth-child(3) > .ui-select-choices-row-inner > .ng-binding').click();

                // adv filter    
                cy.get('[ng-if="!main.no_filter && main.current_module != \'daily_logs\' && ![\'sss_contribution\',\'hdmf_contribution\',\'phic_contribution\', \'remittances_loan\'].includes(main.current_module)"]')
                .click();
                cy.get('.btn-sm').click();
                cy.wait(3000);


            // summaaaary per classification
            cy.get('[select="main._change_tab(\'summary_per_classification\')"] > .nav-link').click();

                // searchbar
                cy.get('tabletoolstrans > .input-group > .form-control').type('Juan')
                // cy.get('[ng-if="!main.no_search_button"]').click();

                // records per page
                //    cy.get('#page-wrapper div.wrapper.wrapper-content.body div.tab-pane.ng-scope.active div.row.col-xs-6.col-sm-6.col-md-3.col-lg-2.pull-right div div span').click();
                //     cy.get(':nth-child(3) > .ui-select-choices-row-inner > .ng-binding').click();
        
                // adv filter    
                cy.get('[ng-if="!main.no_filter && main.current_module != \'daily_logs\' && ![\'sss_contribution\',\'hdmf_contribution\',\'phic_contribution\', \'remittances_loan\'].includes(main.current_module)"]')
                .click();
                cy.get('.btn-sm').click();

                cy.get('#select_payroll_period').click();
                cy.get('.form-group > .ui-select-container > .select2-choice').click();
                cy.get('#ui-select-choices-row-28- > .select2-result-label').click();
        });
    });
  
    // You can add more test cases here for other scenarios
  });
  