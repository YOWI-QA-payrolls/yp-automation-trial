describe('Reports - BIR Form 2316', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should configure BIR 2316 form', () => {
        cy.navigateMenu(['#reports_list > [href="#"]', '#bir > a', '#bir_forms > a']);
        cy.select2First(':nth-child(1) > .form-group > .ui-select-container > .select2-choice');
        cy.get(':nth-child(3) > .btn-group > .btn').click();
    });
});
