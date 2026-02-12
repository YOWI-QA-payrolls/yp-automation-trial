describe('Settings - General Settings - Report Configuration', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should configure all report and payslip settings', () => {
        cy.navigateMenu([
            '#settings_list > a',
            '#company_list > a',
            '#companies_general_settings > a'
        ]);

        cy.get('#tableee', { timeout: 30000 }).should('exist');

        cy.get(':nth-child(9) > td', { timeout: 15000 })
            .should('be.visible')
            .click();

        cy.get('#internal_balance', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#external_balance', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#show_late_on_payslip', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#show_undertime_on_payslip', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#show_absent_on_payslip', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#hide_amount_on_late', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#hide_amount_on_undertime', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_hide_amount_on_absent', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_hide_header_payslip_module_name', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#hide_days_on_payslip', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#hide_hours_on_payslip', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#logo_show_company_address', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#loan_to_date', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#year_to_date', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#summary_of_st', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#show_sss_mpf_on_payslip', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#show_more_employees_one_page', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#show_employmenttype_on_payslip', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#enable_employee_signature', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#enable_employee_acknowledgement_remarks', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#show_zero_net_pay', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_other_payslip_format', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#show_logo_in_payslip', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#auto_email_payslip', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_include_no_timein_timeout_in_absent', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_hide_company_name', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_hide_bank_account', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('.ibox-content > :nth-child(6)', { timeout: 10000 })
            .find('input[type="checkbox"]')
            .each(($checkbox) => {
                if (!$checkbox.is(':checked')) {
                    cy.wrap($checkbox).check();
                }
            });

        cy.get('#is_hide_amounts_on_accountant_report', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_exclude_restday_st_in_bonus', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_include_holiday_pay_for_daily', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_exclude_late_ut_computation', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#exclude_holiday_pay', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_allow_late_no_timeout', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get(':nth-child(3) > .input-group > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('5');

        cy.get(':nth-child(4) > .input-group > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('5');

        cy.get('#is_show_total_number_of_days_worked', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('.col-sm-2 > .ui-select-container > .select2-choices', { timeout: 10000 })
            .should('be.visible')
            .click();

        cy.get(':nth-child(6) > .select2-result-label > .ng-binding', { timeout: 10000 })
            .should('be.visible')
            .click();

        cy.get('#longevity_increase_regularization', { timeout: 10000 })
            .should('exist')
            .click();

        cy.select2First('.form-group > .col-sm-4 > .ui-select-container > .select2-choice > .select2-chosen.ng-binding');

        cy.get('#is_add_100_percent_on_ot_summary', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#activate_sap_entries', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get(':nth-child(5) > .ui-select-container > .select2-choice > .select2-chosen.ng-binding', { timeout: 10000 })
            .should('be.visible')
            .click();

        cy.get('#activate_billing_statement', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#hdmf_same_amount_ee_er', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('#is_allow_advance_leave_credits', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get(':nth-child(61) > :nth-child(2) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('123456789');

        cy.get(':nth-child(61) > :nth-child(3) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('sample_name');

        cy.get(':nth-child(61) > :nth-child(4) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('sample_school');

        cy.get(':nth-child(61) > :nth-child(5) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('sample_school123');

        cy.get(':nth-child(61) > :nth-child(6) > .form-control', { timeout: 10000 })
            .should('be.visible')
            .type('sample_add');

        cy.get('[ng-click="report_settings.ceap_employmenttype = employmenttypes2"] > .fa', { timeout: 10000 })
            .should('be.visible')
            .click();

        cy.get('#salary_show_other_earnings', { timeout: 10000 })
            .should('exist')
            .click();

        cy.get('.col-sm-2.pull-right > .form-group > .btn', { timeout: 10000 })
            .should('exist');
    });
});
