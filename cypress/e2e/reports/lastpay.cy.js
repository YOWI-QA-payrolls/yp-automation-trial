describe('Reports - Last Pay', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should view last pay report and confirm', () => {
        cy.navigateMenu(['#reports_list > [href="#"]']);
        cy.get('#side-menu').contains('a', 'Last Pay', { timeout: 10000 }).should('exist').click({ force: true });
        cy.wait(2000);
        cy.select2First('.select2-choice');
        cy.get('tbody', { timeout: 30000 }).should('exist');
        cy.get('tr.ng-scope > :nth-child(2)').first().click();
        cy.get('.confirm', { timeout: 15000 }).should('be.visible').click();
    });
});
