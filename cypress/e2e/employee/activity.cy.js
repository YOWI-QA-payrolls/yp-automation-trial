describe('Employee Activity', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should navigate to employee performance and search', () => {
        cy.navigateMenu([
            '#reports_list > a',
            '#employee_performance > a',
        ]);

        cy.get('tbody', { timeout: 30000 }).should('exist');

        cy.get('body').then($body => {
            if ($body.find('.hand_cursor').length > 0) {
                cy.get('.hand_cursor > :nth-child(2)').first().click();
                cy.select2First(':nth-child(1) > td > :nth-child(1) > .ui-select-container > .select2-choice > .select2-chosen.ng-binding');
                cy.get('.input-group-btn > .btn').click();
                cy.get('.btn-info').click();
            }
        });
    });
});
