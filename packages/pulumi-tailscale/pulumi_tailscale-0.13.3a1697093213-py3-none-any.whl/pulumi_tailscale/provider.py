# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ProviderArgs', 'Provider']

@pulumi.input_type
class ProviderArgs:
    def __init__(__self__, *,
                 api_key: Optional[pulumi.Input[str]] = None,
                 base_url: Optional[pulumi.Input[str]] = None,
                 oauth_client_id: Optional[pulumi.Input[str]] = None,
                 oauth_client_secret: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tailnet: Optional[pulumi.Input[str]] = None,
                 user_agent: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Provider resource.
        :param pulumi.Input[str] api_key: The API key to use for authenticating requests to the API. Can be set via the TAILSCALE_API_KEY environment variable.
               Conflicts with 'oauth_client_id' and 'oauth_client_secret'.
        :param pulumi.Input[str] base_url: The base URL of the Tailscale API. Defaults to https://api.tailscale.com. Can be set via the TAILSCALE_BASE_URL
               environment variable.
        :param pulumi.Input[str] oauth_client_id: The OAuth application's ID when using OAuth client credentials. Can be set via the TAILSCALE_OAUTH_CLIENT_ID environment
               variable. Both 'oauth_client_id' and 'oauth_client_secret' must be set. Conflicts with 'api_key'.
        :param pulumi.Input[str] oauth_client_secret: The OAuth application's secret when using OAuth client credentials. Can be set via the TAILSCALE_OAUTH_CLIENT_SECRET
               environment variable. Both 'oauth_client_id' and 'oauth_client_secret' must be set. Conflicts with 'api_key'.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: The OAuth 2.0 scopes to request when for the access token generated using the supplied OAuth client credentials. See
               https://tailscale.com/kb/1215/oauth-clients/#scopes for available scopes. Only valid when both 'oauth_client_id' and
               'oauth_client_secret' are set.
        :param pulumi.Input[str] tailnet: The organization name of the Tailnet in which to perform actions. Can be set via the TAILSCALE_TAILNET environment
               variable. Default is the tailnet that owns API credentials passed to the provider.
        :param pulumi.Input[str] user_agent: User-Agent header for API requests.
        """
        ProviderArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            api_key=api_key,
            base_url=base_url,
            oauth_client_id=oauth_client_id,
            oauth_client_secret=oauth_client_secret,
            scopes=scopes,
            tailnet=tailnet,
            user_agent=user_agent,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             api_key: Optional[pulumi.Input[str]] = None,
             base_url: Optional[pulumi.Input[str]] = None,
             oauth_client_id: Optional[pulumi.Input[str]] = None,
             oauth_client_secret: Optional[pulumi.Input[str]] = None,
             scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             tailnet: Optional[pulumi.Input[str]] = None,
             user_agent: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if api_key is not None:
            _setter("api_key", api_key)
        if base_url is not None:
            _setter("base_url", base_url)
        if oauth_client_id is not None:
            _setter("oauth_client_id", oauth_client_id)
        if oauth_client_secret is not None:
            _setter("oauth_client_secret", oauth_client_secret)
        if scopes is not None:
            _setter("scopes", scopes)
        if tailnet is not None:
            _setter("tailnet", tailnet)
        if user_agent is not None:
            _setter("user_agent", user_agent)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[pulumi.Input[str]]:
        """
        The API key to use for authenticating requests to the API. Can be set via the TAILSCALE_API_KEY environment variable.
        Conflicts with 'oauth_client_id' and 'oauth_client_secret'.
        """
        return pulumi.get(self, "api_key")

    @api_key.setter
    def api_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_key", value)

    @property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> Optional[pulumi.Input[str]]:
        """
        The base URL of the Tailscale API. Defaults to https://api.tailscale.com. Can be set via the TAILSCALE_BASE_URL
        environment variable.
        """
        return pulumi.get(self, "base_url")

    @base_url.setter
    def base_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "base_url", value)

    @property
    @pulumi.getter(name="oauthClientId")
    def oauth_client_id(self) -> Optional[pulumi.Input[str]]:
        """
        The OAuth application's ID when using OAuth client credentials. Can be set via the TAILSCALE_OAUTH_CLIENT_ID environment
        variable. Both 'oauth_client_id' and 'oauth_client_secret' must be set. Conflicts with 'api_key'.
        """
        return pulumi.get(self, "oauth_client_id")

    @oauth_client_id.setter
    def oauth_client_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oauth_client_id", value)

    @property
    @pulumi.getter(name="oauthClientSecret")
    def oauth_client_secret(self) -> Optional[pulumi.Input[str]]:
        """
        The OAuth application's secret when using OAuth client credentials. Can be set via the TAILSCALE_OAUTH_CLIENT_SECRET
        environment variable. Both 'oauth_client_id' and 'oauth_client_secret' must be set. Conflicts with 'api_key'.
        """
        return pulumi.get(self, "oauth_client_secret")

    @oauth_client_secret.setter
    def oauth_client_secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "oauth_client_secret", value)

    @property
    @pulumi.getter
    def scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The OAuth 2.0 scopes to request when for the access token generated using the supplied OAuth client credentials. See
        https://tailscale.com/kb/1215/oauth-clients/#scopes for available scopes. Only valid when both 'oauth_client_id' and
        'oauth_client_secret' are set.
        """
        return pulumi.get(self, "scopes")

    @scopes.setter
    def scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "scopes", value)

    @property
    @pulumi.getter
    def tailnet(self) -> Optional[pulumi.Input[str]]:
        """
        The organization name of the Tailnet in which to perform actions. Can be set via the TAILSCALE_TAILNET environment
        variable. Default is the tailnet that owns API credentials passed to the provider.
        """
        return pulumi.get(self, "tailnet")

    @tailnet.setter
    def tailnet(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tailnet", value)

    @property
    @pulumi.getter(name="userAgent")
    def user_agent(self) -> Optional[pulumi.Input[str]]:
        """
        User-Agent header for API requests.
        """
        return pulumi.get(self, "user_agent")

    @user_agent.setter
    def user_agent(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_agent", value)


class Provider(pulumi.ProviderResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 base_url: Optional[pulumi.Input[str]] = None,
                 oauth_client_id: Optional[pulumi.Input[str]] = None,
                 oauth_client_secret: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tailnet: Optional[pulumi.Input[str]] = None,
                 user_agent: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The provider type for the tailscale package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_key: The API key to use for authenticating requests to the API. Can be set via the TAILSCALE_API_KEY environment variable.
               Conflicts with 'oauth_client_id' and 'oauth_client_secret'.
        :param pulumi.Input[str] base_url: The base URL of the Tailscale API. Defaults to https://api.tailscale.com. Can be set via the TAILSCALE_BASE_URL
               environment variable.
        :param pulumi.Input[str] oauth_client_id: The OAuth application's ID when using OAuth client credentials. Can be set via the TAILSCALE_OAUTH_CLIENT_ID environment
               variable. Both 'oauth_client_id' and 'oauth_client_secret' must be set. Conflicts with 'api_key'.
        :param pulumi.Input[str] oauth_client_secret: The OAuth application's secret when using OAuth client credentials. Can be set via the TAILSCALE_OAUTH_CLIENT_SECRET
               environment variable. Both 'oauth_client_id' and 'oauth_client_secret' must be set. Conflicts with 'api_key'.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: The OAuth 2.0 scopes to request when for the access token generated using the supplied OAuth client credentials. See
               https://tailscale.com/kb/1215/oauth-clients/#scopes for available scopes. Only valid when both 'oauth_client_id' and
               'oauth_client_secret' are set.
        :param pulumi.Input[str] tailnet: The organization name of the Tailnet in which to perform actions. Can be set via the TAILSCALE_TAILNET environment
               variable. Default is the tailnet that owns API credentials passed to the provider.
        :param pulumi.Input[str] user_agent: User-Agent header for API requests.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ProviderArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The provider type for the tailscale package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param ProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            ProviderArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_key: Optional[pulumi.Input[str]] = None,
                 base_url: Optional[pulumi.Input[str]] = None,
                 oauth_client_id: Optional[pulumi.Input[str]] = None,
                 oauth_client_secret: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tailnet: Optional[pulumi.Input[str]] = None,
                 user_agent: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProviderArgs.__new__(ProviderArgs)

            __props__.__dict__["api_key"] = None if api_key is None else pulumi.Output.secret(api_key)
            __props__.__dict__["base_url"] = base_url
            __props__.__dict__["oauth_client_id"] = oauth_client_id
            __props__.__dict__["oauth_client_secret"] = None if oauth_client_secret is None else pulumi.Output.secret(oauth_client_secret)
            __props__.__dict__["scopes"] = pulumi.Output.from_input(scopes).apply(pulumi.runtime.to_json) if scopes is not None else None
            __props__.__dict__["tailnet"] = tailnet
            __props__.__dict__["user_agent"] = user_agent
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["apiKey", "oauthClientSecret"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Provider, __self__).__init__(
            'tailscale',
            resource_name,
            __props__,
            opts)

    @property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> pulumi.Output[Optional[str]]:
        """
        The API key to use for authenticating requests to the API. Can be set via the TAILSCALE_API_KEY environment variable.
        Conflicts with 'oauth_client_id' and 'oauth_client_secret'.
        """
        return pulumi.get(self, "api_key")

    @property
    @pulumi.getter(name="baseUrl")
    def base_url(self) -> pulumi.Output[Optional[str]]:
        """
        The base URL of the Tailscale API. Defaults to https://api.tailscale.com. Can be set via the TAILSCALE_BASE_URL
        environment variable.
        """
        return pulumi.get(self, "base_url")

    @property
    @pulumi.getter(name="oauthClientId")
    def oauth_client_id(self) -> pulumi.Output[Optional[str]]:
        """
        The OAuth application's ID when using OAuth client credentials. Can be set via the TAILSCALE_OAUTH_CLIENT_ID environment
        variable. Both 'oauth_client_id' and 'oauth_client_secret' must be set. Conflicts with 'api_key'.
        """
        return pulumi.get(self, "oauth_client_id")

    @property
    @pulumi.getter(name="oauthClientSecret")
    def oauth_client_secret(self) -> pulumi.Output[Optional[str]]:
        """
        The OAuth application's secret when using OAuth client credentials. Can be set via the TAILSCALE_OAUTH_CLIENT_SECRET
        environment variable. Both 'oauth_client_id' and 'oauth_client_secret' must be set. Conflicts with 'api_key'.
        """
        return pulumi.get(self, "oauth_client_secret")

    @property
    @pulumi.getter
    def tailnet(self) -> pulumi.Output[Optional[str]]:
        """
        The organization name of the Tailnet in which to perform actions. Can be set via the TAILSCALE_TAILNET environment
        variable. Default is the tailnet that owns API credentials passed to the provider.
        """
        return pulumi.get(self, "tailnet")

    @property
    @pulumi.getter(name="userAgent")
    def user_agent(self) -> pulumi.Output[Optional[str]]:
        """
        User-Agent header for API requests.
        """
        return pulumi.get(self, "user_agent")

