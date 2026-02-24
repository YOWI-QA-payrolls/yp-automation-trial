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

        cy.get('#advance-filter-btn', { timeout: 15000 }).should('be.visible').click();
        cy.get('#advance-search').click();

        cy.get('tbody', { timeout: 30000 }).should('exist');

        cy.get('[ng-click="create_dialog()"]').click();
        // Wait for the modal/dialog to be visible before accessing fields
        cy.get('.modal, .modal-dialog', { timeout: 10000 }).should('be.visible');
        cy.get('#lastname', { timeout: 10000 }).should('be.visible').type('Lana');
        cy.get('#firstname', { timeout: 10000 }).should('be.visible').type('Del Rey');
        
    });
});
