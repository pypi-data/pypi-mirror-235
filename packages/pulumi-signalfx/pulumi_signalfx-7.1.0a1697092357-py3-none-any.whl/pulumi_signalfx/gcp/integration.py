# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['IntegrationArgs', 'Integration']

@pulumi.input_type
class IntegrationArgs:
    def __init__(__self__, *,
                 enabled: pulumi.Input[bool],
                 custom_metric_type_domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 import_gcp_metrics: Optional[pulumi.Input[bool]] = None,
                 include_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 named_token: Optional[pulumi.Input[str]] = None,
                 poll_rate: Optional[pulumi.Input[int]] = None,
                 project_service_keys: Optional[pulumi.Input[Sequence[pulumi.Input['IntegrationProjectServiceKeyArgs']]]] = None,
                 services: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 use_metric_source_project_for_quota: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Integration resource.
        :param pulumi.Input[bool] enabled: Whether the integration is enabled.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] custom_metric_type_domains: List of additional GCP service domain names that Splunk Observability Cloud will monitor. See [Custom Metric Type Domains documentation](https://dev.splunk.com/observability/docs/integrations/gcp_integration_overview/#Custom-metric-type-domains)
        :param pulumi.Input[bool] import_gcp_metrics: If enabled, Splunk Observability Cloud will sync also Google Cloud Monitoring data. If disabled, Splunk Observability Cloud will import only metadata. Defaults to true.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] include_lists: [Compute Metadata Include List](https://dev.splunk.com/observability/docs/integrations/gcp_integration_overview/).
        :param pulumi.Input[str] name: Name of the integration.
        :param pulumi.Input[str] named_token: Name of the org token to be used for data ingestion. If not specified then default access token is used.
        :param pulumi.Input[int] poll_rate: GCP integration poll rate (in seconds). Value between `60` and `600`. Default: `300`.
        :param pulumi.Input[Sequence[pulumi.Input['IntegrationProjectServiceKeyArgs']]] project_service_keys: GCP projects to add.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] services: GCP service metrics to import. Can be an empty list, or not included, to import 'All services'. See [Google Cloud Platform services](https://docs.splunk.com/Observability/gdi/get-data-in/integrations.html#google-cloud-platform-services) for a list of valid values.
        :param pulumi.Input[bool] use_metric_source_project_for_quota: When this value is set to true Observability Cloud will force usage of a quota from the project where metrics are stored. For this to work the service account provided for the project needs to be provided with serviceusage.services.use permission or Service Usage Consumer role in this project. When set to false default quota settings are used.
        """
        IntegrationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            enabled=enabled,
            custom_metric_type_domains=custom_metric_type_domains,
            import_gcp_metrics=import_gcp_metrics,
            include_lists=include_lists,
            name=name,
            named_token=named_token,
            poll_rate=poll_rate,
            project_service_keys=project_service_keys,
            services=services,
            use_metric_source_project_for_quota=use_metric_source_project_for_quota,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             enabled: pulumi.Input[bool],
             custom_metric_type_domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             import_gcp_metrics: Optional[pulumi.Input[bool]] = None,
             include_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             name: Optional[pulumi.Input[str]] = None,
             named_token: Optional[pulumi.Input[str]] = None,
             poll_rate: Optional[pulumi.Input[int]] = None,
             project_service_keys: Optional[pulumi.Input[Sequence[pulumi.Input['IntegrationProjectServiceKeyArgs']]]] = None,
             services: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             use_metric_source_project_for_quota: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("enabled", enabled)
        if custom_metric_type_domains is not None:
            _setter("custom_metric_type_domains", custom_metric_type_domains)
        if import_gcp_metrics is not None:
            _setter("import_gcp_metrics", import_gcp_metrics)
        if include_lists is not None:
            _setter("include_lists", include_lists)
        if name is not None:
            _setter("name", name)
        if named_token is not None:
            _setter("named_token", named_token)
        if poll_rate is not None:
            _setter("poll_rate", poll_rate)
        if project_service_keys is not None:
            _setter("project_service_keys", project_service_keys)
        if services is not None:
            _setter("services", services)
        if use_metric_source_project_for_quota is not None:
            _setter("use_metric_source_project_for_quota", use_metric_source_project_for_quota)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        Whether the integration is enabled.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="customMetricTypeDomains")
    def custom_metric_type_domains(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of additional GCP service domain names that Splunk Observability Cloud will monitor. See [Custom Metric Type Domains documentation](https://dev.splunk.com/observability/docs/integrations/gcp_integration_overview/#Custom-metric-type-domains)
        """
        return pulumi.get(self, "custom_metric_type_domains")

    @custom_metric_type_domains.setter
    def custom_metric_type_domains(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "custom_metric_type_domains", value)

    @property
    @pulumi.getter(name="importGcpMetrics")
    def import_gcp_metrics(self) -> Optional[pulumi.Input[bool]]:
        """
        If enabled, Splunk Observability Cloud will sync also Google Cloud Monitoring data. If disabled, Splunk Observability Cloud will import only metadata. Defaults to true.
        """
        return pulumi.get(self, "import_gcp_metrics")

    @import_gcp_metrics.setter
    def import_gcp_metrics(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "import_gcp_metrics", value)

    @property
    @pulumi.getter(name="includeLists")
    def include_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        [Compute Metadata Include List](https://dev.splunk.com/observability/docs/integrations/gcp_integration_overview/).
        """
        return pulumi.get(self, "include_lists")

    @include_lists.setter
    def include_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "include_lists", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the integration.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="namedToken")
    def named_token(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the org token to be used for data ingestion. If not specified then default access token is used.
        """
        return pulumi.get(self, "named_token")

    @named_token.setter
    def named_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "named_token", value)

    @property
    @pulumi.getter(name="pollRate")
    def poll_rate(self) -> Optional[pulumi.Input[int]]:
        """
        GCP integration poll rate (in seconds). Value between `60` and `600`. Default: `300`.
        """
        return pulumi.get(self, "poll_rate")

    @poll_rate.setter
    def poll_rate(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "poll_rate", value)

    @property
    @pulumi.getter(name="projectServiceKeys")
    def project_service_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['IntegrationProjectServiceKeyArgs']]]]:
        """
        GCP projects to add.
        """
        return pulumi.get(self, "project_service_keys")

    @project_service_keys.setter
    def project_service_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['IntegrationProjectServiceKeyArgs']]]]):
        pulumi.set(self, "project_service_keys", value)

    @property
    @pulumi.getter
    def services(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        GCP service metrics to import. Can be an empty list, or not included, to import 'All services'. See [Google Cloud Platform services](https://docs.splunk.com/Observability/gdi/get-data-in/integrations.html#google-cloud-platform-services) for a list of valid values.
        """
        return pulumi.get(self, "services")

    @services.setter
    def services(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "services", value)

    @property
    @pulumi.getter(name="useMetricSourceProjectForQuota")
    def use_metric_source_project_for_quota(self) -> Optional[pulumi.Input[bool]]:
        """
        When this value is set to true Observability Cloud will force usage of a quota from the project where metrics are stored. For this to work the service account provided for the project needs to be provided with serviceusage.services.use permission or Service Usage Consumer role in this project. When set to false default quota settings are used.
        """
        return pulumi.get(self, "use_metric_source_project_for_quota")

    @use_metric_source_project_for_quota.setter
    def use_metric_source_project_for_quota(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_metric_source_project_for_quota", value)


@pulumi.input_type
class _IntegrationState:
    def __init__(__self__, *,
                 custom_metric_type_domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 import_gcp_metrics: Optional[pulumi.Input[bool]] = None,
                 include_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 named_token: Optional[pulumi.Input[str]] = None,
                 poll_rate: Optional[pulumi.Input[int]] = None,
                 project_service_keys: Optional[pulumi.Input[Sequence[pulumi.Input['IntegrationProjectServiceKeyArgs']]]] = None,
                 services: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 use_metric_source_project_for_quota: Optional[pulumi.Input[bool]] = None):
        """
        Input properties used for looking up and filtering Integration resources.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] custom_metric_type_domains: List of additional GCP service domain names that Splunk Observability Cloud will monitor. See [Custom Metric Type Domains documentation](https://dev.splunk.com/observability/docs/integrations/gcp_integration_overview/#Custom-metric-type-domains)
        :param pulumi.Input[bool] enabled: Whether the integration is enabled.
        :param pulumi.Input[bool] import_gcp_metrics: If enabled, Splunk Observability Cloud will sync also Google Cloud Monitoring data. If disabled, Splunk Observability Cloud will import only metadata. Defaults to true.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] include_lists: [Compute Metadata Include List](https://dev.splunk.com/observability/docs/integrations/gcp_integration_overview/).
        :param pulumi.Input[str] name: Name of the integration.
        :param pulumi.Input[str] named_token: Name of the org token to be used for data ingestion. If not specified then default access token is used.
        :param pulumi.Input[int] poll_rate: GCP integration poll rate (in seconds). Value between `60` and `600`. Default: `300`.
        :param pulumi.Input[Sequence[pulumi.Input['IntegrationProjectServiceKeyArgs']]] project_service_keys: GCP projects to add.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] services: GCP service metrics to import. Can be an empty list, or not included, to import 'All services'. See [Google Cloud Platform services](https://docs.splunk.com/Observability/gdi/get-data-in/integrations.html#google-cloud-platform-services) for a list of valid values.
        :param pulumi.Input[bool] use_metric_source_project_for_quota: When this value is set to true Observability Cloud will force usage of a quota from the project where metrics are stored. For this to work the service account provided for the project needs to be provided with serviceusage.services.use permission or Service Usage Consumer role in this project. When set to false default quota settings are used.
        """
        _IntegrationState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            custom_metric_type_domains=custom_metric_type_domains,
            enabled=enabled,
            import_gcp_metrics=import_gcp_metrics,
            include_lists=include_lists,
            name=name,
            named_token=named_token,
            poll_rate=poll_rate,
            project_service_keys=project_service_keys,
            services=services,
            use_metric_source_project_for_quota=use_metric_source_project_for_quota,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             custom_metric_type_domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             enabled: Optional[pulumi.Input[bool]] = None,
             import_gcp_metrics: Optional[pulumi.Input[bool]] = None,
             include_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             name: Optional[pulumi.Input[str]] = None,
             named_token: Optional[pulumi.Input[str]] = None,
             poll_rate: Optional[pulumi.Input[int]] = None,
             project_service_keys: Optional[pulumi.Input[Sequence[pulumi.Input['IntegrationProjectServiceKeyArgs']]]] = None,
             services: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             use_metric_source_project_for_quota: Optional[pulumi.Input[bool]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if custom_metric_type_domains is not None:
            _setter("custom_metric_type_domains", custom_metric_type_domains)
        if enabled is not None:
            _setter("enabled", enabled)
        if import_gcp_metrics is not None:
            _setter("import_gcp_metrics", import_gcp_metrics)
        if include_lists is not None:
            _setter("include_lists", include_lists)
        if name is not None:
            _setter("name", name)
        if named_token is not None:
            _setter("named_token", named_token)
        if poll_rate is not None:
            _setter("poll_rate", poll_rate)
        if project_service_keys is not None:
            _setter("project_service_keys", project_service_keys)
        if services is not None:
            _setter("services", services)
        if use_metric_source_project_for_quota is not None:
            _setter("use_metric_source_project_for_quota", use_metric_source_project_for_quota)

    @property
    @pulumi.getter(name="customMetricTypeDomains")
    def custom_metric_type_domains(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of additional GCP service domain names that Splunk Observability Cloud will monitor. See [Custom Metric Type Domains documentation](https://dev.splunk.com/observability/docs/integrations/gcp_integration_overview/#Custom-metric-type-domains)
        """
        return pulumi.get(self, "custom_metric_type_domains")

    @custom_metric_type_domains.setter
    def custom_metric_type_domains(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "custom_metric_type_domains", value)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether the integration is enabled.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="importGcpMetrics")
    def import_gcp_metrics(self) -> Optional[pulumi.Input[bool]]:
        """
        If enabled, Splunk Observability Cloud will sync also Google Cloud Monitoring data. If disabled, Splunk Observability Cloud will import only metadata. Defaults to true.
        """
        return pulumi.get(self, "import_gcp_metrics")

    @import_gcp_metrics.setter
    def import_gcp_metrics(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "import_gcp_metrics", value)

    @property
    @pulumi.getter(name="includeLists")
    def include_lists(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        [Compute Metadata Include List](https://dev.splunk.com/observability/docs/integrations/gcp_integration_overview/).
        """
        return pulumi.get(self, "include_lists")

    @include_lists.setter
    def include_lists(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "include_lists", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the integration.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="namedToken")
    def named_token(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the org token to be used for data ingestion. If not specified then default access token is used.
        """
        return pulumi.get(self, "named_token")

    @named_token.setter
    def named_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "named_token", value)

    @property
    @pulumi.getter(name="pollRate")
    def poll_rate(self) -> Optional[pulumi.Input[int]]:
        """
        GCP integration poll rate (in seconds). Value between `60` and `600`. Default: `300`.
        """
        return pulumi.get(self, "poll_rate")

    @poll_rate.setter
    def poll_rate(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "poll_rate", value)

    @property
    @pulumi.getter(name="projectServiceKeys")
    def project_service_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['IntegrationProjectServiceKeyArgs']]]]:
        """
        GCP projects to add.
        """
        return pulumi.get(self, "project_service_keys")

    @project_service_keys.setter
    def project_service_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['IntegrationProjectServiceKeyArgs']]]]):
        pulumi.set(self, "project_service_keys", value)

    @property
    @pulumi.getter
    def services(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        GCP service metrics to import. Can be an empty list, or not included, to import 'All services'. See [Google Cloud Platform services](https://docs.splunk.com/Observability/gdi/get-data-in/integrations.html#google-cloud-platform-services) for a list of valid values.
        """
        return pulumi.get(self, "services")

    @services.setter
    def services(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "services", value)

    @property
    @pulumi.getter(name="useMetricSourceProjectForQuota")
    def use_metric_source_project_for_quota(self) -> Optional[pulumi.Input[bool]]:
        """
        When this value is set to true Observability Cloud will force usage of a quota from the project where metrics are stored. For this to work the service account provided for the project needs to be provided with serviceusage.services.use permission or Service Usage Consumer role in this project. When set to false default quota settings are used.
        """
        return pulumi.get(self, "use_metric_source_project_for_quota")

    @use_metric_source_project_for_quota.setter
    def use_metric_source_project_for_quota(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_metric_source_project_for_quota", value)


class Integration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_metric_type_domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 import_gcp_metrics: Optional[pulumi.Input[bool]] = None,
                 include_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 named_token: Optional[pulumi.Input[str]] = None,
                 poll_rate: Optional[pulumi.Input[int]] = None,
                 project_service_keys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IntegrationProjectServiceKeyArgs']]]]] = None,
                 services: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 use_metric_source_project_for_quota: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        SignalFx GCP Integration

        > **NOTE** When managing integrations, use a session token of an administrator to authenticate the SignalFx provider. See [Operations that require a session token for an administrator](https://dev.splunk.com/observability/docs/administration/authtokens#Operations-that-require-a-session-token-for-an-administrator). Otherwise you'll receive a 4xx error.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_signalfx as signalfx

        gcp_myteam = signalfx.gcp.Integration("gcpMyteam",
            custom_metric_type_domains=["istio.io"],
            enabled=True,
            import_gcp_metrics=True,
            poll_rate=300,
            project_service_keys=[
                signalfx.gcp.IntegrationProjectServiceKeyArgs(
                    project_id="gcp_project_id_1",
                    project_key=(lambda path: open(path).read())("/path/to/gcp_credentials_1.json"),
                ),
                signalfx.gcp.IntegrationProjectServiceKeyArgs(
                    project_id="gcp_project_id_2",
                    project_key=(lambda path: open(path).read())("/path/to/gcp_credentials_2.json"),
                ),
            ],
            services=["compute"])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] custom_metric_type_domains: List of additional GCP service domain names that Splunk Observability Cloud will monitor. See [Custom Metric Type Domains documentation](https://dev.splunk.com/observability/docs/integrations/gcp_integration_overview/#Custom-metric-type-domains)
        :param pulumi.Input[bool] enabled: Whether the integration is enabled.
        :param pulumi.Input[bool] import_gcp_metrics: If enabled, Splunk Observability Cloud will sync also Google Cloud Monitoring data. If disabled, Splunk Observability Cloud will import only metadata. Defaults to true.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] include_lists: [Compute Metadata Include List](https://dev.splunk.com/observability/docs/integrations/gcp_integration_overview/).
        :param pulumi.Input[str] name: Name of the integration.
        :param pulumi.Input[str] named_token: Name of the org token to be used for data ingestion. If not specified then default access token is used.
        :param pulumi.Input[int] poll_rate: GCP integration poll rate (in seconds). Value between `60` and `600`. Default: `300`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IntegrationProjectServiceKeyArgs']]]] project_service_keys: GCP projects to add.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] services: GCP service metrics to import. Can be an empty list, or not included, to import 'All services'. See [Google Cloud Platform services](https://docs.splunk.com/Observability/gdi/get-data-in/integrations.html#google-cloud-platform-services) for a list of valid values.
        :param pulumi.Input[bool] use_metric_source_project_for_quota: When this value is set to true Observability Cloud will force usage of a quota from the project where metrics are stored. For this to work the service account provided for the project needs to be provided with serviceusage.services.use permission or Service Usage Consumer role in this project. When set to false default quota settings are used.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IntegrationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        SignalFx GCP Integration

        > **NOTE** When managing integrations, use a session token of an administrator to authenticate the SignalFx provider. See [Operations that require a session token for an administrator](https://dev.splunk.com/observability/docs/administration/authtokens#Operations-that-require-a-session-token-for-an-administrator). Otherwise you'll receive a 4xx error.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_signalfx as signalfx

        gcp_myteam = signalfx.gcp.Integration("gcpMyteam",
            custom_metric_type_domains=["istio.io"],
            enabled=True,
            import_gcp_metrics=True,
            poll_rate=300,
            project_service_keys=[
                signalfx.gcp.IntegrationProjectServiceKeyArgs(
                    project_id="gcp_project_id_1",
                    project_key=(lambda path: open(path).read())("/path/to/gcp_credentials_1.json"),
                ),
                signalfx.gcp.IntegrationProjectServiceKeyArgs(
                    project_id="gcp_project_id_2",
                    project_key=(lambda path: open(path).read())("/path/to/gcp_credentials_2.json"),
                ),
            ],
            services=["compute"])
        ```

        :param str resource_name: The name of the resource.
        :param IntegrationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IntegrationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            IntegrationArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_metric_type_domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 import_gcp_metrics: Optional[pulumi.Input[bool]] = None,
                 include_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 named_token: Optional[pulumi.Input[str]] = None,
                 poll_rate: Optional[pulumi.Input[int]] = None,
                 project_service_keys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IntegrationProjectServiceKeyArgs']]]]] = None,
                 services: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 use_metric_source_project_for_quota: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IntegrationArgs.__new__(IntegrationArgs)

            __props__.__dict__["custom_metric_type_domains"] = custom_metric_type_domains
            if enabled is None and not opts.urn:
                raise TypeError("Missing required property 'enabled'")
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["import_gcp_metrics"] = import_gcp_metrics
            __props__.__dict__["include_lists"] = include_lists
            __props__.__dict__["name"] = name
            __props__.__dict__["named_token"] = named_token
            __props__.__dict__["poll_rate"] = poll_rate
            __props__.__dict__["project_service_keys"] = None if project_service_keys is None else pulumi.Output.secret(project_service_keys)
            __props__.__dict__["services"] = services
            __props__.__dict__["use_metric_source_project_for_quota"] = use_metric_source_project_for_quota
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["projectServiceKeys"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Integration, __self__).__init__(
            'signalfx:gcp/integration:Integration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            custom_metric_type_domains: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            import_gcp_metrics: Optional[pulumi.Input[bool]] = None,
            include_lists: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            named_token: Optional[pulumi.Input[str]] = None,
            poll_rate: Optional[pulumi.Input[int]] = None,
            project_service_keys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IntegrationProjectServiceKeyArgs']]]]] = None,
            services: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            use_metric_source_project_for_quota: Optional[pulumi.Input[bool]] = None) -> 'Integration':
        """
        Get an existing Integration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] custom_metric_type_domains: List of additional GCP service domain names that Splunk Observability Cloud will monitor. See [Custom Metric Type Domains documentation](https://dev.splunk.com/observability/docs/integrations/gcp_integration_overview/#Custom-metric-type-domains)
        :param pulumi.Input[bool] enabled: Whether the integration is enabled.
        :param pulumi.Input[bool] import_gcp_metrics: If enabled, Splunk Observability Cloud will sync also Google Cloud Monitoring data. If disabled, Splunk Observability Cloud will import only metadata. Defaults to true.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] include_lists: [Compute Metadata Include List](https://dev.splunk.com/observability/docs/integrations/gcp_integration_overview/).
        :param pulumi.Input[str] name: Name of the integration.
        :param pulumi.Input[str] named_token: Name of the org token to be used for data ingestion. If not specified then default access token is used.
        :param pulumi.Input[int] poll_rate: GCP integration poll rate (in seconds). Value between `60` and `600`. Default: `300`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IntegrationProjectServiceKeyArgs']]]] project_service_keys: GCP projects to add.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] services: GCP service metrics to import. Can be an empty list, or not included, to import 'All services'. See [Google Cloud Platform services](https://docs.splunk.com/Observability/gdi/get-data-in/integrations.html#google-cloud-platform-services) for a list of valid values.
        :param pulumi.Input[bool] use_metric_source_project_for_quota: When this value is set to true Observability Cloud will force usage of a quota from the project where metrics are stored. For this to work the service account provided for the project needs to be provided with serviceusage.services.use permission or Service Usage Consumer role in this project. When set to false default quota settings are used.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IntegrationState.__new__(_IntegrationState)

        __props__.__dict__["custom_metric_type_domains"] = custom_metric_type_domains
        __props__.__dict__["enabled"] = enabled
        __props__.__dict__["import_gcp_metrics"] = import_gcp_metrics
        __props__.__dict__["include_lists"] = include_lists
        __props__.__dict__["name"] = name
        __props__.__dict__["named_token"] = named_token
        __props__.__dict__["poll_rate"] = poll_rate
        __props__.__dict__["project_service_keys"] = project_service_keys
        __props__.__dict__["services"] = services
        __props__.__dict__["use_metric_source_project_for_quota"] = use_metric_source_project_for_quota
        return Integration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="customMetricTypeDomains")
    def custom_metric_type_domains(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of additional GCP service domain names that Splunk Observability Cloud will monitor. See [Custom Metric Type Domains documentation](https://dev.splunk.com/observability/docs/integrations/gcp_integration_overview/#Custom-metric-type-domains)
        """
        return pulumi.get(self, "custom_metric_type_domains")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[bool]:
        """
        Whether the integration is enabled.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="importGcpMetrics")
    def import_gcp_metrics(self) -> pulumi.Output[Optional[bool]]:
        """
        If enabled, Splunk Observability Cloud will sync also Google Cloud Monitoring data. If disabled, Splunk Observability Cloud will import only metadata. Defaults to true.
        """
        return pulumi.get(self, "import_gcp_metrics")

    @property
    @pulumi.getter(name="includeLists")
    def include_lists(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        [Compute Metadata Include List](https://dev.splunk.com/observability/docs/integrations/gcp_integration_overview/).
        """
        return pulumi.get(self, "include_lists")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the integration.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="namedToken")
    def named_token(self) -> pulumi.Output[Optional[str]]:
        """
        Name of the org token to be used for data ingestion. If not specified then default access token is used.
        """
        return pulumi.get(self, "named_token")

    @property
    @pulumi.getter(name="pollRate")
    def poll_rate(self) -> pulumi.Output[Optional[int]]:
        """
        GCP integration poll rate (in seconds). Value between `60` and `600`. Default: `300`.
        """
        return pulumi.get(self, "poll_rate")

    @property
    @pulumi.getter(name="projectServiceKeys")
    def project_service_keys(self) -> pulumi.Output[Optional[Sequence['outputs.IntegrationProjectServiceKey']]]:
        """
        GCP projects to add.
        """
        return pulumi.get(self, "project_service_keys")

    @property
    @pulumi.getter
    def services(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        GCP service metrics to import. Can be an empty list, or not included, to import 'All services'. See [Google Cloud Platform services](https://docs.splunk.com/Observability/gdi/get-data-in/integrations.html#google-cloud-platform-services) for a list of valid values.
        """
        return pulumi.get(self, "services")

    @property
    @pulumi.getter(name="useMetricSourceProjectForQuota")
    def use_metric_source_project_for_quota(self) -> pulumi.Output[Optional[bool]]:
        """
        When this value is set to true Observability Cloud will force usage of a quota from the project where metrics are stored. For this to work the service account provided for the project needs to be provided with serviceusage.services.use permission or Service Usage Consumer role in this project. When set to false default quota settings are used.
        """
        return pulumi.get(self, "use_metric_source_project_for_quota")

