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

            cy.get(':nth-child(14) > td').click();

            // cutoff sched
            cy.get('[heading="Cutoff Schedules"] > .nav-link').click();
            cy.get('.tab-pane.active > .panel-body > .ibox-content > .col-sm-2 > .form-group > .btn').click();
            cy.get('.form-control').type('sample_test');
            cy.get('.btn-success').click();

            // email template

            cy.get('[heading="Email Templates"] > .nav-link').click();
            cy.get('.tab-pane.active > .panel-body > .ibox-content > .col-sm-2.pull-right > .form-group > .btn').click();
            cy.get(':nth-child(1) > .ui-select-container > .select2-choice > .select2-chosen.ng-binding').click();
            cy.get(':nth-child(2) > .select2-result-label > .ng-binding').click();
            cy.get('.input-group-btn > .btn').click();
            cy.get('.btn-group > .btn-info').click();
            cy.get(':nth-child(4) > .ui-select-container > .select2-choice > .select2-chosen.ng-binding').click();
            cy.get(':nth-child(2) > .select2-result-label > .ng-binding').click();
            cy.get('[ng-repeat="(key,module) in main.company_cutoff_schedules_lists"][style=""] > .checkbox > .ng-binding').click();

            cy.get(':nth-child(10) > .btn').click();
            cy.get('.second_dialog > .modal-dialog > .modal-content > .panel > .panel-body > .ibox-content > .row > .form > .col-sm-10 > .form-control').type('sample@gmail.com');
            cy.get('.second_dialog > .modal-dialog > .modal-content > .panel > .panel-footer > .pull-right > .btn').click();
            cy.get('.col-sm-12 > .ui-select-container > .select2-choice > .select2-chosen.ng-binding').click();
            cy.get('.select2-highlighted > .select2-result-label').click();
            cy.get('.pull-right > .btn-success').click();

            // payrol sched
            cy.get('[heading="Payroll Schedules"] > .nav-link').click();
            cy.get('.tab-pane.active > .panel-body > .ibox-content > .col-sm-2 > .form-group > .btn').click();
            cy.get(':nth-child(1) > .ui-select-container > .select2-choice > .select2-chosen.ng-binding').click();
            cy.get('.select2-highlighted > .select2-result-label > .ng-binding').click();
            cy.get(':nth-child(4) > .form-control').type('sample');
            cy.get('[ng-repeat="header in main.company_cutoff_schedules_lists"][style=""] > .input-group > .input-group-btn > .btn').click();
            cy.get('.btn-success').click()

        }); // Closing it('profile') test case
    }); // Closing describe('settings')
    
}); // Closing describe('login')