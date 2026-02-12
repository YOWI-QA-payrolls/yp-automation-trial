describe('Reports - BIR Form 1604C', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should configure BIR 1604C form', () => {
        cy.navigateMenu(['#reports_list > [href="#"]', '#bir > a', '#bir_forms > a']);
        cy.get('[heading="BIR Form No. 1604C"] > .nav-link', { timeout: 15000 }).should('be.visible').click();
        cy.select2First(':nth-child(2) > .form-group > .ui-select-container > .select2-choice > .select2-chosen.ng-binding');
    });
});
