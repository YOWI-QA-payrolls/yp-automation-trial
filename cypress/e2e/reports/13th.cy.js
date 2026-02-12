describe('Reports - 13th Month (Bonus)', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should view bonus report details', () => {
        cy.navigateMenu(['#reports_list > [href="#"]', '#bonus > a']);
        cy.select2First('.col-sm-3 > .form-group > .ui-select-container > .select2-choice > .select2-chosen.ng-binding');
        cy.get('tabletoolstrans > .input-group > .form-control', { timeout: 15000 }).should('be.visible').type('juan');
        cy.get('.form-group > .btn').click();
        cy.get('tbody', { timeout: 30000 }).should('exist');
        cy.get('tbody tr:first [ng-click="details_dialog(record)"]').click();
        cy.get('.panel > .panel-footer > .pull-right > .btn').click();
    });
});
