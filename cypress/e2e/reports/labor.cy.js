describe('Reports - Labor Summary', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should view labor summary report', () => {
        cy.navigateMenu(['#reports_list > [href="#"]', '#labor_summary > a']);
        cy.select2First('.select2-chosen.ng-binding');
        cy.get('#advance-search').click();
        cy.get(':nth-child(6) > .btn', { timeout: 15000 }).click();
    });
});
