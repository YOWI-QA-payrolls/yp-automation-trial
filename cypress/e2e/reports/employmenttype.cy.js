describe('Reports - Certificate of Employment', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should generate certificate of employment', () => {
        cy.navigateMenu(['#reports_list > [href="#"]', '#certificate_of_employment > a']);
        cy.get('label > .ng-pristine', { timeout: 15000 }).should('exist').click();
        cy.select2First('.select2-chosen.ng-binding');
        cy.get('.form-group > .btn', { timeout: 15000 }).should('not.be.disabled').click();
        cy.get('.form-group > .ng-pristine').type('employment');
    });
});
