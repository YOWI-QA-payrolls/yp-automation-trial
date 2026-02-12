describe('Settings - GL Accounts - Assigned Accounts', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should navigate to GL Accounts assigned accounts page', () => {
        cy.navigateMenu([
            '#settings_list > a',
            '#company_list > a',
            '#profiles > a',
            '#gl_accounts > a'
        ]);
    });
});
