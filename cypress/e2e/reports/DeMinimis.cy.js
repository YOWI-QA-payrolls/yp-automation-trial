describe('Reports - De Minimis', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should view de minimis report', () => {
        cy.navigateMenu(['#reports_list > [href="#"]', '#de_minimis_report2 > a']);
        cy.select2First('.select2-choice');
        cy.get('.form-group > .btn').click();
    });
});
