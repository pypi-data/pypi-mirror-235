# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'CapacityReservationFleetInstanceMatchCriteria',
    'CapacityReservationFleetTenancy',
    'Ec2FleetCapacityRebalanceReplacementStrategy',
    'Ec2FleetCapacityReservationOptionsRequestUsageStrategy',
    'Ec2FleetExcessCapacityTerminationPolicy',
    'Ec2FleetInstanceRequirementsRequestAcceleratorManufacturersItem',
    'Ec2FleetInstanceRequirementsRequestAcceleratorNamesItem',
    'Ec2FleetInstanceRequirementsRequestAcceleratorTypesItem',
    'Ec2FleetInstanceRequirementsRequestBareMetal',
    'Ec2FleetInstanceRequirementsRequestBurstablePerformance',
    'Ec2FleetInstanceRequirementsRequestCpuManufacturersItem',
    'Ec2FleetInstanceRequirementsRequestInstanceGenerationsItem',
    'Ec2FleetInstanceRequirementsRequestLocalStorage',
    'Ec2FleetInstanceRequirementsRequestLocalStorageTypesItem',
    'Ec2FleetSpotOptionsRequestAllocationStrategy',
    'Ec2FleetSpotOptionsRequestInstanceInterruptionBehavior',
    'Ec2FleetTagSpecificationResourceType',
    'Ec2FleetTargetCapacitySpecificationRequestDefaultTargetCapacityType',
    'Ec2FleetTargetCapacitySpecificationRequestTargetCapacityUnitType',
    'Ec2FleetType',
    'FlowLogDestinationOptionsPropertiesFileFormat',
    'FlowLogLogDestinationType',
    'FlowLogResourceType',
    'FlowLogTrafficType',
    'IpamPoolAwsService',
    'IpamPoolIpamScopeType',
    'IpamPoolPublicIpSource',
    'IpamPoolState',
    'IpamScopeType',
    'KeyPairKeyFormat',
    'KeyPairKeyType',
    'LaunchTemplateCpuOptionsAmdSevSnp',
    'NetworkInsightsAccessScopeAnalysisFindingsFound',
    'NetworkInsightsAccessScopeAnalysisStatus',
    'NetworkInsightsAccessScopeProtocol',
    'NetworkInsightsAnalysisStatus',
    'NetworkInsightsPathProtocol',
    'PrefixListAddressFamily',
    'SpotFleetEbsBlockDeviceVolumeType',
    'SpotFleetInstanceRequirementsRequestAcceleratorManufacturersItem',
    'SpotFleetInstanceRequirementsRequestAcceleratorNamesItem',
    'SpotFleetInstanceRequirementsRequestAcceleratorTypesItem',
    'SpotFleetInstanceRequirementsRequestBareMetal',
    'SpotFleetInstanceRequirementsRequestBurstablePerformance',
    'SpotFleetInstanceRequirementsRequestCpuManufacturersItem',
    'SpotFleetInstanceRequirementsRequestInstanceGenerationsItem',
    'SpotFleetInstanceRequirementsRequestLocalStorage',
    'SpotFleetInstanceRequirementsRequestLocalStorageTypesItem',
    'SpotFleetRequestConfigDataAllocationStrategy',
    'SpotFleetRequestConfigDataExcessCapacityTerminationPolicy',
    'SpotFleetRequestConfigDataInstanceInterruptionBehavior',
    'SpotFleetRequestConfigDataTargetCapacityUnitType',
    'SpotFleetRequestConfigDataType',
    'SpotFleetSpotCapacityRebalanceReplacementStrategy',
    'SpotFleetSpotPlacementTenancy',
    'SpotFleetTagSpecificationResourceType',
    'VpcEndpointType',
]


class CapacityReservationFleetInstanceMatchCriteria(str, Enum):
    OPEN = "open"


class CapacityReservationFleetTenancy(str, Enum):
    DEFAULT = "default"


class Ec2FleetCapacityRebalanceReplacementStrategy(str, Enum):
    LAUNCH = "launch"
    LAUNCH_BEFORE_TERMINATE = "launch-before-terminate"


class Ec2FleetCapacityReservationOptionsRequestUsageStrategy(str, Enum):
    USE_CAPACITY_RESERVATIONS_FIRST = "use-capacity-reservations-first"


