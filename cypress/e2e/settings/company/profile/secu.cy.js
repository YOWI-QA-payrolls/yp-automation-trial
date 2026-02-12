describe('Settings - Company Profile - Security', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should navigate to security settings page', () => {
        cy.navigateMenu([
            '#settings_list > a',
            '#company_list > a',
            '#profiles > a'
        ]);
        cy.get('[heading="Security"] > .nav-link, a:contains("Security")', { timeout: 15000 }).should('exist').click({ force: true });
    });
});
