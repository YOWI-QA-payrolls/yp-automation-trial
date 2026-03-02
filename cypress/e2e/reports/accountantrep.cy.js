// cypress/e2e/reports/accountantrep.cy.js

describe('Reports - Accountant Reports', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should view accountant report', () => {
        cy.navigateMenu(['#reports_list > [href="#"]', '#accountant_reports > a']);
        cy.wait(1000);
        cy.select2First('.select2-chosen.ng-binding');
        cy.get('.col-sm-1 > .btn').click();
    });
});
