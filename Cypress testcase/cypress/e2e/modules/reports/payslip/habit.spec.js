/// <reference types="cypress" />

describe('habit dashboards', () => {

    beforeEach(() => {
        cy.visit("/habits")
    })

    it("display modal after clicking add button", () => {
        cy.contains("button", "Add").click()
        cy.contains("Add a new habit").should("be.visible")
    })

    it("Display new habit in list", () => {
        cy.get("#habit-add-btn").click()
        cy.get("input[placeholder='Habit']").type("this is my text")
        cy.get("[class='btn btn-primary']").click()
        cy.contains("this is my text")
            .should("be.visible")
            .and("have.class", "HabitCard__habit-container")
    })

    it("toggle icon after clicking item in list", () => {
        cy.get("#habit-add-btn").click()
        cy.get("input[placeholder='Habit']").type("this is my text")
        cy.get("[class='btn btn-primary']").click()
        cy.contains("this is my text")
            .should("be.visible")
            .and("have.class", "HabitCard__habit-container")
        cy.get("[src='/static/media/close.fa7e5ead.svg']").should("be.visible")
        cy.contains("this is my text").click()
        cy.get("[src='/static/media/check.9e8832df.svg']").should("be.visible")
    })

    it("modal should not close with incomplete fields", () => {
        cy.get("#habit-add-btn").click()
        // cy.get("input[placeholder='Habit']").type("this is my text")
        cy.get("[class='btn btn-primary']").click()
        cy.contains("Add a new habit")
            .should("be.visible")
            .and("have.class", "modal-title h4")
    })

    it("modal should close after clicking close button", () => {
        cy.get("#habit-add-btn").click()
        cy.contains("Add a new habit")
            .should("be.visible")
            .and("have.class", "modal-title h4")
        cy.get("[class='btn btn-secondary']").click()
        cy.get("[class='Habit-header']").should("be.visible")

    })

})

