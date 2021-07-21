import pulumi
from pulumi.resource import ResourceOptions
from pulumi_azure_native import resources
import pulumi_azure_native as azure_native

RG_NAME=""
LOCATION= "eastus"
PG_SERVER_NAME=""
DB_NAME="app01"
DB_ADMIN="sql"
DB_ADMIN_PW="Admin123456!"
FW_NAME="Global"

# Create an Azure Resource Group
resource_group = azure_native.resources.ResourceGroup(RG_NAME,
    location=LOCATION,
    resource_group_name=RG_NAME
)

#Create Postgre instance
pgserver = azure_native.dbforpostgresql.Server(PG_SERVER_NAME,
    location=LOCATION,
    properties=azure_native.dbforpostgresql.ServerPropertiesForDefaultCreateArgs(
        administrator_login=DB_ADMIN,
        administrator_login_password=DB_ADMIN_PW,
        create_mode="Default",
        minimal_tls_version="TLS1_2",
        ssl_enforcement="Enabled",
        version="10",
        storage_profile=azure_native.dbforpostgresql.StorageProfileArgs(
            backup_retention_days=7,
            geo_redundant_backup="Disabled",
            storage_mb=5120,
        ),
    ),
    resource_group_name=RG_NAME,
    server_name=PG_SERVER_NAME,
    sku=azure_native.dbforpostgresql.SkuArgs(
        capacity=2,
        family="Gen5",
        name="B_Gen5_2",
        tier="Basic",
    ),
    opts=ResourceOptions(depends_on=[resource_group])
)

#Create DB
database = azure_native.dbforpostgresql.Database(DB_NAME,
    charset="UTF8",
    collation="English_United States.1252",
    database_name=DB_NAME,
    resource_group_name=RG_NAME,
    server_name=PG_SERVER_NAME,
    opts=ResourceOptions(depends_on=[resource_group, pgserver])
)

#Create FW access Rule
firewall_rule = azure_native.dbforpostgresql.FirewallRule(FW_NAME,
    firewall_rule_name=FW_NAME,
    resource_group_name=RG_NAME,
    server_name=PG_SERVER_NAME,
    start_ip_address="0.0.0.0",
    end_ip_address="255.255.255.255",
    opts=ResourceOptions(depends_on=[resource_group,pgserver])
)