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
        it('customized late', function() { this.skip();
            cy.get('#settings_list > a').click();
            cy.get('#company_list > a').click({ force: true });
            cy.get('#profiles > a').click({ force: true });
            cy.get('#companies_general_settings > a').click();

            cy.get(':nth-child(9) > td').click();

            cy.wait(3000);

            cy.get('#internal_balance').click();
            cy.get('#external_balance').click();

            cy.get('#show_late_on_payslip').click();
            cy.get('#show_undertime_on_payslip').click();
            cy.get('#show_absent_on_payslip').click();

            cy.get('#hide_amount_on_late').click();
            cy.get('#hide_amount_on_undertime').click();
            cy.get('#is_hide_amount_on_absent').click();
            cy.get('#is_hide_header_payslip_module_name').click();
            cy.get('#hide_days_on_payslip').click();
            cy.get('#hide_hours_on_payslip').click();
            cy.get('#logo_show_company_address').click();
            cy.get('#loan_to_date').click();
            cy.get('#year_to_date').click();
            cy.get('#summary_of_st').click();
            cy.get('#show_sss_mpf_on_payslip').click();
            cy.get('#show_more_employees_one_page').click();
            cy.get('#show_employmenttype_on_payslip').click();
            cy.get('#enable_employee_signature').click();
            cy.get('#enable_employee_acknowledgement_remarks').click();
            cy.get('#show_zero_net_pay').click();
            cy.get('#is_other_payslip_format').click();
            cy.get('#show_logo_in_payslip').click();
            cy.get('#auto_email_payslip').click();
            cy.get('#is_include_no_timein_timeout_in_absent').click();

            cy.get('#is_hide_company_name').click();
            cy.get('#is_hide_bank_account').click();

            cy.get('.ibox-content > :nth-child(6)')
                .find('input[type="checkbox"]')
                .each(($checkbox) => {
                    if (!$checkbox.is(':checked')) {
                        cy.wrap($checkbox).check();
                    }
                });

            cy.get('#is_hide_amounts_on_accountant_report').click();
            cy.get('#is_exclude_restday_st_in_bonus').click();
            cy.get('#is_include_holiday_pay_for_daily').click();
            cy.get('#is_exclude_late_ut_computation').click();
            cy.get('#exclude_holiday_pay').click();

            cy.get('#is_allow_late_no_timeout').click();

            

            // Uncomment and modify the following lines as needed for your test
            cy.get(':nth-child(3) > .input-group > .form-control').type('5');
            cy.get(':nth-child(4) > .input-group > .form-control').type('5');

            cy.get('#is_show_total_number_of_days_worked').click();
            cy.get('.col-sm-2 > .ui-select-container > .select2-choices').click();

            cy.get(':nth-child(6) > .select2-result-label > .ng-binding').click();
            cy.get('#longevity_increase_regularization').click();

            cy.get('.form-group > .col-sm-4 > .ui-select-container > .select2-choice > .select2-chosen.ng-binding').click();
            cy.get(':nth-child(2) > .select2-result-label').click();

            cy.get('#is_add_100_percent_on_ot_summary').click();

            cy.get('#activate_sap_entries').click();

            cy.get(':nth-child(5) > .ui-select-container > .select2-choice > .select2-chosen.ng-binding').click();

            cy.get('#activate_billing_statement').click();

            cy.get('#hdmf_same_amount_ee_er').click();

            cy.get('#is_allow_advance_leave_credits').click();

            cy.get(':nth-child(61) > :nth-child(2) > .form-control').type('123456789');

            cy.get(':nth-child(61) > :nth-child(3) > .form-control').type('sample_name');
            cy.get(':nth-child(61) > :nth-child(4) > .form-control').type('sample_school');
            cy.get(':nth-child(61) > :nth-child(5) > .form-control').type('sample_school123');
            cy.get(':nth-child(61) > :nth-child(6) > .form-control').type('sample_add');

            cy.get('[ng-click="report_settings.ceap_employmenttype = employmenttypes2"] > .fa').click();
            cy.get('#salary_show_other_earnings').click();
            cy.get('.col-sm-2.pull-right > .form-group > .btn');

            
        });
    });
});
