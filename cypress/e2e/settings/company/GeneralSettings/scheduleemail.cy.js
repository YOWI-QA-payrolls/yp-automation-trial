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

            cy.get(':nth-child(12) > td').click();

            // create
            cy.get('.form-group > .btn').click();

            cy.get(':nth-child(1) > .col-sm-7 > .form-group > .form-control').type('testing');
            cy.get(':nth-child(2) > .col-sm-7 > .form-group > .form-control').type('subject_test');
            cy.get(':nth-child(1) > .col-sm-5 > .ui-select-container > .select2-choice > .select2-chosen.ng-binding').click();
            cy.get('.select2-highlighted > .select2-result-label > .ng-binding').click();
            cy.get(':nth-child(2) > .col-sm-5 > .ui-select-container > .select2-choice > .select2-chosen.ng-binding').click();
            cy.get(':nth-child(4) > .select2-result-label > .ng-binding').click();
            cy.get(':nth-child(4) > .btn').click();
            cy.get('.col-sm-10 > .form-control').type('sample@gmail.com');
            cy.get('.second_dialog > .modal-dialog > .modal-content > .panel > .panel-body > .ibox-content > .row > .form > .col-sm-2 > .btn').click();
            cy.get('.second_dialog > .modal-dialog > .modal-content > .panel > .panel-footer > .pull-right > .btn-success').click();

            cy.get(':nth-child(9) > .form-group > .form-control').type('sample testiing');
            cy.get('.pull-right > .btn-success').click();

 
        }); // Closing it.skip('profile') test case
    }); // Closing describe('settings')
    
}); // Closing describe('login')