# boldx-infra
AWS infrastructure 

-----

This project contains the AWS infrastructure stack for this BoldX masterclass.

You can fork this repo and run it on github.

You will need to set 3 repository secrets:

- AWS_ACCOUNT_ID
- AWS_ACCESS_KEY_ID
- AWS_SECRET_ACCESS_KEY

Alternately, you can run it locally, following the instructions below.

---

###Requirements

- virtualenv
- aws-cdk
- kubectl


###How to run this project manually

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

1 - Find the **arn** of the role  `Boldx-Eks-Admin-Role`

#####- using aws-cli:

```
ROLE_ARN=$(aws iam get-role --role-name Boldx-Eks-Admin-Role | jq -r ".Role.Arn")
```

#####- using the console:
https://console.aws.amazon.com/iam/home#/roles/Boldx-Eks-Admin-Role

2 - Update kube config

```
aws eks update-kubeconfig --name boldtech-dev-eks --region eu-west-1 --role-arn ${ROLE_ARN}
```

3 - Test kubectl

```
kubectl get node
```



