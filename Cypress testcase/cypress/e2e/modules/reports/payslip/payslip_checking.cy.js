/// <reference types="cypress" />

describe("DMPI payslip checking", () => {
  beforeEach(() => {
    cy.visit("https://staging-dmpi2.yahshuasupport.com/signin/?login=yes");
    cy.contains("h3", "Welcome to Delmonte Payroll!").should("be.visible");
    cy.get("input#email").type("yahshua.qa@ypo.com");
    cy.get("input#password").type("DMPI$taging30k");
    cy.contains("button", "Log in").click();
    cy.contains("div", "Logging In...").should("be.visible");
    cy.contains("h2", "Dashboard").should("be.visible");
    cy.contains("button", "Close").click({ force: true });
    // cy.contains('button', 'Close').click()
    // cy.get('@btn',{timeout: 5000}).click({multiple: true})
  });

  var payroll_period = "May 10, 2023 - May 26, 2023 (PLTN MNS)";

  it.skip("Test login", () => {
    cy.visit("https://staging-dmpi2.yahshuasupport.com/signin/?login=yes");
    cy.contains("h3", "Welcome to Delmonte Payroll!").should("be.visible");
    cy.get("input#email").type("yahshua.qa@ypo.com");
    cy.get("input#password").type("DMPI$taging30k");
    cy.contains("button", "Log in").click();
    cy.contains("div", "Logging In...").should("be.visible");
    cy.contains("h2", "Dashboard").should("be.visible");
    cy.contains("button", "Close").click({ force: true });
  });

  it("Test Payslip earnings and deductions", () => {
    // Open payroll register module
    cy.get("#reports_list").click();
    cy.get("#payroll_register").should("be.visible");
    cy.get("#payroll_register").click();
    cy.contains("h2", "Payroll Register").should("be.visible");

    //selecting the payroll period
    cy.contains("Select...")
      .should("be.visible")
      .then(() => {
        cy.contains("Select...").click();
      });
    cy.contains(payroll_period).click();
    cy.get(
      "#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.sk-spinner.sk-spinner-cube-grid"
    ).should("be.visible");

    var employee = "";
    var chapa = '20787';
    // Getting chapa number
    // cy.get(
    //   "#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(8) > div > div > table.sticky-col > tbody > tr:nth-child(1) > th:nth-child(1) > span"
    // )
    //   .invoke("text")
    //   .then((text) => {
    //     chapa = text.replace(/\s/g, " ");
    //   });

      var dict = []
    // Getting employee name
    cy.get(
      "#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(8) > div > div > table.sticky-col > tbody > tr:nth-child(1) > th:nth-child(2) > span"
    )
      .invoke("text")
      .then((text) => {
        employee = text.replace(/\s/g, " ");
        console.log(employee);
        console.log(chapa);
        cy.get(
          "#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > input"
        )
          .type(chapa)
          .type("{enter}}");
        cy.get(
          "#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(8) > div > div > table.table-bordered.table-hover.sticky-enabled"
        ).each(($tablediv, tabledivIndex) => {
          cy.get($tablediv)
            .find("thead > tr > th")
            .not(".ng-hide")
            .each(($cell, cellIndex) => {
              const text = $cell.text();
              var data = {}
              data.header = text.trim()

              cy.get($tablediv)
                .find("tbody > tr > th, td")
                .not('.ng-hide')
                .eq(cellIndex)
                .invoke('text')
                .then((text1) => {
                  data.body = text1.trim()
                  dict.push(data)
                    })
            });
        }).then(() => {
          window.localStorage.setItem('data',JSON.stringify(dict))
        })
      });


    // cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div.row.pull-right.col-sm-6 > tabletoolstrans > div > input')
    //   .type(chapa)

    //     // Open Payslip module.
    //     cy.get('#reports_list').click()
    //     cy.get('#payslip').should('be.visible')
    //     cy.get('#payslip').click()
    //     cy.contains('h2','Payslip').should('be.visible')

    //   //selecting the payroll period
    //   cy.contains('Select...')
    //   .should('be.visible')
    //   .then(() => {
    //     cy.contains('Select...').click()
    //     })
    //   cy.contains(payroll_period).click()

    // // Selecting the employee to check
    // cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(2) > div:nth-child(2) > div > div').click()
    // cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(2) > div:nth-child(2) > div > div > div > div > input')
    //   .type(chapa)
    //   .focus()
    //   .type('{enter}')
    // cy.get('#page-wrapper > div.wrapper.wrapper-content.body > div > div > div > div > div:nth-child(2) > div.col-sm-2 > div > button').click()

    // //Getting employee payslip data (Earnings and deeductions)
    // cy.get('#table > tbody')
    //   .invoke('text')
    //   .then((text) => {
    //     const formattedText = text.replace(/\s/g, ' ')
    //     console.log(formattedText)
    //   })
  });
});
