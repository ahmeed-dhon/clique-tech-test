### deploy-monitoring directory 
- contains ansible script to deploy the monitoring and alerting service and to run the dummy log generator using python3

### test_package directory
- contains files that will be used by ansible to deploy the monitoring and alerting service and the dummy log generator

### how to run
```
cd deploy-monitoring
ansible-playbook -i inventories/prod/hosts setup-service-monitor.yaml
```