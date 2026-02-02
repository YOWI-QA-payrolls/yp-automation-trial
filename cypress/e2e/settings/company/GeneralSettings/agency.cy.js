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
            cy.get('#companies_general_settings > a').click({ force: true });

            cy.wait(2000);

            cy.get(':nth-child(7) > td').click();

            cy.get('#has_agency').click();

            cy.get('[ng-if="agency.has_agency"][style=""] > .input-group > .form-control').type('testname');

            cy.get(':nth-child(3) > .input-group > .form-control').type('500');

            cy.get('.form-group > .btn').click();
 
        }); // Closing it.skip('profile') test case
    }); // Closing describe('settings')
    
}); // Closing describe('login')