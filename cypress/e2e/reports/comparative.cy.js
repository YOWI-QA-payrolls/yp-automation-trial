describe('Reports - Comparative Earnings', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should configure and run comparative earnings report', () => {
        cy.navigateMenu(['#reports_list > [href="#"]', '#comparative_earnings > a']);
        cy.select2First(':nth-child(2) > .form-group > .ui-select-container > .select2-choice > .select2-chosen.ng-binding');
        cy.select2First(':nth-child(3) > .form-group > .ui-select-container > .select2-choice > .select2-chosen.ng-binding');
        cy.get('.form-group > .btn', { timeout: 15000 }).should('not.be.disabled').click();
    });
});
