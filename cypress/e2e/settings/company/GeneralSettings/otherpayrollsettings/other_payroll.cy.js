describe('Settings - General Settings - Other Payroll Settings', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should configure other payroll premium rate settings', () => {
        cy.navigateMenu([
            '#settings_list > a',
            '#company_list > a',
            '#companies_general_settings > a'
        ]);

        cy.get('#tableee', { timeout: 30000 }).should('exist');

        cy.get(':nth-child(10) > td', { timeout: 15000 })
            .should('be.visible')
            .click();

        cy.get(':nth-child(2) > td', { timeout: 10000 })
            .should('be.visible')
            .click();

        cy.get('#no_holiday_pay', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('.col-sm-4 > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('5');

        cy.select2First('.col-sm-8 > .ui-select-container > .select2-choice > .select2-chosen.ng-binding');

        cy.get(':nth-child(5) > .ui-select-container > .select2-choice > .select2-chosen.ng-binding', { timeout: 10000 })
            .should('be.visible')
            .click();

        cy.get(':nth-child(2) > .select2-result-label > .ng-binding', { timeout: 10000 })
            .should('be.visible')
            .click();

        cy.get(':nth-child(6) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('500');

        cy.get(':nth-child(7) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('500');

        cy.get(':nth-child(8) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('500');

        cy.get(':nth-child(9) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('500');

        cy.get(':nth-child(10) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('500');

        cy.get(':nth-child(11) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('500');

        cy.get(':nth-child(12) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('500');

        cy.get(':nth-child(13) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('500');

        cy.get(':nth-child(14) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('500');

        cy.get(':nth-child(15) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('500');

        cy.get(':nth-child(16) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('500');

        cy.get(':nth-child(17) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('500');

        cy.get(':nth-child(18) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('500');

        cy.get(':nth-child(19) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('500');

        cy.get(':nth-child(20) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('500');

        cy.get(':nth-child(21) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('500');

        cy.get(':nth-child(22) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('500');

        cy.get(':nth-child(23) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('500');

        cy.get(':nth-child(24) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('500');

        cy.get(':nth-child(25) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('500');

        cy.get(':nth-child(26) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('500');

        cy.get(':nth-child(27) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('500');
    });
});
