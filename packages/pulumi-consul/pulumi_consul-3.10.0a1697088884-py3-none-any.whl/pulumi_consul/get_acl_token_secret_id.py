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
    'GetAclTokenSecretIdResult',
    'AwaitableGetAclTokenSecretIdResult',
    'get_acl_token_secret_id',
    'get_acl_token_secret_id_output',
]

@pulumi.output_type
class GetAclTokenSecretIdResult:
    """
    A collection of values returned by getAclTokenSecretId.
    """
    def __init__(__self__, accessor_id=None, encrypted_secret_id=None, id=None, namespace=None, partition=None, pgp_key=None, secret_id=None):
        if accessor_id and not isinstance(accessor_id, str):
            raise TypeError("Expected argument 'accessor_id' to be a str")
        pulumi.set(__self__, "accessor_id", accessor_id)
        if encrypted_secret_id and not isinstance(encrypted_secret_id, str):
            raise TypeError("Expected argument 'encrypted_secret_id' to be a str")
        pulumi.set(__self__, "encrypted_secret_id", encrypted_secret_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if namespace and not isinstance(namespace, str):
            raise TypeError("Expected argument 'namespace' to be a str")
        pulumi.set(__self__, "namespace", namespace)
        if partition and not isinstance(partition, str):
            raise TypeError("Expected argument 'partition' to be a str")
        pulumi.set(__self__, "partition", partition)
        if pgp_key and not isinstance(pgp_key, str):
            raise TypeError("Expected argument 'pgp_key' to be a str")
        pulumi.set(__self__, "pgp_key", pgp_key)
        if secret_id and not isinstance(secret_id, str):
            raise TypeError("Expected argument 'secret_id' to be a str")
        pulumi.set(__self__, "secret_id", secret_id)

    @property
    @pulumi.getter(name="accessorId")
    def accessor_id(self) -> str:
        return pulumi.get(self, "accessor_id")

    @property
    @pulumi.getter(name="encryptedSecretId")
    def encrypted_secret_id(self) -> str:
        return pulumi.get(self, "encrypted_secret_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def namespace(self) -> Optional[str]:
        return pulumi.get(self, "namespace")

    @property
    @pulumi.getter
    def partition(self) -> Optional[str]:
        return pulumi.get(self, "partition")

    @property
    @pulumi.getter(name="pgpKey")
    def pgp_key(self) -> Optional[str]:
        return pulumi.get(self, "pgp_key")

    @property
    @pulumi.getter(name="secretId")
    def secret_id(self) -> str:
        """
        The secret ID of the ACL token if `pgp_key` has not been set.
        """
        return pulumi.get(self, "secret_id")


class AwaitableGetAclTokenSecretIdResult(GetAclTokenSecretIdResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAclTokenSecretIdResult(
            accessor_id=self.accessor_id,
            encrypted_secret_id=self.encrypted_secret_id,
            id=self.id,
            namespace=self.namespace,
            partition=self.partition,
            pgp_key=self.pgp_key,
            secret_id=self.secret_id)


def get_acl_token_secret_id(accessor_id: Optional[str] = None,
                            namespace: Optional[str] = None,
                            partition: Optional[str] = None,
                            pgp_key: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAclTokenSecretIdResult:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_consul as consul

    test_acl_policy = consul.AclPolicy("testAclPolicy",
        rules="node \\"\\" { policy = \\"read\\" }",
        datacenters=["dc1"])
    test_acl_token = consul.AclToken("testAclToken",
        description="test",
        policies=[test_acl_policy.name],
        local=True)
    read = consul.get_acl_token_secret_id_output(accessor_id=test_acl_token.id,
        pgp_key="keybase:my_username")
    pulumi.export("consulAclTokenSecretId", read.encrypted_secret_id)
    ```


    :param str accessor_id: The accessor ID of the ACL token.
    :param str namespace: The namespace to lookup the token.
    :param str partition: The partition to lookup the token.
    """
    __args__ = dict()
    __args__['accessorId'] = accessor_id
    __args__['namespace'] = namespace
    __args__['partition'] = partition
    __args__['pgpKey'] = pgp_key
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('consul:index/getAclTokenSecretId:getAclTokenSecretId', __args__, opts=opts, typ=GetAclTokenSecretIdResult).value

    return AwaitableGetAclTokenSecretIdResult(
        accessor_id=pulumi.get(__ret__, 'accessor_id'),
        encrypted_secret_id=pulumi.get(__ret__, 'encrypted_secret_id'),
        id=pulumi.get(__ret__, 'id'),
        namespace=pulumi.get(__ret__, 'namespace'),
        partition=pulumi.get(__ret__, 'partition'),
        pgp_key=pulumi.get(__ret__, 'pgp_key'),
        secret_id=pulumi.get(__ret__, 'secret_id'))


@_utilities.lift_output_func(get_acl_token_secret_id)
def get_acl_token_secret_id_output(accessor_id: Optional[pulumi.Input[str]] = None,
                                   namespace: Optional[pulumi.Input[Optional[str]]] = None,
                                   partition: Optional[pulumi.Input[Optional[str]]] = None,
                                   pgp_key: Optional[pulumi.Input[Optional[str]]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAclTokenSecretIdResult]:
    """
    ## Example Usage

    ```python
    import pulumi
    import pulumi_consul as consul

    test_acl_policy = consul.AclPolicy("testAclPolicy",
        rules="node \\"\\" { policy = \\"read\\" }",
        datacenters=["dc1"])
    test_acl_token = consul.AclToken("testAclToken",
        description="test",
        policies=[test_acl_policy.name],
        local=True)
    read = consul.get_acl_token_secret_id_output(accessor_id=test_acl_token.id,
        pgp_key="keybase:my_username")
    pulumi.export("consulAclTokenSecretId", read.encrypted_secret_id)
    ```


    :param str accessor_id: The accessor ID of the ACL token.
    :param str namespace: The namespace to lookup the token.
    :param str partition: The partition to lookup the token.
    """
    ...
