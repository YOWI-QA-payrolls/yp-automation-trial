describe('Reports - Longevity Increase', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should filter longevity report by date', () => {
        cy.navigateMenu(['#reports_list > [href="#"]', '#longevity_increase > a']);
        cy.get('.input-group > :nth-child(1) > .btn', { timeout: 15000 }).should('be.visible').click();
        cy.get('.uib-datepicker-popup .uib-left', { timeout: 10000 }).click();
        cy.get('.uib-datepicker-popup').contains('1').click();
        cy.get('.hand_cursor').click();
    });
});
