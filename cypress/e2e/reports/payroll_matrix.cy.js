describe('Reports - Payroll Summary Matrix', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should select payroll and search matrix', () => {
        cy.navigateMenu(['#reports_list > [href="#"]', '#payroll_summary_matrix > a']);
        cy.select2First('.select2-choices');
        cy.get('#advance-search', { timeout: 15000 }).should('be.visible').click();
    });
});
