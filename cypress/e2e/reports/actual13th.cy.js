describe('Reports - Accrual 13th Month Pay', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should view accrual 13th month report', () => {
        cy.navigateMenu(['#reports_list > [href="#"]', '#accrual_thirteenth_month_pays > a']);
        cy.select2First('.col-sm-3 > .form-group > .ui-select-container > .select2-choice > .select2-chosen.ng-binding');
        cy.get('tabletoolstrans > .input-group > .form-control', { timeout: 15000 }).should('be.visible').type('juan');
        cy.get('.form-group > .btn', { timeout: 15000 }).should('not.be.disabled').click();
    });
});
