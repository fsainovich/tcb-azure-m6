#Azure Location
variable "AZURE_LOCATION" {
    type = string
    default = "eastus"
}

#RG NameAzure Location
variable "RG_NAME" {
    type = string
    default = ""
}

#POSTGRE name
variable "PG_NAME" {
    type = string
    default = ""
}

#Subscription ID
variable "SUB_ID" {
    type = string
    default = ""
}

#Principal Client ID
variable "CLI_ID" {
    type = string
    default = ""
}

#Principal Client SECRET
variable "CLI_SECRET" {
    type = string
    default = ""
} 

#Tenant ID  
variable "TEN_ID" {
    type = string
    default = ""
} 