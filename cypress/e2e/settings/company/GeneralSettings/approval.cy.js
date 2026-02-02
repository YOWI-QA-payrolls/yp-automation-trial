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
        it.skip('10 mins late', () => {

            cy.get('#settings_list > a').click();
            cy.get('#company_list > a').click({ force: true });
            cy.get('#profiles > a').click({ force: true });
            cy.get('#companies_general_settings > a').click();

            cy.wait(2000);

            cy.get(':nth-child(4) > td').click();

            cy.get('#has_approval_hierarchy').click();
            cy.get('#is_allow_bypass_approval').click();

            cy.get('#allowed_credit_adjustment').click();

            cy.get('#auto_request_overtime').click();

            cy.get('.form-group > .btn').click();
 
        }); // Closing it.skip('profile') test case
    }); // Closing describe('settings')
    
}); // Closing describe('login')