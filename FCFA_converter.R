FCFA <- function(euros) {
  a <- 655.957*euros
  p <- round(a,2) 
  paste(p, "Francs CFA")
} 
FCFA(1.67)

