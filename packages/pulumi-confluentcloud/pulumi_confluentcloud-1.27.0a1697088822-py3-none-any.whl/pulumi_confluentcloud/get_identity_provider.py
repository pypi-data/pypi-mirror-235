# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetIdentityProviderResult',
    'AwaitableGetIdentityProviderResult',
    'get_identity_provider',
    'get_identity_provider_output',
]

@pulumi.output_type
class GetIdentityProviderResult:
    """
    A collection of values returned by getIdentityProvider.
    """
    def __init__(__self__, description=None, display_name=None, id=None, issuer=None, jwks_uri=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if issuer and not isinstance(issuer, str):
            raise TypeError("Expected argument 'issuer' to be a str")
        pulumi.set(__self__, "issuer", issuer)
        if jwks_uri and not isinstance(jwks_uri, str):
            raise TypeError("Expected argument 'jwks_uri' to be a str")
        pulumi.set(__self__, "jwks_uri", jwks_uri)

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        (Required String) A description for the Identity Provider.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        (Required String) A human-readable name for the Identity Provider.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        (Required String) The ID of the Identity Provider, for example, `op-abc123`.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def issuer(self) -> str:
        """
        (Required String) A publicly reachable issuer URI for the Identity Provider. The unique issuer URI string represents the entity for issuing tokens.
        """
        return pulumi.get(self, "issuer")

    @property
    @pulumi.getter(name="jwksUri")
    def jwks_uri(self) -> str:
        """
        (Required String) A publicly reachable JSON Web Key Set (JWKS) URI for the Identity Provider. A JSON Web Key Set (JWKS) provides a set of keys containing the public keys used to verify any JSON Web Token (JWT) issued by your OAuth 2.0 identity provider.
        """
        return pulumi.get(self, "jwks_uri")


class AwaitableGetIdentityProviderResult(GetIdentityProviderResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIdentityProviderResult(
            description=self.description,
            display_name=self.display_name,
            id=self.id,
            issuer=self.issuer,
            jwks_uri=self.jwks_uri)


def get_identity_provider(display_name: Optional[str] = None,
                          id: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIdentityProviderResult:
    """
    [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](https://docs.confluent.io/cloud/current/api.html#section/Versioning/API-Lifecycle-Policy)

    `IdentityProvider` describes an Identity Provider data source.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_confluentcloud as confluentcloud

    example_using_id_identity_provider = confluentcloud.get_identity_provider(id="op-abc123")
    pulumi.export("exampleUsingId", example_using_id_identity_provider)
    example_using_name_identity_provider = confluentcloud.get_identity_provider(display_name="My OIDC Provider: Azure AD")
    pulumi.export("exampleUsingName", example_using_name_identity_provider)
    ```


    :param str display_name: A human-readable name for the Identity Provider.
           
           > **Note:** Exactly one from the `id` and `display_name` attributes must be specified.
    :param str id: The ID of the Identity Provider, for example, `op-abc123`.
    """
    __args__ = dict()
    __args__['displayName'] = display_name
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('confluentcloud:index/getIdentityProvider:getIdentityProvider', __args__, opts=opts, typ=GetIdentityProviderResult).value

    return AwaitableGetIdentityProviderResult(
        description=pulumi.get(__ret__, 'description'),
        display_name=pulumi.get(__ret__, 'display_name'),
        id=pulumi.get(__ret__, 'id'),
        issuer=pulumi.get(__ret__, 'issuer'),
        jwks_uri=pulumi.get(__ret__, 'jwks_uri'))


@_utilities.lift_output_func(get_identity_provider)
def get_identity_provider_output(display_name: Optional[pulumi.Input[Optional[str]]] = None,
                                 id: Optional[pulumi.Input[Optional[str]]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIdentityProviderResult]:
    """
    [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](https://docs.confluent.io/cloud/current/api.html#section/Versioning/API-Lifecycle-Policy)

    `IdentityProvider` describes an Identity Provider data source.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_confluentcloud as confluentcloud

    example_using_id_identity_provider = confluentcloud.get_identity_provider(id="op-abc123")
    pulumi.export("exampleUsingId", example_using_id_identity_provider)
    example_using_name_identity_provider = confluentcloud.get_identity_provider(display_name="My OIDC Provider: Azure AD")
    pulumi.export("exampleUsingName", example_using_name_identity_provider)
    ```


    :param str display_name: A human-readable name for the Identity Provider.
           
           > **Note:** Exactly one from the `id` and `display_name` attributes must be specified.
    :param str id: The ID of the Identity Provider, for example, `op-abc123`.
    """
    ...
