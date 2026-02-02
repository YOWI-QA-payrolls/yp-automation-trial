
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
        it('should search calendar', function() { this.skip();
             cy.get('#approval_list > [href="#"]').click();
             cy.get('#cash_advance_approval > a').click();

             //calendar 
             cy.get('.input-group > :nth-child(1) > .btn').click();
             cy.get('thead > :nth-child(1) > :nth-child(1) > .btn').click();
             cy.get('.uib-datepicker-popup').contains('11').click();
             cy.get('tabletoolsdaterange3 > .input-group > .form-control.ng-pristine').clear().type('01/30/2024');
             // cy.get('.hand_cursor').click();
 
                         
             // searchbar
             // cy.get('tabletoolstrans > .input-group > .form-control').type('eyt')
             // cy.get('[ng-if="!main.no_search_button"]').click();
 
             cy.wait(2000);
 
             // adv filter    
             cy.get('[ng-if="!main.no_filter && main.current_module != \'daily_logs\' && ![\'sss_contribution\',\'hdmf_contribution\',\'phic_contribution\', \'remittances_loan\'].includes(main.current_module)"]')
             .click();
             cy.wait(2000);
             cy.get('.col-sm-12 > .btn-success').click();
 
            //  auto approval
            cy.get('#page-wrapper div.ng-scope div.col-sm-2 a span.select2-chosen.ng-binding').click();
             cy.get(':nth-child(3) > .select2-result-label > .ng-binding').click();
             cy.get('#auto_approval_1').click();
             cy.get('div[ng-if="main.page_type == \'approval\'"] > .btn').click();
             cy.get('.confirm').click();
   
 
            //  // popup approve
            //  cy.get('tbody > [style=""] > :nth-child(4)').click();
            //  cy.get('span.ng-scope > :nth-child(1) > label').click();
            //  cy.get('#leave_submit').click();
            //  cy.wait(3000);
            //  cy.get('.confirm').click();

        });
    });
  
    // You can add more test cases here for other scenarios
  });
  