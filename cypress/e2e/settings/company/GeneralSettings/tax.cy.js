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
        it('10 mins late', function() { this.skip();

            cy.get('#settings_list > a').click();
            cy.get('#company_list > a').click({ force: true });
            cy.get('#companies_general_settings > a').click({ force: true });

            cy.wait(2000);

            cy.get(':nth-child(8) > td').click();

            cy.get('#activate_monthly_tax_calculation').click();

            cy.get('#is_activate_custom_months_daily_minimum_wage').click();
            cy.get('#activate_average_tax_calculation').click();

            cy.get('#de_minimis').click();

            cy.get('#is_total_threshold').click();
            cy.get('#is_fixed_deminimis_basic_salary').click();

            cy.get('#minimum_wage').click();
 
        }); // Closing it.skip('profile') test case
    }); // Closing describe('settings')
    
}); // Closing describe('login')