# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['ListenerAdditionalCertificateAttachmentArgs', 'ListenerAdditionalCertificateAttachment']

@pulumi.input_type
class ListenerAdditionalCertificateAttachmentArgs:
    def __init__(__self__, *,
                 certificate_id: pulumi.Input[str],
                 listener_id: pulumi.Input[str],
                 dry_run: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a ListenerAdditionalCertificateAttachment resource.
        :param pulumi.Input[str] certificate_id: Certificate ID. Currently, only server certificates are supported.
        :param pulumi.Input[str] listener_id: The ID of the tcpssl listener.
        :param pulumi.Input[bool] dry_run: Whether to PreCheck only this request, value: - **true**: sends a check request and does not create a resource. Check items include whether required parameters, request format, and business restrictions have been filled in. If the check fails, the corresponding error is returned. If the check passes, the error code 'DryRunOperation' is returned '. - **false** (default): Sends a normal request, returns the HTTP 2xx status code after the check, and directly performs the operation.
        """
        ListenerAdditionalCertificateAttachmentArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            certificate_id=certificate_id,
            listener_id=listener_id,
            dry_run=dry_run,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             certificate_id: pulumi.Input[str],
             listener_id: pulumi.Input[str],
             dry_run: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("certificate_id", certificate_id)
        _setter("listener_id", listener_id)
        if dry_run is not None:
            _setter("dry_run", dry_run)

    @property
    @pulumi.getter(name="certificateId")
    def certificate_id(self) -> pulumi.Input[str]:
        """
        Certificate ID. Currently, only server certificates are supported.
        """
        return pulumi.get(self, "certificate_id")

    @certificate_id.setter
    def certificate_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "certificate_id", value)

    @property
    @pulumi.getter(name="listenerId")
    def listener_id(self) -> pulumi.Input[str]:
        """
        The ID of the tcpssl listener.
        """
        return pulumi.get(self, "listener_id")

    @listener_id.setter
    def listener_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "listener_id", value)

    @property
    @pulumi.getter(name="dryRun")
    def dry_run(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to PreCheck only this request, value: - **true**: sends a check request and does not create a resource. Check items include whether required parameters, request format, and business restrictions have been filled in. If the check fails, the corresponding error is returned. If the check passes, the error code 'DryRunOperation' is returned '. - **false** (default): Sends a normal request, returns the HTTP 2xx status code after the check, and directly performs the operation.
        """
        return pulumi.get(self, "dry_run")

    @dry_run.setter
    def dry_run(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "dry_run", value)


@pulumi.input_type
class _ListenerAdditionalCertificateAttachmentState:
    def __init__(__self__, *,
                 certificate_id: Optional[pulumi.Input[str]] = None,
                 dry_run: Optional[pulumi.Input[bool]] = None,
                 listener_id: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ListenerAdditionalCertificateAttachment resources.
        :param pulumi.Input[str] certificate_id: Certificate ID. Currently, only server certificates are supported.
        :param pulumi.Input[bool] dry_run: Whether to PreCheck only this request, value: - **true**: sends a check request and does not create a resource. Check items include whether required parameters, request format, and business restrictions have been filled in. If the check fails, the corresponding error is returned. If the check passes, the error code 'DryRunOperation' is returned '. - **false** (default): Sends a normal request, returns the HTTP 2xx status code after the check, and directly performs the operation.
        :param pulumi.Input[str] listener_id: The ID of the tcpssl listener.
        :param pulumi.Input[str] status: The status of the resource.
        """
        _ListenerAdditionalCertificateAttachmentState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            certificate_id=certificate_id,
            dry_run=dry_run,
            listener_id=listener_id,
            status=status,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             certificate_id: Optional[pulumi.Input[str]] = None,
             dry_run: Optional[pulumi.Input[bool]] = None,
             listener_id: Optional[pulumi.Input[str]] = None,
             status: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if certificate_id is not None:
            _setter("certificate_id", certificate_id)
        if dry_run is not None:
            _setter("dry_run", dry_run)
        if listener_id is not None:
            _setter("listener_id", listener_id)
        if status is not None:
            _setter("status", status)

    @property
    @pulumi.getter(name="certificateId")
    def certificate_id(self) -> Optional[pulumi.Input[str]]:
        """
        Certificate ID. Currently, only server certificates are supported.
        """
        return pulumi.get(self, "certificate_id")

    @certificate_id.setter
    def certificate_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_id", value)

    @property
    @pulumi.getter(name="dryRun")
    def dry_run(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to PreCheck only this request, value: - **true**: sends a check request and does not create a resource. Check items include whether required parameters, request format, and business restrictions have been filled in. If the check fails, the corresponding error is returned. If the check passes, the error code 'DryRunOperation' is returned '. - **false** (default): Sends a normal request, returns the HTTP 2xx status code after the check, and directly performs the operation.
        """
        return pulumi.get(self, "dry_run")

    @dry_run.setter
    def dry_run(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "dry_run", value)

    @property
    @pulumi.getter(name="listenerId")
    def listener_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the tcpssl listener.
        """
        return pulumi.get(self, "listener_id")

    @listener_id.setter
    def listener_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "listener_id", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the resource.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)


class ListenerAdditionalCertificateAttachment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate_id: Optional[pulumi.Input[str]] = None,
                 dry_run: Optional[pulumi.Input[bool]] = None,
                 listener_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a NLB Listener Additional Certificate Attachment resource.

        For information about NLB Listener Additional Certificate Attachment and how to use it, see [What is Listener Additional Certificate Attachment](https://www.alibabacloud.com/help/en/server-load-balancer/latest/nlb-instances-change).

        > **NOTE:** Available since v1.209.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tf-example"
        default_resource_groups = alicloud.resourcemanager.get_resource_groups()
        default_zones = alicloud.nlb.get_zones()
        default_network = alicloud.vpc.Network("defaultNetwork",
            vpc_name=name,
            cidr_block="10.4.0.0/16")
        default_switch = alicloud.vpc.Switch("defaultSwitch",
            vswitch_name=name,
            cidr_block="10.4.0.0/24",
            vpc_id=default_network.id,
            zone_id=default_zones.zones[0].id)
        default1 = alicloud.vpc.Switch("default1",
            vswitch_name=name,
            cidr_block="10.4.1.0/24",
            vpc_id=default_network.id,
            zone_id=default_zones.zones[1].id)
        default_security_group = alicloud.ecs.SecurityGroup("defaultSecurityGroup", vpc_id=default_network.id)
        default_load_balancer = alicloud.nlb.LoadBalancer("defaultLoadBalancer",
            load_balancer_name=name,
            resource_group_id=default_resource_groups.ids[0],
            load_balancer_type="Network",
            address_type="Internet",
            address_ip_version="Ipv4",
            vpc_id=default_network.id,
            tags={
                "Created": "TF",
                "For": "example",
            },
            zone_mappings=[
                alicloud.nlb.LoadBalancerZoneMappingArgs(
                    vswitch_id=default_switch.id,
                    zone_id=default_zones.zones[0].id,
                ),
                alicloud.nlb.LoadBalancerZoneMappingArgs(
                    vswitch_id=default1.id,
                    zone_id=default_zones.zones[1].id,
                ),
            ])
        default_server_group = alicloud.nlb.ServerGroup("defaultServerGroup",
            resource_group_id=default_resource_groups.ids[0],
            server_group_name=name,
            server_group_type="Instance",
            vpc_id=default_network.id,
            scheduler="Wrr",
            protocol="TCPSSL",
            connection_drain=True,
            connection_drain_timeout=60,
            address_ip_version="Ipv4",
            health_check=alicloud.nlb.ServerGroupHealthCheckArgs(
                health_check_url="/adc/index.html",
                health_check_domain="tf-iac.com",
                health_check_enabled=True,
                health_check_type="TCP",
                health_check_connect_port=0,
                healthy_threshold=2,
                unhealthy_threshold=2,
                health_check_connect_timeout=5,
                health_check_interval=10,
                http_check_method="GET",
                health_check_http_codes=[
                    "http_2xx",
                    "http_3xx",
                    "http_4xx",
                ],
            ),
            tags={
                "Created": "TF",
                "For": "example",
            })
        default_listener = alicloud.nlb.Listener("defaultListener",
            listener_protocol="TCPSSL",
            listener_port=1883,
            security_policy_id="tls_cipher_policy_1_0",
            listener_description=name,
            load_balancer_id=default_load_balancer.id,
            server_group_id=default_server_group.id,
            idle_timeout=900,
            proxy_protocol_enabled=True,
            sec_sensor_enabled=True,
            alpn_enabled=True,
            alpn_policy="HTTP2Optional",
            cps=10000,
            mss=0)
        default_service_certificate = alicloud.cas.ServiceCertificate("defaultServiceCertificate",
            certificate_name=name,
            cert=\"\"\"-----BEGIN CERTIFICATE-----
        MIIDRjCCAq+gAwIBAgIJAJn3ox4K13PoMA0GCSqGSIb3DQEBBQUAMHYxCzAJBgNV
        BAYTAkNOMQswCQYDVQQIEwJCSjELMAkGA1UEBxMCQkoxDDAKBgNVBAoTA0FMSTEP
        MA0GA1UECxMGQUxJWVVOMQ0wCwYDVQQDEwR0ZXN0MR8wHQYJKoZIhvcNAQkBFhB0
        ZXN0QGhvdG1haWwuY29tMB4XDTE0MTEyNDA2MDQyNVoXDTI0MTEyMTA2MDQyNVow
        djELMAkGA1UEBhMCQ04xCzAJBgNVBAgTAkJKMQswCQYDVQQHEwJCSjEMMAoGA1UE
        ChMDQUxJMQ8wDQYDVQQLEwZBTElZVU4xDTALBgNVBAMTBHRlc3QxHzAdBgkqhkiG
        9w0BCQEWEHRlc3RAaG90bWFpbC5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJ
        AoGBAM7SS3e9+Nj0HKAsRuIDNSsS3UK6b+62YQb2uuhKrp1HMrOx61WSDR2qkAnB
        coG00Uz38EE+9DLYNUVQBK7aSgLP5M1Ak4wr4GqGyCgjejzzh3DshUzLCCy2rook
        KOyRTlPX+Q5l7rE1fcSNzgepcae5i2sE1XXXzLRIDIvQxcspAgMBAAGjgdswgdgw
        HQYDVR0OBBYEFBdy+OuMsvbkV7R14f0OyoLoh2z4MIGoBgNVHSMEgaAwgZ2AFBdy
        +OuMsvbkV7R14f0OyoLoh2z4oXqkeDB2MQswCQYDVQQGEwJDTjELMAkGA1UECBMC
        QkoxCzAJBgNVBAcTAkJKMQwwCgYDVQQKEwNBTEkxDzANBgNVBAsTBkFMSVlVTjEN
        MAsGA1UEAxMEdGVzdDEfMB0GCSqGSIb3DQEJARYQdGVzdEBob3RtYWlsLmNvbYIJ
        AJn3ox4K13PoMAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQEFBQADgYEAY7KOsnyT
        cQzfhiiG7ASjiPakw5wXoycHt5GCvLG5htp2TKVzgv9QTliA3gtfv6oV4zRZx7X1
        Ofi6hVgErtHaXJheuPVeW6eAW8mHBoEfvDAfU3y9waYrtUevSl07643bzKL6v+Qd
        DUBTxOAvSYfXTtI90EAxEG/bJJyOm5LqoiA=
        -----END CERTIFICATE-----
        \"\"\",
            key=\"\"\"-----BEGIN RSA PRIVATE KEY-----
        MIICXAIBAAKBgQDO0kt3vfjY9BygLEbiAzUrEt1Cum/utmEG9rroSq6dRzKzsetV
        kg0dqpAJwXKBtNFM9/BBPvQy2DVFUASu2koCz+TNQJOMK+BqhsgoI3o884dw7IVM
        ywgstq6KJCjskU5T1/kOZe6xNX3Ejc4HqXGnuYtrBNV118y0SAyL0MXLKQIDAQAB
        AoGAfe3NxbsGKhN42o4bGsKZPQDfeCHMxayGp5bTd10BtQIE/ST4BcJH+ihAS7Bd
        6FwQlKzivNd4GP1MckemklCXfsVckdL94e8ZbJl23GdWul3v8V+KndJHqv5zVJmP
        hwWoKimwIBTb2s0ctVryr2f18N4hhyFw1yGp0VxclGHkjgECQQD9CvllsnOwHpP4
        MdrDHbdb29QrobKyKW8pPcDd+sth+kP6Y8MnCVuAKXCKj5FeIsgVtfluPOsZjPzz
        71QQWS1dAkEA0T0KXO8gaBQwJhIoo/w6hy5JGZnrNSpOPp5xvJuMAafs2eyvmhJm
        Ev9SN/Pf2VYa1z6FEnBaLOVD6hf6YQIsPQJAX/CZPoW6dzwgvimo1/GcY6eleiWE
        qygqjWhsh71e/3bz7yuEAnj5yE3t7Zshcp+dXR3xxGo0eSuLfLFxHgGxwQJAAxf8
        9DzQ5NkPkTCJi0sqbl8/03IUKTgT6hcbpWdDXa7m8J3wRr3o5nUB+TPQ5nzAbthM
        zWX931YQeACcwhxvHQJBAN5mTzzJD4w4Ma6YTaNHyXakdYfyAWrOkPIWZxfhMfXe
        DrlNdiysTI4Dd1dLeErVpjsckAaOW/JDG5PCSwkaMxk=
        -----END RSA PRIVATE KEY-----
        \"\"\")
        default_listener_additional_certificate_attachment = alicloud.nlb.ListenerAdditionalCertificateAttachment("defaultListenerAdditionalCertificateAttachment",
            certificate_id=default_service_certificate.id,
            listener_id=default_listener.id)
        ```

        ## Import

        NLB Listener Additional Certificate Attachment can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:nlb/listenerAdditionalCertificateAttachment:ListenerAdditionalCertificateAttachment example <listener_id>:<certificate_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] certificate_id: Certificate ID. Currently, only server certificates are supported.
        :param pulumi.Input[bool] dry_run: Whether to PreCheck only this request, value: - **true**: sends a check request and does not create a resource. Check items include whether required parameters, request format, and business restrictions have been filled in. If the check fails, the corresponding error is returned. If the check passes, the error code 'DryRunOperation' is returned '. - **false** (default): Sends a normal request, returns the HTTP 2xx status code after the check, and directly performs the operation.
        :param pulumi.Input[str] listener_id: The ID of the tcpssl listener.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ListenerAdditionalCertificateAttachmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a NLB Listener Additional Certificate Attachment resource.

        For information about NLB Listener Additional Certificate Attachment and how to use it, see [What is Listener Additional Certificate Attachment](https://www.alibabacloud.com/help/en/server-load-balancer/latest/nlb-instances-change).

        > **NOTE:** Available since v1.209.0.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "tf-example"
        default_resource_groups = alicloud.resourcemanager.get_resource_groups()
        default_zones = alicloud.nlb.get_zones()
        default_network = alicloud.vpc.Network("defaultNetwork",
            vpc_name=name,
            cidr_block="10.4.0.0/16")
        default_switch = alicloud.vpc.Switch("defaultSwitch",
            vswitch_name=name,
            cidr_block="10.4.0.0/24",
            vpc_id=default_network.id,
            zone_id=default_zones.zones[0].id)
        default1 = alicloud.vpc.Switch("default1",
            vswitch_name=name,
            cidr_block="10.4.1.0/24",
            vpc_id=default_network.id,
            zone_id=default_zones.zones[1].id)
        default_security_group = alicloud.ecs.SecurityGroup("defaultSecurityGroup", vpc_id=default_network.id)
        default_load_balancer = alicloud.nlb.LoadBalancer("defaultLoadBalancer",
            load_balancer_name=name,
            resource_group_id=default_resource_groups.ids[0],
            load_balancer_type="Network",
            address_type="Internet",
            address_ip_version="Ipv4",
            vpc_id=default_network.id,
            tags={
                "Created": "TF",
                "For": "example",
            },
            zone_mappings=[
                alicloud.nlb.LoadBalancerZoneMappingArgs(
                    vswitch_id=default_switch.id,
                    zone_id=default_zones.zones[0].id,
                ),
                alicloud.nlb.LoadBalancerZoneMappingArgs(
                    vswitch_id=default1.id,
                    zone_id=default_zones.zones[1].id,
                ),
            ])
        default_server_group = alicloud.nlb.ServerGroup("defaultServerGroup",
            resource_group_id=default_resource_groups.ids[0],
            server_group_name=name,
            server_group_type="Instance",
            vpc_id=default_network.id,
            scheduler="Wrr",
            protocol="TCPSSL",
            connection_drain=True,
            connection_drain_timeout=60,
            address_ip_version="Ipv4",
            health_check=alicloud.nlb.ServerGroupHealthCheckArgs(
                health_check_url="/adc/index.html",
                health_check_domain="tf-iac.com",
                health_check_enabled=True,
                health_check_type="TCP",
                health_check_connect_port=0,
                healthy_threshold=2,
                unhealthy_threshold=2,
                health_check_connect_timeout=5,
                health_check_interval=10,
                http_check_method="GET",
                health_check_http_codes=[
                    "http_2xx",
                    "http_3xx",
                    "http_4xx",
                ],
            ),
            tags={
                "Created": "TF",
                "For": "example",
            })
        default_listener = alicloud.nlb.Listener("defaultListener",
            listener_protocol="TCPSSL",
            listener_port=1883,
            security_policy_id="tls_cipher_policy_1_0",
            listener_description=name,
            load_balancer_id=default_load_balancer.id,
            server_group_id=default_server_group.id,
            idle_timeout=900,
            proxy_protocol_enabled=True,
            sec_sensor_enabled=True,
            alpn_enabled=True,
            alpn_policy="HTTP2Optional",
            cps=10000,
            mss=0)
        default_service_certificate = alicloud.cas.ServiceCertificate("defaultServiceCertificate",
            certificate_name=name,
            cert=\"\"\"-----BEGIN CERTIFICATE-----
        MIIDRjCCAq+gAwIBAgIJAJn3ox4K13PoMA0GCSqGSIb3DQEBBQUAMHYxCzAJBgNV
        BAYTAkNOMQswCQYDVQQIEwJCSjELMAkGA1UEBxMCQkoxDDAKBgNVBAoTA0FMSTEP
        MA0GA1UECxMGQUxJWVVOMQ0wCwYDVQQDEwR0ZXN0MR8wHQYJKoZIhvcNAQkBFhB0
        ZXN0QGhvdG1haWwuY29tMB4XDTE0MTEyNDA2MDQyNVoXDTI0MTEyMTA2MDQyNVow
        djELMAkGA1UEBhMCQ04xCzAJBgNVBAgTAkJKMQswCQYDVQQHEwJCSjEMMAoGA1UE
        ChMDQUxJMQ8wDQYDVQQLEwZBTElZVU4xDTALBgNVBAMTBHRlc3QxHzAdBgkqhkiG
        9w0BCQEWEHRlc3RAaG90bWFpbC5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJ
        AoGBAM7SS3e9+Nj0HKAsRuIDNSsS3UK6b+62YQb2uuhKrp1HMrOx61WSDR2qkAnB
        coG00Uz38EE+9DLYNUVQBK7aSgLP5M1Ak4wr4GqGyCgjejzzh3DshUzLCCy2rook
        KOyRTlPX+Q5l7rE1fcSNzgepcae5i2sE1XXXzLRIDIvQxcspAgMBAAGjgdswgdgw
        HQYDVR0OBBYEFBdy+OuMsvbkV7R14f0OyoLoh2z4MIGoBgNVHSMEgaAwgZ2AFBdy
        +OuMsvbkV7R14f0OyoLoh2z4oXqkeDB2MQswCQYDVQQGEwJDTjELMAkGA1UECBMC
        QkoxCzAJBgNVBAcTAkJKMQwwCgYDVQQKEwNBTEkxDzANBgNVBAsTBkFMSVlVTjEN
        MAsGA1UEAxMEdGVzdDEfMB0GCSqGSIb3DQEJARYQdGVzdEBob3RtYWlsLmNvbYIJ
        AJn3ox4K13PoMAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQEFBQADgYEAY7KOsnyT
        cQzfhiiG7ASjiPakw5wXoycHt5GCvLG5htp2TKVzgv9QTliA3gtfv6oV4zRZx7X1
        Ofi6hVgErtHaXJheuPVeW6eAW8mHBoEfvDAfU3y9waYrtUevSl07643bzKL6v+Qd
        DUBTxOAvSYfXTtI90EAxEG/bJJyOm5LqoiA=
        -----END CERTIFICATE-----
        \"\"\",
            key=\"\"\"-----BEGIN RSA PRIVATE KEY-----
        MIICXAIBAAKBgQDO0kt3vfjY9BygLEbiAzUrEt1Cum/utmEG9rroSq6dRzKzsetV
        kg0dqpAJwXKBtNFM9/BBPvQy2DVFUASu2koCz+TNQJOMK+BqhsgoI3o884dw7IVM
        ywgstq6KJCjskU5T1/kOZe6xNX3Ejc4HqXGnuYtrBNV118y0SAyL0MXLKQIDAQAB
        AoGAfe3NxbsGKhN42o4bGsKZPQDfeCHMxayGp5bTd10BtQIE/ST4BcJH+ihAS7Bd
        6FwQlKzivNd4GP1MckemklCXfsVckdL94e8ZbJl23GdWul3v8V+KndJHqv5zVJmP
        hwWoKimwIBTb2s0ctVryr2f18N4hhyFw1yGp0VxclGHkjgECQQD9CvllsnOwHpP4
        MdrDHbdb29QrobKyKW8pPcDd+sth+kP6Y8MnCVuAKXCKj5FeIsgVtfluPOsZjPzz
        71QQWS1dAkEA0T0KXO8gaBQwJhIoo/w6hy5JGZnrNSpOPp5xvJuMAafs2eyvmhJm
        Ev9SN/Pf2VYa1z6FEnBaLOVD6hf6YQIsPQJAX/CZPoW6dzwgvimo1/GcY6eleiWE
        qygqjWhsh71e/3bz7yuEAnj5yE3t7Zshcp+dXR3xxGo0eSuLfLFxHgGxwQJAAxf8
        9DzQ5NkPkTCJi0sqbl8/03IUKTgT6hcbpWdDXa7m8J3wRr3o5nUB+TPQ5nzAbthM
        zWX931YQeACcwhxvHQJBAN5mTzzJD4w4Ma6YTaNHyXakdYfyAWrOkPIWZxfhMfXe
        DrlNdiysTI4Dd1dLeErVpjsckAaOW/JDG5PCSwkaMxk=
        -----END RSA PRIVATE KEY-----
        \"\"\")
        default_listener_additional_certificate_attachment = alicloud.nlb.ListenerAdditionalCertificateAttachment("defaultListenerAdditionalCertificateAttachment",
            certificate_id=default_service_certificate.id,
            listener_id=default_listener.id)
        ```

        ## Import

        NLB Listener Additional Certificate Attachment can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:nlb/listenerAdditionalCertificateAttachment:ListenerAdditionalCertificateAttachment example <listener_id>:<certificate_id>
        ```

        :param str resource_name: The name of the resource.
        :param ListenerAdditionalCertificateAttachmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ListenerAdditionalCertificateAttachmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ListenerAdditionalCertificateAttachmentArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate_id: Optional[pulumi.Input[str]] = None,
                 dry_run: Optional[pulumi.Input[bool]] = None,
                 listener_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ListenerAdditionalCertificateAttachmentArgs.__new__(ListenerAdditionalCertificateAttachmentArgs)

            if certificate_id is None and not opts.urn:
                raise TypeError("Missing required property 'certificate_id'")
            __props__.__dict__["certificate_id"] = certificate_id
            __props__.__dict__["dry_run"] = dry_run
            if listener_id is None and not opts.urn:
                raise TypeError("Missing required property 'listener_id'")
            __props__.__dict__["listener_id"] = listener_id
            __props__.__dict__["status"] = None
        super(ListenerAdditionalCertificateAttachment, __self__).__init__(
            'alicloud:nlb/listenerAdditionalCertificateAttachment:ListenerAdditionalCertificateAttachment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            certificate_id: Optional[pulumi.Input[str]] = None,
            dry_run: Optional[pulumi.Input[bool]] = None,
            listener_id: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None) -> 'ListenerAdditionalCertificateAttachment':
        """
        Get an existing ListenerAdditionalCertificateAttachment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] certificate_id: Certificate ID. Currently, only server certificates are supported.
        :param pulumi.Input[bool] dry_run: Whether to PreCheck only this request, value: - **true**: sends a check request and does not create a resource. Check items include whether required parameters, request format, and business restrictions have been filled in. If the check fails, the corresponding error is returned. If the check passes, the error code 'DryRunOperation' is returned '. - **false** (default): Sends a normal request, returns the HTTP 2xx status code after the check, and directly performs the operation.
        :param pulumi.Input[str] listener_id: The ID of the tcpssl listener.
        :param pulumi.Input[str] status: The status of the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ListenerAdditionalCertificateAttachmentState.__new__(_ListenerAdditionalCertificateAttachmentState)

        __props__.__dict__["certificate_id"] = certificate_id
        __props__.__dict__["dry_run"] = dry_run
        __props__.__dict__["listener_id"] = listener_id
        __props__.__dict__["status"] = status
        return ListenerAdditionalCertificateAttachment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="certificateId")
    def certificate_id(self) -> pulumi.Output[str]:
        """
        Certificate ID. Currently, only server certificates are supported.
        """
        return pulumi.get(self, "certificate_id")

    @property
    @pulumi.getter(name="dryRun")
    def dry_run(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to PreCheck only this request, value: - **true**: sends a check request and does not create a resource. Check items include whether required parameters, request format, and business restrictions have been filled in. If the check fails, the corresponding error is returned. If the check passes, the error code 'DryRunOperation' is returned '. - **false** (default): Sends a normal request, returns the HTTP 2xx status code after the check, and directly performs the operation.
        """
        return pulumi.get(self, "dry_run")

    @property
    @pulumi.getter(name="listenerId")
    def listener_id(self) -> pulumi.Output[str]:
        """
        The ID of the tcpssl listener.
        """
        return pulumi.get(self, "listener_id")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the resource.
        """
        return pulumi.get(self, "status")

