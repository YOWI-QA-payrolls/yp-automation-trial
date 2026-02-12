describe('Settings - General Settings - Leave Settings', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should configure leave payroll settings', () => {
        cy.navigateMenu([
            '#settings_list > a',
            '#company_list > a',
            '#companies_general_settings > a'
        ]);

        cy.get('#tableee', { timeout: 30000 }).should('exist');

        cy.get(':nth-child(10) > td', { timeout: 15000 })
            .should('be.visible')
            .click();

        cy.get(':nth-child(4) > td', { timeout: 10000 })
            .should('be.visible')
            .click();

        cy.get('#leave_credit_conversion', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_allow_limit_for_leave_credits', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_activate_hours_based_on_schedule', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#allow_leave_application_on_sp_holiday', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_round_off_leave_credits', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('.form-control', { timeout: 10000 })
            .should('be.visible')
            .type('1');

        cy.get('#is_activate_fix_leave_reason', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('.col-sm-2 > .form-group > .btn', { timeout: 10000 })
            .should('exist');
    });
});
