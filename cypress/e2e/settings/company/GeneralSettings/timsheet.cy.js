describe('login', () => {
    // This code will run before each test case in this describe block
    beforeEach(() => {
        // Load login credentials from the fixture file
        cy.fixture('credentials').then(credentials => {
            const { url, email, pass } = credentials;
 
            // Login
            cy.visit(url);
            cy.get(':nth-child(1) > .form-control').type(email);
            cy.get(':nth-child(2) > .form-control').type(pass);
            cy.get('.custom-mb').click();
        });
    });
 
    describe('settings', () => {
        it('10 mins late', () => {

            cy.get('#settings_list > a').click();
            cy.get('#company_list > a').click({ force: true });
            cy.get('#profiles > a').click({ force: true });
            cy.get('#companies_general_settings > a').click();

            cy.wait(2000);

            cy.get('#tableee > tbody > tr:nth-child(5) > td > h3:nth-child(1) > a').click();

            cy.get('#schedule_in_timekeeper').click();

            cy.get('#is_activate_auto_generate_employee_id').click();

            cy.get('#is_activate_auto_generate_employee_id').click();

            cy.get('#ex_autocomplete_logs').click();
            
            cy.get('#fifo_logs').click();

            cy.get('#work_from_home').click();

            cy.get('#is_activate_specific_ot_holiday').click();

            cy.get('#is_activate_specific_ot_holiday_per_range').click();

            cy.get('#is_activate_qr_scanner').click

            cy.get('#activate_rfid').click();

            cy.get('#is_activate_one_log_restriction').click();

            cy.get('#is_activate_geo_fencing').click();

            cy.get('#biometrics_use_system_id').click();

            cy.get('#is_activate_add_reason').click();

            cy.get('#is_activate_auto_generate_employee_id').click();
            
            cy.get('#is_activate_qr_scanner').click();
            
 
 
        }); // Closing it('profile') test case
    }); // Closing describe('settings')
    
}); // Closing describe('login')