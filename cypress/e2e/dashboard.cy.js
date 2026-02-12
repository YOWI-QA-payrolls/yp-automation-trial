describe('Dashboard', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    describe('Dashboard Navigation', () => {
        it('should verify dashboard loads successfully after login', () => {
            cy.get('#dashboard', { timeout: 15000 }).should('be.visible').click();
        });
    });
});
