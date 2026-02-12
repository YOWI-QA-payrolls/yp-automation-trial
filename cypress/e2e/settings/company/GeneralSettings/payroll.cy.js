describe('Settings - General Settings - Payroll Configuration', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should configure all payroll settings toggles and dropdowns', () => {
        cy.navigateMenu([
            '#settings_list > a',
            '#company_list > a',
            '#companies_general_settings > a'
        ]);

        cy.get('#tableee', { timeout: 30000 }).should('exist');

        cy.get(':nth-child(2) > td', { timeout: 15000 })
            .should('be.visible')
            .click();

        cy.get('#exclude_cola_overtime', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#exclude_cola_leave', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#commissions', { timeout: 10000 })
            .should('exist')
            .click();

        cy.select2First(':nth-child(18) > :nth-child(2) > .ui-select-container > .select2-choice > .select2-chosen.ng-binding');

        cy.select2First(':nth-child(21) > :nth-child(2) > .ui-select-container > .select2-choice');

        cy.select2First(':nth-child(5) > .ui-select-container > .select2-choice');

        cy.select2First(':nth-child(8) > .ui-select-container > .select2-choice');

        cy.get('#activate_late_amount_holiday', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#activate_late_amount_restday', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_dynamic_schedule', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#transfer_undertime_after_gross_pay', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#exclude_grace_period', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#activate_early_timein', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#activate_early_timein_range', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#paid_incomplete_logs', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#show_inactive_employees', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#work_restday_exclude_st', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_resday_premium_complete_weekly', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_exclude_holiday_pay_for_unworked_special_holiday', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#enable_holiday_pay_configuration', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#use_hourly_rate_in_premiums', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#merge_holiday_to_basic_pay', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#merge_holiday_to_basic_pay', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_set_as_default_restday', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#no_holiday_pay', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#mns_no_work_no_pay', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#paid_holiday_rd', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#activate_school_modules', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#allow_zero_salary', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#employee_threshold_salary', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#complete_basic_pay', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#hdmf_basic_pay_percentage', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#phic_use_basic_pay', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#exclude_holiday_pay_in_contribution', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#exclude_holiday_pay_in_contribution_but_include_woh_days', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#exclude_leave_with_pay_in_basic_pay', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#tax_offset', { timeout: 10000 })
            .should('exist');

        cy.get('#allow_ot_allowance', { timeout: 10000 })
            .should('exist');

        cy.get('#is_activate_allowance_based_on_time', { timeout: 10000 })
            .should('exist');

        cy.get('#is_activate_auto_allowance_for_restday', { timeout: 10000 })
            .should('exist');

        cy.get('#overtime_calculation_by_quarter', { timeout: 10000 })
            .should('exist');

        cy.get('#activate_currency_converter', { timeout: 10000 })
            .should('exist');

        cy.get('#lock_schedule_editing', { timeout: 10000 })
            .should('exist');

        cy.get('#is_weekly_hours_schedule', { timeout: 10000 })
            .should('exist');

        cy.get('#is_activate_earnings_breakdown', { timeout: 10000 })
            .should('exist');

        cy.get('#show_payroll_approval_column', { timeout: 10000 })
            .should('exist');

        cy.get('#employee_require_statutory_id', { timeout: 10000 })
            .should('exist');

        cy.get('#is_activate_fix_setup_allowances', { timeout: 10000 })
            .should('exist');
    });
});
