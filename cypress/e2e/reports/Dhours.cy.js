describe('Reports - Daily Hours Worked', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should filter daily hours worked by date', () => {
        cy.navigateMenu(['#reports_list > [href="#"]', '#daily_hours_worked > a']);
        cy.get('[ng-click="main.open_date(\'filter_date_from\')"]', { timeout: 15000 }).should('be.visible').click();
        cy.get('.btn-group > .btn-info', { timeout: 10000 }).click();
        cy.get('.input-group > .hand_cursor').click();
    });
});
