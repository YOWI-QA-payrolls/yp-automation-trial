/// <reference types="cypress" />

describe("Locators", () => {
    beforeEach(() => {
        cy.visit("/elements")
    })

    it("locating elements with get", () => {
        // Get all elements by tag name
        cy.get("button");
        
        // Get all elements by className
        cy.get(".btn-with-class")

        //Get all elements with specific class
        cy.get("[class='Elements-btn btn-with-class']")
        cy.get("[class='Elements-btn btn-with-class more-btn-classes']")

        //Get all elements with ID
        cy.get("[id='btn-with-id']")

        //Get all elements by specific attribute
        cy.get("[type='submit']")

        //Get elements by tag name and class
        cy.get("button.Elements-btn")

        //Get all elements by tag name and class and id
        cy.get("button.Elements-btn#btn-with-id")

        //Get all elements by tag name and class and type attribute
        cy.get('button.Elements-btn[type="submit"]')
    })

    it("locating elements with contains", () => {
        //Get elements with text
        cy.contains("Unique Text")

        //Get elemtns with not unique text
        cy.contains("Not Unique Text")

        //Get elements with get + contains
        cy.get("[type='submit']").contains("Not Unique Text")

    })

    it("Locating elemtns with find", () => {
        //Get elemtns with find
        cy.get("[id='form-1']").find(".btn-2")

    })

})