class Ec2FleetExcessCapacityTerminationPolicy(str, Enum):
    TERMINATION = "termination"
    NO_TERMINATION = "no-termination"


class Ec2FleetInstanceRequirementsRequestAcceleratorManufacturersItem(str, Enum):
    NVIDIA = "nvidia"
    AMD = "amd"
    AMAZON_WEB_SERVICES = "amazon-web-services"
    XILINX = "xilinx"


class Ec2FleetInstanceRequirementsRequestAcceleratorNamesItem(str, Enum):
    A100 = "a100"
    V100 = "v100"
    K80 = "k80"
    T4 = "t4"
    M60 = "m60"
    RADEON_PRO_V520 = "radeon-pro-v520"
    VU9P = "vu9p"
    INFERENTIA = "inferentia"
    K520 = "k520"


class Ec2FleetInstanceRequirementsRequestAcceleratorTypesItem(str, Enum):
    GPU = "gpu"
    FPGA = "fpga"
    INFERENCE = "inference"


class Ec2FleetInstanceRequirementsRequestBareMetal(str, Enum):
    INCLUDED = "included"
    REQUIRED = "required"
    EXCLUDED = "excluded"


class Ec2FleetInstanceRequirementsRequestBurstablePerformance(str, Enum):
    INCLUDED = "included"
    REQUIRED = "required"
    EXCLUDED = "excluded"


class Ec2FleetInstanceRequirementsRequestCpuManufacturersItem(str, Enum):
    INTEL = "intel"
    AMD = "amd"
    AMAZON_WEB_SERVICES = "amazon-web-services"


class Ec2FleetInstanceRequirementsRequestInstanceGenerationsItem(str, Enum):
    CURRENT = "current"
    PREVIOUS = "previous"


class Ec2FleetInstanceRequirementsRequestLocalStorage(str, Enum):
    INCLUDED = "included"
    REQUIRED = "required"
    EXCLUDED = "excluded"


class Ec2FleetInstanceRequirementsRequestLocalStorageTypesItem(str, Enum):
    HDD = "hdd"
    SSD = "ssd"


class Ec2FleetSpotOptionsRequestAllocationStrategy(str, Enum):
    LOWEST_PRICE = "lowest-price"
    DIVERSIFIED = "diversified"
    CAPACITY_OPTIMIZED = "capacityOptimized"
    CAPACITY_OPTIMIZED_PRIORITIZED = "capacityOptimizedPrioritized"
    PRICE_CAPACITY_OPTIMIZED = "priceCapacityOptimized"


class Ec2FleetSpotOptionsRequestInstanceInterruptionBehavior(str, Enum):
    HIBERNATE = "hibernate"
    STOP = "stop"
    TERMINATE = "terminate"


class Ec2FleetTagSpecificationResourceType(str, Enum):
    CLIENT_VPN_ENDPOINT = "client-vpn-endpoint"
    CUSTOMER_GATEWAY = "customer-gateway"
    DEDICATED_HOST = "dedicated-host"
    DHCP_OPTIONS = "dhcp-options"
    EGRESS_ONLY_INTERNET_GATEWAY = "egress-only-internet-gateway"
    ELASTIC_GPU = "elastic-gpu"
    ELASTIC_IP = "elastic-ip"
    EXPORT_IMAGE_TASK = "export-image-task"
    EXPORT_INSTANCE_TASK = "export-instance-task"
    FLEET = "fleet"
    FPGA_IMAGE = "fpga-image"
    HOST_RESERVATION = "host-reservation"
    IMAGE = "image"
    IMPORT_IMAGE_TASK = "import-image-task"
    IMPORT_SNAPSHOT_TASK = "import-snapshot-task"
    INSTANCE = "instance"
    INTERNET_GATEWAY = "internet-gateway"
    KEY_PAIR = "key-pair"
    LAUNCH_TEMPLATE = "launch-template"
    LOCAL_GATEWAY_ROUTE_TABLE_VPC_ASSOCIATION = "local-gateway-route-table-vpc-association"
    NATGATEWAY = "natgateway"
    NETWORK_ACL = "network-acl"
    NETWORK_INSIGHTS_ANALYSIS = "network-insights-analysis"
    NETWORK_INSIGHTS_PATH = "network-insights-path"
    NETWORK_INTERFACE = "network-interface"
    PLACEMENT_GROUP = "placement-group"
    RESERVED_INSTANCES = "reserved-instances"
    ROUTE_TABLE = "route-table"
    SECURITY_GROUP = "security-group"
    SNAPSHOT = "snapshot"
    SPOT_FLEET_REQUEST = "spot-fleet-request"
    SPOT_INSTANCES_REQUEST = "spot-instances-request"
    SUBNET = "subnet"
    TRAFFIC_MIRROR_FILTER = "traffic-mirror-filter"
    TRAFFIC_MIRROR_SESSION = "traffic-mirror-session"
    TRAFFIC_MIRROR_TARGET = "traffic-mirror-target"
    TRANSIT_GATEWAY = "transit-gateway"
    TRANSIT_GATEWAY_ATTACHMENT = "transit-gateway-attachment"
    TRANSIT_GATEWAY_CONNECT_PEER = "transit-gateway-connect-peer"
    TRANSIT_GATEWAY_MULTICAST_DOMAIN = "transit-gateway-multicast-domain"
    TRANSIT_GATEWAY_ROUTE_TABLE = "transit-gateway-route-table"
    VOLUME = "volume"
    VPC = "vpc"
    VPC_FLOW_LOG = "vpc-flow-log"
    VPC_PEERING_CONNECTION = "vpc-peering-connection"
    VPN_CONNECTION = "vpn-connection"
    VPN_GATEWAY = "vpn-gateway"


