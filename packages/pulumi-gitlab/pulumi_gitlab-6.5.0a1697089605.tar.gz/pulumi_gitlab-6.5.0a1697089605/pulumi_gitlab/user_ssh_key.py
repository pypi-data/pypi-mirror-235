# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['UserSshKeyArgs', 'UserSshKey']

@pulumi.input_type
class UserSshKeyArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 title: pulumi.Input[str],
                 user_id: pulumi.Input[int],
                 expires_at: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a UserSshKey resource.
        :param pulumi.Input[str] key: The ssh key. The SSH key `comment` (trailing part) is optional and ignored for diffing, because GitLab overrides it with the username and GitLab hostname.
        :param pulumi.Input[str] title: The title of the ssh key.
        :param pulumi.Input[int] user_id: The ID or username of the user.
        :param pulumi.Input[str] expires_at: The expiration date of the SSH key in ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ)
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "title", title)
        pulumi.set(__self__, "user_id", user_id)
        if expires_at is not None:
            pulumi.set(__self__, "expires_at", expires_at)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The ssh key. The SSH key `comment` (trailing part) is optional and ignored for diffing, because GitLab overrides it with the username and GitLab hostname.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        """
        The title of the ssh key.
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Input[int]:
        """
        The ID or username of the user.
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: pulumi.Input[int]):
        pulumi.set(self, "user_id", value)

    @property
    @pulumi.getter(name="expiresAt")
    def expires_at(self) -> Optional[pulumi.Input[str]]:
        """
        The expiration date of the SSH key in ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ)
        """
        return pulumi.get(self, "expires_at")

    @expires_at.setter
    def expires_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expires_at", value)


@pulumi.input_type
class _UserSshKeyState:
    def __init__(__self__, *,
                 created_at: Optional[pulumi.Input[str]] = None,
                 expires_at: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 key_id: Optional[pulumi.Input[int]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering UserSshKey resources.
        :param pulumi.Input[str] created_at: The time when this key was created in GitLab.
        :param pulumi.Input[str] expires_at: The expiration date of the SSH key in ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ)
        :param pulumi.Input[str] key: The ssh key. The SSH key `comment` (trailing part) is optional and ignored for diffing, because GitLab overrides it with the username and GitLab hostname.
        :param pulumi.Input[int] key_id: The ID of the ssh key.
        :param pulumi.Input[str] title: The title of the ssh key.
        :param pulumi.Input[int] user_id: The ID or username of the user.
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if expires_at is not None:
            pulumi.set(__self__, "expires_at", expires_at)
        if key is not None:
            pulumi.set(__self__, "key", key)
        if key_id is not None:
            pulumi.set(__self__, "key_id", key_id)
        if title is not None:
            pulumi.set(__self__, "title", title)
        if user_id is not None:
            pulumi.set(__self__, "user_id", user_id)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        The time when this key was created in GitLab.
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter(name="expiresAt")
    def expires_at(self) -> Optional[pulumi.Input[str]]:
        """
        The expiration date of the SSH key in ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ)
        """
        return pulumi.get(self, "expires_at")

    @expires_at.setter
    def expires_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expires_at", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        The ssh key. The SSH key `comment` (trailing part) is optional and ignored for diffing, because GitLab overrides it with the username and GitLab hostname.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter(name="keyId")
    def key_id(self) -> Optional[pulumi.Input[int]]:
        """
        The ID of the ssh key.
        """
        return pulumi.get(self, "key_id")

    @key_id.setter
    def key_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "key_id", value)

    @property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[str]]:
        """
        The title of the ssh key.
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> Optional[pulumi.Input[int]]:
        """
        The ID or username of the user.
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "user_id", value)


