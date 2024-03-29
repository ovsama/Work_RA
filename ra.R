#https://ourcodingclub.github.io/tutorials/writing-r-package/
install.packages("devtools")
install.packages("roxygen2")

install.packages("reticulate")


toupper("Menactra") 
tolower("ADULTES") 



getwd()
setwd("C:/Users/DELL/Desktop/Outils_de traitement/GenMed_products")

install.packages("xlsx")
library("xlsx")

install.packages("readxl")
library("readxl")
Data <- read_excel("C:/Users/DELL/Desktop/Outils_de traitement/GenMed_products/Version finale REQUIS CCS-FSA_dec2021.xlsx")
Data
summary(Data) 
str(Data)
mode(Data)
Data[1,]

ncol(Data) # it throws 26 but We got 31 columns !!