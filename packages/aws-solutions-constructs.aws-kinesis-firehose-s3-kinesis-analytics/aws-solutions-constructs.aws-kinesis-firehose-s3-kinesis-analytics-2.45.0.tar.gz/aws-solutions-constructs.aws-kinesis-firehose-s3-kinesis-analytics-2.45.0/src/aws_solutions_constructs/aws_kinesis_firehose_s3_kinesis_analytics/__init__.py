'''
# aws-kinesisfirehose-s3-and-kinesisanalytics module

<!--BEGIN STABILITY BANNER-->---


![Stability: Experimental](https://img.shields.io/badge/stability-Experimental-important.svg?style=for-the-badge)

> All classes are under active development and subject to non-backward compatible changes or removal in any
> future version. These are not subject to the [Semantic Versioning](https://semver.org/) model.
> This means that while you may use them, you may need to update your source code when upgrading to a newer version of this package.

---
<!--END STABILITY BANNER-->

| **Reference Documentation**:| <span style="font-weight: normal">https://docs.aws.amazon.com/solutions/latest/constructs/</span>|
|:-------------|:-------------|

<div style="height:8px"></div>

| **Language**     | **Package**        |
|:-------------|-----------------|
|![Python Logo](https://docs.aws.amazon.com/cdk/api/latest/img/python32.png) Python|`aws_solutions_constructs.aws_kinesisfirehose_s3_and_kinesisanalytics`|
|![Typescript Logo](https://docs.aws.amazon.com/cdk/api/latest/img/typescript32.png) Typescript|`@aws-solutions-constructs/aws-kinesisfirehose-s3-and-kinesisanalytics`|
|![Java Logo](https://docs.aws.amazon.com/cdk/api/latest/img/java32.png) Java|`software.amazon.awsconstructs.services.kinesisfirehoses3kinesisanalytics`|

## Overview

This AWS Solutions Construct implements an Amazon Kinesis Firehose delivery stream connected to an Amazon S3 bucket, and an Amazon Kinesis Analytics application.

Here is a minimal deployable pattern definition:

Typescript

```python
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { KinesisFirehoseToAnalyticsAndS3 } from '@aws-solutions-constructs/aws-kinesisfirehose-s3-and-kinesisanalytics';

new KinesisFirehoseToAnalyticsAndS3(this, 'FirehoseToS3AndAnalyticsPattern', {
  kinesisAnalyticsProps: {
    inputs: [{
      inputSchema: {
        recordColumns: [{
          name: 'ticker_symbol',
          sqlType: 'VARCHAR(4)',
          mapping: '$.ticker_symbol'
        }, {
          name: 'sector',
          sqlType: 'VARCHAR(16)',
          mapping: '$.sector'
        }, {
          name: 'change',
          sqlType: 'REAL',
          mapping: '$.change'
        }, {
          name: 'price',
          sqlType: 'REAL',
          mapping: '$.price'
        }],
        recordFormat: {
          recordFormatType: 'JSON'
        },
        recordEncoding: 'UTF-8'
      },
      namePrefix: 'SOURCE_SQL_STREAM'
    }]
  }
});
```

Python

```python
from aws_solutions_constructs.aws_kinesis_firehose_s3_kinesis_analytics import KinesisFirehoseToAnalyticsAndS3
from aws_cdk import (
    aws_kinesisanalytics as kinesisanalytics,
    Stack
)
from constructs import Construct

KinesisFirehoseToAnalyticsAndS3(self, 'FirehoseToS3AndAnalyticsPattern',
                                kinesis_analytics_props=kinesisanalytics.CfnApplicationProps(
                                    inputs=[kinesisanalytics.CfnApplication.InputProperty(
                                        input_schema=kinesisanalytics.CfnApplication.InputSchemaProperty(
                                            record_columns=[kinesisanalytics.CfnApplication.RecordColumnProperty(
                                                name='ticker_symbol',
                                                sql_type='VARCHAR(4)',
                                                mapping='$.ticker_symbol'
                                            ), kinesisanalytics.CfnApplication.RecordColumnProperty(
                                                name='sector',
                                                sql_type='VARCHAR(16)',
                                                mapping='$.sector'
                                            ), kinesisanalytics.CfnApplication.RecordColumnProperty(
                                                name='change',
                                                sql_type='REAL',
                                                mapping='$.change'
                                            ), kinesisanalytics.CfnApplication.RecordColumnProperty(
                                                name='price',
                                                sql_type='REAL',
                                                mapping='$.price'
                                            )],
                                            record_format=kinesisanalytics.CfnApplication.RecordFormatProperty(
                                                record_format_type='JSON'
                                            ),
                                            record_encoding='UTF-8'
                                        ),
                                        name_prefix='SOURCE_SQL_STREAM'
                                    )]
                                )
                                )
```

Java

```java
import software.constructs.Construct;
import java.util.List;

import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awscdk.services.kinesisanalytics.*;
import software.amazon.awscdk.services.kinesisanalytics.CfnApplication.*;
import software.amazon.awsconstructs.services.kinesisfirehoses3kinesisanalytics.*;

new KinesisFirehoseToAnalyticsAndS3(this, "FirehoseToS3AndAnalyticsPattern",
        new KinesisFirehoseToAnalyticsAndS3Props.Builder()
                .kinesisAnalyticsProps(new CfnApplicationProps.Builder()
                        .inputs(List.of(new InputProperty.Builder()
                                .inputSchema(new InputSchemaProperty.Builder()
                                        .recordColumns(List.of(
                                                new RecordColumnProperty.Builder()
                                                        .name("ticker_symbol")
                                                        .sqlType("VARCHAR(4)")
                                                        .mapping("$.ticker_symbol")
                                                        .build(),
                                                new RecordColumnProperty.Builder()
                                                        .name("sector")
                                                        .sqlType("VARCHAR(16)")
                                                        .mapping("$.sector")
                                                        .build(),
                                                new RecordColumnProperty.Builder()
                                                        .name("change")
                                                        .sqlType("REAL")
                                                        .mapping("$.change")
                                                        .build(),
                                                new RecordColumnProperty.Builder()
                                                        .name("price")
                                                        .sqlType("REAL")
                                                        .mapping("$.price")
                                                        .build()))
                                        .recordFormat(new RecordFormatProperty.Builder()
                                                .recordFormatType("JSON")
                                                .build())
                                        .recordEncoding("UTF-8")
                                        .build())
                                .namePrefix("SOURCE_SQL_STREAM")
                                .build()))
                        .build())
                .build());
```

## Pattern Construct Props

| **Name**     | **Type**        | **Description** |
|:-------------|:----------------|-----------------|
|kinesisFirehoseProps?|[`kinesisFirehose.CfnDeliveryStreamProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStreamProps.html)|Optional user-provided props to override the default props for the Kinesis Firehose delivery stream.|
|kinesisAnalyticsProps?|[`kinesisAnalytics.CfnApplicationProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesisanalytics.CfnApplicationProps.html)|Optional user-provided props to override the default props for the Kinesis Analytics application.|
|existingBucketObj?|[`s3.IBucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html)|Existing instance of S3 Bucket object. If this is provided, then also providing bucketProps is an error. |
|bucketProps?|[`s3.BucketProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html)|User provided props to override the default props for the S3 Bucket.|
|logGroupProps?|[`logs.LogGroupProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.LogGroupProps.html)|User provided props to override the default props for for the CloudWatchLogs LogGroup.|
|loggingBucketProps?|[`s3.BucketProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html)|Optional user provided props to override the default props for the S3 Logging Bucket.|
|logS3AccessLogs?| boolean|Whether to turn on Access Logging for the S3 bucket. Creates an S3 bucket with associated storage costs for the logs. Enabling Access Logging is a best practice. default - true|

## Pattern Properties

| **Name**     | **Type**        | **Description** |
|:-------------|:----------------|-----------------|
|kinesisAnalytics|[`kinesisAnalytics.CfnApplication`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesisanalytics.CfnApplication.html)|Returns an instance of the Kinesis Analytics application created by the pattern.|
|kinesisFirehose|[`kinesisFirehose.CfnDeliveryStream`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_kinesisfirehose.CfnDeliveryStream.html)|Returns an instance of the Kinesis Firehose delivery stream created by the pattern.|
|kinesisFirehoseRole|[`iam.Role`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.Role.html)|Returns an instance of the iam.Role created by the construct for Kinesis Data Firehose delivery stream.|
|kinesisFirehoseLogGroup|[`logs.LogGroup`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_logs.LogGroup.html)|Returns an instance of the LogGroup created by the construct for Kinesis Data Firehose delivery stream|
|s3Bucket?|[`s3.Bucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html)|Returns an instance of the S3 bucket created by the pattern.|
|s3LoggingBucket?|[`s3.Bucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.Bucket.html)|Returns an instance of s3.Bucket created by the construct as the logging bucket for the primary bucket.|
|s3BucketInterface|[`s3.IBucket`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.IBucket.html)|Returns an instance of s3.IBucket created by the construct.|

## Default settings

Out of the box implementation of the Construct without any override will set the following defaults:

### Amazon Kinesis Firehose

* Enable CloudWatch logging for Kinesis Firehose
* Configure least privilege access IAM role for Amazon Kinesis Firehose

### Amazon S3 Bucket

* Configure Access logging for S3 Bucket
* Enable server-side encryption for S3 Bucket using AWS managed KMS Key
* Enforce encryption of data in transit
* Turn on the versioning for S3 Bucket
* Don't allow public access for S3 Bucket
* Retain the S3 Bucket when deleting the CloudFormation stack
* Applies Lifecycle rule to move noncurrent object versions to Glacier storage after 90 days

### Amazon Kinesis Data Analytics

* Configure least privilege access IAM role for Amazon Kinesis Analytics

## Architecture

![Architecture Diagram](architecture.png)

---


© Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from ._jsii import *

import aws_cdk.aws_iam as _aws_cdk_aws_iam_ceddda9d
import aws_cdk.aws_kinesisanalytics as _aws_cdk_aws_kinesisanalytics_ceddda9d
import aws_cdk.aws_kinesisfirehose as _aws_cdk_aws_kinesisfirehose_ceddda9d
import aws_cdk.aws_logs as _aws_cdk_aws_logs_ceddda9d
import aws_cdk.aws_s3 as _aws_cdk_aws_s3_ceddda9d
import constructs as _constructs_77d1e7e8


class KinesisFirehoseToAnalyticsAndS3(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-solutions-constructs/aws-kinesisfirehose-s3-and-kinesisanalytics.KinesisFirehoseToAnalyticsAndS3",
):
    '''
    :summary: The KinesisFirehoseToAnalyticsAndS3 class.
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        bucket_props: typing.Optional[typing.Union[_aws_cdk_aws_s3_ceddda9d.BucketProps, typing.Dict[builtins.str, typing.Any]]] = None,
        existing_bucket_obj: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
        kinesis_analytics_props: typing.Optional[typing.Union[_aws_cdk_aws_kinesisanalytics_ceddda9d.CfnApplicationProps, typing.Dict[builtins.str, typing.Any]]] = None,
        kinesis_firehose_props: typing.Any = None,
        logging_bucket_props: typing.Optional[typing.Union[_aws_cdk_aws_s3_ceddda9d.BucketProps, typing.Dict[builtins.str, typing.Any]]] = None,
        log_group_props: typing.Optional[typing.Union[_aws_cdk_aws_logs_ceddda9d.LogGroupProps, typing.Dict[builtins.str, typing.Any]]] = None,
        log_s3_access_logs: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param scope: - represents the scope for all the resources.
        :param id: - this is a a scope-unique id.
        :param bucket_props: User provided props to override the default props for the S3 Bucket. Default: - Default props are used
        :param existing_bucket_obj: Existing instance of S3 Bucket object, providing both this and ``bucketProps`` will cause an error. Default: - None
        :param kinesis_analytics_props: Optional user-provided props to override the default props for the Kinesis Analytics application. Default: - Default props are used.
        :param kinesis_firehose_props: Optional user-provided props to override the default props for the Kinesis Firehose delivery stream. Default: - Default props are used.
        :param logging_bucket_props: Optional user provided props to override the default props for the S3 Logging Bucket. Default: - Default props are used
        :param log_group_props: User provided props to override the default props for the CloudWatchLogs LogGroup. Default: - Default props are used
        :param log_s3_access_logs: Whether to turn on Access Logs for the S3 bucket with the associated storage costs. Enabling Access Logging is a best practice. Default: - true

        :access: public
        :since: 0.8.0
        :summary: Constructs a new instance of the KinesisFirehoseToAnalyticsAndS3 class.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aad7dee973d6b09ff410d711c611112f24e0cc0f698983430b8cde682b5cce1b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = KinesisFirehoseToAnalyticsAndS3Props(
            bucket_props=bucket_props,
            existing_bucket_obj=existing_bucket_obj,
            kinesis_analytics_props=kinesis_analytics_props,
            kinesis_firehose_props=kinesis_firehose_props,
            logging_bucket_props=logging_bucket_props,
            log_group_props=log_group_props,
            log_s3_access_logs=log_s3_access_logs,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="kinesisAnalytics")
    def kinesis_analytics(
        self,
    ) -> _aws_cdk_aws_kinesisanalytics_ceddda9d.CfnApplication:
        return typing.cast(_aws_cdk_aws_kinesisanalytics_ceddda9d.CfnApplication, jsii.get(self, "kinesisAnalytics"))

    @builtins.property
    @jsii.member(jsii_name="kinesisFirehose")
    def kinesis_firehose(
        self,
    ) -> _aws_cdk_aws_kinesisfirehose_ceddda9d.CfnDeliveryStream:
        return typing.cast(_aws_cdk_aws_kinesisfirehose_ceddda9d.CfnDeliveryStream, jsii.get(self, "kinesisFirehose"))

    @builtins.property
    @jsii.member(jsii_name="kinesisFirehoseLogGroup")
    def kinesis_firehose_log_group(self) -> _aws_cdk_aws_logs_ceddda9d.LogGroup:
        return typing.cast(_aws_cdk_aws_logs_ceddda9d.LogGroup, jsii.get(self, "kinesisFirehoseLogGroup"))

    @builtins.property
    @jsii.member(jsii_name="kinesisFirehoseRole")
    def kinesis_firehose_role(self) -> _aws_cdk_aws_iam_ceddda9d.Role:
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.Role, jsii.get(self, "kinesisFirehoseRole"))

    @builtins.property
    @jsii.member(jsii_name="s3BucketInterface")
    def s3_bucket_interface(self) -> _aws_cdk_aws_s3_ceddda9d.IBucket:
        return typing.cast(_aws_cdk_aws_s3_ceddda9d.IBucket, jsii.get(self, "s3BucketInterface"))

    @builtins.property
    @jsii.member(jsii_name="s3Bucket")
    def s3_bucket(self) -> typing.Optional[_aws_cdk_aws_s3_ceddda9d.Bucket]:
        return typing.cast(typing.Optional[_aws_cdk_aws_s3_ceddda9d.Bucket], jsii.get(self, "s3Bucket"))

    @builtins.property
    @jsii.member(jsii_name="s3LoggingBucket")
    def s3_logging_bucket(self) -> typing.Optional[_aws_cdk_aws_s3_ceddda9d.Bucket]:
        return typing.cast(typing.Optional[_aws_cdk_aws_s3_ceddda9d.Bucket], jsii.get(self, "s3LoggingBucket"))


