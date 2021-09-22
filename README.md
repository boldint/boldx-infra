# boldtech-infra
AWS infrastructure 

-----

This project contains the AWS infrastructure stack for BoldTech

###Requirements

- virtualenv
- aws-cdk
- kubectl


###How to run this project

1 - Create a python virtual environment

```virtualenv -p python3.8 venv ```

2 - Activate the environment

```source venv/bin/activate```

3 - Install project requirements

````pip install -r requirements.txt````

4 - Set your AWS account ID

```export AWS_ACCOUNT_ID=XXXXXXX```

5 - Bootstrap cdk

```cdk bootstrap```

6 - Check stack differences

```cdk diff```

7 - Deploy stack

```cdk deploy --all```

---

###How to connect to the cluster

1 - Find the **arn** of the role  `boldtech-dev-eks-admin`

#####- using aws-cli:

```
ROLE_ARN=$(aws iam get-role --role-name boldtech-dev-eks-admin | jq -r ".Role.Arn")
```

#####- using the console:
https://console.aws.amazon.com/iam/home#/roles/boldtech-dev-eks-admin

2 - Update kube config

```
aws eks update-kubeconfig --name boldtech-dev-eks --region eu-west-1 --role-arn ${ROLE_ARN}
```

3 - Test kubectl

```
kubectl get node
```



