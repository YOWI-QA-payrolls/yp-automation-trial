describe('Reports - BIR Form 1601C', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should configure BIR 1601C form', () => {
        cy.navigateMenu(['#reports_list > [href="#"]', '#bir > a', '#bir_forms > a']);
        cy.get('[heading="BIR Form No. 1601C"] > .nav-link', { timeout: 15000 }).should('be.visible').click();
        cy.get('.active > .panel-body > .col-sm-2 > .form-group > .input-group > .input-group-btn > .btn', { timeout: 15000 }).should('be.visible').click();
        cy.get('.uib-datepicker-popup', { timeout: 10000 }).contains('February').click();
        cy.get(':nth-child(3) > .input-group-btn > .btn').click();
        cy.get('.active > .panel-body > :nth-child(5) > .btn-group > .btn', { timeout: 15000 }).should('not.be.disabled').click();
    });
});
