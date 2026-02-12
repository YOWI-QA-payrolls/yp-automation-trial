describe('Reports - Last Pay', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should view last pay report and confirm', () => {
        cy.navigateMenu(['#reports_list > [href="#"]']);
        cy.get('#side-menu').contains('Last Pay').should('exist').click({ force: true });
        cy.select2First('.select2-arrow > b');
        cy.get('tbody', { timeout: 30000 }).should('exist');
        cy.get('tr.ng-scope > :nth-child(2)').click();
        cy.get('.confirm', { timeout: 15000 }).should('be.visible').click();
    });
});
