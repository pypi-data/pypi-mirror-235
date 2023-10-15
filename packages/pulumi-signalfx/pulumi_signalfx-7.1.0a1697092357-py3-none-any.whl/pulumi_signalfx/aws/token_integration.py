# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['TokenIntegrationArgs', 'TokenIntegration']

@pulumi.input_type
class TokenIntegrationArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a TokenIntegration resource.
        :param pulumi.Input[str] name: The name of this integration
        """
        TokenIntegrationArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if name is not None:
            _setter("name", name)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of this integration
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _TokenIntegrationState:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 signalfx_aws_account: Optional[pulumi.Input[str]] = None,
                 token_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering TokenIntegration resources.
        :param pulumi.Input[str] name: The name of this integration
        :param pulumi.Input[str] signalfx_aws_account: The AWS Account ARN to use with your policies/roles, provided by Splunk Observability.
        :param pulumi.Input[str] token_id: The SignalFx-generated AWS token to use with an AWS integration.
        """
        _TokenIntegrationState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            name=name,
            signalfx_aws_account=signalfx_aws_account,
            token_id=token_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             name: Optional[pulumi.Input[str]] = None,
             signalfx_aws_account: Optional[pulumi.Input[str]] = None,
             token_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if name is not None:
            _setter("name", name)
        if signalfx_aws_account is not None:
            _setter("signalfx_aws_account", signalfx_aws_account)
        if token_id is not None:
            _setter("token_id", token_id)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of this integration
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="signalfxAwsAccount")
    def signalfx_aws_account(self) -> Optional[pulumi.Input[str]]:
        """
        The AWS Account ARN to use with your policies/roles, provided by Splunk Observability.
        """
        return pulumi.get(self, "signalfx_aws_account")

    @signalfx_aws_account.setter
    def signalfx_aws_account(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "signalfx_aws_account", value)

    @property
    @pulumi.getter(name="tokenId")
    def token_id(self) -> Optional[pulumi.Input[str]]:
        """
        The SignalFx-generated AWS token to use with an AWS integration.
        """
        return pulumi.get(self, "token_id")

    @token_id.setter
    def token_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "token_id", value)


class TokenIntegration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Splunk Observability AWS CloudWatch integrations using security tokens. For help with this integration see [Connect to AWS CloudWatch](https://docs.signalfx.com/en/latest/integrations/amazon-web-services.html#connect-to-aws).

        > **NOTE** When managing integrations, use a session token of an administrator to authenticate the Splunk Observability provider. See [Operations that require a session token for an administrator](https://dev.splunk.com/observability/docs/administration/authtokens#Operations-that-require-a-session-token-for-an-administrator).

        > **WARNING** This resource implements a part of a workflow. You must use it with `aws.Integration`.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws
        import pulumi_signalfx as signalfx

        aws_myteam_token = signalfx.aws.TokenIntegration("awsMyteamToken")
        # Make yourself an AWS IAM role here
        aws_sfx_role = aws.iam.Role("awsSfxRole")
        # Stuff here that uses the external and account ID
        aws_myteam = signalfx.aws.Integration("awsMyteam",
            enabled=True,
            integration_id=aws_myteam_token.id,
            token="put_your_token_here",
            key="put_your_key_here",
            regions=["us-east-1"],
            poll_rate=300,
            import_cloud_watch=True,
            enable_aws_usage=True,
            custom_namespace_sync_rules=[signalfx.aws.IntegrationCustomNamespaceSyncRuleArgs(
                default_action="Exclude",
                filter_action="Include",
                filter_source="filter('code', '200')",
                namespace="my-custom-namespace",
            )],
            namespace_sync_rules=[signalfx.aws.IntegrationNamespaceSyncRuleArgs(
                default_action="Exclude",
                filter_action="Include",
                filter_source="filter('code', '200')",
                namespace="AWS/EC2",
            )])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of this integration
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[TokenIntegrationArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Splunk Observability AWS CloudWatch integrations using security tokens. For help with this integration see [Connect to AWS CloudWatch](https://docs.signalfx.com/en/latest/integrations/amazon-web-services.html#connect-to-aws).

        > **NOTE** When managing integrations, use a session token of an administrator to authenticate the Splunk Observability provider. See [Operations that require a session token for an administrator](https://dev.splunk.com/observability/docs/administration/authtokens#Operations-that-require-a-session-token-for-an-administrator).

        > **WARNING** This resource implements a part of a workflow. You must use it with `aws.Integration`.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws
        import pulumi_signalfx as signalfx

        aws_myteam_token = signalfx.aws.TokenIntegration("awsMyteamToken")
        # Make yourself an AWS IAM role here
        aws_sfx_role = aws.iam.Role("awsSfxRole")
        # Stuff here that uses the external and account ID
        aws_myteam = signalfx.aws.Integration("awsMyteam",
            enabled=True,
            integration_id=aws_myteam_token.id,
            token="put_your_token_here",
            key="put_your_key_here",
            regions=["us-east-1"],
            poll_rate=300,
            import_cloud_watch=True,
            enable_aws_usage=True,
            custom_namespace_sync_rules=[signalfx.aws.IntegrationCustomNamespaceSyncRuleArgs(
                default_action="Exclude",
                filter_action="Include",
                filter_source="filter('code', '200')",
                namespace="my-custom-namespace",
            )],
            namespace_sync_rules=[signalfx.aws.IntegrationNamespaceSyncRuleArgs(
                default_action="Exclude",
                filter_action="Include",
                filter_source="filter('code', '200')",
                namespace="AWS/EC2",
            )])
        ```

        :param str resource_name: The name of the resource.
        :param TokenIntegrationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TokenIntegrationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            TokenIntegrationArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TokenIntegrationArgs.__new__(TokenIntegrationArgs)

            __props__.__dict__["name"] = name
            __props__.__dict__["signalfx_aws_account"] = None
            __props__.__dict__["token_id"] = None
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["signalfxAwsAccount", "tokenId"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(TokenIntegration, __self__).__init__(
            'signalfx:aws/tokenIntegration:TokenIntegration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            name: Optional[pulumi.Input[str]] = None,
            signalfx_aws_account: Optional[pulumi.Input[str]] = None,
            token_id: Optional[pulumi.Input[str]] = None) -> 'TokenIntegration':
        """
        Get an existing TokenIntegration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of this integration
        :param pulumi.Input[str] signalfx_aws_account: The AWS Account ARN to use with your policies/roles, provided by Splunk Observability.
        :param pulumi.Input[str] token_id: The SignalFx-generated AWS token to use with an AWS integration.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TokenIntegrationState.__new__(_TokenIntegrationState)

        __props__.__dict__["name"] = name
        __props__.__dict__["signalfx_aws_account"] = signalfx_aws_account
        __props__.__dict__["token_id"] = token_id
        return TokenIntegration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of this integration
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="signalfxAwsAccount")
    def signalfx_aws_account(self) -> pulumi.Output[str]:
        """
        The AWS Account ARN to use with your policies/roles, provided by Splunk Observability.
        """
        return pulumi.get(self, "signalfx_aws_account")

    @property
    @pulumi.getter(name="tokenId")
    def token_id(self) -> pulumi.Output[str]:
        """
        The SignalFx-generated AWS token to use with an AWS integration.
        """
        return pulumi.get(self, "token_id")

