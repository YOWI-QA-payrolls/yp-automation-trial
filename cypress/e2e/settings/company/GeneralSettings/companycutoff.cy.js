describe('Settings - General Settings - Company Cutoff', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should configure cutoff schedules, email templates, and payroll schedules', () => {
        cy.navigateMenu([
            '#settings_list > a',
            '#company_list > a',
            '#companies_general_settings > a'
        ]);

        cy.get('#tableee', { timeout: 30000 }).should('exist');

        cy.get(':nth-child(14) > td', { timeout: 15000 })
            .should('be.visible')
            .click();

        cy.get('[heading="Cutoff Schedules"] > .nav-link', { timeout: 10000 })
            .should('be.visible')
            .click();

        cy.get('.tab-pane.active > .panel-body > .ibox-content > .col-sm-2 > .form-group > .btn', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();

        cy.get('.form-control', { timeout: 10000 })
            .should('be.visible')
            .type('sample_test');

        cy.get('.btn-success', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();

        cy.get('[heading="Email Templates"] > .nav-link', { timeout: 10000 })
            .should('be.visible')
            .click();

        cy.get('.tab-pane.active > .panel-body > .ibox-content > .col-sm-2.pull-right > .form-group > .btn', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();

        cy.select2First(':nth-child(1) > .ui-select-container > .select2-choice > .select2-chosen.ng-binding');

        cy.get('.input-group-btn > .btn', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();

        cy.get('.btn-group > .btn-info', { timeout: 10000 })
            .should('be.visible')
            .click();

        cy.select2First(':nth-child(4) > .ui-select-container > .select2-choice > .select2-chosen.ng-binding');

        cy.get('[ng-repeat="(key,module) in main.company_cutoff_schedules_lists"]:first .checkbox .ng-binding', { timeout: 10000 })
            .should('be.visible')
            .click();

        cy.get(':nth-child(10) > .btn', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();

        cy.get('.second_dialog > .modal-dialog > .modal-content > .panel > .panel-body > .ibox-content > .row > .form > .col-sm-10 > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('sample@gmail.com');

        cy.get('.second_dialog > .modal-dialog > .modal-content > .panel > .panel-footer > .pull-right > .btn', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();

        cy.select2First('.col-sm-12 > .ui-select-container > .select2-choice > .select2-chosen.ng-binding');

        cy.get('.pull-right > .btn-success', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();

        cy.get('[heading="Payroll Schedules"] > .nav-link', { timeout: 10000 })
            .should('be.visible')
            .click();

        cy.get('.tab-pane.active > .panel-body > .ibox-content > .col-sm-2 > .form-group > .btn', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();

        cy.select2First(':nth-child(1) > .ui-select-container > .select2-choice > .select2-chosen.ng-binding');

        cy.get(':nth-child(4) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('sample');

        cy.get('[ng-repeat="header in main.company_cutoff_schedules_lists"]:first .input-group .input-group-btn .btn', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();

        cy.get('.btn-success', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();
    });
});
