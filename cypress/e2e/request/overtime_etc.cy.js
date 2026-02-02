
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
            cy.get('#requests_list > a').click().click();
            cy.get('#undertime_overtime_request > a').click();

            // //calendar 
            // cy.get('.input-group > :nth-child(1) > .btn').click();
            // cy.get('thead > :nth-child(1) > :nth-child(1) > .btn').click();
            // cy.get('.uib-datepicker-popup').contains('11').click();
            // cy.get('tabletoolsdaterange2 > .input-group > .form-control.ng-pristine').clear().type('01/11/2024');
            // // cy.get('.hand_cursor').click();

                        
            // // searchbar
            // cy.get('tabletoolstrans > .input-group > .form-control').type('Juan')
            // cy.get('[ng-if="!main.no_search_button"]').click();

            // // cy.wait(2000);

            // // adv filter    
            // cy.get('[ng-if="!main.no_filter && main.current_module != \'daily_logs\' && ![\'sss_contribution\',\'hdmf_contribution\',\'phic_contribution\', \'remittances_loan\'].includes(main.current_module)"]')
            // .click();
            // cy.wait(2000);
            // cy.get('.btn-sm').click();

            // cy.get('.col-sm-3 > .pull-right > .btn').click();
            // cy.get('.select2-input').click();
            // cy.get(':nth-child(2) > .select2-result-label > .ng-binding').click();
            // cy.get('.form-inline > :nth-child(2) > .form-control').type('8');
            // cy.get(':nth-child(4) > .form-control').type('30');
            // cy.get(':nth-child(9) > .form-control').type('testing');
            // cy.get(':nth-child(10) > .form-control').type('testing123');
            // cy.get('.pull-right > .btn-success').click();
            // // cy.get('.confirm').click();
            // cy.get('.cancel').click();
            // cy.get('.col-sm-8 > .pull-right > .btn').click();

            // // cy.get('#requests_list > a').click().click();
            // // cy.get('#undertime_overtime_request > a').click();

            // //overtime
            // cy.get('#request_tab > :nth-child(2) > a').click();

            //   //calendar 
            //   cy.get('.input-group > :nth-child(1) > .btn').click();
            // //   cy.get('thead > :nth-child(1) > :nth-child(1) > .btn').click();
            // //   cy.get('.uib-datepicker-popup').contains('11').click();
            // //   cy.get('tabletoolsdaterange2 > .input-group > .form-control.ng-pristine').clear().type('01/11/2024');
            //   // cy.get('.hand_cursor').click();
  
                          
            //   // searchbar
            // //   cy.get('tabletoolstrans > .input-group > .form-control').type('Juan')
            // //   cy.get('[ng-if="!main.no_search_button"]').click();
  
            //   cy.wait(2000);
  
            //   // adv filter    
            //   cy.get('[ng-if="!main.no_filter && main.current_module != \'daily_logs\' && ![\'sss_contribution\',\'hdmf_contribution\',\'phic_contribution\', \'remittances_loan\'].includes(main.current_module)"]')
            //   .click();
            //   // cy.wait(2000);
            //   cy.get('.btn-sm').click();
  
            //   cy.get('.col-sm-3 > .pull-right > .btn').click();
            //   cy.get('.select2-input').click();
            //   cy.get(':nth-child(2) > .select2-result-label > .ng-binding').click();
            //   cy.get('.form-inline > :nth-child(2) > .form-control').type('8');
            //   cy.get(':nth-child(4) > .form-control').type('30');
            //   cy.get(':nth-child(9) > .form-control').type('testing');
            // //   cy.get(':nth-child(10) > .form-control').type('testing123');
            //   cy.get('.pull-right > .btn-success').click();
            // //   cy.get('.confirm').click();
            //   cy.get('.cancel').click();
            //   cy.get('.col-sm-8 > .pull-right > .btn').click();

            // // hooliday
            // cy.get('#request_tab > :nth-child(3) > a').click();
            
            // //calendar 
            // cy.get('.input-group > :nth-child(1) > .btn').click();
            // //   cy.get('thead > :nth-child(1) > :nth-child(1) > .btn').click();
            // //   cy.get('.uib-datepicker-popup').contains('11').click();
            // //   cy.get('tabletoolsdaterange2 > .input-group > .form-control.ng-pristine').clear().type('01/11/2024');
            //     // cy.get('.hand_cursor').click();
    
                            
            //     // searchbar
            // //   cy.get('tabletoolstrans > .input-group > .form-control').type('Juan')
            // //   cy.get('[ng-if="!main.no_search_button"]').click();
    
            //     // cy.wait(2000);
    
            //     // adv filter    
            //     cy.get('[ng-if="!main.no_filter && main.current_module != \'daily_logs\' && ![\'sss_contribution\',\'hdmf_contribution\',\'phic_contribution\', \'remittances_loan\'].includes(main.current_module)"]')
            //     .click();
            //     cy.wait(2000);
            //     cy.get('.btn-sm').click();
    
            //     cy.get('.col-sm-3 > .pull-right > .btn').click();
            //     cy.get('.select2-input').click();
            //     cy.get(':nth-child(2) > .select2-result-label > .ng-binding').click();
            //     cy.get('.form-inline > :nth-child(2) > .form-control').type('8');
            //     cy.get(':nth-child(4) > .form-control').type('30');
            //     // cy.get(':nth-child(9) > .form-control').type('testing');
            // //   cy.get(':nth-child(10) > .form-control').type('testing123');
            //     cy.get('.pull-right > .btn-success').click();
            // //   cy.get('.confirm').click();
            //     // cy.get('.cancel').click();
            //     // cy.get('.col-sm-8 > .pull-right > .btn').click();
            //     cy.get(':nth-child(8) > .form-control').type('testing');
            //     cy.get('.pull-right > .btn-white').click();
                
            //     //restday 
            //     cy.get('#request_tab > :nth-child(4) > a').click(); 

            //     cy.get('.input-group > :nth-child(1) > .btn').click();
            //     //   cy.get('thead > :nth-child(1) > :nth-child(1) > .btn').click();
            //     //   cy.get('.uib-datepicker-popup').contains('11').click();
            //     cy.get('tabletoolsdaterange2 > .input-group > .form-control.ng-scope').clear().type('01/21/2024');
            //     // cy.get('.hand_cursor').click();
        
                                
            //     // searchbar
            //     //   cy.get('tabletoolstrans > .input-group > .form-control').type('Juan')
            //     //   cy.get('[ng-if="!main.no_search_button"]').click();
        
            //     // cy.wait(2000);
    
            //     // adv filter    
            //     cy.get('[ng-if="!main.no_filter && main.current_module != \'daily_logs\' && ![\'sss_contribution\',\'hdmf_contribution\',\'phic_contribution\', \'remittances_loan\'].includes(main.current_module)"]')
            //     .click();
            //     cy.wait(2000);
            //     cy.get('.btn-sm').click();
    
            //     cy.get('.col-sm-3 > .pull-right > .btn').click();
            //     cy.get('.select2-input').click();
            //     cy.get(':nth-child(2) > .select2-result-label > .ng-binding').click();
            //     cy.get('.form-inline > :nth-child(2) > .form-control').type('8');
            //     cy.get(':nth-child(4) > .form-control').type('30');
            //     cy.get(':nth-child(8) > .form-control').type('testing');
            //     cy.get('.pull-right > .btn-success').click();
            //     //   cy.get('.confirm').click();
            //     cy.get('.cancel').click();
            //     cy.get('.col-sm-8 > .pull-right > .btn').click();

                // business
                cy.get('#request_tab > :nth-child(5) > a').click();

                cy.wait(2000);

                cy.get('[ng-if="!main.no_filter && main.current_module != \'daily_logs\' && ![\'sss_contribution\',\'hdmf_contribution\',\'phic_contribution\', \'remittances_loan\'].includes(main.current_module)"]')
                .click();
                // cy.wait(2000);
                cy.get('.btn-sm').click();

                cy.get('.col-sm-3 > .pull-right > .btn').click();
                cy.get('.select2-chosen.ng-binding').click();
                cy.get(':nth-child(2) > .select2-result-label > .ng-binding').click();
                cy.get('[ng-show="official_business.employee"] > .col-sm-8 > :nth-child(2)')
                cy.get('#whole_day').click();
                cy.get(':nth-child(8) > .form-control').type('testing');
                cy.get('.pull-right > .btn-success').click();
                cy.get('.cancel').click();
                cy.get('.col-sm-8 > .pull-right > .btn').click();

            




        });
    });
  
    // You can add more test cases here for other scenarios
  });
  