describe('Reports - Employee Ledgers', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should search employee ledger', () => {
        cy.navigateMenu(['#reports_list > [href="#"]', '#employeeledger > a']);
        cy.get('.form-group > .btn', { timeout: 15000 }).should('be.visible').click();
        cy.get('tabletoolstrans > .input-group > .form-control', { timeout: 15000 }).type('juan');
        cy.get('.form-group > .btn').click();
    });
});
