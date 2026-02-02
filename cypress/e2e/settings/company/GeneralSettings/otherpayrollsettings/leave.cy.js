describe('login', () => {
    // This code will run before each test case in this describe block
    beforeEach(() => {
        // Load login credentials from the fixture file
        cy.fixture('credentials').then(credentials => {
            const { url, email, pass } = credentials;
 
            // Login
            cy.visit(url);
            cy.get('#email').type(email);
            cy.get('#password').type(pass);
            cy.get('#signin-button').click();
        });
    });

    describe('settings', () => {
        it('customized late', function() { this.skip();
            
            cy.get('#settings_list > a').click();
            cy.get('#company_list > a').click({ force: true });
            cy.get('#profiles > a').click({ force: true });
            cy.get('#companies_general_settings > a').click();

            cy.get(':nth-child(10) > td').click();

            cy.get(':nth-child(4) > td').click();

            cy.get('#leave_credit_conversion').click();

            cy.get('#is_allow_limit_for_leave_credits').click();

            cy.get('#is_activate_hours_based_on_schedule').click();

            cy.get('#allow_leave_application_on_sp_holiday').click();
            
            cy.get('#is_round_off_leave_credits').click();
            cy.get('.form-control').type('1');

            cy.get('#is_activate_fix_leave_reason').click();

            cy.get('.col-sm-2 > .form-group > .btn');



 
        }); // Closing it.skip('profile') test case
    }); // Closing describe('settings')
    
}); // Closing describe('login')