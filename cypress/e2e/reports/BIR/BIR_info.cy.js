describe('Reports - BIR Information', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should search and view BIR information', () => {
        cy.navigateMenu(['#reports_list > [href="#"]', '#bir > a', '#bir_informations > a']);
        cy.get('tabletoolstrans > .input-group > .form-control', { timeout: 15000 }).should('be.visible').type('Juan');
        cy.get('[ng-if="!main.no_search_button"]').click();
        cy.get('tbody', { timeout: 30000 }).should('exist');
        cy.get('tbody tr:first .align_left').click();
        cy.get('body').then(($body) => {
            if ($body.find('#submit_button').length > 0) {
                cy.get('#submit_button').click();
            }
        });
    });
});
