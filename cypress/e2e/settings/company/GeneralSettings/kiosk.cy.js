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

            cy.get(':nth-child(11) > td').click();

            cy.get('#show_payslip_not_viewed');
            cy.get('#is_show_legend_daily_logs')
            cy.get('#is_kiosk_user_disable_request').click();

            cy.get('#is_use_schedule_code').click();
            cy.get('#is_sort_leave_type_by_code').click();

            cy.get('#is_hide_overtime').click();
            cy.get('#is_hide_undertime').click();
            cy.get('#is_hide_workonholiday').click();
            cy.get('#is_hide_workonrestday').click();
            cy.get('#is_hide_leave').click();
            cy.get('#is_hide_officialbusiness').click();
            cy.get('#hide_cash_advance').click();

            cy.get('#show_calendar').click();
            cy.get('#is_activate_timekeeping_module').click();

            cy.get('#show_certificates').click();

            cy.get('#has_timein_out_access').click();
            cy.get('[ng-if="kiosk_settings.has_timein_out_access"][style=""] > .col-sm-8 > .ui-select-container > .select2-choices > .select2-search-field > .select2-input').click();

            cy.get(':nth-child(2) > .select2-result-label > .ng-binding').click();

            cy.get(':nth-child(4) > .col-sm-8 > .ui-select-container > .select2-choices > .select2-search-field > .select2-input').click();
            cy.get('.select2-highlighted > .select2-result-label > .ng-binding').click();
            cy.get('#has_project_timekeeping').click();

            cy.get('.form-group > .btn').click();
 
        }); // Closing it.skip('profile') test case
    }); // Closing describe('settings')
    
}); // Closing describe('login')