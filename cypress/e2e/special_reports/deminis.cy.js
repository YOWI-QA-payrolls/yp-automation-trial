describe('Special Reports - De Minimis / ECA Report', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should navigate to De Minimis ECA report and generate it', () => {
        cy.navigateMenu([
            '#dmpi_reports_list > [href="#"]',
            '#de_minimis_eca > a'
        ]);

        cy.get('.form-group > .btn', { timeout: 10000 })
            .should('be.visible')
            .should('not.be.disabled')
            .click();
    });
});
