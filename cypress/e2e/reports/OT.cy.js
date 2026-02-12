describe('Reports - OT Summary', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should search OT summary and change payroll period', () => {
        cy.navigateMenu(['#reports_list > [href="#"]', '#ot_summary > a']);
        cy.get('tabletoolstrans > .input-group > .form-control', { timeout: 15000 }).should('be.visible').type('Juan');
        cy.get('#advance-search').click();
        cy.get('tbody', { timeout: 30000 }).should('exist');
        cy.get('tbody tr:first > :nth-child(3)').click();
        cy.get('#select_payroll_period', { timeout: 15000 }).should('exist').click({ force: true });
        cy.get('[ng-click="main.filter.pay_period = main.payroll_histories"] > .fa').click();
        cy.get('.form-group > .btn').click();
    });
});
