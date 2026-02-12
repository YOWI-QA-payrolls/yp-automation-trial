describe('Settings - General Settings - Employee Info Settings', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should toggle employee information display settings', () => {
        cy.navigateMenu([
            '#settings_list > a',
            '#company_list > a',
            '#companies_general_settings > a'
        ]);

        cy.get('#tableee', { timeout: 30000 }).should('exist');

        cy.get(':nth-child(10) > td', { timeout: 15000 })
            .should('be.visible')
            .click();

        cy.get(':nth-child(8) > td', { timeout: 10000 })
            .should('be.visible')
            .click();

        cy.get('#is_show_employee_division', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_show_class', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_show_employee_section_unit_subunit', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_show_shift', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_show_overtime_leave_offset', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_show_early_time_in_range', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_show_posting_keys', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('.form-group > .btn', { timeout: 10000 })
            .should('exist');
    });
});
