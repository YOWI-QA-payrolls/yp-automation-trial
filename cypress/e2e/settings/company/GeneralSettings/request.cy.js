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
        it('10 mins late', () => {

            cy.get('#settings_list > a').click();
            cy.get('#company_list > a').click({ force: true });
            cy.get('#profiles > a').click({ force: true });
            cy.get('#companies_general_settings > a').click();

            cy.wait(2000);

            cy.get(':nth-child(3) > td').click();
            
            cy.get('#ex_overtime_max').click();

            // cy.get(':nth-child(5) > :nth-child(2) > .form-control').type('1');

            // cy.get(':nth-child(4) > .form-control').type('3');

            cy.get('#overtime_request_maximum').click();

            // cy.get(':nth-child(9) > .input-group > .form-control').type(3);

            cy.get('#ex_holiday').click();
            cy.get('#ex_holiday_all_employees').click();
            cy.get('#ex_restday').click();

            cy.get('#ot_rule').click();

            // cy.get(':nth-child(19) > .input-group > .form-control').type('10');

            cy.get('#ot_threshold').click();
            cy.get(':nth-child(21) > .form-group > .input-group > .form-control').type('10');

            cy.get('#minimum_ot').click();
            cy.get('#is_disabled_overtime_on_restday').click();

            cy.get('#late_threshold').click();

            cy.get('#is_late_accumulated').click();

            cy.get('#disable_late_undertime_if_rd_or_holiday').click();

            cy.get('#exclude_night_diff_rate').click();

            cy.get('#ut_rule').click();

            cy.get('#night_diff_threshold').click();

            cy.get('#nd_minimum').click();

            cy.get('#nd_rule').click();

            cy.get('#restrict_halfday').click();

            cy.get('#activate_union_leave').click();
            
            cy.get('#word_hrs_as_ot').click();

            cy.get('#allow_customized_hours').click();

            cy.get('#hide_leave_amount').click();

            cy.get('#hide_overtime_module').click();

            cy.get('#activate_overtime_compensation').click();

            cy.get('#allow_custom_conversion').click();

            cy.get('#restrict_days_to_apply_leave').click();

            
            cy.get('#emergency_leave').click();

            cy.get('#early_in_as_ot').click();

            cy.get('#is_allow_holiday_restday_single_application').click();

            cy.get('#enable_ot_restriction').click();

            cy.get('#is_enabled_ot_application_previous_payroll').click();

            cy.get('#allow_ob_restday_holiday').click();

            cy.get('#is_time_log_requests_active').click();

            cy.get('#is_activate_allowance').click();
            cy.get('#is_lunch').click();

            cy.get('#is_activate_change_schedule_request').click();

            cy.get('#is_allow_zero_minute_overtime').click();

            cy.get('.row > :nth-child(3) > .btn').click();
            cy.get(':nth-child(1) > .form-control').type('1');
            cy.get('.form > :nth-child(2) > .form-control').type('2');
            cy.get(':nth-child(3) > .form-control').type('3');
            cy.get('[ng-click="main.multiple_select(restriction_day_list,\'leave_types\',leave_types)"]').click();
            cy.get('.pull-right > .btn-success').click();


            cy.get('#woh_hrs_as_ot').click();

            cy.get(':nth-child(1) > .ui-select-container > .select2-choice > .select2-chosen.ng-binding').click();
            cy.get(':nth-child(6) > .select2-result-label > .ng-binding').click();

            cy.get('[ng-click="lunch_allowance_setting.departments = departments2"] > .fa').click();
            cy.get('[ng-click="lunch_allowance_setting.positions = lunch_positions"] > .fa').click();

            cy.get('.col-sm-2 > .form-control').type('150');
            cy.get('.col-sm-1 > .btn').click();

            // cy.get('.form-group > .btn').click();
 
        }); // Closing it.skip('profile') test case
    }); // Closing describe('settings')
    
}); // Closing describe('login')