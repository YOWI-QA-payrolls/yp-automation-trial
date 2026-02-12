describe('Settings - General Settings - Schedule Email', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should create a scheduled email notification', () => {
        cy.navigateMenu([
            '#settings_list > a',
            '#company_list > a',
            '#companies_general_settings > a'
        ]);

        cy.get('#tableee', { timeout: 30000 }).should('exist');

        cy.get(':nth-child(12) > td', { timeout: 15000 })
            .should('be.visible')
            .click();

        cy.get('.form-group > .btn', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();

        cy.get(':nth-child(1) > .col-sm-7 > .form-group > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('testing');

        cy.get(':nth-child(2) > .col-sm-7 > .form-group > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('subject_test');

        cy.select2First(':nth-child(1) > .col-sm-5 > .ui-select-container > .select2-choice > .select2-chosen.ng-binding');

        cy.get(':nth-child(2) > .col-sm-5 > .ui-select-container > .select2-choice > .select2-chosen.ng-binding', { timeout: 10000 })
            .should('be.visible')
            .click();

        cy.get(':nth-child(4) > .select2-result-label > .ng-binding', { timeout: 10000 })
            .should('be.visible')
            .click();

        cy.get(':nth-child(4) > .btn', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();

        cy.get('.col-sm-10 > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('sample@gmail.com');

        cy.get('.second_dialog > .modal-dialog > .modal-content > .panel > .panel-body > .ibox-content > .row > .form > .col-sm-2 > .btn', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();

        cy.get('.second_dialog > .modal-dialog > .modal-content > .panel > .panel-footer > .pull-right > .btn-success', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();

        cy.get(':nth-child(9) > .form-group > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('sample testiing');

        cy.get('.pull-right > .btn-success', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();
    });
});
