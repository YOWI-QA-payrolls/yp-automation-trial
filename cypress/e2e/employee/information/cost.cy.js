describe('Employee Cost Center', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should navigate to cost center and select from dropdown', () => {
        cy.visit('https://yp2.yahshuasolutions.com/employees/information/cost_centers/main_page');
        cy.get('#side-menu', { timeout: 20000 }).should('exist');

        cy.get('#advance-filter-btn', { timeout: 15000 }).should('be.visible').click();
        cy.get('#advance-search').click();

        cy.get('tbody', { timeout: 30000 }).should('exist');

        cy.get('tbody > :nth-child(3) > :nth-child(2)').click();
        cy.select2First(':nth-child(1) > .ui-select-container > .select2-choice > .select2-chosen.ng-binding');
    });
});
