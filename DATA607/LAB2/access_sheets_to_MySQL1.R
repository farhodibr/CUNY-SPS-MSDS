

# Libraries
library(DBI)
library(RMySQL)
library(dplyr)
library(googlesheets4)

# URL of the publicly accessible "movie_reviews" Sheet
sheet_url <- sheet_url <- "https://docs.google.com/spreadsheets/d/1x7uAbOozoNutaFOfbq_X8c33vzSXvqshJxZgu_MfJhI/edit?usp=sharing"
sheet_name <- "Form Responses 1"

# Read the data from the sheet
data <- read_sheet(sheet_url, sheet = sheet_name)
glimpse(data)
print(colnames(data))
# Credentials to access database from MySQL
db_host <- Sys.getenv("DB_HOST")
db_port <- as.integer(Sys.getenv("DB_PORT"))
db_name <- Sys.getenv("DB_NAME")
db_user <- Sys.getenv("DB_USER")
db_pass <- Sys.getenv("DB_PASS")
print(db_host)

# MySQL database connection
con <- dbConnect(
                 drv = RMySQL::MySQL(), 
                 dbname = db_name, 
                 host = db_host,
                 username = db_user,
                 password = db_pass
                 )

query <- paste("CREATE TABLE Movies_new1 (
              Timestamp DATETIME,
              Name CHAR(100) PRIMARY KEY,
              Gladiator2 INT,
              Wolfs INT,
              The_Substance INT,
              Bad_Boys4 INT,
              The_Beekeeper INT,
              Rebel_Ridge INT)
                ", sep = "")

dbExecute(con, query)

# Transfer data into MySQL. Iterating through each variable values row in data.
for (i in 1:nrow(data)) {
  name <- data$Name[i]
  gladiator2 <- data$Gladiator2[i]
  wolfs <- data$Wolfs[i]
  the_substance <- data$The_Substance[i]
  bad_boys4 <- data$Bad_Boys4[i]
  the_beekeeper <- data$The_Beekeeper[i]
  rebel_ridge <- data$Rebel_Ridge[i]
  
  #SQL code to insert values for same variables in each new row in MySQL database
  query <- paste0(
    "INSERT IGNORE INTO Movies_new1 (Name, Gladiator2, Wolfs, The_Substance, Bad_Boys4, The_Beekeeper, Rebel_Ridge) VALUES (",
    "'", name, "', ",
    "'", gladiator2, "', ",
    "'", wolfs, "', ",
    "'", the_substance, "', ",
    "'", bad_boys4, "', ",
    "'", the_beekeeper, "', ",
    "'", rebel_ridge, "')"
  )
  
  dbExecute(con, query)
}

#create R code to transfer data from MysQL to R
# Query to select all data from the table
query <- "SELECT * FROM Movies_new1"
# Execute the query and fetch the results
df <- dbGetQuery(con, query)
# Print the data
print(df)
glimpse(df)
summary(df)

#remove Timestamp column

df <- df |> select(-Timestamp)
glimpse(df)




# Replace zeros with the mean of each numeric column and round the values
df <- df %>%
  mutate(across(where(is.numeric), ~ {
    column_mean <- round(mean(.x[.x != 0], na.rm = TRUE))
    .x[.x == 0] <- column_mean
    round(.x, 0)
  }))
summary(df)


# Print the updated data
print(df)
glimpse(df)





# Write the data to a CSV file
write.csv(data, "C:/CUNY_MSDS/DATA607/LAB2/Movie_Reviews.csv", row.names = FALSE)



# Disconnecting from MySQL
dbDisconnect(con)

print("Data inserted successfully.")

#Show warnings
warnings()

#rmarkdown::render("C:/CUNY_MSDS/DATA607/LAB2/access_sheets_to_MySQL1.R")

