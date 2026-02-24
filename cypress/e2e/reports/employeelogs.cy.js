describe('Reports - Employee Logs Monitoring', () => {
  beforeEach(() => {
    cy.viewport(1280, 900);
    cy.login();
  });

  it('should filter employee logs by date', () => {
    cy.navigateMenu(['#reports_list > [href="#"]', '#employee_logs_monitoring > a']);

    cy.get('.input-group input:visible', { timeout: 15000 })
      .should('have.length.at.least', 2)
      .then(($inputs) => {
        const $from = $inputs.eq(0);
        const $to = $inputs.eq(1);

        const fromType = ($from.attr('type') || '').toLowerCase();
        const toType = ($to.attr('type') || '').toLowerCase();

        const fromVal =
          fromType === 'datetime-local' ? '2026-02-01T00:00' :
          fromType === 'date' ? '2026-02-01' :
          '02/01/2026';

        const toVal =
          toType === 'datetime-local' ? '2026-02-23T23:59' :
          toType === 'date' ? '2026-02-23' :
          '02/23/2026';

        // FROM
        cy.wrap($from)
          .click({ force: true })            // focus
          .invoke('val', fromVal)
          .trigger('input')
          .trigger('change');

        // TO
        cy.wrap($to)
          .click({ force: true })            // focus
          .invoke('val', toVal)
          .trigger('input')
          .trigger('change');
      });

    // click somewhere else instead of blur (safe)
    cy.get('body').click(0, 0);

    cy.get(':nth-child(8) > .btn').click();

    cy.contains('Incorrect date from inputted.').should('not.exist');
  });
});
