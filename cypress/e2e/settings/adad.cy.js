describe('Settings - Additional Data', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should navigate to additional data settings page', () => {
        cy.navigateMenu([
            '#settings_list > a'
        ]);
    });
});
