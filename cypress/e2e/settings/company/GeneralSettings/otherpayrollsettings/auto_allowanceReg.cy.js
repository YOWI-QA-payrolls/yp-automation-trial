describe('Settings - General Settings - Auto Allowance Registration', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should configure auto allowance registration with date pickers', () => {
        cy.navigateMenu([
            '#settings_list > a',
            '#company_list > a',
            '#companies_general_settings > a'
        ]);

        cy.get('#tableee', { timeout: 30000 }).should('exist');

        cy.get(':nth-child(10) > td', { timeout: 15000 })
            .should('be.visible')
            .click();

        cy.get(':nth-child(5) > td', { timeout: 10000 })
            .should('be.visible')
            .click();

        cy.get('[ng-repeat-start="(idx,record) in main.records2"]:first td .align_left a [ng-show="!static_key"] .btn', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();

        cy.get('[ng-repeat-end=""]:first .align_left .col-sm-12 .table-responsive #table tbody tr :nth-child(1) .input-group .input-group-btn .btn', { timeout: 10000 })
            .should('be.visible')
            .click();
        cy.get('.btn-info', { timeout: 10000 })
            .should('be.visible')
            .click();

        cy.get('[ng-repeat-end=""]:first .align_left .col-sm-12 .table-responsive #table tbody tr :nth-child(2) .input-group .input-group-btn .btn', { timeout: 10000 })
            .should('be.visible')
            .click();
        cy.get('.uib-datepicker-popup', { timeout: 10000 })
            .should('be.visible')
            .contains('15')
            .click();

        cy.get('[ng-repeat-end=""]:first .align_left .col-sm-12 .table-responsive #table tbody tr :nth-child(3) .input-group .input-group-btn .btn', { timeout: 10000 })
            .should('be.visible')
            .click();
        cy.get('.uib-datepicker-popup', { timeout: 10000 })
            .should('be.visible')
            .contains('30')
            .click();

        cy.get('[ng-repeat-end=""]:first .align_left .col-sm-12 .table-responsive #table tbody tr :nth-child(4) .input-group .input-group-btn .btn', { timeout: 10000 })
            .should('be.visible')
            .click();
        cy.get('.uib-datepicker-popup', { timeout: 10000 })
            .should('be.visible')
            .contains('15')
            .click();

        cy.get('[ng-repeat-end=""]:first .align_left .col-sm-12 .table-responsive #table tbody tr :nth-child(5) .input-group .input-group-btn .btn', { timeout: 10000 })
            .should('be.visible')
            .click();
        cy.get('.uib-datepicker-popup', { timeout: 10000 })
            .should('be.visible')
            .contains('30')
            .click();

        cy.get(':nth-child(4) > td > .align_left > a > [ng-show="!static_key"] > .btn', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();

        cy.get(':nth-child(5) > .align_left > .col-sm-12 > .table-responsive > #table > tbody > tr > :nth-child(1) > .input-group > .input-group-btn > .btn', { timeout: 10000 })
            .should('be.visible')
            .click();
        cy.get('.btn-info', { timeout: 10000 })
            .should('be.visible')
            .click();

        cy.get(':nth-child(5) > .align_left > .col-sm-12 > .table-responsive > #table > tbody > tr > :nth-child(2) > .input-group > .input-group-btn > .btn', { timeout: 10000 })
            .should('be.visible')
            .click();
        cy.get('.uib-datepicker-popup', { timeout: 10000 })
            .should('be.visible')
            .contains('15')
            .click();

        cy.get(':nth-child(5) > .align_left > .col-sm-12 > .table-responsive > #table > tbody > tr > :nth-child(3) > .input-group > .input-group-btn > .btn', { timeout: 10000 })
            .should('be.visible')
            .click();
        cy.get('.uib-datepicker-popup', { timeout: 10000 })
            .should('be.visible')
            .contains('30')
            .click();

        cy.get(':nth-child(5) > .align_left > .col-sm-12 > .table-responsive > #table > tbody > tr > :nth-child(4) > .input-group > .input-group-btn > .btn', { timeout: 10000 })
            .should('be.visible')
            .click();
        cy.get('.uib-datepicker-popup', { timeout: 10000 })
            .should('be.visible')
            .contains('15')
            .click();

        cy.get(':nth-child(5) > .align_left > .col-sm-12 > .table-responsive > #table > tbody > tr > :nth-child(5) > .input-group > .input-group-btn > .btn', { timeout: 10000 })
            .should('be.visible')
            .click();
        cy.get('.uib-datepicker-popup', { timeout: 10000 })
            .should('be.visible')
            .contains('30')
            .click();
    });
});
