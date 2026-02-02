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

            cy.get(':nth-child(1) > td').click();

            cy.get('.form-control').clear().type('10');

            cy.wait(2000);

            cy.get('.form-group > .btn').click();

            // cy.get('#add_gp').click();
 
        }); // Closing it.skip('profile') test case
    }); // Closing describe('settings')

    describe('settings', () => {
        it.skip('customized late', () => {
            
            cy.get('#settings_list > a').click();
            cy.get('#company_list > a').click({ force: true });
            cy.get('#profiles > a').click({ force: true });
            cy.get('#companies_general_settings > a').click();

            cy.wait(2000);

            cy.get(':nth-child(1) > td').click();

            cy.get('#customize_late').click();

            cy.get(':nth-child(1) > .form-control').type('5');

            cy.get('.form > :nth-child(2) > .form-control').type('10');

            cy.get(':nth-child(3) > .form-control').type('10');

            cy.get('.pull-right > .btn-success').click();

            // cy.get('#add_gp').click();
 
        }); // Closing it.skip('profile') test case
    }); // Closing describe('settings')

    describe('settings', () => {
        it.skip('customized late', () => {
            
            cy.get('#settings_list > a').click();
            cy.get('#company_list > a').click({ force: true });
            cy.get('#profiles > a').click({ force: true });
            cy.get('#companies_general_settings > a').click();


            cy.get(':nth-child(1) > td').click();


            cy.wait(5000);



            // cy.get('#add_gp').click();
 
        }); // Closing it.skip('profile') test case
    }); // Closing describe('settings')
    
}); // Closing describe('login')