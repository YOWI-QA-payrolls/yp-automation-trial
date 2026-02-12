describe('Reports - Employment Status: New Hire', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should view new hire report', () => {
        cy.navigateMenu([
            '#reports_list > [href="#"]',
            '#employee_status_list > a'
        ]);
        cy.get('#new_hire > a', { timeout: 15000 }).should('exist').click({ force: true });
        cy.get('.form-group > .btn', { timeout: 15000 }).should('be.visible').click();
        cy.get('tabletoolstrans > .input-group > .form-control', { timeout: 15000 }).type('wow');
        cy.get('[ng-if="!main.no_search_button"]').click();
    });
});
