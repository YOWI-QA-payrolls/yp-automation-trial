// cypress/e2e/reports/accountantrep.cy.js

describe('Reports - Accountant Reports', () => {
    beforeEach(() => {
        cy.viewport(1280, 900);
        cy.login();
    });

    it('should view accountant report', () => {
        cy.navigateMenu(['#reports_list > [href="#"]', '#accountant_reports > a']);
        cy.wait(3000);
        cy.get('body').then($body => {
            if ($body.find('.select2-chosen').length > 0) {
                cy.select2First('.select2-chosen');
            } else if ($body.find('.select2-choice').length > 0) {
                cy.select2First('.select2-choice');
            }
            if ($body.find('.col-sm-1 > .btn').length > 0) {
                cy.get('.col-sm-1 > .btn').first().click();
            }
        });
    });
});
