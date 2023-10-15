# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

import types

__config__ = pulumi.Config('openstack')


class _ExportableConfig(types.ModuleType):
    @property
    def allow_reauth(self) -> Optional[bool]:
        """
        If set to `false`, OpenStack authorization won't be perfomed automatically, if the initial auth token get expired.
        Defaults to `true`
        """
        return __config__.get_bool('allowReauth') or _utilities.get_env_bool('OS_ALLOW_REAUTH')

    @property
    def application_credential_id(self) -> Optional[str]:
        """
        Application Credential ID to login with.
        """
        return __config__.get('applicationCredentialId')

    @property
    def application_credential_name(self) -> Optional[str]:
        """
        Application Credential name to login with.
        """
        return __config__.get('applicationCredentialName')

    @property
    def application_credential_secret(self) -> Optional[str]:
        """
        Application Credential secret to login with.
        """
        return __config__.get('applicationCredentialSecret')

    @property
    def auth_url(self) -> Optional[str]:
        """
        The Identity authentication URL.
        """
        return __config__.get('authUrl')

    @property
    def cacert_file(self) -> Optional[str]:
        """
        A Custom CA certificate.
        """
        return __config__.get('cacertFile')

    @property
    def cert(self) -> Optional[str]:
        """
        A client certificate to authenticate with.
        """
        return __config__.get('cert')

    @property
    def cloud(self) -> Optional[str]:
        """
        An entry in a `clouds.yaml` file to use.
        """
        return __config__.get('cloud') or _utilities.get_env('OS_CLOUD')

    @property
    def default_domain(self) -> Optional[str]:
        """
        The name of the Domain ID to scope to if no other domain is specified. Defaults to `default` (Identity v3).
        """
        return __config__.get('defaultDomain')

    @property
    def delayed_auth(self) -> Optional[bool]:
        """
        If set to `false`, OpenStack authorization will be perfomed, every time the service provider client is called. Defaults
        to `true`.
        """
        return __config__.get_bool('delayedAuth') or _utilities.get_env_bool('OS_DELAYED_AUTH')

    @property
    def disable_no_cache_header(self) -> Optional[bool]:
        """
        If set to `true`, the HTTP `Cache-Control: no-cache` header will not be added by default to all API requests.
        """
        return __config__.get_bool('disableNoCacheHeader')

    @property
    def domain_id(self) -> Optional[str]:
        """
        The ID of the Domain to scope to (Identity v3).
        """
        return __config__.get('domainId')

    @property
    def domain_name(self) -> Optional[str]:
        """
        The name of the Domain to scope to (Identity v3).
        """
        return __config__.get('domainName')

    @property
    def enable_logging(self) -> Optional[bool]:
        """
        Outputs very verbose logs with all calls made to and responses from OpenStack
        """
        return __config__.get_bool('enableLogging')

    @property
    def endpoint_overrides(self) -> Optional[str]:
        """
        A map of services with an endpoint to override what was from the Keystone catalog
        """
        return __config__.get('endpointOverrides')

    @property
    def endpoint_type(self) -> Optional[str]:
        return __config__.get('endpointType') or _utilities.get_env('OS_ENDPOINT_TYPE')

    @property
    def insecure(self) -> Optional[bool]:
        """
        Trust self-signed certificates.
        """
        return __config__.get_bool('insecure') or _utilities.get_env_bool('OS_INSECURE')

    @property
    def key(self) -> Optional[str]:
        """
        A client private key to authenticate with.
        """
        return __config__.get('key')

    @property
    def max_retries(self) -> Optional[int]:
        """
        How many times HTTP connection should be retried until giving up.
        """
        return __config__.get_int('maxRetries')

    @property
    def password(self) -> Optional[str]:
        """
        Password to login with.
        """
        return __config__.get('password')

    @property
    def project_domain_id(self) -> Optional[str]:
        """
        The ID of the domain where the proejct resides (Identity v3).
        """
        return __config__.get('projectDomainId')

    @property
    def project_domain_name(self) -> Optional[str]:
        """
        The name of the domain where the project resides (Identity v3).
        """
        return __config__.get('projectDomainName')

    @property
    def region(self) -> Optional[str]:
        """
        The OpenStack region to connect to.
        """
        return __config__.get('region') or _utilities.get_env('OS_REGION_NAME')

    @property
    def swauth(self) -> Optional[bool]:
        """
        Use Swift's authentication system instead of Keystone. Only used for interaction with Swift.
        """
        return __config__.get_bool('swauth') or _utilities.get_env_bool('OS_SWAUTH')

    @property
    def system_scope(self) -> Optional[bool]:
        """
        If set to `true`, system scoped authorization will be enabled. Defaults to `false` (Identity v3).
        """
        return __config__.get_bool('systemScope')

    @property
    def tenant_id(self) -> Optional[str]:
        """
        The ID of the Tenant (Identity v2) or Project (Identity v3) to login with.
        """
        return __config__.get('tenantId')

    @property
    def tenant_name(self) -> Optional[str]:
        """
        The name of the Tenant (Identity v2) or Project (Identity v3) to login with.
        """
        return __config__.get('tenantName')

    @property
    def token(self) -> Optional[str]:
        """
        Authentication token to use as an alternative to username/password.
        """
        return __config__.get('token')

    @property
    def use_octavia(self) -> Optional[bool]:
        """
        If set to `true`, API requests will go the Load Balancer service (Octavia) instead of the Networking service (Neutron).
        """
        return __config__.get_bool('useOctavia') or _utilities.get_env_bool('OS_USE_OCTAVIA')

    @property
    def user_domain_id(self) -> Optional[str]:
        """
        The ID of the domain where the user resides (Identity v3).
        """
        return __config__.get('userDomainId')

    @property
    def user_domain_name(self) -> Optional[str]:
        """
        The name of the domain where the user resides (Identity v3).
        """
        return __config__.get('userDomainName')

    @property
    def user_id(self) -> Optional[str]:
        """
        User ID to login with.
        """
        return __config__.get('userId')

    @property
    def user_name(self) -> Optional[str]:
        """
        Username to login with.
        """
        return __config__.get('userName')

