# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

import types

__config__ = pulumi.Config('keycloak')


class _ExportableConfig(types.ModuleType):
    @property
    def additional_headers(self) -> Optional[str]:
        return __config__.get('additionalHeaders')

    @property
    def base_path(self) -> Optional[str]:
        return __config__.get('basePath')

    @property
    def client_id(self) -> Optional[str]:
        return __config__.get('clientId')

    @property
    def client_secret(self) -> Optional[str]:
        return __config__.get('clientSecret')

    @property
    def client_timeout(self) -> int:
        """
        Timeout (in seconds) of the Keycloak client
        """
        return __config__.get_int('clientTimeout') or (_utilities.get_env_int('KEYCLOAK_CLIENT_TIMEOUT') or 5)

    @property
    def initial_login(self) -> Optional[bool]:
        """
        Whether or not to login to Keycloak instance on provider initialization
        """
        return __config__.get_bool('initialLogin')

    @property
    def password(self) -> Optional[str]:
        return __config__.get('password')

    @property
    def realm(self) -> Optional[str]:
        return __config__.get('realm')

    @property
    def red_hat_sso(self) -> Optional[bool]:
        """
        When true, the provider will treat the Keycloak instance as a Red Hat SSO server, specifically when parsing the version
        returned from the /serverinfo API endpoint.
        """
        return __config__.get_bool('redHatSso')

    @property
    def root_ca_certificate(self) -> Optional[str]:
        """
        Allows x509 calls using an unknown CA certificate (for development purposes)
        """
        return __config__.get('rootCaCertificate')

    @property
    def tls_insecure_skip_verify(self) -> Optional[bool]:
        """
        Allows ignoring insecure certificates when set to true. Defaults to false. Disabling security check is dangerous and
        should be avoided.
        """
        return __config__.get_bool('tlsInsecureSkipVerify')

    @property
    def url(self) -> Optional[str]:
        """
        The base URL of the Keycloak instance, before `/auth`
        """
        return __config__.get('url')

    @property
    def username(self) -> Optional[str]:
        return __config__.get('username')

