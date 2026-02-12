describe('Employee Schedule - Group Employee', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should create a group employee entry', () => {
        cy.navigateMenu([
            '#employee_list > a',
            '#employeeschedule > a',
        ]);
        cy.get('.navbar > .nav > :nth-child(3) > a', { timeout: 15000 }).should('be.visible').click({ force: true });

        cy.get('.col-sm-2 > .btn', { timeout: 15000 }).should('be.visible').click();
        cy.get('.form-control').type('testing');
        cy.select2First('.select2-input');
        cy.select2First('.select2-input');
    });
});
