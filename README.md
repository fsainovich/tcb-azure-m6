tcb-azure-m6

BootCamp Azure – Module 6

Azure Postgre

Requeriments and Instructions Terraform:

- Run commands in a linux host (needs terraform);
- Create azure user principal: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/service_principal_client_secret
- Set Azure parameters.tf and tfvar.tf
- terraform init -> terraform validate -> terraform plan -out plan -> terraform apply plan.


Requeriments and Instructions Pulumi:

- Create pulumi account (always free for individual use);
- Install pulumi;
- Login azure with az cli;
- Install python 3.9.2 (minimum);
- Clone pulumi files;
- Set variables in __main__.py;
- Run in root folder of project:
	- pulumi stack init;
	- pulumi up;
	- pulumi destroy (destroy env);
	- pulumi stack rm (delete stack).
