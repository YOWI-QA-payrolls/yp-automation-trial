describe('Reports - Payroll Summary', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should view payroll summary report', () => {
        cy.navigateMenu(['#reports_list > [href="#"]', '#payroll_summary > a']);
        cy.select2First('.select2-chosen.ng-binding');
        cy.get('#advance-search').click();
    });
});
