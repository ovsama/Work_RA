library(shiny)

# Define UI
ui <- fluidPage(
  titlePanel("Currency Converter"),
  sidebarLayout(
    sidebarPanel(
      numericInput("amount_eur", "Enter amount in EUR:", value = 1, min = 0),
      actionButton("convert", "Convert")
    ),
    mainPanel(
      textOutput("result")
    )
  )
)

# Define server logic
server <- function(input, output) {
  observeEvent(input$convert, {
    amount_fcfa <- input$amount_eur * 655.957  # Fixed exchange rate
    output$result <- renderText({
      paste(input$amount_eur, "EUR is equal to", round(amount_fcfa, 2), "FCFA")
    })
  })
}

# Run the application
shinyApp(ui = ui, server = server)