class Ec2FleetTargetCapacitySpecificationRequestDefaultTargetCapacityType(str, Enum):
    ON_DEMAND = "on-demand"
    SPOT = "spot"


class Ec2FleetTargetCapacitySpecificationRequestTargetCapacityUnitType(str, Enum):
    VCPU = "vcpu"
    MEMORY_MIB = "memory-mib"
    UNITS = "units"


class Ec2FleetType(str, Enum):
    MAINTAIN = "maintain"
    REQUEST = "request"
    INSTANT = "instant"


class FlowLogDestinationOptionsPropertiesFileFormat(str, Enum):
    PLAIN_TEXT = "plain-text"
    PARQUET = "parquet"


class FlowLogLogDestinationType(str, Enum):
    """
    Specifies the type of destination to which the flow log data is to be published. Flow log data can be published to CloudWatch Logs or Amazon S3.
    """
    CLOUD_WATCH_LOGS = "cloud-watch-logs"
    S3 = "s3"
    KINESIS_DATA_FIREHOSE = "kinesis-data-firehose"


class FlowLogResourceType(str, Enum):
    """
    The type of resource for which to create the flow log. For example, if you specified a VPC ID for the ResourceId property, specify VPC for this property.
    """
    NETWORK_INTERFACE = "NetworkInterface"
    SUBNET = "Subnet"
    VPC = "VPC"
    TRANSIT_GATEWAY = "TransitGateway"
    TRANSIT_GATEWAY_ATTACHMENT = "TransitGatewayAttachment"


class FlowLogTrafficType(str, Enum):
    """
    The type of traffic to log. You can log traffic that the resource accepts or rejects, or all traffic.
    """
    ACCEPT = "ACCEPT"
    ALL = "ALL"
    REJECT = "REJECT"


class IpamPoolAwsService(str, Enum):
    """
    Limits which service in Amazon Web Services that the pool can be used in.
    """
    EC2 = "ec2"


class IpamPoolIpamScopeType(str, Enum):
    """
    Determines whether this scope contains publicly routable space or space for a private network
    """
    PUBLIC = "public"
    PRIVATE = "private"


class IpamPoolPublicIpSource(str, Enum):
    """
    The IP address source for pools in the public scope. Only used for provisioning IP address CIDRs to pools in the public scope. Default is `byoip`.
    """
    BYOIP = "byoip"
    AMAZON = "amazon"


class IpamPoolState(str, Enum):
    """
    The state of this pool. This can be one of the following values: "create-in-progress", "create-complete", "modify-in-progress", "modify-complete", "delete-in-progress", or "delete-complete"
    """
    CREATE_IN_PROGRESS = "create-in-progress"
    CREATE_COMPLETE = "create-complete"
    MODIFY_IN_PROGRESS = "modify-in-progress"
    MODIFY_COMPLETE = "modify-complete"
    DELETE_IN_PROGRESS = "delete-in-progress"
    DELETE_COMPLETE = "delete-complete"