class UserSshKey(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 expires_at: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        The `UserSshKey` resource allows to manage the lifecycle of an SSH key assigned to a user.

        **Upstream API**: [GitLab API docs](https://docs.gitlab.com/ee/api/users.html#single-ssh-key)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_gitlab as gitlab

        example_user = gitlab.get_user(username="example-user")
        example_user_ssh_key = gitlab.UserSshKey("exampleUserSshKey",
            user_id=example_user.id,
            title="example-key",
            key="ssh-ed25519 AAAA...",
            expires_at="2016-01-21T00:00:00.000Z")
        ```

        ## Import

        You can import a user ssh key using an id made up of `{user-id}:{key}`, e.g.

        ```sh
         $ pulumi import gitlab:index/userSshKey:UserSshKey example 42:1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] expires_at: The expiration date of the SSH key in ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ)
        :param pulumi.Input[str] key: The ssh key. The SSH key `comment` (trailing part) is optional and ignored for diffing, because GitLab overrides it with the username and GitLab hostname.
        :param pulumi.Input[str] title: The title of the ssh key.
        :param pulumi.Input[int] user_id: The ID or username of the user.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UserSshKeyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The `UserSshKey` resource allows to manage the lifecycle of an SSH key assigned to a user.

        **Upstream API**: [GitLab API docs](https://docs.gitlab.com/ee/api/users.html#single-ssh-key)

        ## Example Usage

        ```python
        import pulumi
        import pulumi_gitlab as gitlab

        example_user = gitlab.get_user(username="example-user")
        example_user_ssh_key = gitlab.UserSshKey("exampleUserSshKey",
            user_id=example_user.id,
            title="example-key",
            key="ssh-ed25519 AAAA...",
            expires_at="2016-01-21T00:00:00.000Z")
        ```

        ## Import

        You can import a user ssh key using an id made up of `{user-id}:{key}`, e.g.

        ```sh
         $ pulumi import gitlab:index/userSshKey:UserSshKey example 42:1
        ```

        :param str resource_name: The name of the resource.
        :param UserSshKeyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserSshKeyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 expires_at: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UserSshKeyArgs.__new__(UserSshKeyArgs)

            __props__.__dict__["expires_at"] = expires_at
            if key is None and not opts.urn:
                raise TypeError("Missing required property 'key'")
            __props__.__dict__["key"] = key
            if title is None and not opts.urn:
                raise TypeError("Missing required property 'title'")
            __props__.__dict__["title"] = title
            if user_id is None and not opts.urn:
                raise TypeError("Missing required property 'user_id'")
            __props__.__dict__["user_id"] = user_id
            __props__.__dict__["created_at"] = None
            __props__.__dict__["key_id"] = None
        super(UserSshKey, __self__).__init__(
            'gitlab:index/userSshKey:UserSshKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            expires_at: Optional[pulumi.Input[str]] = None,
            key: Optional[pulumi.Input[str]] = None,
            key_id: Optional[pulumi.Input[int]] = None,
            title: Optional[pulumi.Input[str]] = None,
            user_id: Optional[pulumi.Input[int]] = None) -> 'UserSshKey':
        """
        Get an existing UserSshKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] created_at: The time when this key was created in GitLab.
        :param pulumi.Input[str] expires_at: The expiration date of the SSH key in ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ)
        :param pulumi.Input[str] key: The ssh key. The SSH key `comment` (trailing part) is optional and ignored for diffing, because GitLab overrides it with the username and GitLab hostname.
        :param pulumi.Input[int] key_id: The ID of the ssh key.
        :param pulumi.Input[str] title: The title of the ssh key.
        :param pulumi.Input[int] user_id: The ID or username of the user.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _UserSshKeyState.__new__(_UserSshKeyState)

        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["expires_at"] = expires_at
        __props__.__dict__["key"] = key
        __props__.__dict__["key_id"] = key_id
        __props__.__dict__["title"] = title
        __props__.__dict__["user_id"] = user_id
        return UserSshKey(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The time when this key was created in GitLab.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="expiresAt")
    def expires_at(self) -> pulumi.Output[Optional[str]]:
        """
        The expiration date of the SSH key in ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ)
        """
        return pulumi.get(self, "expires_at")

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[str]:
        """
        The ssh key. The SSH key `comment` (trailing part) is optional and ignored for diffing, because GitLab overrides it with the username and GitLab hostname.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter(name="keyId")
    def key_id(self) -> pulumi.Output[int]:
        """
        The ID of the ssh key.
        """
        return pulumi.get(self, "key_id")

    @property
    @pulumi.getter
    def title(self) -> pulumi.Output[str]:
        """
        The title of the ssh key.
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Output[int]:
        """
        The ID or username of the user.
        """
        return pulumi.get(self, "user_id")

