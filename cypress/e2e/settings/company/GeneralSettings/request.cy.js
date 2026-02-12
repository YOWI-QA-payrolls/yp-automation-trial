describe('Settings - General Settings - Request Configuration', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should configure overtime, leave, and request settings', () => {
        cy.navigateMenu([
            '#settings_list > a',
            '#company_list > a',
            '#companies_general_settings > a'
        ]);

        cy.get('#tableee', { timeout: 30000 }).should('exist');

        cy.get(':nth-child(3) > td', { timeout: 15000 })
            .should('be.visible')
            .click();

        cy.get('#ex_overtime_max', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#overtime_request_maximum', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#ex_holiday', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#ex_holiday_all_employees', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#ex_restday', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#ot_rule', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#ot_threshold', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get(':nth-child(21) > .form-group > .input-group > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('10');

        cy.get('#minimum_ot', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_disabled_overtime_on_restday', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#late_threshold', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_late_accumulated', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#disable_late_undertime_if_rd_or_holiday', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#exclude_night_diff_rate', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#ut_rule', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#night_diff_threshold', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#nd_minimum', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#nd_rule', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#restrict_halfday', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#activate_union_leave', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#word_hrs_as_ot', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#allow_customized_hours', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#hide_leave_amount', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#hide_overtime_module', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#activate_overtime_compensation', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#allow_custom_conversion', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#restrict_days_to_apply_leave', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#emergency_leave', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#early_in_as_ot', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_allow_holiday_restday_single_application', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#enable_ot_restriction', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_enabled_ot_application_previous_payroll', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#allow_ob_restday_holiday', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_time_log_requests_active', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_activate_allowance', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_lunch', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_activate_change_schedule_request', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_allow_zero_minute_overtime', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('.row > :nth-child(3) > .btn', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();

        cy.get(':nth-child(1) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('1');

        cy.get('.form > :nth-child(2) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('2');

        cy.get(':nth-child(3) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('3');

        cy.get('[ng-click="main.multiple_select(restriction_day_list,\'leave_types\',leave_types)"]', { timeout: 10000 })
            .should('be.visible')
            .click();

        cy.get('.pull-right > .btn-success', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();

        cy.get('#woh_hrs_as_ot', { timeout: 10000 })
            .should('exist')
            .click();

        cy.select2First(':nth-child(1) > .ui-select-container > .select2-choice > .select2-chosen.ng-binding');

        cy.get('[ng-click="lunch_allowance_setting.departments = departments2"] > .fa', { timeout: 10000 })
            .should('be.visible')
            .click();

        cy.get('[ng-click="lunch_allowance_setting.positions = lunch_positions"] > .fa', { timeout: 10000 })
            .should('be.visible')
            .click();

        cy.get('.col-sm-2 > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('150');

        cy.get('.col-sm-1 > .btn', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();
    });
});
