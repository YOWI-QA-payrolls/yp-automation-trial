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
        it('customized late', () => {
            
            cy.get('#settings_list > a').click();
            cy.get('#company_list > a').click({ force: true });
            cy.get('#profiles > a').click({ force: true });
            cy.get('#companies_general_settings > a').click();

            cy.get(':nth-child(10) > td').click();

            cy.get(':nth-child(3) > td').click();

            // cy.get('#activate_contribution_payroll_settings').click();
            cy.get('#exclude_contribution_employment_type').click();
            cy.get('[ng-click="main.excluded_employment_type_contribution = main.employmenttypes2"] > .fa').click();
            // cy.get('#is_merged_statutory_contribution').click();

            cy.get('.form-group > .btn');

 
        }); // Closing it('profile') test case
    }); // Closing describe('settings')
    
}); // Closing describe('login')