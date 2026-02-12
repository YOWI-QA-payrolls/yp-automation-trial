describe('Reports - Advanced Filter', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should apply advanced filter on daily logs', () => {
        cy.navigateMenu([
            '#timesheets_list > a',
            '#daily_logs > a'
        ]);

        cy.get('.input-group > :nth-child(1) > .btn', { timeout: 15000 }).should('be.visible').click();
        cy.get('.uib-datepicker-popup').contains('13').click();
        cy.get('.input-group > :nth-child(5) > .btn').click();
        cy.get('.uib-datepicker-popup').contains('19').click();

        cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > button.btn.btn-default.dropdown-toggle.ng-scope', { timeout: 15000 })
            .click({ force: true });

        cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > ul > li:nth-child(6) > a')
            .click();

        cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > div:nth-child(4) > button:nth-child(4)', { timeout: 15000 })
            .should('be.visible')
            .click();

        cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-footer > div > button.btn.btn-sm.btn-success')
            .click();
    });
});
