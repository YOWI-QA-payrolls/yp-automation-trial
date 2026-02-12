describe('Reports - BIR Withholding Tax', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should search and view withholding records', () => {
        cy.navigateMenu(['#reports_list > [href="#"]', '#bir > a', '#bir_1601c_form > a']);
        cy.get('tabletoolstrans > .input-group > .form-control', { timeout: 15000 }).should('be.visible').type('Juan');
        cy.get('[ng-if="!main.no_search_button"]').click();
        cy.get('tbody', { timeout: 30000 }).should('exist');
        cy.get('tbody tr:first > :nth-child(3)').click();
    });
});