class IpamScopeType(str, Enum):
    """
    Determines whether this scope contains publicly routable space or space for a private network
    """
    PUBLIC = "public"
    PRIVATE = "private"


class KeyPairKeyFormat(str, Enum):
    """
    The format of the private key
    """
    PEM = "pem"
    PPK = "ppk"


class KeyPairKeyType(str, Enum):
    """
    The crypto-system used to generate a key pair.
    """
    RSA = "rsa"
    ED25519 = "ed25519"


class LaunchTemplateCpuOptionsAmdSevSnp(str, Enum):
    """
    Indicates whether to enable the instance for AMD SEV-SNP. AMD SEV-SNP is supported with M6a, R6a, and C6a instance types only.
    """
    ENABLED = "enabled"
    DISABLED = "disabled"


class NetworkInsightsAccessScopeAnalysisFindingsFound(str, Enum):
    TRUE = "true"
    FALSE = "false"
    UNKNOWN = "unknown"


class NetworkInsightsAccessScopeAnalysisStatus(str, Enum):
    RUNNING = "running"
    FAILED = "failed"
    SUCCEEDED = "succeeded"


class NetworkInsightsAccessScopeProtocol(str, Enum):
    TCP = "tcp"
    UDP = "udp"


class NetworkInsightsAnalysisStatus(str, Enum):
    RUNNING = "running"
    FAILED = "failed"
    SUCCEEDED = "succeeded"


class NetworkInsightsPathProtocol(str, Enum):
    TCP = "tcp"
    UDP = "udp"


class PrefixListAddressFamily(str, Enum):
    """
    Ip Version of Prefix List.
    """
    I_PV4 = "IPv4"
    I_PV6 = "IPv6"


class SpotFleetEbsBlockDeviceVolumeType(str, Enum):
    GP2 = "gp2"
    GP3 = "gp3"
    IO1 = "io1"
    IO2 = "io2"
    SC1 = "sc1"
    ST1 = "st1"
    STANDARD = "standard"


class SpotFleetInstanceRequirementsRequestAcceleratorManufacturersItem(str, Enum):
    NVIDIA = "nvidia"
    AMD = "amd"
    AMAZON_WEB_SERVICES = "amazon-web-services"
    XILINX = "xilinx"


class SpotFleetInstanceRequirementsRequestAcceleratorNamesItem(str, Enum):
    A100 = "a100"
    V100 = "v100"
    K80 = "k80"
    T4 = "t4"
    M60 = "m60"
    RADEON_PRO_V520 = "radeon-pro-v520"
    VU9P = "vu9p"
    INFERENTIA = "inferentia"
    K520 = "k520"


class SpotFleetInstanceRequirementsRequestAcceleratorTypesItem(str, Enum):
    GPU = "gpu"
    FPGA = "fpga"
    INFERENCE = "inference"


class SpotFleetInstanceRequirementsRequestBareMetal(str, Enum):
    INCLUDED = "included"
    REQUIRED = "required"
    EXCLUDED = "excluded"


class SpotFleetInstanceRequirementsRequestBurstablePerformance(str, Enum):
    INCLUDED = "included"
    REQUIRED = "required"
    EXCLUDED = "excluded"


class SpotFleetInstanceRequirementsRequestCpuManufacturersItem(str, Enum):
    INTEL = "intel"
    AMD = "amd"
    AMAZON_WEB_SERVICES = "amazon-web-services"


class SpotFleetInstanceRequirementsRequestInstanceGenerationsItem(str, Enum):
    CURRENT = "current"
    PREVIOUS = "previous"


class SpotFleetInstanceRequirementsRequestLocalStorage(str, Enum):
    INCLUDED = "included"
    REQUIRED = "required"
    EXCLUDED = "excluded"


class SpotFleetInstanceRequirementsRequestLocalStorageTypesItem(str, Enum):
    HDD = "hdd"
    SSD = "ssd"


class SpotFleetRequestConfigDataAllocationStrategy(str, Enum):
    CAPACITY_OPTIMIZED = "capacityOptimized"
    CAPACITY_OPTIMIZED_PRIORITIZED = "capacityOptimizedPrioritized"
    DIVERSIFIED = "diversified"
    LOWEST_PRICE = "lowestPrice"
    PRICE_CAPACITY_OPTIMIZED = "priceCapacityOptimized"


