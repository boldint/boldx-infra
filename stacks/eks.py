#
#  ██████╗  ██████╗ ██╗     ██████╗ ██╗███╗   ██╗████████╗
#  ██╔══██╗██╔═══██╗██║     ██╔══██╗██║████╗  ██║╚══██╔══╝
#  ██████╔╝██║   ██║██║     ██║  ██║██║██╔██╗ ██║   ██║
#  ██╔══██╗██║   ██║██║     ██║  ██║██║██║╚██╗██║   ██║
#  ██████╔╝╚██████╔╝███████╗██████╔╝██║██║ ╚████║   ██║
#  ╚═════╝  ╚═════╝ ╚══════╝╚═════╝ ╚═╝╚═╝  ╚═══╝   ╚═╝
#
# Copyright Bold International 2021
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software
# and associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies
# or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from aws_cdk import (
    core,
    aws_eks as eks,
    aws_ec2 as ec2,
    aws_iam as iam
)


class EKS(core.Stack):

    def __init__(self, scope: core.Construct, id: str, vpc, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        node_instance_type = "m5.large"

        cluster_admin = iam.Role(
            scope=self,
            id="BoldxEksAdminRole",
            role_name="Boldx-Eks-Admin-Role",
            assumed_by=iam.AccountRootPrincipal()
        )

        cluster = eks.Cluster(
            scope=self,
            id="BoldxEks",
            cluster_name="boldx-eks",
            version=eks.KubernetesVersion.V1_21,
            default_capacity=3,
            masters_role=cluster_admin,
            vpc=vpc
        )

        cluster.add_auto_scaling_group_capacity(
            id='AutoScalingGroup',
            instance_type=ec2.InstanceType(node_instance_type)
        )



