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
    aws_ec2 as ec2
)


class Network(core.Stack):

    def __init__(self, scope: core.Construct, id: str, cidr_range: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # VPC creation
        self.vpc = ec2.Vpc(
            scope=self,
            id="BoldxVpc",
            max_azs=3,
            cidr=cidr_range,

            subnet_configuration=[
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PUBLIC,
                    name="Public"
                ),
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.PRIVATE,
                    name="Private"
                ),
                ec2.SubnetConfiguration(
                    subnet_type=ec2.SubnetType.ISOLATED,
                    name="Internal"
                )
            ]
        )

        core.CfnOutput(
            scope=self,
            id="vpc-id",
            value=self.vpc.vpc_id
        )