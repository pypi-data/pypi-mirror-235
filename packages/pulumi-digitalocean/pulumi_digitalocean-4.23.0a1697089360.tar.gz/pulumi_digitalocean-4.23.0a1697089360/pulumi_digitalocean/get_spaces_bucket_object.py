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
    'GetSpacesBucketObjectResult',
    'AwaitableGetSpacesBucketObjectResult',
    'get_spaces_bucket_object',
    'get_spaces_bucket_object_output',
]

@pulumi.output_type
class GetSpacesBucketObjectResult:
    """
    A collection of values returned by getSpacesBucketObject.
    """
    def __init__(__self__, body=None, bucket=None, cache_control=None, content_disposition=None, content_encoding=None, content_language=None, content_length=None, content_type=None, etag=None, expiration=None, expires=None, id=None, key=None, last_modified=None, metadata=None, range=None, region=None, version_id=None, website_redirect_location=None):
        if body and not isinstance(body, str):
            raise TypeError("Expected argument 'body' to be a str")
        pulumi.set(__self__, "body", body)
        if bucket and not isinstance(bucket, str):
            raise TypeError("Expected argument 'bucket' to be a str")
        pulumi.set(__self__, "bucket", bucket)
        if cache_control and not isinstance(cache_control, str):
            raise TypeError("Expected argument 'cache_control' to be a str")
        pulumi.set(__self__, "cache_control", cache_control)
        if content_disposition and not isinstance(content_disposition, str):
            raise TypeError("Expected argument 'content_disposition' to be a str")
        pulumi.set(__self__, "content_disposition", content_disposition)
        if content_encoding and not isinstance(content_encoding, str):
            raise TypeError("Expected argument 'content_encoding' to be a str")
        pulumi.set(__self__, "content_encoding", content_encoding)
        if content_language and not isinstance(content_language, str):
            raise TypeError("Expected argument 'content_language' to be a str")
        pulumi.set(__self__, "content_language", content_language)
        if content_length and not isinstance(content_length, int):
            raise TypeError("Expected argument 'content_length' to be a int")
        pulumi.set(__self__, "content_length", content_length)
        if content_type and not isinstance(content_type, str):
            raise TypeError("Expected argument 'content_type' to be a str")
        pulumi.set(__self__, "content_type", content_type)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if expiration and not isinstance(expiration, str):
            raise TypeError("Expected argument 'expiration' to be a str")
        pulumi.set(__self__, "expiration", expiration)
        if expires and not isinstance(expires, str):
            raise TypeError("Expected argument 'expires' to be a str")
        pulumi.set(__self__, "expires", expires)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if key and not isinstance(key, str):
            raise TypeError("Expected argument 'key' to be a str")
        pulumi.set(__self__, "key", key)
        if last_modified and not isinstance(last_modified, str):
            raise TypeError("Expected argument 'last_modified' to be a str")
        pulumi.set(__self__, "last_modified", last_modified)
        if metadata and not isinstance(metadata, dict):
            raise TypeError("Expected argument 'metadata' to be a dict")
        pulumi.set(__self__, "metadata", metadata)
        if range and not isinstance(range, str):
            raise TypeError("Expected argument 'range' to be a str")
        pulumi.set(__self__, "range", range)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if version_id and not isinstance(version_id, str):
            raise TypeError("Expected argument 'version_id' to be a str")
        pulumi.set(__self__, "version_id", version_id)
        if website_redirect_location and not isinstance(website_redirect_location, str):
            raise TypeError("Expected argument 'website_redirect_location' to be a str")
        pulumi.set(__self__, "website_redirect_location", website_redirect_location)

    @property
    @pulumi.getter
    def body(self) -> str:
        """
        Object data (see **limitations above** to understand cases in which this field is actually available)
        """
        return pulumi.get(self, "body")

    @property
    @pulumi.getter
    def bucket(self) -> str:
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter(name="cacheControl")
    def cache_control(self) -> str:
        """
        Specifies caching behavior along the request/reply chain.
        """
        return pulumi.get(self, "cache_control")

    @property
    @pulumi.getter(name="contentDisposition")
    def content_disposition(self) -> str:
        """
        Specifies presentational information for the object.
        """
        return pulumi.get(self, "content_disposition")

    @property
    @pulumi.getter(name="contentEncoding")
    def content_encoding(self) -> str:
        """
        Specifies what content encodings have been applied to the object and thus what decoding mechanisms must be applied to obtain the media-type referenced by the Content-Type header field.
        """
        return pulumi.get(self, "content_encoding")

    @property
    @pulumi.getter(name="contentLanguage")
    def content_language(self) -> str:
        """
        The language the content is in.
        """
        return pulumi.get(self, "content_language")

    @property
    @pulumi.getter(name="contentLength")
    def content_length(self) -> int:
        """
        Size of the body in bytes.
        """
        return pulumi.get(self, "content_length")

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> str:
        """
        A standard MIME type describing the format of the object data.
        """
        return pulumi.get(self, "content_type")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        [ETag](https://en.wikipedia.org/wiki/HTTP_ETag) generated for the object (an MD5 sum of the object content in case it's not encrypted)
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def expiration(self) -> str:
        """
        If the object expiration is configured (see [object lifecycle management](http://docs.aws.amazon.com/AmazonS3/latest/dev/object-lifecycle-mgmt.html)), the field includes this header. It includes the expiry-date and rule-id key value pairs providing object expiration information. The value of the rule-id is URL encoded.
        """
        return pulumi.get(self, "expiration")

    @property
    @pulumi.getter
    def expires(self) -> str:
        """
        The date and time at which the object is no longer cacheable.
        """
        return pulumi.get(self, "expires")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def key(self) -> str:
        return pulumi.get(self, "key")

    @property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> str:
        """
        Last modified date of the object in RFC1123 format (e.g. `Mon, 02 Jan 2006 15:04:05 MST`)
        """
        return pulumi.get(self, "last_modified")

    @property
    @pulumi.getter
    def metadata(self) -> Mapping[str, Any]:
        """
        A map of metadata stored with the object in Spaces
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def range(self) -> Optional[str]:
        return pulumi.get(self, "range")

    @property
    @pulumi.getter
    def region(self) -> str:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="versionId")
    def version_id(self) -> str:
        """
        The latest version ID of the object returned.
        """
        return pulumi.get(self, "version_id")

    @property
    @pulumi.getter(name="websiteRedirectLocation")
    def website_redirect_location(self) -> str:
        """
        If the bucket is configured as a website, redirects requests for this object to another object in the same bucket or to an external URL. Spaces stores the value of this header in the object metadata.
        """
        return pulumi.get(self, "website_redirect_location")


class AwaitableGetSpacesBucketObjectResult(GetSpacesBucketObjectResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSpacesBucketObjectResult(
            body=self.body,
            bucket=self.bucket,
            cache_control=self.cache_control,
            content_disposition=self.content_disposition,
            content_encoding=self.content_encoding,
            content_language=self.content_language,
            content_length=self.content_length,
            content_type=self.content_type,
            etag=self.etag,
            expiration=self.expiration,
            expires=self.expires,
            id=self.id,
            key=self.key,
            last_modified=self.last_modified,
            metadata=self.metadata,
            range=self.range,
            region=self.region,
            version_id=self.version_id,
            website_redirect_location=self.website_redirect_location)


def get_spaces_bucket_object(bucket: Optional[str] = None,
                             key: Optional[str] = None,
                             range: Optional[str] = None,
                             region: Optional[str] = None,
                             version_id: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSpacesBucketObjectResult:
    """
    The Spaces object data source allows access to the metadata and
    _optionally_ (see below) content of an object stored inside a Spaces bucket.

    > **Note:** The content of an object (`body` field) is available only for objects which have a human-readable
    `Content-Type` (`text/*` and `application/json`). This is to prevent printing unsafe characters and potentially
    downloading large amount of data which would be thrown away in favor of metadata.

    ## Example Usage

    The following example retrieves a text object (which must have a `Content-Type`
    value starting with `text/`) and uses it as the `user_data` for a Droplet:

    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    bootstrap_script = digitalocean.get_spaces_bucket_object(bucket="ourcorp-deploy-config",
        region="nyc3",
        key="droplet-bootstrap-script.sh")
    web = digitalocean.Droplet("web",
        image="ubuntu-18-04-x64",
        region="nyc2",
        size="s-1vcpu-1gb",
        user_data=bootstrap_script.body)
    ```


    :param str bucket: The name of the bucket to read the object from.
    :param str key: The full path to the object inside the bucket
    :param str region: The slug of the region where the bucket is stored.
    :param str version_id: Specific version ID of the object returned (defaults to latest version)
    """
    __args__ = dict()
    __args__['bucket'] = bucket
    __args__['key'] = key
    __args__['range'] = range
    __args__['region'] = region
    __args__['versionId'] = version_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('digitalocean:index/getSpacesBucketObject:getSpacesBucketObject', __args__, opts=opts, typ=GetSpacesBucketObjectResult).value

    return AwaitableGetSpacesBucketObjectResult(
        body=pulumi.get(__ret__, 'body'),
        bucket=pulumi.get(__ret__, 'bucket'),
        cache_control=pulumi.get(__ret__, 'cache_control'),
        content_disposition=pulumi.get(__ret__, 'content_disposition'),
        content_encoding=pulumi.get(__ret__, 'content_encoding'),
        content_language=pulumi.get(__ret__, 'content_language'),
        content_length=pulumi.get(__ret__, 'content_length'),
        content_type=pulumi.get(__ret__, 'content_type'),
        etag=pulumi.get(__ret__, 'etag'),
        expiration=pulumi.get(__ret__, 'expiration'),
        expires=pulumi.get(__ret__, 'expires'),
        id=pulumi.get(__ret__, 'id'),
        key=pulumi.get(__ret__, 'key'),
        last_modified=pulumi.get(__ret__, 'last_modified'),
        metadata=pulumi.get(__ret__, 'metadata'),
        range=pulumi.get(__ret__, 'range'),
        region=pulumi.get(__ret__, 'region'),
        version_id=pulumi.get(__ret__, 'version_id'),
        website_redirect_location=pulumi.get(__ret__, 'website_redirect_location'))


@_utilities.lift_output_func(get_spaces_bucket_object)
def get_spaces_bucket_object_output(bucket: Optional[pulumi.Input[str]] = None,
                                    key: Optional[pulumi.Input[str]] = None,
                                    range: Optional[pulumi.Input[Optional[str]]] = None,
                                    region: Optional[pulumi.Input[str]] = None,
                                    version_id: Optional[pulumi.Input[Optional[str]]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSpacesBucketObjectResult]:
    """
    The Spaces object data source allows access to the metadata and
    _optionally_ (see below) content of an object stored inside a Spaces bucket.

    > **Note:** The content of an object (`body` field) is available only for objects which have a human-readable
    `Content-Type` (`text/*` and `application/json`). This is to prevent printing unsafe characters and potentially
    downloading large amount of data which would be thrown away in favor of metadata.

    ## Example Usage

    The following example retrieves a text object (which must have a `Content-Type`
    value starting with `text/`) and uses it as the `user_data` for a Droplet:

    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    bootstrap_script = digitalocean.get_spaces_bucket_object(bucket="ourcorp-deploy-config",
        region="nyc3",
        key="droplet-bootstrap-script.sh")
    web = digitalocean.Droplet("web",
        image="ubuntu-18-04-x64",
        region="nyc2",
        size="s-1vcpu-1gb",
        user_data=bootstrap_script.body)
    ```


    :param str bucket: The name of the bucket to read the object from.
    :param str key: The full path to the object inside the bucket
    :param str region: The slug of the region where the bucket is stored.
    :param str version_id: Specific version ID of the object returned (defaults to latest version)
    """
    ...
