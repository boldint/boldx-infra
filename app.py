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

from aws_cdk import core
from config import config
from stacks.network import Network
from stacks.eks import EKS


account = config.get("account_id")
region = config.get("region")

app = core.App()

#eu_west_1_vpc = Network(
#   scope=app,
#    id="BoldxNetwork",
#    cidr_range="172.16.0.0/16",
#    env=core.Environment(account=account, region=region)
#)

eu_west_1_eks = EKS(
    scope=app,
    id="BoldxEks",
    env=core.Environment(account=account, region=region)
    #vpc=eu_west_1_vpc.vpc
)

app.synth()

