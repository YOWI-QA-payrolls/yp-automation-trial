describe('Employee Tax Beginning Balance', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should navigate to tax balance and fill in amounts', () => {
        cy.navigateMenu([
            '#employee_list > a',
            '#tax_beginning_balance > a',
        ]);

        cy.get('tabletoolstrans > .input-group > .form-control', { timeout: 15000 })
            .should('be.visible')
            .type('caleb');

        cy.get('#advance-filter-btn').click();
        cy.get('[ng-if="!main.no_search_button"]', { timeout: 10000 }).click();

        cy.get('tbody', { timeout: 30000 }).should('exist');

        cy.get('.hand_cursor > :nth-child(2)').click();
        cy.get(':nth-child(1) > :nth-child(1) > .input-group > .input-group-btn > .btn').click();
        cy.get('.btn-info').click();
        cy.get(':nth-child(1) > :nth-child(2) > .form-control').type('1000');
        cy.get(':nth-child(1) > :nth-child(3) > .form-control').type('1000');
        cy.get(':nth-child(1) > :nth-child(4) > .form-control').type('1000');
        cy.get(':nth-child(1) > :nth-child(5) > .form-control').type('1000');
        cy.get(':nth-child(1) > :nth-child(6) > .form-control').type('1000');
        cy.get(':nth-child(1) > :nth-child(7) > .form-control').type('1000');
    });
});
