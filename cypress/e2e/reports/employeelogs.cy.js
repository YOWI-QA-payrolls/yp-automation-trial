describe('Reports - Employee Logs Monitoring', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should filter employee logs by date', () => {
        cy.navigateMenu(['#reports_list > [href="#"]', '#employee_logs_monitoring > a']);
        cy.get('[ng-click="main.open_date(\'filter_date_from\')"]', { timeout: 15000 }).should('be.visible').click();
        cy.get('.uib-datepicker-popup .uib-left', { timeout: 10000 }).click();
        cy.get('.uib-datepicker-popup').contains('1').click();
        cy.get(':nth-child(8) > .btn').click();
    });
});
