describe('Reports - Regular Payroll Register', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should view regular payroll register', () => {
        cy.navigateMenu(['#reports_list > [href="#"]', '#payroll_register > a']);
        cy.select2First('[ng-hide="$select.isEmpty()"]');
    });
});
