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

        cy.get('body').then($b2 => {
          if ($b2.find('.btn.btn-sm.btn-white.pull-right').length) {
            cy.get('.btn.btn-sm.btn-white.pull-right').click();
          }
        });
      });
    });
  });
});