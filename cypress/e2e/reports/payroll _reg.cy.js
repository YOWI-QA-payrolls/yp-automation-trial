describe('Reports - Payroll Register', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should view payroll register with filter', () => {
        cy.navigateMenu(['#reports_list > [href="#"]', '#payroll_register > a']);
        cy.select2First('.col-sm-4 > .form-group > .ui-select-container > .select2-choice > .select2-chosen.ng-binding');
        cy.get('.input-group > .form-control').type('juan');
        cy.get(':nth-child(1) > [ng-show="main.columns.hours_days_present.selected"]', { timeout: 10000 }).should('be.visible').click();
    });
});
