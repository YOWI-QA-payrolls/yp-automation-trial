describe('Employee Profile', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should navigate to employee info and create a new profile', () => {
        cy.navigateMenu([
            '#employee_list > a',
            '#information_list > a',
            '#employeeinfo > a',
        ]);

        cy.get('body').then($body => {
            if (!$body.find('#advance-search').length) {
                cy.get('#advance-filter-btn', { timeout: 15000 }).should('be.visible').click();
            }
        });
        cy.get('#advance-search', { timeout: 10000 }).should('be.visible').click();

        cy.get('tbody', { timeout: 30000 }).should('exist');

        cy.get('[ng-click="create_dialog()"]').first().click({ force: true });
        cy.get('.modal.in', { timeout: 15000 }).should('be.visible');
        cy.get('#lastname', { timeout: 10000 }).should('be.visible').type('Lana');
        cy.get('body').then($body => {
            if ($body.find('#firstname').length > 0) {
                cy.get('#firstname').scrollIntoView().should('be.visible').type('Del Rey');
            }
        });
        
    });
});
