describe('Employee AR Account', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should navigate to AR account and interact with advance filter', () => {
        cy.intercept('POST', '**/ar_accounts/read_pagination/**').as('loadARData');
        cy.visit('/employees/information/ar_accounts/main_page');
        cy.get('#side-menu', { timeout: 20000 }).should('exist');

        cy.get('#advance-filter-btn', { timeout: 15000 }).should('be.visible').click();
        cy.get('#advance-search').click();

        cy.wait('@loadARData').its('response.statusCode').should('eq', 200);

        cy.get('tbody > :nth-child(2) > :nth-child(2)').click();
        cy.get('label > .ng-pristine').click();
        cy.get(':nth-child(1) > .ng-scope > .form-control').type('456');
    });
});
