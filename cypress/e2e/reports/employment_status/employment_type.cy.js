describe('Reports - Employment Status: Employment Type', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should view employment type report', () => {
        cy.navigateMenu([
            '#reports_list > [href="#"]',
            '#employee_status_list > a'
        ]);
        cy.get('#employment_type > a', { timeout: 15000 }).should('exist').click({ force: true });
        cy.get('.form-group > .btn', { timeout: 15000 }).should('be.visible').click();
        cy.get('tabletoolstrans > .input-group > .form-control', { timeout: 15000 }).type('wow');
        cy.get('[ng-if="!main.no_search_button"]').click();
    });
});
