// const { describe } = require("mocha");

describe('login', () => {
    // This code will run before each test case in this describe block
    beforeEach(() => {
        // Load login credentials from the fixture file
        cy.fixture('credentials').then(credentials => {
            const { url, email, pass } = credentials;
  
            // Login
        cy.viewport(1280, 800);

            cy.visit(url);
            cy.get(':nth-child(1) > .form-control').type(email);
            cy.get(':nth-child(2) > .form-control').type(pass);
            cy.get('.custom-mb').click();
            
        });
    });
  
    describe('Daily log', () => {
        it('should calendar search', () => {
        cy.get('#timesheets').click();
        cy.get('#daily_logs > a').click();
        cy.wait(2000);
        cy.get('.input-group > :nth-child(1) > .btn').click();
        cy.get('.uib-datepicker-popup').contains('13').click();
        cy.get('.input-group > :nth-child(5) > .btn').click();
        cy.get('.uib-datepicker-popup').contains('19').click()
        cy.wait(3000);
        // cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > button:nth-child(2)').click();
        // cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > div > div.popover-inner > div > div > div > span.ng-scope > div:nth-child(1) > div').click();
        // cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > div > div.popover-inner > div > div > div > span.ng-scope > div:nth-child(1) > div > div > div > input')
        // .type('Complete {enter}');
        // cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > div > div.popover-inner > div > div > div > span.ng-scope > div:nth-child(2) > div')
        // .click();
        // cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > div > div.popover-inner > div > div > div > span.ng-scope > div:nth-child(2) > div > div > div > input')
        // .type('Normal {enter}');
        // // cy.get('.select2-highlighted > .select2-result-label > .ng-binding')
        // cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > div > div.popover-inner > div > div > div > span.ng-scope > div:nth-child(3) > div')
        // .click();
        // cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > div > div.popover-inner > div > div > div > span.ng-scope > div:nth-child(3) > div > ul > li > input')
        // .type('Main {enter}');
        // cy.get('[ng-click="main.multiple_select(filters,\'division\',divisions2)"] > .fa').click();
        // cy.get('[ng-click="main.multiple_select(filters,\'department\',departments2);main.change_by_department(current_scope,filters.department,null,\'employees2\',include_inactive.value,filters)"] > .fa')
        // .click();
        // cy.get('[ng-click="main.multiple_select(filters,\'position\',positions3);main.change_by_position(current_scope,filters.position,include_inactive.value,filters)"] > .fa')
        // .click();
        // cy.get('.btn-sm').click();

        //toggle

        // cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > button.btn.btn-default.dropdown-toggle.ng-scope')
        // .click({ force: true });

        // cy.get('[ng-if="!main.key_in_list(main.current_module,[\'employee_leave_monitoring\',\'leave_accruals\',\'employee_contributions\',\'employee_additional_pay\',\'employee_other_additional_pay\',\'employee_deductions\',\'employee_recurring_deductions\',\'employee_other_deductions\',\'payroll_register\',\'logs_\',\'complete_timesheet\',\'analysis\',\'detailed_accounting_entries\',\'summary_accounting_entries\',\'ut_approval\',\'ot_approval\',\'holiday_approval\',\'restday_approval\',\'official_business_approval\',\'top10_early_birds2\',\'early_birds2\',\'top10_late_employees\',\'monthly_late_employees\',\'late_employees2\',\'absences\',\'summary_absences\',\'monthly_absent_employees\',\'accrual_thirteenth_month_pays\',\'accrual_thirteenth_month_pays_by_cc\',\'logs_verification_reports\',\'activity_report\',\'pdc_employee_profile\',\'pdc_employee_location\',\'pdc_employee_department_and_position\',\'pdc_employee_employment_type\',\'pdc_employee_class\',\'pdc_employee_cost_center\',\'pdc_employee_division\',\'pdc_employee_section\',\'pdc_employee_salary\',\'pdc_employee_bank_account\',\'pdc_employee_statutory\',\'pdc_employee_additional_pay\',\'pdc_employee_other_additional_pay\',\'pdc_employee_deduction\',\'pdc_employee_recurring_deduction\',\'pdc_employee_other_deduction\',\'pdc_employee_activity\',\'deductionbalances\',\'break_report_details\',\'payroll_registers2\',\'pdc_employee_schedule\',\'payroll_calculator\',\'logs2\',\'project_timekeeping_report\'])"]')
        // .click();
        // cy.get('[ng-if="main.key_in_list(main.current_module,[\'logs_verification_reports\', \'summary_logs_verification_reports\',\'other_summary_logs_verification_reports\',\'classification_summary_logs_verification_reports\',\'daily_logs\'])"]').click();
        // cy.get('[ng-if="main.has_import && (main.current_sessions.role == \'create\' || main.current_sessions.role == \'edit\')"] > .ng-scope').click();
        // cy.get('[ng-if="main.has_print"] > .ng-scope').click();

        // cy.get('.dropdown-menu > :nth-child(5) > a').click();
        // // Click on the dropdown to open it
        // cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > div:nth-child(3) > button:nth-child(4) > i')
        // .should('be.visible')
        // .click();
      

        // // Assuming this is part of a Cypress test

        // // Click the button at div:nth-child(4) > button:nth-child(4)
        // cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > div:nth-child(4) > button:nth-child(4)')
        // .click();

        // // Click the button at div > button.btn.btn-sm.btn-success in the panel-footer
        // cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-footer > div > button.btn.btn-sm.btn-success')
        // .click();

        //resave logs address

        cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > button.btn.btn-default.dropdown-toggle.ng-scope')
        .click({ force: true });
        // Assuming this is part of a Cypress test

        // Click the icon at div:nth-child(3) > button:nth-child(4) > i
        cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > ul > li:nth-child(6) > a')
        .click();

        // Click the button at div:nth-child(4) > button:nth-child(4)
        cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > div:nth-child(4) > button:nth-child(4)')
        .click();

        // Click the button at div > button.btn.btn-sm.btn-success in the panel-footer
        cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-footer > div > button.btn.btn-sm.btn-success')
        .click();


        




        });
    });
  
    // You can add more test cases here for other scenarios
  });
  