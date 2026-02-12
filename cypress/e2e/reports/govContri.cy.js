describe('Reports - Government Contributions Summary', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should interact with government contributions date picker', () => {
        cy.navigateMenu(['#reports_list > [href="#"]', '#government_contributions_summary > a']);
        cy.get(':nth-child(2) > .form-group > .input-group > .input-group-btn > .btn', { timeout: 15000 }).should('be.visible').click();
        cy.get('.uib-datepicker-popup', { timeout: 10000 }).contains('February').click();
        cy.get(':nth-child(3) > .form-group > p.input-group > .input-group-btn > .btn').click();
        cy.get('tbody', { timeout: 30000 }).should('exist');
        cy.get('tbody tr:first > :nth-child(6) > .form-control').type('1');
        cy.get(':nth-child(5) > :nth-child(3) > .btn-group > a > .btn').click();
    });
});
