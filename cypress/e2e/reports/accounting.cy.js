describe('Reports - Accounting Entries', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should view accounting entries report', () => {
        cy.navigateMenu(['#reports_list > [href="#"]', '#accounting_entries > a']);
        cy.select2First('.select2-search-field > .select2-input');
        cy.get('label > .ng-pristine', { timeout: 15000 }).should('exist').click();
    });
});
