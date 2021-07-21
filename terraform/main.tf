#Create Resource Group
resource "azurerm_resource_group" "TCB-AZURE-M6" {
  name     = var.RG_NAME
  location = var.AZURE_LOCATION
}

#Create DB Instance
resource "azurerm_postgresql_server" "postgre" {
  depends_on = [
    azurerm_resource_group.TCB-AZURE-M6  
  ]
  name                = var.PG_NAME
  location            = var.AZURE_LOCATION
  resource_group_name = var.RG_NAME

  sku_name = "B_Gen5_2"

  storage_mb                   = 5120
  backup_retention_days        = 7
  geo_redundant_backup_enabled = false
  auto_grow_enabled            = true

  administrator_login          = "sql"
  administrator_login_password = "Admin123456!"
  version                      = "10"
  ssl_enforcement_enabled      = true
}

#Create DataBase
resource "azurerm_postgresql_database" "db01" {
  depends_on = [
    azurerm_resource_group.TCB-AZURE-M6  
  ]
  name                = "db01"
  resource_group_name = var.RG_NAME
  server_name         = azurerm_postgresql_server.postgre.name
  charset             = "UTF8"
  collation           = "English_United States.1252"
}

#Create FW access rule - for test only
resource "azurerm_postgresql_firewall_rule" "global_access" {
  depends_on = [
    azurerm_resource_group.TCB-AZURE-M6  
  ]
  name                = "global_access"
  resource_group_name = var.RG_NAME
  server_name         = azurerm_postgresql_server.postgre.name
  start_ip_address    = "0.0.0.0"
  end_ip_address      = "255.255.255.255"
}
