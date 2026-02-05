
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
             cy.get('#transfer_approval_request > a').click();

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

             // auto approval (conditional - only if dropdown has options)
             cy.get('body').then($body => {
                 if ($body.find('[ng-model="filters.auto_approval_option"] .select2-choice').length > 0) {
                     cy.get('[ng-model="filters.auto_approval_option"] .select2-choice').click();

                     cy.get('body').then($innerBody => {
                         if ($innerBody.find('#ui-select-choices-2 li:nth-child(3)').length > 0) {
                             cy.get('#ui-select-choices-2 li:nth-child(3)').click();
                             cy.get('.btn-success').click();
                         }
                     });
                 }
             });

             // Wait for any toast to disappear
             cy.get('.toast-title', { timeout: 10000 }).should('not.exist');

             // popup approve (conditional - only if data exists in table)
             cy.get('body').then($body => {
                 if ($body.find('tbody tr.hand_cursor').length > 0) {
                     cy.get('tbody tr.hand_cursor > :nth-child(6)').click();
                     cy.get('#leave_submit').click();
                     cy.wait(2000);
                     cy.get('.toast-title', { timeout: 10000 }).should('not.exist');
                     cy.get('.confirm').click();
                 }
             });

        });
    });
    // You can add more test cases here for other scenarios
  });
  