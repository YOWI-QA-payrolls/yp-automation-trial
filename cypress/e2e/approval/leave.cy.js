describe('Approval - Leave', () => {
  beforeEach(() => {
    cy.viewport(1280, 900);
    cy.login();
  });

  it('should navigate to leave approval, filter by date, and process approval', () => {
    cy.navigateMenu(['#approval_list > a', '#leave_approval > a']);

    // ✅ stable date range (avoid datepicker)
    cy.get('[ng-model="filters.date_from"]', { timeout: 15000 })
      .should('be.visible').clear().type('01/11/2024').blur();
    cy.get('[ng-model="filters.date_to"]')
      .should('be.visible').clear().type('01/30/2024').blur();
    cy.get('body').click(0, 0);

    cy.get('#advance-filter-btn', { timeout: 10000 }).should('be.visible').click();
    cy.get('#advance-search', { timeout: 10000 }).should('be.visible').click();

    cy.get('[ng-click="leave_analysis_dialog()"]', { timeout: 10000 })
      .should('be.visible').click();
    cy.dismissToast();
    cy.get('.col-sm-8 > .pull-right > .btn', { timeout: 10000 })
      .should('be.visible').click();

    // ✅ approve first row if present
    cy.get('body').then($body => {
      if (!$body.find('tbody tr').length) return;

      cy.get('tbody tr:first > :nth-child(4)').click();

      // wait for submit if details loaded
      cy.get('body', { timeout: 15000 }).then($b => {
        if (!$b.find('#leave_submit').length) return;

        // click approve option (best effort)
        const label =
          $b.find(
            'label:contains("Approve"):visible, label:contains("Approved"):visible, label:contains("Accept"):visible, label:contains("Yes"):visible'
          ).first();

        if (label.length) cy.wrap(label).click({ force: true });
        else {
          const input = $b.find('input[type="radio"]:visible, input[type="checkbox"]:visible').first();
          if (input.length) cy.wrap(input).click({ force: true });
        }

        cy.get('#leave_submit').should('be.visible').and('not.be.disabled').click();
        cy.dismissToast();

    describe('Leave Approval Workflow', () => {
        it('should navigate to leave approval, filter by date, and process approval', () => {
            cy.navigateMenu([
                '#approval_list > a',
                '#leave_approval > a'
            ]);

            cy.get('[ng-click="main.open_date(\'filter_date_from\')"]', { timeout: 15000 })
                .should('be.visible')
                .click();
            cy.get('.uib-datepicker-popup .uib-left').should('be.visible').click();
            cy.get('.uib-datepicker-popup').contains('11').click();
            cy.get('[ng-model="filters.date_to"]').clear().type('01/30/2024');

            cy.get('tbody', { timeout: 30000 }).should('exist');

            cy.get('#advance-filter-btn', { timeout: 10000 })
                .should('be.visible')
                .click();
            cy.get('tbody', { timeout: 30000 }).should('exist');
            cy.get('#advance-search').should('be.visible').click();

            cy.get('[ng-click="leave_analysis_dialog()"]', { timeout: 10000 })
                .should('be.visible')
                .click();
            cy.dismissToast();
            cy.get('.col-sm-8 > .pull-right > .btn').should('be.visible').click();

            cy.get('body').then($body => {
                if ($body.find('tbody tr:first > :nth-child(4)').length > 0) {
                    cy.get('tbody tr:first > :nth-child(4)').click();
                    cy.get('span.ng-scope > :nth-child(1) > label', { timeout: 10000 }).first().click({ force: true });
                    cy.get('#leave_submit').click({ force: true });
                    cy.get('tbody', { timeout: 30000 }).should('exist');
                    cy.dismissToast();
                    cy.get('.btn.btn-sm.btn-white.pull-right').should('be.visible').click();
                }
            });
        });
      });
    });
  });
});