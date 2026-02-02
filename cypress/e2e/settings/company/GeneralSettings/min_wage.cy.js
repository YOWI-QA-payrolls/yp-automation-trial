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

            cy.get(':nth-child(16) > td').click();

            cy.wait(3000);

            cy.get('.form-group > .btn').click();
            cy.get('[ng-click="minimum_wage.locations = all_locations"] > .fa').click();
            cy.get('.input-group-btn > .btn').click();
            cy.get('.btn-info').click();
            cy.get(':nth-child(3) > .form-control').type('556');
            cy.get('.btn-success').click();

            // cy.get('[ng-click="minimum_wage.locations = all_locations"] > .fa').click();
            // cy.get('.input-group-btn > .btn').click();
            // cy.get('.btn-info').click();
            // cy.get(':nth-child(3) > .form-control').type('556');

            // cy.get('.btn-success').click();


        }); // Closing it.skip('profile') test case
    }); // Closing describe('settings')
    
}); // Closing describe('login')