from aws_cdk import core
from aws_cdk import (
    aws_ec2 as ec2,
    aws_ecs as ecs,
    aws_ecr as ecr,
    aws_iam as iam,
    aws_ecs_patterns as ecs_patterns,
    core,
)

class BoboExplorerStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create a VPC
        vpc = ec2.Vpc(
            self, "christiansVpc", 
            max_azs = 2,
            )     # default is all AZs in region, 
                  # but you can limit to avoid reaching resource quota

        # Create ECS cluster
        cluster = ecs.Cluster(self, "christiansCluster", vpc=vpc)

        # Add an AutoScalingGroup with spot instances to the existing cluster
        cluster.add_capacity("AsgSpot",
            max_capacity=2,
            min_capacity=1,
            desired_capacity=2,
            instance_type=ec2.InstanceType("t2.micro"),
            spot_price="0.0010",
            # Enable the Automated Spot Draining support for Amazon ECS
            spot_instance_draining=True
        )

        # Build Dockerfile from local folder and push to ECR
        image = ecs.ContainerImage.from_asset('app')

        # Create Fargate service
        fargate_service = ecs_patterns.ApplicationLoadBalancedFargateService(
            self, "christiansFargateService",
            cluster=cluster,            # Required
            cpu=256,                    # Default is 256 (512 is 0.5 vCPU)
            desired_count=1,            # Default is 1
            task_image_options=ecs_patterns.ApplicationLoadBalancedTaskImageOptions(
                image=image, 
                container_port=8501,
                ),
            memory_limit_mib=512,      # Default is 512
            public_load_balancer=True)  # Default is True

        # Add policies to task role
        fargate_service.task_definition.add_to_task_role_policy(iam.PolicyStatement(
            effect=iam.Effect.ALLOW,
            actions = ["comprehend:*"],
            resources = ["*"],
            )
        )

        # Setup task auto-scaling
        scaling = fargate_service.service.auto_scale_task_count(
            max_capacity=10
        )
        scaling.scale_on_cpu_utilization(
            "CpuScaling",
            target_utilization_percent=50,
            scale_in_cooldown=core.Duration.seconds(60),
            scale_out_cooldown=core.Duration.seconds(60),
        )
