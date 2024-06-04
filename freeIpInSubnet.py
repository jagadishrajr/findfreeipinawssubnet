import boto3
import ipaddress, argparse

ec2Client = boto3.client('ec2')
parser=argparse.ArgumentParser()
parser.add_argument("--subnetId", help="Provide subnetId", required=True)
args=parser.parse_args()
subnetId = args.subnetId

descibeSubnets = ec2Client.describe_subnets(
    SubnetIds=[
        subnetId,
    ]
)
networkInterfaces = ec2Client.describe_network_interfaces(
    Filters=[
        {
            'Name': 'subnet-id',
            'Values': [
                subnetId,
            ]
        }
    ]
)
for subnet in descibeSubnets['Subnets']:
    subnetCidrBlock = subnet['CidrBlock']
usedIpList = []
for interface in networkInterfaces['NetworkInterfaces']:
    usedIpList.append(interface['PrivateIpAddress'])

allIpsInCidrBlock = [str(ip) for ip in ipaddress.IPv4Network(subnetCidrBlock)]

# remove first four items from allIpsInCidrBlock as they are reserved for AWS
allIpsInCidrBlock = allIpsInCidrBlock[4:]
# remove last item from allIpsInCidrBlock as it is the broadcast address
allIpsInCidrBlock.pop()
# remove usedIpList items from allIpsInCidrBlock
allIpsInCidrBlock = [ip for ip in allIpsInCidrBlock if ip not in usedIpList]
for freeIp in allIpsInCidrBlock:
    print(freeIp)