@jsii.data_type(
    jsii_type="@aws-solutions-constructs/aws-kinesisfirehose-s3-and-kinesisanalytics.KinesisFirehoseToAnalyticsAndS3Props",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_props": "bucketProps",
        "existing_bucket_obj": "existingBucketObj",
        "kinesis_analytics_props": "kinesisAnalyticsProps",
        "kinesis_firehose_props": "kinesisFirehoseProps",
        "logging_bucket_props": "loggingBucketProps",
        "log_group_props": "logGroupProps",
        "log_s3_access_logs": "logS3AccessLogs",
    },
)
class KinesisFirehoseToAnalyticsAndS3Props:
    def __init__(
        self,
        *,
        bucket_props: typing.Optional[typing.Union[_aws_cdk_aws_s3_ceddda9d.BucketProps, typing.Dict[builtins.str, typing.Any]]] = None,
        existing_bucket_obj: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
        kinesis_analytics_props: typing.Optional[typing.Union[_aws_cdk_aws_kinesisanalytics_ceddda9d.CfnApplicationProps, typing.Dict[builtins.str, typing.Any]]] = None,
        kinesis_firehose_props: typing.Any = None,
        logging_bucket_props: typing.Optional[typing.Union[_aws_cdk_aws_s3_ceddda9d.BucketProps, typing.Dict[builtins.str, typing.Any]]] = None,
        log_group_props: typing.Optional[typing.Union[_aws_cdk_aws_logs_ceddda9d.LogGroupProps, typing.Dict[builtins.str, typing.Any]]] = None,
        log_s3_access_logs: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''The properties for the KinesisFirehoseToAnalyticsAndS3 class.

        :param bucket_props: User provided props to override the default props for the S3 Bucket. Default: - Default props are used
        :param existing_bucket_obj: Existing instance of S3 Bucket object, providing both this and ``bucketProps`` will cause an error. Default: - None
        :param kinesis_analytics_props: Optional user-provided props to override the default props for the Kinesis Analytics application. Default: - Default props are used.
        :param kinesis_firehose_props: Optional user-provided props to override the default props for the Kinesis Firehose delivery stream. Default: - Default props are used.
        :param logging_bucket_props: Optional user provided props to override the default props for the S3 Logging Bucket. Default: - Default props are used
        :param log_group_props: User provided props to override the default props for the CloudWatchLogs LogGroup. Default: - Default props are used
        :param log_s3_access_logs: Whether to turn on Access Logs for the S3 bucket with the associated storage costs. Enabling Access Logging is a best practice. Default: - true
        '''
        if isinstance(bucket_props, dict):
            bucket_props = _aws_cdk_aws_s3_ceddda9d.BucketProps(**bucket_props)
        if isinstance(kinesis_analytics_props, dict):
            kinesis_analytics_props = _aws_cdk_aws_kinesisanalytics_ceddda9d.CfnApplicationProps(**kinesis_analytics_props)
        if isinstance(logging_bucket_props, dict):
            logging_bucket_props = _aws_cdk_aws_s3_ceddda9d.BucketProps(**logging_bucket_props)
        if isinstance(log_group_props, dict):
            log_group_props = _aws_cdk_aws_logs_ceddda9d.LogGroupProps(**log_group_props)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c3cdb5041f170ac6ee1da4cc714c260c0b617aa32379a00a408e918ca5a23a6)
            check_type(argname="argument bucket_props", value=bucket_props, expected_type=type_hints["bucket_props"])
            check_type(argname="argument existing_bucket_obj", value=existing_bucket_obj, expected_type=type_hints["existing_bucket_obj"])
            check_type(argname="argument kinesis_analytics_props", value=kinesis_analytics_props, expected_type=type_hints["kinesis_analytics_props"])
            check_type(argname="argument kinesis_firehose_props", value=kinesis_firehose_props, expected_type=type_hints["kinesis_firehose_props"])
            check_type(argname="argument logging_bucket_props", value=logging_bucket_props, expected_type=type_hints["logging_bucket_props"])
            check_type(argname="argument log_group_props", value=log_group_props, expected_type=type_hints["log_group_props"])
            check_type(argname="argument log_s3_access_logs", value=log_s3_access_logs, expected_type=type_hints["log_s3_access_logs"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if bucket_props is not None:
            self._values["bucket_props"] = bucket_props
        if existing_bucket_obj is not None:
            self._values["existing_bucket_obj"] = existing_bucket_obj
        if kinesis_analytics_props is not None:
            self._values["kinesis_analytics_props"] = kinesis_analytics_props
        if kinesis_firehose_props is not None:
            self._values["kinesis_firehose_props"] = kinesis_firehose_props
        if logging_bucket_props is not None:
            self._values["logging_bucket_props"] = logging_bucket_props
        if log_group_props is not None:
            self._values["log_group_props"] = log_group_props
        if log_s3_access_logs is not None:
            self._values["log_s3_access_logs"] = log_s3_access_logs

    @builtins.property
    def bucket_props(self) -> typing.Optional[_aws_cdk_aws_s3_ceddda9d.BucketProps]:
        '''User provided props to override the default props for the S3 Bucket.

        :default: - Default props are used
        '''
        result = self._values.get("bucket_props")
        return typing.cast(typing.Optional[_aws_cdk_aws_s3_ceddda9d.BucketProps], result)

    @builtins.property
    def existing_bucket_obj(self) -> typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket]:
        '''Existing instance of S3 Bucket object, providing both this and ``bucketProps`` will cause an error.

        :default: - None
        '''
        result = self._values.get("existing_bucket_obj")
        return typing.cast(typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket], result)

    @builtins.property
    def kinesis_analytics_props(
        self,
    ) -> typing.Optional[_aws_cdk_aws_kinesisanalytics_ceddda9d.CfnApplicationProps]:
        '''Optional user-provided props to override the default props for the Kinesis Analytics application.

        :default: - Default props are used.
        '''
        result = self._values.get("kinesis_analytics_props")
        return typing.cast(typing.Optional[_aws_cdk_aws_kinesisanalytics_ceddda9d.CfnApplicationProps], result)

    @builtins.property
    def kinesis_firehose_props(self) -> typing.Any:
        '''Optional user-provided props to override the default props for the Kinesis Firehose delivery stream.

        :default: - Default props are used.
        '''
        result = self._values.get("kinesis_firehose_props")
        return typing.cast(typing.Any, result)

    @builtins.property
    def logging_bucket_props(
        self,
    ) -> typing.Optional[_aws_cdk_aws_s3_ceddda9d.BucketProps]:
        '''Optional user provided props to override the default props for the S3 Logging Bucket.

        :default: - Default props are used
        '''
        result = self._values.get("logging_bucket_props")
        return typing.cast(typing.Optional[_aws_cdk_aws_s3_ceddda9d.BucketProps], result)

    @builtins.property
    def log_group_props(
        self,
    ) -> typing.Optional[_aws_cdk_aws_logs_ceddda9d.LogGroupProps]:
        '''User provided props to override the default props for the CloudWatchLogs LogGroup.

        :default: - Default props are used
        '''
        result = self._values.get("log_group_props")
        return typing.cast(typing.Optional[_aws_cdk_aws_logs_ceddda9d.LogGroupProps], result)

    @builtins.property
    def log_s3_access_logs(self) -> typing.Optional[builtins.bool]:
        '''Whether to turn on Access Logs for the S3 bucket with the associated storage costs.

        Enabling Access Logging is a best practice.

        :default: - true
        '''
        result = self._values.get("log_s3_access_logs")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisFirehoseToAnalyticsAndS3Props(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "KinesisFirehoseToAnalyticsAndS3",
    "KinesisFirehoseToAnalyticsAndS3Props",
]

publication.publish()

def _typecheckingstub__aad7dee973d6b09ff410d711c611112f24e0cc0f698983430b8cde682b5cce1b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    bucket_props: typing.Optional[typing.Union[_aws_cdk_aws_s3_ceddda9d.BucketProps, typing.Dict[builtins.str, typing.Any]]] = None,
    existing_bucket_obj: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
    kinesis_analytics_props: typing.Optional[typing.Union[_aws_cdk_aws_kinesisanalytics_ceddda9d.CfnApplicationProps, typing.Dict[builtins.str, typing.Any]]] = None,
    kinesis_firehose_props: typing.Any = None,
    logging_bucket_props: typing.Optional[typing.Union[_aws_cdk_aws_s3_ceddda9d.BucketProps, typing.Dict[builtins.str, typing.Any]]] = None,
    log_group_props: typing.Optional[typing.Union[_aws_cdk_aws_logs_ceddda9d.LogGroupProps, typing.Dict[builtins.str, typing.Any]]] = None,
    log_s3_access_logs: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c3cdb5041f170ac6ee1da4cc714c260c0b617aa32379a00a408e918ca5a23a6(
    *,
    bucket_props: typing.Optional[typing.Union[_aws_cdk_aws_s3_ceddda9d.BucketProps, typing.Dict[builtins.str, typing.Any]]] = None,
    existing_bucket_obj: typing.Optional[_aws_cdk_aws_s3_ceddda9d.IBucket] = None,
    kinesis_analytics_props: typing.Optional[typing.Union[_aws_cdk_aws_kinesisanalytics_ceddda9d.CfnApplicationProps, typing.Dict[builtins.str, typing.Any]]] = None,
    kinesis_firehose_props: typing.Any = None,
    logging_bucket_props: typing.Optional[typing.Union[_aws_cdk_aws_s3_ceddda9d.BucketProps, typing.Dict[builtins.str, typing.Any]]] = None,
    log_group_props: typing.Optional[typing.Union[_aws_cdk_aws_logs_ceddda9d.LogGroupProps, typing.Dict[builtins.str, typing.Any]]] = None,
    log_s3_access_logs: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass
