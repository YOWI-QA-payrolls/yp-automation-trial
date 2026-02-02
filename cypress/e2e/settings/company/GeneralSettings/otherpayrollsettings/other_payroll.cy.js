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

            cy.get(':nth-child(2) > td').click();

            cy.get('#no_holiday_pay').click();
            cy.get('.col-sm-4 > .form-control').type('5');

            cy.get('.col-sm-8 > .ui-select-container > .select2-choice > .select2-chosen.ng-binding').click();
            cy.get('.select2-highlighted > .select2-result-label > .ng-binding').click();

            cy.get(':nth-child(5) > .ui-select-container > .select2-choice > .select2-chosen.ng-binding').click();
            cy.get(':nth-child(2) > .select2-result-label > .ng-binding').click();

            cy.wait(3000);

            cy.get(':nth-child(6) > .form-control').type('500');
            cy.get(':nth-child(7) > .form-control').type('500');
            cy.get(':nth-child(8) > .form-control').type('500');
            cy.get(':nth-child(9) > .form-control').type('500');
            cy.get(':nth-child(10) > .form-control').type('500');
            cy.get(':nth-child(11) > .form-control').type('500');
            cy.get(':nth-child(12) > .form-control').type('500');
            cy.get(':nth-child(13) > .form-control').type('500');
            cy.get(':nth-child(14) > .form-control').type('500');
            cy.get(':nth-child(15) > .form-control').type('500');
            cy.get(':nth-child(16) > .form-control').type('500');
            cy.get(':nth-child(17) > .form-control').type('500');
            cy.get(':nth-child(18) > .form-control').type('500');
            cy.get(':nth-child(19) > .form-control').type('500');
            cy.get(':nth-child(20) > .form-control').type('500');
            cy.get(':nth-child(21) > .form-control').type('500');
            cy.get(':nth-child(22) > .form-control').type('500');
            cy.get(':nth-child(23) > .form-control').type('500');
            cy.get(':nth-child(24) > .form-control').type('500');
            cy.get(':nth-child(25) > .form-control').type('500');
            cy.get(':nth-child(26) > .form-control').type('500');
            cy.get(':nth-child(27) > .form-control').type('500');

            // cy.get('.form-group > .btn').click();
 
        }); // Closing it.skip('profile') test case
    }); // Closing describe('settings')
    
}); // Closing describe('login')