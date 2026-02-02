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
        it.skip('profile', () => {
            cy.get('#settings_list > a').click();
            cy.get('#company_list > a').click({ force: true });
            cy.get('#profiles > a').click({ force: true });
            cy.get('#gl_accounts > a').click();

            cy.get('.form-group > .btn').click();

            cy.get('.form > :nth-child(1) > .form-control').type('testingcode123');
            cy.get(':nth-child(2) > .form-control').type('testingcode');

            // cy.get('.btn-success').click();
            
        }); // Closing it.skip('profile') test case
    }); // Closing describe('settings')
}); // Closing describe('login')