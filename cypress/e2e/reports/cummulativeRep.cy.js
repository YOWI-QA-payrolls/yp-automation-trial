describe('Reports - Cumulative Leave Monitoring', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should search and click cumulative report record', () => {
        cy.navigateMenu(['#reports_list > [href="#"]', '#cumulative_leave_monitoring_report > a']);
        cy.get('tabletoolstrans > .input-group > .form-control', { timeout: 15000 }).should('be.visible').type('Juan');
        cy.get('#advance-search').click();
        cy.get('tbody', { timeout: 30000 }).should('exist');
        cy.get('tbody tr:first > :nth-child(3)').click();
    });
});
