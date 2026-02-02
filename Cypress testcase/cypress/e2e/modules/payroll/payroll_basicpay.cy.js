/// <reference types="cypress" />

describe("Basic pay testcases", () => {
  beforeEach(() => {
    cy.viewport(1400, 900);
    cy.login2("admin_demo@gmail.com", "YP$taging30k")
    // cy.visit("https://staging-yp.yahshuasupport.com/signin/");
    // cy.get('#root > div.bg-loginscreen > div.middle-box.text-center.loginscreen.wow.fadeIn.animated > div > div.logo.mb-3 > img').should("be.visible");
    // cy.get('input[placeholder="Email"]').type("admin_demo@gmail.com");
    // cy.get('input[placeholder="Password"]').type("YP$taging30k");
    // cy.contains("button", "Sign In").click();
    // cy.contains("div", "Signing in...").should("be.visible");
  });

  it.skip("BASIC PAY = PERFECT ATTENDANCE - 1", () => {
  /*
    Default Monthly Salary Computation is - unchecked.
    Complete Attendance (Receive full basic pay every payroll) is - checked

    Expected result: Basic pay should be half of basic salary
  */
    cy.get('#settings_list').click();
    cy.wait(1000)
    cy.get('#company_list').click();
    cy.wait(1000)
    cy.get('#companies_general_settings').click();
    cy.contains("h2", "Company | General Settings").should('be.visible');
    cy.get('#tableee > tbody > tr:nth-child(2) > td > h3:nth-child(1) > a').click(); // To click the payroll settings

    cy.wait(5000)
    cy.get('#is_default_monthly_computation').uncheck()
    cy.get('#is_default_monthly_computation').should('not.be.checked')
    // cy.get('#include_restday_computing_prorated').check()
    // cy.get('#show_actual_hours_in_display').check()
    cy.get('#complete_basic_pay').check()
    cy.get('#complete_basic_pay').should('be.checked')
    cy.wait(3000)
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div.col-sm-2.pull-right > div > button').click()

    //Create complete logs for employee in daily logs.

    cy.get('#timesheets').click()
    cy.get('#daily_logs').click()
    cy.wait(5000)
    cy.get('#page-wrapper > div.row.wrapper.border-bottom.white-bg.page-heading > div.col-sm-4 > div > div > div > div > button')
      .click() // To click dropdown beside create button.
    cy.get('#page-wrapper > div.row.wrapper.border-bottom.white-bg.page-heading > div.col-sm-4 > div > div > div > div > ul > li > a')
      .click() // To click create complete timesheets.
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-heading > h3').should('be.visible')

    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > form > div.row.ng-scope > div:nth-child(1) > p.input-group > span > button > i')
      .click() // To click calendar button.
    cy.wait(2000)
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > form > div.row.ng-scope > div:nth-child(1) > p.input-group > div > ul > li:nth-child(1) > div > div > div > table > thead > tr:nth-child(1) > th:nth-child(2)')
      .click() // To click date picker.
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > form > div.row.ng-scope > div:nth-child(1) > p.input-group > div > ul > li:nth-child(1) > div > div > div > table > thead > tr > th:nth-child(2)')
      .click() // Click year picker
    cy.contains("span", '2023').click()
    cy.contains("span", 'January').click()
    cy.wait(2000)
    cy.contains("span", '15').click()

    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > form > div.row.ng-scope > div:nth-child(2) > p.input-group > span > button')
      .click() // To click end date calendar.
    cy.wait(2000)
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > form > div.row.ng-scope > div:nth-child(2) > p.input-group > div > ul > li:nth-child(1) > div > div > div > table > thead > tr:nth-child(1) > th:nth-child(2)')
      .click() // To click date picker.
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > form > div.row.ng-scope > div:nth-child(2) > p.input-group > div > ul > li:nth-child(1) > div > div > div > table > thead > tr:nth-child(1) > th:nth-child(2)')
      .click() // Click year picker
    cy.contains("span", '2023').click()
    cy.contains("span", 'January').click()
    cy.wait(2000)
    cy.contains("span", '31').click()
    // To enter reason
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > form > div:nth-child(3) > textarea')
      .type("Created by YAHSHUA QA automation");
    // To select employee.
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > form > div:nth-child(7) > div > ul > li > input')
      .click()
      .type('test')
      .type('{enter}')
    cy.get('#label2').click() // To select Create complete timesheets radio button.
    cy.wait(1000)
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-footer > div > button.btn.btn-sm.btn-success')
      .click() // To click save button.
    cy.wait(5000)

    // Create payroll.

    cy.get('#payroll_default').click()
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.btn-group.pull-right > button').click() // To click create button.
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > div.form-group > div > a > span.select2-chosen.ng-binding')
      .click() // Click payroll schedule dropdown.
    cy.contains('div', 'Quincenal').click()
    cy.get('#first').click() // Select first quincenal
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > span > div:nth-child(10) > p.input-group > span > button')
      .click()
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > span > div:nth-child(10) > p.input-group > div > ul > li:nth-child(1) > div > div > div > table > thead > tr:nth-child(1) > th:nth-child(2)')
      .click() // Click date picker
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > span > div:nth-child(10) > p.input-group > div > ul > li:nth-child(1) > div > div > div > table > thead > tr > th:nth-child(2)')
      .click() // Click year picker.
    cy.contains("span", '2023').click()
    cy.contains("span", 'January').click()
    cy.wait(2000)
    cy.contains("span", '15').click()

    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > span > div:nth-child(14) > p.input-group > span > button')
      .click() // Click paymentdate calendar.
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > span > div:nth-child(14) > p.input-group > div > ul > li:nth-child(1) > div > div > div > table > thead > tr:nth-child(1) > th:nth-child(2)')
      .click() //Click date picker.
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > span > div:nth-child(14) > p.input-group > div > ul > li:nth-child(1) > div > div > div > table > thead > tr > th:nth-child(2)')
      .click() //Click year picker.
    cy.contains("span", '2023').click()
    cy.contains("button", 'January').click()
    cy.wait(2000)
    cy.contains("span", '29').click()
    cy.wait(3000)

    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > span > div:nth-child(32)')
      .type("Create by YAHSHUA QA automation") // Write remarks for payroll.

    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-footer > div > button.btn.btn-sm.btn-success')
      .click() // Save the current payroll created.
    cy.wait(2000)
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(3) > div > div > a > abbr')
      .click() // Clear month filter
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(4) > div > span > input')
      .type('Create by YAHSHUA QA automation')
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(4) > div > span > span > button')
      .click() // Click search button
    cy.wait(1000)

    //Generate payroll for employee.

    cy.get('#table > tbody > tr > td:nth-child(3) > span > span').click() // Open created payroll
    cy.wait(1000)
    cy.get('#page-wrapper > div.row.wrapper.border-bottom.white-bg.page-heading > div.col-sm-4 > div > div > button').click() // Click Batch generate
    cy.get('#dialog_select_all').click() // Deselect all
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > div.input-group.m-b > input')
      .type('test')
    cy.get('#is_selected_0').click()
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-footer > div > button.btn.btn-sm.btn-success')
      .click() // Generate payroll of employee

    // Check if the employee basic pay is correct. Basic pay should be half of the basic salary.

    cy.get('#table-payroll-generation > tbody > tr.ng-scope > td.ng-scope > span').invoke('text').as('basicSalary');
    cy.get('#table-payroll-generation > tbody > tr.ng-scope > td:nth-child(14) > b').invoke('text').as('basicPay');
    cy.get('@basicSalary').then((val1) => { 
      const parsedVal1 = parseFloat(val1.replaceAll(',',''));
      // cy.log(parsedVal1)
      cy.get('@basicPay').then((val2) => {
        const parsedVal2 = parseFloat(val2.replaceAll(',',''));
        // cy.log(parsedVal2)

        const isHalf = parsedVal2 === parsedVal1 / 2;

        if (isHalf) {
          cy.log("PASSED");
        }
      })
    })

    // Reset created payroll

    cy.get('#payroll_default').click()
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(3) > div > div > a > abbr')
      .click() // Clear month filter
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(4) > div > span > input')
      .type('Create by YAHSHUA QA automation')
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(4) > div > span > span > button')
      .click() // Click search button
    cy.wait(1000)
    cy.get('#table > tbody > tr > td:nth-child(3) > span > span').trigger('contextmenu', { button: 2 }); // Right click created payroll
    cy.wait(1000)
    cy.get('#page-top > div.angular-bootstrap-contextmenu.dropdown.clearfix > ul > li:nth-child(4) > a').click() // Delete created payroll
    cy.get('#page-top > div.sweet-alert.show-input.showSweetAlert.visible > fieldset > input[type=text]').type('QA testings');
    cy.get('#page-top > div.sweet-alert.show-input.showSweetAlert.visible > div.sa-button-container > button.confirm').click();// Confirm delete button
    cy.get('#page-top > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > button.confirm').click(); // confirm
    cy.wait(3000)

    // Reset employee daily logs.

    cy.get('#timesheets').click()
    cy.get('#daily_logs').click()
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(2) > tabletoolsdaterange2 > p > span:nth-child(1) > button')
      .click()
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(2) > tabletoolsdaterange2 > p > div.ng-pristine.ng-untouched.ng-valid.ng-scope.ng-not-empty.ng-valid-date-disabled > ul > li:nth-child(1) > div > div > div > table > thead > tr:nth-child(1) > th:nth-child(2)').click()
    cy.contains('span' , 'January').click()
    cy.contains('span' , '15').click()
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(2) > tabletoolsdaterange2 > p > span:nth-child(5) > button').click()
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(2) > tabletoolsdaterange2 > p > div:nth-child(7) > ul > li:nth-child(1) > div > div > div > table > thead > tr:nth-child(1) > th:nth-child(2)').click()
    cy.contains('span' , 'January').click()
    cy.contains('span' , '31').click()
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.col-sm-12.col-md-6.col-lg-3 > div.ui-select-container.ui-select-multiple.select2.select2-container.select2-container-multi.ng-valid.ng-not-empty > ul > li > input')
      .type('test')
      .type('{enter}')
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.col-xs-1 > div > button').click()
    cy.wait(4000)
    cy.get('#c_select_all').click({ force: true }).should('be.checked');
    cy.wait(2000)
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > button.btn.btn-default.dropdown-toggle.ng-scope')
      .click()
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > ul > li:nth-child(8)')
      .click()
    cy.get('#page-top > div.sweet-alert.show-input.showSweetAlert.visible > div.sa-button-container > button.confirm').click()
  })

  it.skip("BASIC PAY = PERFECT ATTENDANCE - 2", () => {
    /*
      Default Monthly Salary Computation is - checked.
      Complete Attendance (Receive full basic pay every payroll) is - unchecked
  
      Expected result: Basic pay should be half of basic salary
    */
    cy.get('#settings_list').click();
    cy.wait(1000)
    cy.get('#company_list').click();
    cy.wait(1000)
    cy.get('#companies_general_settings').click();
    cy.contains("h2", "Company | General Settings").should('be.visible');
    cy.get('#tableee > tbody > tr:nth-child(2) > td > h3:nth-child(1) > a').click(); // To click the payroll settings

    cy.wait(5000)
    cy.get('#is_default_monthly_computation').check()
    cy.get('#is_default_monthly_computation').should('be.checked')
    // cy.get('#include_restday_computing_prorated').check()
    // cy.get('#show_actual_hours_in_display').check()
    cy.get('#complete_basic_pay').uncheck()
    cy.get('#complete_basic_pay').should('not.be.checked')
    cy.wait(3000)
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div.col-sm-2.pull-right > div > button').click()

    //Create complete logs for employee in daily logs.

    cy.get('#timesheets').click()
    cy.get('#daily_logs').click()
    cy.wait(5000)
    cy.get('#page-wrapper > div.row.wrapper.border-bottom.white-bg.page-heading > div.col-sm-4 > div > div > div > div > button')
      .click() // To click dropdown beside create button.
    cy.get('#page-wrapper > div.row.wrapper.border-bottom.white-bg.page-heading > div.col-sm-4 > div > div > div > div > ul > li > a')
      .click() // To click create complete timesheets.
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-heading > h3').should('be.visible')

    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > form > div.row.ng-scope > div:nth-child(1) > p.input-group > span > button > i')
      .click() // To click calendar button.
    cy.wait(2000)
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > form > div.row.ng-scope > div:nth-child(1) > p.input-group > div > ul > li:nth-child(1) > div > div > div > table > thead > tr:nth-child(1) > th:nth-child(2)')
      .click() // To click date picker.
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > form > div.row.ng-scope > div:nth-child(1) > p.input-group > div > ul > li:nth-child(1) > div > div > div > table > thead > tr > th:nth-child(2)')
      .click() // Click year picker
    cy.contains("span", '2023').click()
    cy.contains("span", 'January').click()
    cy.wait(2000)
    cy.contains("span", '15').click()

    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > form > div.row.ng-scope > div:nth-child(2) > p.input-group > span > button')
      .click() // To click end date calendar.
    cy.wait(2000)
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > form > div.row.ng-scope > div:nth-child(2) > p.input-group > div > ul > li:nth-child(1) > div > div > div > table > thead > tr:nth-child(1) > th:nth-child(2)')
      .click() // To click date picker.
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > form > div.row.ng-scope > div:nth-child(2) > p.input-group > div > ul > li:nth-child(1) > div > div > div > table > thead > tr:nth-child(1) > th:nth-child(2)')
      .click() // Click year picker
    cy.contains("span", '2023').click()
    cy.contains("span", 'January').click()
    cy.wait(2000)
    cy.contains("span", '31').click()
    // To enter reason
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > form > div:nth-child(3) > textarea')
      .type("Created by YAHSHUA QA automation");
    // To select employee.
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > form > div:nth-child(7) > div > ul > li > input')
      .click()
      .type('test')
      .type('{enter}')
    cy.get('#label2').click() // To select Create complete timesheets radio button.
    cy.wait(1000)
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-footer > div > button.btn.btn-sm.btn-success')
      .click() // To click save button.
    cy.wait(2000)

    // Create payroll.

    cy.get('#payroll_default').click()
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.btn-group.pull-right > button').click() // To click create button.
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > div.form-group > div > a > span.select2-chosen.ng-binding')
      .click() // Click payroll schedule dropdown.
    cy.contains('div', 'Quincenal').click()
    cy.get('#first').click() // Select first quincenal
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > span > div:nth-child(10) > p.input-group > span > button')
      .click()
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > span > div:nth-child(10) > p.input-group > div > ul > li:nth-child(1) > div > div > div > table > thead > tr:nth-child(1) > th:nth-child(2)')
      .click() // Click date picker
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > span > div:nth-child(10) > p.input-group > div > ul > li:nth-child(1) > div > div > div > table > thead > tr > th:nth-child(2)')
      .click() // Click year picker.
    cy.contains("span", '2023').click()
    cy.contains("span", 'January').click()
    cy.wait(2000)
    cy.contains("span", '15').click()

    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > span > div:nth-child(14) > p.input-group > span > button')
      .click() // Click paymentdate calendar.
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > span > div:nth-child(14) > p.input-group > div > ul > li:nth-child(1) > div > div > div > table > thead > tr:nth-child(1) > th:nth-child(2)')
      .click() //Click date picker.
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > span > div:nth-child(14) > p.input-group > div > ul > li:nth-child(1) > div > div > div > table > thead > tr > th:nth-child(2)')
      .click() //Click year picker.
    cy.contains("span", '2023').click()
    cy.contains("button", 'January').click()
    cy.wait(2000)
    cy.contains("span", '29').click()
    cy.wait(3000)

    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > span > div:nth-child(32)')
      .type("Create by YAHSHUA QA automation") // Write remarks for payroll.

    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-footer > div > button.btn.btn-sm.btn-success')
      .click() // Save the current payroll created.
    cy.wait(2000)
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(3) > div > div > a > abbr')
      .click() // Clear month filter
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(4) > div > span > input')
      .type('Create by YAHSHUA QA automation')
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(4) > div > span > span > button')
      .click() // Click search button
    cy.wait(1000)

    //Generate payroll for employee.

    cy.get('#table > tbody > tr > td:nth-child(3) > span > span').click() // Open created payroll
    cy.wait(1000)
    cy.get('#page-wrapper > div.row.wrapper.border-bottom.white-bg.page-heading > div.col-sm-4 > div > div > button').click() // Click Batch generate
    cy.get('#dialog_select_all').click() // Deselect all
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > div.input-group.m-b > input')
      .type('test')
    cy.get('#is_selected_0').click()
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-footer > div > button.btn.btn-sm.btn-success')
      .click() // Generate payroll of employee

    // Check if the employee basic pay is correct. Basic pay should be half of the basic salary.

    cy.get('#table-payroll-generation > tbody > tr.ng-scope > td.ng-scope > span').invoke('text').as('basicSalary');
    cy.get('#table-payroll-generation > tbody > tr.ng-scope > td:nth-child(14) > b').invoke('text').as('basicPay');
    cy.get('@basicSalary').then((val1) => { 
      const parsedVal1 = parseFloat(val1.replaceAll(',',''));
      // cy.log(parsedVal1)
      cy.get('@basicPay').then((val2) => {
        const parsedVal2 = parseFloat(val2.replaceAll(',',''));
        // cy.log(parsedVal2)

        const isHalf = parsedVal2 === parsedVal1 / 2;

        if (isHalf) {
          cy.log("PASSED");
        }
      })
    })

    // Reset created payroll

    cy.get('#payroll_default').click()
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(3) > div > div > a > abbr')
      .click() // Clear month filter
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(4) > div > span > input')
      .type('Create by YAHSHUA QA automation')
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(4) > div > span > span > button')
      .click() // Click search button
    cy.wait(1000)
    cy.get('#table > tbody > tr > td:nth-child(3) > span > span').trigger('contextmenu', { button: 2 }); // Right click created payroll
    cy.wait(1000)
    cy.get('#page-top > div.angular-bootstrap-contextmenu.dropdown.clearfix > ul > li:nth-child(4) > a').click() // Delete created payroll
    cy.get('#page-top > div.sweet-alert.show-input.showSweetAlert.visible > fieldset > input[type=text]').type('QA testings');
    cy.get('#page-top > div.sweet-alert.show-input.showSweetAlert.visible > div.sa-button-container > button.confirm').click();// Confirm delete button
    cy.wait(1000)
    cy.get('#page-top > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > button.confirm').click(); // confirm
    cy.wait(3000)

    // Reset employee daily logs.

    cy.get('#timesheets').click()
    cy.get('#daily_logs').click()
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(2) > tabletoolsdaterange2 > p > span:nth-child(1) > button')
      .click()
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(2) > tabletoolsdaterange2 > p > div.ng-pristine.ng-untouched.ng-valid.ng-scope.ng-not-empty.ng-valid-date-disabled > ul > li:nth-child(1) > div > div > div > table > thead > tr:nth-child(1) > th:nth-child(2)').click()
    cy.contains('span' , 'January').click()
    cy.contains('span' , '15').click()
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(2) > tabletoolsdaterange2 > p > span:nth-child(5) > button').click()
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(2) > tabletoolsdaterange2 > p > div:nth-child(7) > ul > li:nth-child(1) > div > div > div > table > thead > tr:nth-child(1) > th:nth-child(2)').click()
    cy.contains('span' , 'January').click()
    cy.contains('span' , '31').click()
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.col-sm-12.col-md-6.col-lg-3 > div.ui-select-container.ui-select-multiple.select2.select2-container.select2-container-multi.ng-valid.ng-not-empty > ul > li > input')
      .type('test')
      .type('{enter}')
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.col-xs-1 > div > button').click()
    cy.wait(4000)
    cy.get('#c_select_all').click({ force: true }).should('be.checked');
    cy.wait(2000)
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > button.btn.btn-default.dropdown-toggle.ng-scope')
      .click()
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > ul > li:nth-child(8)')
      .click()
    cy.get('#page-top > div.sweet-alert.show-input.showSweetAlert.visible > div.sa-button-container > button.confirm').click()
  })

it.skip("BASIC PAY = PERFECT ATTENDANCE - 3", () => {
  /*
    Default Monthly Salary Computation is - unchecked.
    Complete Attendance (Receive full basic pay every payroll) is - unchecked

    Expected result: Basic pay should be half of basic salary
  */
    cy.get('#settings_list').click();
    cy.wait(1000)
    cy.get('#company_list').click();
    cy.wait(1000)
    cy.get('#companies_general_settings').click();
    cy.contains("h2", "Company | General Settings").should('be.visible');
    cy.get('#tableee > tbody > tr:nth-child(2) > td > h3:nth-child(1) > a').click(); // To click the payroll settings

    cy.wait(5000)
    cy.get('#is_default_monthly_computation').uncheck()
    cy.get('#is_default_monthly_computation').should('not.be.checked')
    // cy.get('#include_restday_computing_prorated').check()
    // cy.get('#show_actual_hours_in_display').check()
    cy.get('#complete_basic_pay').uncheck()
    cy.get('#complete_basic_pay').should('not.be.checked')
    cy.wait(3000)
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div.col-sm-2.pull-right > div > button').click()

    //Create complete logs for employee in daily logs.

    cy.get('#timesheets').click()
    cy.get('#daily_logs').click()
    cy.wait(5000)
    cy.get('#page-wrapper > div.row.wrapper.border-bottom.white-bg.page-heading > div.col-sm-4 > div > div > div > div > button')
      .click() // To click dropdown beside create button.
    cy.get('#page-wrapper > div.row.wrapper.border-bottom.white-bg.page-heading > div.col-sm-4 > div > div > div > div > ul > li > a')
      .click() // To click create complete timesheets.
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-heading > h3').should('be.visible')

    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > form > div.row.ng-scope > div:nth-child(1) > p.input-group > span > button > i')
      .click() // To click calendar button.
    cy.wait(2000)
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > form > div.row.ng-scope > div:nth-child(1) > p.input-group > div > ul > li:nth-child(1) > div > div > div > table > thead > tr:nth-child(1) > th:nth-child(2)')
      .click() // To click date picker.
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > form > div.row.ng-scope > div:nth-child(1) > p.input-group > div > ul > li:nth-child(1) > div > div > div > table > thead > tr > th:nth-child(2)')
      .click() // Click year picker
    cy.contains("span", '2023').click()
    cy.contains("span", 'January').click()
    cy.wait(2000)
    cy.contains("span", '15').click()

    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > form > div.row.ng-scope > div:nth-child(2) > p.input-group > span > button')
      .click() // To click end date calendar.
    cy.wait(2000)
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > form > div.row.ng-scope > div:nth-child(2) > p.input-group > div > ul > li:nth-child(1) > div > div > div > table > thead > tr:nth-child(1) > th:nth-child(2)')
      .click() // To click date picker.
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > form > div.row.ng-scope > div:nth-child(2) > p.input-group > div > ul > li:nth-child(1) > div > div > div > table > thead > tr:nth-child(1) > th:nth-child(2)')
      .click() // Click year picker
    cy.contains("span", '2023').click()
    cy.contains("span", 'January').click()
    cy.wait(2000)
    cy.contains("span", '31').click()
    // To enter reason
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > form > div:nth-child(3) > textarea')
      .type("Created by YAHSHUA QA automation");
    // To select employee.
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > form > div:nth-child(7) > div > ul > li > input')
      .click()
      .type('test')
      .type('{enter}')
    cy.get('#label2').click() // To select Create complete timesheets radio button.
    cy.wait(1000)
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-footer > div > button.btn.btn-sm.btn-success')
      .click() // To click save button.
    cy.wait(2000)

    // Create payroll.

    cy.get('#payroll_default').click()
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.btn-group.pull-right > button').click() // To click create button.
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > div.form-group > div > a > span.select2-chosen.ng-binding')
      .click() // Click payroll schedule dropdown.
    cy.contains('div', 'Quincenal').click()
    cy.get('#first').click() // Select first quincenal
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > span > div:nth-child(10) > p.input-group > span > button')
      .click()
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > span > div:nth-child(10) > p.input-group > div > ul > li:nth-child(1) > div > div > div > table > thead > tr:nth-child(1) > th:nth-child(2)')
      .click() // Click date picker
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > span > div:nth-child(10) > p.input-group > div > ul > li:nth-child(1) > div > div > div > table > thead > tr > th:nth-child(2)')
      .click() // Click year picker.
    cy.contains("span", '2023').click()
    cy.contains("span", 'January').click()
    cy.wait(2000)
    cy.contains("span", '15').click()

    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > span > div:nth-child(14) > p.input-group > span > button')
      .click() // Click paymentdate calendar.
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > span > div:nth-child(14) > p.input-group > div > ul > li:nth-child(1) > div > div > div > table > thead > tr:nth-child(1) > th:nth-child(2)')
      .click() //Click date picker.
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > span > div:nth-child(14) > p.input-group > div > ul > li:nth-child(1) > div > div > div > table > thead > tr > th:nth-child(2)')
      .click() //Click year picker.
    cy.contains("span", '2023').click()
    cy.contains("button", 'January').click()
    cy.wait(2000)
    cy.contains("span", '29').click()
    cy.wait(3000)

    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > span > div:nth-child(32)')
      .type("Create by YAHSHUA QA automation") // Write remarks for payroll.

    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-footer > div > button.btn.btn-sm.btn-success')
      .click() // Save the current payroll created.
    cy.wait(2000)
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(3) > div > div > a > abbr')
      .click() // Clear month filter
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(4) > div > span > input')
      .type('Create by YAHSHUA QA automation')
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(4) > div > span > span > button')
      .click() // Click search button
    cy.wait(1000)

    //Generate payroll for employee.

    cy.get('#table > tbody > tr > td:nth-child(3) > span > span').click() // Open created payroll
    cy.wait(1000)
    cy.get('#page-wrapper > div.row.wrapper.border-bottom.white-bg.page-heading > div.col-sm-4 > div > div > button').click() // Click Batch generate
    cy.get('#dialog_select_all').click() // Deselect all
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > div.input-group.m-b > input')
      .type('test')
    cy.get('#is_selected_0').click()
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-footer > div > button.btn.btn-sm.btn-success')
      .click() // Generate payroll of employee

    // Check if the employee basic pay is correct. Basic pay should be half of the basic salary.

    cy.get('#table-payroll-generation > tbody > tr.ng-scope > td.ng-scope > span').invoke('text').as('basicSalary');
    cy.get('#table-payroll-generation > tbody > tr.ng-scope > td:nth-child(14) > b').invoke('text').as('basicPay');
    cy.get('@basicSalary').then((val1) => { 
      const parsedVal1 = parseFloat(val1.replaceAll(',',''));
      // cy.log(parsedVal1)
      cy.get('@basicPay').then((val2) => {
        const parsedVal2 = parseFloat(val2.replaceAll(',',''));
        // cy.log(parsedVal2)

        const isHalf = parsedVal2 === parsedVal1 / 2;

        if (isHalf) {
          cy.log("PASSED");
        }
      })
    })

    // Reset created payroll

    cy.get('#payroll_default').click()
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(3) > div > div > a > abbr')
      .click() // Clear month filter
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(4) > div > span > input')
      .type('Create by YAHSHUA QA automation')
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(4) > div > span > span > button')
      .click() // Click search button
    cy.wait(1000)
    cy.get('#table > tbody > tr > td:nth-child(3) > span > span').trigger('contextmenu', { button: 2 }); // Right click created payroll
    cy.wait(1000)
    cy.get('#page-top > div.angular-bootstrap-contextmenu.dropdown.clearfix > ul > li:nth-child(4) > a').click() // Delete created payroll
    cy.get('#page-top > div.sweet-alert.show-input.showSweetAlert.visible > fieldset > input[type=text]').type('QA testings');
    cy.get('#page-top > div.sweet-alert.show-input.showSweetAlert.visible > div.sa-button-container > button.confirm').click();// Confirm delete button
    cy.get('#page-top > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > button.confirm').click(); // confirm
    cy.wait(2000)

    // Reset employee daily logs.

    cy.get('#timesheets').click()
    cy.get('#daily_logs').click()
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(2) > tabletoolsdaterange2 > p > span:nth-child(1) > button')
      .click()
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(2) > tabletoolsdaterange2 > p > div.ng-pristine.ng-untouched.ng-valid.ng-scope.ng-not-empty.ng-valid-date-disabled > ul > li:nth-child(1) > div > div > div > table > thead > tr:nth-child(1) > th:nth-child(2)').click()
    cy.contains('span' , 'January').click()
    cy.contains('span' , '15').click()
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(2) > tabletoolsdaterange2 > p > span:nth-child(5) > button').click()
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(2) > tabletoolsdaterange2 > p > div:nth-child(7) > ul > li:nth-child(1) > div > div > div > table > thead > tr:nth-child(1) > th:nth-child(2)').click()
    cy.contains('span' , 'January').click()
    cy.contains('span' , '31').click()
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.col-sm-12.col-md-6.col-lg-3 > div.ui-select-container.ui-select-multiple.select2.select2-container.select2-container-multi.ng-valid.ng-not-empty > ul > li > input')
      .type('test')
      .type('{enter}')
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.col-xs-1 > div > button').click()
    cy.wait(4000)
    cy.get('#c_select_all').click({ force: true }).should('be.checked');
    cy.wait(2000)
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > button.btn.btn-default.dropdown-toggle.ng-scope')
      .click()
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > ul > li:nth-child(8)')
      .click()
    cy.get('#page-top > div.sweet-alert.show-input.showSweetAlert.visible > div.sa-button-container > button.confirm').click()
  })

  it("BASIC PAY = ST WITH LATE - 1", () => {
    /*
      Default Monthly Salary Computation is - checked.
      Complete Attendance (Receive full basic pay every payroll) is - unchecked
      Transfer late after gross pay - checked.
      Late Exemption - checked.
  
      Expected result: Basic pay should be total ST minus late.
    */

    cy.get('#settings_list').click();
    cy.wait(1000)
    cy.get('#company_list').click();
    cy.wait(1000)
    cy.get('#companies_general_settings').click();
    cy.contains("h2", "Company | General Settings").should('be.visible');
    cy.get('#tableee > tbody > tr:nth-child(2) > td > h3:nth-child(1) > a').click(); // To click the payroll settings

    cy.wait(5000)
    cy.get('#is_default_monthly_computation').check()
    cy.get('#is_default_monthly_computation').should('be.checked')
    // cy.get('#include_restday_computing_prorated').check()
    // cy.get('#show_actual_hours_in_display').check()
    cy.get('#complete_basic_pay').uncheck()
    cy.get('#complete_basic_pay').should('not.be.checked')
    cy.get('#transfer_late_after_gross_pay').check()
    cy.get('#transfer_late_after_gross_pay').should('be.checked')
    cy.get('#late_exemption').check()
    cy.get('#late_exemption').should('be.checked')

    cy.wait(3000)
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div.col-sm-2.pull-right > div > button').click()

    //Create logs with late for employee in daily logs.

    cy.get('#timesheets').click()
    cy.get('#daily_logs').click()
    cy.wait(5000)
    cy.get('#page-wrapper > div.row.wrapper.border-bottom.white-bg.page-heading > div.col-sm-4 > div > div > div > div > button')
      .click() // To click dropdown beside create button.
    cy.get('#page-wrapper > div.row.wrapper.border-bottom.white-bg.page-heading > div.col-sm-4 > div > div > div > div > ul > li > a')
      .click() // To click create complete timesheets.
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-heading > h3').should('be.visible')

    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > form > div.row.ng-scope > div:nth-child(1) > p.input-group > span > button > i')
      .click() // To click calendar button.
    cy.wait(2000)
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > form > div.row.ng-scope > div:nth-child(1) > p.input-group > div > ul > li:nth-child(1) > div > div > div > table > thead > tr:nth-child(1) > th:nth-child(2)')
      .click() // To click date picker.
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > form > div.row.ng-scope > div:nth-child(1) > p.input-group > div > ul > li:nth-child(1) > div > div > div > table > thead > tr > th:nth-child(2)')
      .click() // Click year picker
    cy.contains("span", '2023').click()
    cy.contains("span", 'January').click()
    cy.wait(2000)
    cy.contains("span", '15').click()

    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > form > div.row.ng-scope > div:nth-child(2) > p.input-group > span > button')
      .click() // To click end date calendar.
    cy.wait(2000)
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > form > div.row.ng-scope > div:nth-child(2) > p.input-group > div > ul > li:nth-child(1) > div > div > div > table > thead > tr:nth-child(1) > th:nth-child(2)')
      .click() // To click date picker.
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > form > div.row.ng-scope > div:nth-child(2) > p.input-group > div > ul > li:nth-child(1) > div > div > div > table > thead > tr:nth-child(1) > th:nth-child(2)')
      .click() // Click year picker
    cy.contains("span", '2023').click()
    cy.contains("span", 'January').click()
    cy.wait(2000)
    cy.contains("span", '31').click()
    // To enter reason
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > form > div:nth-child(3) > textarea')
      .type("Created by YAHSHUA QA automation");
    // To select employee.
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > form > div:nth-child(7) > div > ul > li > input')
      .click()
      .type('test')
      .type('{enter}')
    cy.get('#label2').click() // To select Create complete timesheets radio button.
    cy.wait(1000)
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-footer > div > button.btn.btn-sm.btn-success')
      .click() // To click save button.
    cy.wait(2000)

      // Setup for late

    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(2) > tabletoolsdaterange2 > p > span:nth-child(1) > button')
    .click()
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(2) > tabletoolsdaterange2 > p > div.ng-pristine.ng-untouched.ng-valid.ng-scope.ng-not-empty.ng-valid-date-disabled > ul > li:nth-child(1) > div > div > div > table > thead > tr:nth-child(1) > th:nth-child(2)').click()
    cy.contains('span' , 'January').click()
    cy.contains('span' , '21').click()
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(2) > tabletoolsdaterange2 > p > span:nth-child(5) > button').click()
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(2) > tabletoolsdaterange2 > p > div:nth-child(7) > ul > li:nth-child(1) > div > div > div > table > thead > tr:nth-child(1) > th:nth-child(2)').click()
    cy.contains('span' , 'January').click()
    cy.contains('span' , '21').click()
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.col-sm-12.col-md-6.col-lg-3 > div.ui-select-container.ui-select-multiple.select2.select2-container.select2-container-multi.ng-valid.ng-not-empty > ul > li > input')
      .type('test')
      .type('{enter}')
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.col-xs-1 > div > button').click()
    cy.wait(2000)
    cy.get('#table > tbody > tr > td:nth-child(6) > span > span.ng-scope > button:nth-child(1)').click() // Click pencil button on time in.
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > div:nth-child(3) > div > div > table > tbody > tr:nth-child(2) > td.form-group.uib-time.hours > input')
      .clear()
      .type('09')
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-footer > div > button.btn.btn-sm.btn-success')
      .click()
    cy.wait(10000)


    //   // Create payroll.

    cy.get('#payroll_default').click()
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.btn-group.pull-right > button').click() // To click create button.
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > div.form-group > div > a > span.select2-chosen.ng-binding')
      .click() // Click payroll schedule dropdown.
    cy.contains('div', 'Quincenal').click()
    cy.get('#first').click() // Select first quincenal
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > span > div:nth-child(10) > p.input-group > span > button')
      .click()
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > span > div:nth-child(10) > p.input-group > div > ul > li:nth-child(1) > div > div > div > table > thead > tr:nth-child(1) > th:nth-child(2)')
      .click() // Click date picker
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > span > div:nth-child(10) > p.input-group > div > ul > li:nth-child(1) > div > div > div > table > thead > tr > th:nth-child(2)')
      .click() // Click year picker.
    cy.contains("span", '2023').click()
    cy.contains("span", 'January').click()
    cy.wait(2000)
    cy.contains("span", '15').click()

    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > span > div:nth-child(14) > p.input-group > span > button')
      .click() // Click paymentdate calendar.
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > span > div:nth-child(14) > p.input-group > div > ul > li:nth-child(1) > div > div > div > table > thead > tr:nth-child(1) > th:nth-child(2)')
      .click() //Click date picker.
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > span > div:nth-child(14) > p.input-group > div > ul > li:nth-child(1) > div > div > div > table > thead > tr > th:nth-child(2)')
      .click() //Click year picker.
    cy.contains("span", '2023').click()
    cy.contains("button", 'January').click()
    cy.wait(2000)
    cy.contains("span", '29').click()
    cy.wait(3000)

    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > form > span > div:nth-child(32)')
      .type("Create by YAHSHUA QA automation") // Write remarks for payroll.

    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-footer > div > button.btn.btn-sm.btn-success')
      .click() // Save the current payroll created.
    // cy.wait(2000)

    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(3) > div > div > a > abbr')
      .click() // Clear month filter
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(4) > div > span > input')
      .type('Create by YAHSHUA QA automation')
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(4) > div > span > span > button')
      .click() // Click search button
    cy.wait(1000)

    //Generate payroll for employee.

    cy.get('#table > tbody > tr > td:nth-child(3) > span > span').click() // Open created payroll
    cy.wait(1000)
    cy.get('#page-wrapper > div.row.wrapper.border-bottom.white-bg.page-heading > div.col-sm-4 > div > div > button').click() // Click Batch generate
    cy.get('#dialog_select_all').click() // Deselect all
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-body > div > div.row > div.input-group.m-b > input')
      .type('test')
    cy.get('#is_selected_0').click()
    cy.get('#page-top > div.modal.fade.ng-scope.ng-isolate-scope.in > div > div > div > div.panel-footer > div > button.btn.btn-sm.btn-success')
      .click() // Generate payroll of employee

    // Check if the employee basic pay is correct. Basic pay should be half of the basic salary.

    cy.get('#table-payroll-generation > tbody > tr.ng-scope > td.ng-scope > span').invoke('text').as('basicSalary');
    cy.get('#table-payroll-generation > tbody > tr.ng-scope > td:nth-child(14) > b').invoke('text').as('basicPay');
    cy.get('@basicSalary').then((val1) => { 
      const parsedVal1 = parseFloat(val1.replaceAll(',',''));
      // cy.log(parsedVal1)
      cy.get('@basicPay').then((val2) => {
        const parsedVal2 = parseFloat(val2.replaceAll(',',''));
        // cy.log(parsedVal2)

        const isHalf = parsedVal2 === parsedVal1 / 2;

        if (isHalf) {
          cy.log("PASSED");
        }
      })
    })

    cy.get('#table-payroll-generation > tbody > tr.ng-scope > td:nth-child(10) > span')
      .should('be.visible')

    // Reset created payroll

    cy.get('#payroll_default').click()
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(3) > div > div > a > abbr')
      .click() // Clear month filter
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(4) > div > span > input')
      .type('Create by YAHSHUA QA automation')
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(4) > div > span > span > button')
      .click() // Click search button
    cy.wait(1000)
    cy.get('#table > tbody > tr > td:nth-child(3) > span > span').trigger('contextmenu', { button: 2 }); // Right click created payroll
    cy.wait(1000)
    cy.get('#page-top > div.angular-bootstrap-contextmenu.dropdown.clearfix > ul > li:nth-child(4) > a').click() // Delete created payroll
    cy.get('#page-top > div.sweet-alert.show-input.showSweetAlert.visible > fieldset > input[type=text]').type('QA testings');
    cy.get('#page-top > div.sweet-alert.show-input.showSweetAlert.visible > div.sa-button-container > button.confirm').click();// Confirm delete button
    cy.get('#page-top > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > button.confirm').click(); // confirm
    cy.wait(3000)

    // Reset employee daily logs.

    cy.get('#timesheets').click()
    cy.get('#daily_logs').click()
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(2) > tabletoolsdaterange2 > p > span:nth-child(1) > button')
      .click()
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(2) > tabletoolsdaterange2 > p > div.ng-pristine.ng-untouched.ng-valid.ng-scope.ng-not-empty.ng-valid-date-disabled > ul > li:nth-child(1) > div > div > div > table > thead > tr:nth-child(1) > th:nth-child(2)').click()
    cy.contains('span' , 'January').click()
    cy.contains('span' , '15').click()
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(2) > tabletoolsdaterange2 > p > span:nth-child(5) > button').click()
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(2) > tabletoolsdaterange2 > p > div:nth-child(7) > ul > li:nth-child(1) > div > div > div > table > thead > tr:nth-child(1) > th:nth-child(2)').click()
    cy.contains('span' , 'January').click()
    cy.contains('span' , '31').click()
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.col-sm-12.col-md-6.col-lg-3 > div.ui-select-container.ui-select-multiple.select2.select2-container.select2-container-multi.ng-valid.ng-not-empty > ul > li > input')
      .type('test')
      .type('{enter}')
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.col-xs-1 > div > button').click()
    cy.wait(4000)
    cy.get('#c_select_all').click({ force: true }).should('be.checked');
    cy.wait(2000)
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > button.btn.btn-default.dropdown-toggle.ng-scope')
      .click()
    cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > div > div > ul > li:nth-child(8)')
      .click()
    cy.wait(1000)
    cy.get('#page-top > div.sweet-alert.show-input.showSweetAlert.visible > div.sa-button-container > button.confirm').click()
  })

})
