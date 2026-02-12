describe('Settings - General Settings - Tax Configuration', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should configure tax calculation settings', () => {
        cy.navigateMenu([
            '#settings_list > a',
            '#company_list > a',
            '#companies_general_settings > a'
        ]);

        cy.get('#tableee', { timeout: 30000 }).should('exist');

        cy.get(':nth-child(8) > td', { timeout: 15000 })
            .should('be.visible')
            .click();

        cy.get('#activate_monthly_tax_calculation', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_activate_custom_months_daily_minimum_wage', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#activate_average_tax_calculation', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#de_minimis', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_total_threshold', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_fixed_deminimis_basic_salary', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#minimum_wage', { timeout: 10000 })
            .should('exist')
            .click();
    });
});
