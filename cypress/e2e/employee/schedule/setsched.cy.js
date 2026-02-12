describe('Employee Schedule - Set Schedule', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should navigate to set schedule page and click fixed side', () => {
        cy.navigateMenu([
            '#employee_list > a',
            '#employeeschedule > a',
        ]);
        cy.get('.navbar > .nav > :nth-child(4) > a', { timeout: 15000 }).should('be.visible').click();

        cy.get('.fixed-side', { timeout: 15000 }).should('be.visible').click();
    });
});
