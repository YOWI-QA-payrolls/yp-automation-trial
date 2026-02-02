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

            cy.get(':nth-child(1) > td').click();

            cy.get(':nth-child(6) > :nth-child(14) > .my-ui-select > .select2-choice > .select2-arrow > b').click();







            // cy.get('[ng-repeat-end=""][style=""] > .align_left > .col-sm-12 > .table-responsive > #table > tbody > tr > :nth-child(2) > .input-group > .form-control').type('05/15/2024');


 
        }); // Closing it.skip('profile') test case
    }); // Closing describe('settings')
    
}); // Closing describe('login')