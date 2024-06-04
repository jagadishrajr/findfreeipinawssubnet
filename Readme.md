# List of unused AWS Subnet private IPs (v4)

Generate the list of free IPs (v4) in an AWS VPC Subnet.

## Usage

Install the requirements.

```
pip3 install requirements.txt
```

Execute the command.

```
python freeIpInSubnet.py  --subnetId=subnet-xxx
```

### Output

```
172.31.16.3
172.31.16.4
172.31.16.5
172.31.16.6
172.31.16.7
...
```

## Python version

Tested on Python 3.9
