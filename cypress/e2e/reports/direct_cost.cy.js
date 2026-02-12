describe('Reports - Direct Cost', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should configure and run direct cost report', () => {
        cy.navigateMenu(['#reports_list > [href="#"]', '#direct_cost > a']);
        cy.get('.form-group > .btn', { timeout: 15000 }).should('be.visible').click();
        cy.get('#select_payroll_period', { timeout: 15000 }).should('exist').click({ force: true });
        cy.get('[ng-click="main.filter.pay_period = main.payroll_histories"]').click();
        cy.get('.form-group > .btn', { timeout: 15000 }).should('not.be.disabled').click();
    });
});