class SpotFleetRequestConfigDataExcessCapacityTerminationPolicy(str, Enum):
    DEFAULT = "Default"
    NO_TERMINATION = "NoTermination"


class SpotFleetRequestConfigDataInstanceInterruptionBehavior(str, Enum):
    HIBERNATE = "hibernate"
    STOP = "stop"
    TERMINATE = "terminate"


class SpotFleetRequestConfigDataTargetCapacityUnitType(str, Enum):
    VCPU = "vcpu"
    MEMORY_MIB = "memory-mib"
    UNITS = "units"


class SpotFleetRequestConfigDataType(str, Enum):
    MAINTAIN = "maintain"
    REQUEST = "request"


class SpotFleetSpotCapacityRebalanceReplacementStrategy(str, Enum):
    LAUNCH = "launch"
    LAUNCH_BEFORE_TERMINATE = "launch-before-terminate"


class SpotFleetSpotPlacementTenancy(str, Enum):
    DEDICATED = "dedicated"
    DEFAULT = "default"
    HOST = "host"


class SpotFleetTagSpecificationResourceType(str, Enum):
    CLIENT_VPN_ENDPOINT = "client-vpn-endpoint"
    CUSTOMER_GATEWAY = "customer-gateway"
    DEDICATED_HOST = "dedicated-host"
    DHCP_OPTIONS = "dhcp-options"
    EGRESS_ONLY_INTERNET_GATEWAY = "egress-only-internet-gateway"
    ELASTIC_GPU = "elastic-gpu"
    ELASTIC_IP = "elastic-ip"
    EXPORT_IMAGE_TASK = "export-image-task"
    EXPORT_INSTANCE_TASK = "export-instance-task"
    FLEET = "fleet"
    FPGA_IMAGE = "fpga-image"
    HOST_RESERVATION = "host-reservation"
    IMAGE = "image"
    IMPORT_IMAGE_TASK = "import-image-task"
    IMPORT_SNAPSHOT_TASK = "import-snapshot-task"
    INSTANCE = "instance"
    INTERNET_GATEWAY = "internet-gateway"
    KEY_PAIR = "key-pair"
    LAUNCH_TEMPLATE = "launch-template"
    LOCAL_GATEWAY_ROUTE_TABLE_VPC_ASSOCIATION = "local-gateway-route-table-vpc-association"
    NATGATEWAY = "natgateway"
    NETWORK_ACL = "network-acl"
    NETWORK_INSIGHTS_ANALYSIS = "network-insights-analysis"
    NETWORK_INSIGHTS_PATH = "network-insights-path"
    NETWORK_INTERFACE = "network-interface"
    PLACEMENT_GROUP = "placement-group"
    RESERVED_INSTANCES = "reserved-instances"
    ROUTE_TABLE = "route-table"
    SECURITY_GROUP = "security-group"
    SNAPSHOT = "snapshot"
    SPOT_FLEET_REQUEST = "spot-fleet-request"
    SPOT_INSTANCES_REQUEST = "spot-instances-request"
    SUBNET = "subnet"
    TRAFFIC_MIRROR_FILTER = "traffic-mirror-filter"
    TRAFFIC_MIRROR_SESSION = "traffic-mirror-session"
    TRAFFIC_MIRROR_TARGET = "traffic-mirror-target"
    TRANSIT_GATEWAY = "transit-gateway"
    TRANSIT_GATEWAY_ATTACHMENT = "transit-gateway-attachment"
    TRANSIT_GATEWAY_CONNECT_PEER = "transit-gateway-connect-peer"
    TRANSIT_GATEWAY_MULTICAST_DOMAIN = "transit-gateway-multicast-domain"
    TRANSIT_GATEWAY_ROUTE_TABLE = "transit-gateway-route-table"
    VOLUME = "volume"
    VPC = "vpc"
    VPC_FLOW_LOG = "vpc-flow-log"
    VPC_PEERING_CONNECTION = "vpc-peering-connection"
    VPN_CONNECTION = "vpn-connection"
    VPN_GATEWAY = "vpn-gateway"


class VpcEndpointType(str, Enum):
    INTERFACE = "Interface"
    GATEWAY = "Gateway"
    GATEWAY_LOAD_BALANCER = "GatewayLoadBalancer"
