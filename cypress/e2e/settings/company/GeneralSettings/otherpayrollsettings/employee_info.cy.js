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
        it('customized late', () => {
            
            cy.get('#settings_list > a').click();
            cy.get('#company_list > a').click({ force: true });
            cy.get('#profiles > a').click({ force: true });
            cy.get('#companies_general_settings > a').click();

            cy.get(':nth-child(10) > td').click();

            cy.get(':nth-child(8) > td').click();

            cy.get('#is_show_employee_division').click();
            cy.get('#is_show_class').click();
            

            cy.get('#is_show_employee_section_unit_subunit').click();

            cy.get('#is_show_shift').click();

            cy.get('#is_show_overtime_leave_offset').click();

            cy.get('#is_show_early_time_in_range').click();

            cy.get('#is_show_posting_keys').click();

            cy.get('.form-group > .btn');


 
        }); // Closing it('profile') test case
    }); // Closing describe('settings')
    
}); // Closing describe('login')