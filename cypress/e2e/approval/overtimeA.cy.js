
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
  
    describe('navigate to overtime timesheet', () => {
        it('should search calendar', () => {
            cy.get('#approval_list > a').click();
            cy.get('#undertime_overtime_approval > a').click();
            

            // //calendar 
            // cy.get('[ng-click="main.open_date(\'filter_date_from\')"]').click();
            // cy.get('.uib-datepicker-popup .uib-left').click();
            // cy.get('.uib-datepicker-popup').contains('11').click();
            // cy.get('[ng-model="filters.date_to"]').clear().type('01/30/2024');
            // cy.get('.hand_cursor').click();

                        
            // // searchbar
            // cy.get('#search-input').type('eyt')
            // cy.get('#advance-search').click();

            // // cy.wait(2000);

            // // adv filter    
            // cy.get('[ng-if="!main.no_filter && main.current_module != \'daily_logs\' && ![\'sss_contribution\',\'hdmf_contribution\',\'phic_contribution\', \'remittances_loan\'].includes(main.current_module)"]')
            // .click();
            // cy.wait(2000);
            // cy.get('.btn-sm').click();

            // popup approve
            // cy.get('tbody > [style=""] > :nth-child(4)').click();
            // cy.get('span.ng-scope > :nth-child(1) > label').click();
            // cy.get('.pull-right > .btn-success').click();
            // cy.get('.confirm').click();

            //  popup disapprove
            // cy.get('tr.hand_cursor > :nth-child(4)').click();
            // cy.get('span.ng-scope > :nth-child(2) > label').click();
            // cy.get('.pull-right > .btn-success').click();
            // cy.get('.confirm').click();



            // auto approval
            // cy.get('.select2-choice').click();
            // cy.get(':nth-child(3) > .select2-result-label > .ng-binding').click();
            // cy.get('#auto_approval_0').click();
            // cy.get('.btn-success').click();
            // cy.get('.confirm').click();


            //Dialog box
            // cy.get('.btn-default.col-sm').click();
            // cy.get('.col-xs-2 > .ui-select-container > .select2-choice').click();
            // cy.get(':nth-child(3) > .select2-result-label > .ng-binding').click();
            // cy.get(':nth-child(6) > .table-responsive > #table > tbody > tr.ng-scope > :nth-child(1) > .checkbox').click();
            // cy.get('.pull-right > .btn-success').click();
            // cy.get('.confirm').click();



            // //overtime
            // cy.get('#approval_tab > :nth-child(2) > a').click();


            // //calendar 
            // cy.get('[ng-click="main.open_date(\'filter_date_from\')"]').click();
            // cy.get('.uib-datepicker-popup .uib-left').click();
            // cy.get('.uib-datepicker-popup').contains('11').click();
            // cy.get('[ng-model="filters.date_to"]').clear().type('01/30/2024');
            // cy.get('.hand_cursor').click();

                        
            // // searchbar
            // cy.get('#search-input').type('eyt')
            // cy.get('#advance-search').click();

            // cy.wait(2000);

            // adv filter    
            // cy.get('[ng-if="!main.no_filter && main.current_module != \'daily_logs\' && ![\'sss_contribution\',\'hdmf_contribution\',\'phic_contribution\', \'remittances_loan\'].includes(main.current_module)"]')
            // .click();
            // cy.wait(2000);
            // cy.get('.btn-sm').click();

            // auto approval
            // cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > form > div.col-sm-2 > div > a').click();
            // cy.get(':nth-child(3) > .select2-result-label > .ng-binding').click();
            // cy.get('#auto_approval_0').click();
            // cy.get('.btn-success').click();
            // cy.get('.confirm').click();
  

            // popup approve
            // cy.get('tbody > [style=""] > :nth-child(4)').click();
            // cy.get('span.ng-scope > :nth-child(1) > label').click();
            // cy.get('.pull-right > .btn-success').click();
            // cy.wait(3000);
            // cy.get('.confirm').click();

            // // hooliday
            // cy.get('#approval_tab > :nth-child(3) > a').click();
            
            //  //calendar 
            // cy.get('[ng-click="main.open_date(\'filter_date_from\')"]').click();
            // cy.get('.uib-datepicker-popup .uib-left').click();
            // cy.get('.uib-datepicker-popup').contains('11').click();
            // cy.get('[ng-model="filters.date_to"]').clear().type('01/30/2024');
            // // cy.get('.hand_cursor').click();

                        
            // // searchbar
            // // cy.get('#search-input').type('eyt')
            // // cy.get('#advance-search').click();

            // cy.wait(2000);

            // // adv filter    
            // cy.get('[ng-if="!main.no_filter && main.current_module != \'daily_logs\' && ![\'sss_contribution\',\'hdmf_contribution\',\'phic_contribution\', \'remittances_loan\'].includes(main.current_module)"]')
            // .click();
            // cy.wait(2000);
            // cy.get('.btn-sm').click();

            // // auto approval
            // cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > form > div.col-sm-2 > div > a').click();
            // cy.get(':nth-child(3) > .select2-result-label > .ng-binding').click();
            // cy.get('#auto_approval_0').click();
            // cy.get('.btn-success').click();
            // cy.get('.confirm').click();
  

            // // popup approve
            // cy.get('tbody > [style=""] > :nth-child(4)').click();
            // cy.get('span.ng-scope > :nth-child(1) > label').click();
            // cy.get('.pull-right > .btn-success').click();
            // cy.wait(3000);
            // cy.get('.confirm').click();
                
            //     //restday 
            // cy.get('#approval_tab > :nth-child(4) > a').click(); 

             //calendar 
            //  cy.get('[ng-click="main.open_date(\'filter_date_from\')"]').click();
            //  cy.get('.uib-datepicker-popup .uib-left').click();
            //  cy.get('.uib-datepicker-popup').contains('11').click();
            //  cy.get('[ng-model="filters.date_to"]').clear().type('01/30/2024');
             // cy.get('.hand_cursor').click();
 
                         
             // searchbar
             // cy.get('#search-input').type('eyt')
             // cy.get('#advance-search').click();
 
            //  cy.wait(2000);
 
            //  // adv filter    
            //  cy.get('[ng-if="!main.no_filter && main.current_module != \'daily_logs\' && ![\'sss_contribution\',\'hdmf_contribution\',\'phic_contribution\', \'remittances_loan\'].includes(main.current_module)"]')
            //  .click();
            //  cy.wait(2000);
            //  cy.get('.btn-sm').click();
 
            //  // auto approval
            //  cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div > div > div > form > div.col-sm-2 > div > a').click();
            //  cy.get(':nth-child(3) > .select2-result-label > .ng-binding').click();
            //  cy.get('#auto_approval_0').click();
            //  cy.get('.btn-success').click();
            //  cy.get('.confirm').click();
   
 
            //  // popup approve
            //  cy.get('tbody > [style=""] > :nth-child(4)').click();
            //  cy.get('span.ng-scope > :nth-child(1) > label').click();
            //  cy.get('.pull-right > .btn-success').click();
            //  cy.wait(3000);
            //  cy.get('.confirm').click();

                // business
             cy.get('#approval_tab > :nth-child(5) > a').click();

             //calendar (conditional - only if date elements exist)
             cy.get('body').then($body => {
                 if ($body.find('[ng-click="main.open_date(\'filter_date_from\')"]').length > 0) {
                     cy.get('[ng-click="main.open_date(\'filter_date_from\')"]').click();
                     cy.get('.uib-datepicker-popup .uib-left').click();
                     cy.get('.uib-datepicker-popup').contains('11').click();
                 }
                 if ($body.find('[ng-model="filters.date_to"]').length > 0) {
                     cy.get('[ng-model="filters.date_to"]').clear().type('01/30/2024');
                 }
             });

             // Wait for any toast to disappear
             cy.get('.toast-title', { timeout: 10000 }).should('not.exist');

             cy.wait(2000);

             // adv filter (conditional)
             cy.get('body').then($body => {
                 if ($body.find('#advance-filter-btn').length > 0) {
                     cy.get('#advance-filter-btn').click();
                     cy.wait(2000);
                     cy.get('#advance-search').click();
                 }
             });

             // auto approval (conditional - only if elements exist)
             cy.get('body').then($body => {
                 if ($body.find('[ng-model="ot_request.auto_approval_option"] .select2-choice').length > 0) {
                     cy.get('[ng-model="ot_request.auto_approval_option"] .select2-choice').click();

                     cy.get('body').then($innerBody => {
                         if ($innerBody.find('#ui-select-choices-0 li:nth-child(3)').length > 0) {
                             cy.get('#ui-select-choices-0 li:nth-child(3)').click();
                             cy.get('#auto_approval').click();
                             cy.get('#apply_status_btn').click();
                             cy.get('.confirm').click();
                         }
                     });
                 }
             });

             // Wait for any toast to disappear
             cy.get('.toast-title', { timeout: 10000 }).should('not.exist');

             // popup approve (conditional - only if data exists)
             cy.get('body').then($body => {
                 if ($body.find('tbody > [style=""] > :nth-child(4)').length > 0) {
                     cy.get('tbody > [style=""] > :nth-child(4)').click();
                     cy.get('span.ng-scope > :nth-child(1) > label').click();
                     cy.get('.pull-right > .btn-success').click();
                     cy.wait(3000);
                     cy.get('.toast-title', { timeout: 10000 }).should('not.exist');
                     cy.get('.confirm').click();
                 }
             });

        });
    });
  
    // You can add more test cases here for other scenarios
  });
  