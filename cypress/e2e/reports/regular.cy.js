describe('Reports - Regular Payroll Register', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should view regular payroll register', () => {
        cy.navigateMenu(['#reports_list > [href="#"]', '#payroll_register > a']);
        cy.get('[ng-hide="$select.isEmpty()"]').first().click({ force: true });
        cy.get('.select2-results .select2-result-label', { timeout: 10000 }).first().click({ force: true });
    });
});
