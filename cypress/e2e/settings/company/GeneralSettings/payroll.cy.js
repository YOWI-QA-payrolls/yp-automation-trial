describe('login', () => {
    // This code will run before each test case in this describe block
    beforeEach(() => {
        // Load login credentials from the fixture file
        cy.fixture('credentials').then(credentials => {
            const { url, email, pass } = credentials;
 
            // Login
            cy.visit(url);
            cy.get('#email').type(email);
            cy.get('#password').type(pass);
            cy.get('#signin-button').click();
        });
    });

    describe('settings', () => {
        it('customized late', () => {
            
            cy.get('#settings_list > a').click();
            cy.get('#company_list > a').click({ force: true });
            cy.get('#profiles > a').click({ force: true });
            cy.get('#companies_general_settings > a').click();

            cy.get(':nth-child(2) > td').click();

            // settings

            cy.get('#exclude_cola_overtime').click();
            cy.get('#exclude_cola_leave').click();

            cy.get('#commissions').click();

            cy.get(':nth-child(18) > :nth-child(2) > .ui-select-container > .select2-choice > .select2-chosen.ng-binding').click();

            cy.get(':nth-child(2) > .select2-result-label > .ng-binding').click();

            cy.get(':nth-child(21) > :nth-child(2) > .ui-select-container > .select2-choice').click();
            cy.get(':nth-child(2) > .select2-result-label > .ng-binding').click();

            cy.get(':nth-child(5) > .ui-select-container > .select2-choice').click();
            cy.get(':nth-child(2) > .select2-result-label > .ng-binding').click();


            cy.get(':nth-child(8) > .ui-select-container > .select2-choice').click();
            cy.get(':nth-child(2) > .select2-result-label > .ng-binding').click();

            cy.get('#activate_late_amount_holiday').click();

            cy.get('#activate_late_amount_restday').click();

            cy.get('#is_dynamic_schedule').click();

            cy.get('#transfer_undertime_after_gross_pay').click();

            cy.get('#exclude_grace_period').click();

            cy.get('#activate_early_timein').click();

            cy.get('#activate_early_timein_range').click();

            cy.get('#paid_incomplete_logs').click();

            cy.get('#show_inactive_employees').click();

            cy.get('#work_restday_exclude_st').click();

            cy.get('#is_resday_premium_complete_weekly').click();

            cy.get('#is_exclude_holiday_pay_for_unworked_special_holiday').click();

            cy.get('#enable_holiday_pay_configuration').click();

            // cy.get('#fixed_hour_on_holiday').click();

            cy.get('#use_hourly_rate_in_premiums').click();

            cy.get('#merge_holiday_to_basic_pay').click();

            cy.get('#merge_holiday_to_basic_pay').click();

            cy.get('#is_set_as_default_restday').click();

            cy.get('#no_holiday_pay').click();
            cy.get('#mns_no_work_no_pay').click();

            cy.get('#paid_holiday_rd').click();

            cy.get('#activate_school_modules').click();

            cy.get('#allow_zero_salary').click();

            cy.get('#employee_threshold_salary').click();

            cy.get('#complete_basic_pay').click();

            cy.get('#hdmf_basic_pay_percentage').click();

            cy.get('#phic_use_basic_pay').click();

            cy.get('#exclude_holiday_pay_in_contribution').click();

            cy.get('#exclude_holiday_pay_in_contribution_but_include_woh_days').click();

            cy.get('#exclude_leave_with_pay_in_basic_pay').click();


            cy.get('#tax_offset')

            cy.get('#allow_ot_allowance')

            cy.get('#is_activate_allowance_based_on_time')

            cy.get('#is_activate_auto_allowance_for_restday')

            cy.get('#overtime_calculation_by_quarter')

            cy.get('#activate_currency_converter')

            cy.get('#lock_schedule_editing')

            cy.get('#is_weekly_hours_schedule')

            cy.get('#is_activate_earnings_breakdown')

            cy.get('#show_payroll_approval_column')

            cy.get('#employee_require_statutory_id')

            cy.get('#is_activate_fix_setup_allowances')


        }); // Closing it('profile') test case
    }); // Closing describe('settings')
    
}); // Closing describe('login')