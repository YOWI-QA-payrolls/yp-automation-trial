describe('Settings - General Settings - Timesheet Configuration', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should configure timesheet and timekeeping settings', () => {
        cy.navigateMenu([
            '#settings_list > a',
            '#company_list > a',
            '#companies_general_settings > a'
        ]);

        cy.get('#tableee > tbody > tr', { timeout: 15000 })
            .should('have.length.greaterThan', 0);

        cy.get('#tableee > tbody > tr:nth-child(5) > td > h3:nth-child(1) > a', { timeout: 10000 })
            .should('be.visible')
            .click();

        cy.get('#schedule_in_timekeeper', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_activate_auto_generate_employee_id', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_activate_auto_generate_employee_id', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#ex_autocomplete_logs', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#fifo_logs', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#work_from_home', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_activate_specific_ot_holiday', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_activate_specific_ot_holiday_per_range', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_activate_qr_scanner', { timeout: 10000 })
            .should('exist');

        cy.get('#activate_rfid', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_activate_one_log_restriction', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_activate_geo_fencing', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#biometrics_use_system_id', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_activate_add_reason', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_activate_auto_generate_employee_id', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_activate_qr_scanner', { timeout: 10000 })
            .should('exist')
            .click();
    });
});
