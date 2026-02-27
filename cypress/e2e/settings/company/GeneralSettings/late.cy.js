describe('Settings - General Settings - Late Configuration', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should set late grace period to 10 minutes and save', () => {
        cy.navigateMenu([
            '#settings_list > a',
            '#company_list > a',
            '#companies_general_settings > a'
        ]);

        cy.waitForSettingsTable();
        cy.clickSettingsRow('Late');

        cy.get('.form-control', { timeout: 10000 })
            .first()
            .should('be.visible')
            .clear()
            .type('10');

        cy.get('.form-group > .btn', { timeout: 10000 })
            .first()
            .should('be.visible')
            .should('not.be.disabled')
            .click();
    });

    it('should configure customized late deduction tiers', () => {
        cy.navigateMenu([
            '#settings_list > a',
            '#company_list > a',
            '#companies_general_settings > a'
        ]);

        cy.waitForSettingsTable();
        cy.clickSettingsRow('Late');

        cy.get('#customize_late', { timeout: 10000 })
            .should('exist')
            .click({ force: true });
        cy.wait(1000);

        cy.get(':nth-child(1) > .form-control', { timeout: 10000 })
            .first()
            .type('5', { force: true });

        cy.get('.form > :nth-child(2) > .form-control', { timeout: 10000 })
            .type('10', { force: true });

        cy.get(':nth-child(3) > .form-control', { timeout: 10000 })
            .first()
            .type('10', { force: true });

        cy.get('.pull-right > .btn-success', { timeout: 10000 })
            .should('not.be.disabled')
            .click({ force: true });
    });

    it('should configure late multiplier and offset timeout settings', () => {
        cy.navigateMenu([
            '#settings_list > a',
            '#company_list > a',
            '#companies_general_settings > a'
        ]);

        cy.waitForSettingsTable();
        cy.clickSettingsRow('Late');

        cy.get('#is_late_multiplier_used', { timeout: 10000 })
            .should('exist')
            .click();

        cy.wait(1000);

        cy.get('#offset_timeout', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_consider_grace_period_for_flexible_schdule', { timeout: 10000 })
            .should('exist')
            .click();
    });
});
