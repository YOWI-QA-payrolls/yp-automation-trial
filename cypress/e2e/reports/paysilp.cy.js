describe('Reports - Payslip', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should generate and view payslip', () => {
        cy.navigateMenu(['#reports_list > [href="#"]', '#payslip > a']);
        cy.select2First(':nth-child(1) > .form-group > .ui-select-container > .select2-choice > .select2-arrow > b');
        cy.select2First(':nth-child(2) > .form-group > .ui-select-container > .select2-choice');
        cy.get('.form-group > .btn', { timeout: 15000 }).should('not.be.disabled').click();
        cy.get('.btn-group > .btn', { timeout: 15000 }).should('be.visible').click();
    });
});
