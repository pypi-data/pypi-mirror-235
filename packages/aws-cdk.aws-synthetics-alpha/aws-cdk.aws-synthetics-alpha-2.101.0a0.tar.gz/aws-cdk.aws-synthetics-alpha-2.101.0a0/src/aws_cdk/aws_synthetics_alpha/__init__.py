'''
# Amazon CloudWatch Synthetics Construct Library

<!--BEGIN STABILITY BANNER-->---


![Deprecated](https://img.shields.io/badge/deprecated-critical.svg?style=for-the-badge)

> This API may emit warnings. Backward compatibility is not guaranteed.

---
<!--END STABILITY BANNER-->

All constructs moved to aws-cdk-lib/aws-synthetics.

Amazon CloudWatch Synthetics allow you to monitor your application by generating **synthetic** traffic. The traffic is produced by a **canary**: a configurable script that runs on a schedule. You configure the canary script to follow the same routes and perform the same actions as a user, which allows you to continually verify your user experience even when you don't have any traffic on your applications.

## Canary

To illustrate how to use a canary, assume your application defines the following endpoint:

```console
% curl "https://api.example.com/user/books/topbook/"
The Hitchhikers Guide to the Galaxy
```

The below code defines a canary that will hit the `books/topbook` endpoint every 5 minutes:

```python
canary = synthetics.Canary(self, "MyCanary",
    schedule=synthetics.Schedule.rate(Duration.minutes(5)),
    test=synthetics.Test.custom(
        code=synthetics.Code.from_asset(path.join(__dirname, "canary")),
        handler="index.handler"
    ),
    runtime=synthetics.Runtime.SYNTHETICS_NODEJS_PUPPETEER_4_0,
    environment_variables={
        "stage": "prod"
    }
)
```

The following is an example of an `index.js` file which exports the `handler` function:

```js
const synthetics = require('Synthetics');
const log = require('SyntheticsLogger');

const pageLoadBlueprint = async function () {
  // Configure the stage of the API using environment variables
  const url = `https://api.example.com/${process.env.stage}/user/books/topbook/`;

  const page = await synthetics.getPage();
  const response = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 30000 });
  // Wait for page to render. Increase or decrease wait time based on endpoint being monitored.
  await page.waitFor(15000);
  // This will take a screenshot that will be included in test output artifacts.
  await synthetics.takeScreenshot('loaded', 'loaded');
  const pageTitle = await page.title();
  log.info('Page title: ' + pageTitle);
  if (response.status() !== 200) {
    throw 'Failed to load page!';
  }
};

exports.handler = async () => {
  return await pageLoadBlueprint();
};
```

> **Note:** The function **must** be called `handler`.

The canary will automatically produce a CloudWatch Dashboard:

![UI Screenshot](images/ui-screenshot.png)

The Canary code will be executed in a lambda function created by Synthetics on your behalf. The Lambda function includes a custom [runtime](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html) provided by Synthetics. The provided runtime includes a variety of handy tools such as [Puppeteer](https://www.npmjs.com/package/puppeteer-core) (for nodejs based one) and Chromium.

To learn more about Synthetics capabilities, check out the [docs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.html).

### Canary Schedule

You can specify the schedule on which a canary runs by providing a
[`Schedule`](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-synthetics.Schedule.html)
object to the `schedule` property.

Configure a run rate of up to 60 minutes with `Schedule.rate`:

```python
schedule = synthetics.Schedule.rate(Duration.minutes(5))
```

You can also specify a [cron expression](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_cron.html) with `Schedule.cron`:

```python
schedule = synthetics.Schedule.cron(
    hour="0,8,16"
)
```

If you want the canary to run just once upon deployment, you can use `Schedule.once()`.

### Deleting underlying resources on canary deletion

When you delete a lambda, the following underlying resources are isolated in your AWS account:

* Lambda Function that runs your canary script
* S3 Bucket for artifact storage
* IAM roles and policies
* Log Groups in CloudWatch Logs.

To learn more about these underlying resources, see
[Synthetics Canaries Deletion](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/synthetics_canaries_deletion.html).

In the CDK, you can configure your canary to delete the underlying lambda function when the canary is deleted.
This can be provisioned by setting `cleanup: Cleanup.LAMBDA`. Note that this
will create a custom resource under the hood that takes care of the lambda deletion for you.

```python
canary = synthetics.Canary(self, "Canary",
    test=synthetics.Test.custom(
        handler="index.handler",
        code=synthetics.Code.from_inline("/* Synthetics handler code")
    ),
    cleanup=synthetics.Cleanup.LAMBDA,
    runtime=synthetics.Runtime.SYNTHETICS_NODEJS_PUPPETEER_4_0
)
```

> Note: To properly clean up your canary on deletion, you still have to manually delete other resources
> like S3 buckets and CloudWatch logs.

### Configuring the Canary Script

To configure the script the canary executes, use the `test` property. The `test` property accepts a `Test` instance that can be initialized by the `Test` class static methods. Currently, the only implemented method is `Test.custom()`, which allows you to bring your own code. In the future, other methods will be added. `Test.custom()` accepts `code` and `handler` properties -- both are required by Synthetics to create a lambda function on your behalf.

The `synthetics.Code` class exposes static methods to bundle your code artifacts:

* `code.fromInline(code)` - specify an inline script.
* `code.fromAsset(path)` - specify a .zip file or a directory in the local filesystem which will be zipped and uploaded to S3 on deployment. See the above Note for directory structure.
* `code.fromBucket(bucket, key[, objectVersion])` - specify an S3 object that contains the .zip file of your runtime code. See the above Note for directory structure.

Using the `Code` class static initializers:

```python
# To supply the code from a S3 bucket:
import aws_cdk.aws_s3 as s3
# To supply the code inline:
synthetics.Canary(self, "Inline Canary",
    test=synthetics.Test.custom(
        code=synthetics.Code.from_inline("/* Synthetics handler code */"),
        handler="index.handler"
    ),
    runtime=synthetics.Runtime.SYNTHETICS_NODEJS_PUPPETEER_4_0
)

# To supply the code from your local filesystem:
synthetics.Canary(self, "Asset Canary",
    test=synthetics.Test.custom(
        code=synthetics.Code.from_asset(path.join(__dirname, "canary")),
        handler="index.handler"
    ),
    runtime=synthetics.Runtime.SYNTHETICS_NODEJS_PUPPETEER_4_0
)
bucket = s3.Bucket(self, "Code Bucket")
synthetics.Canary(self, "Bucket Canary",
    test=synthetics.Test.custom(
        code=synthetics.Code.from_bucket(bucket, "canary.zip"),
        handler="index.handler"
    ),
    runtime=synthetics.Runtime.SYNTHETICS_NODEJS_PUPPETEER_4_0
)
```

> **Note:** Synthetics have a specified folder structure for canaries. For Node scripts supplied via `code.fromAsset()` or `code.fromBucket()`, the canary resource requires the following folder structure:
>
> ```plaintext
> canary/
> ├── nodejs/
>    ├── node_modules/
>         ├── <filename>.js
> ```
>
> For Python scripts supplied via `code.fromAsset()` or `code.fromBucket()`, the canary resource requires the following folder structure:
>
> ```plaintext
> canary/
> ├── python/
>     ├── <filename>.py
> ```
>
> See Synthetics [docs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_WritingCanary.html).

### Running a canary on a VPC

You can specify what [VPC a canary executes in](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_VPC.html).
This can allow for monitoring services that may be internal to a specific VPC. To place a canary within a VPC, you can specify the `vpc` property with the desired `VPC` to place then canary in.
This will automatically attach the appropriate IAM permissions to attach to the VPC. This will also create a Security Group and attach to the default subnets for the VPC unless specified via `vpcSubnets` and `securityGroups`.

```python
import aws_cdk.aws_ec2 as ec2

# vpc: ec2.IVpc

synthetics.Canary(self, "Vpc Canary",
    test=synthetics.Test.custom(
        code=synthetics.Code.from_asset(path.join(__dirname, "canary")),
        handler="index.handler"
    ),
    runtime=synthetics.Runtime.SYNTHETICS_NODEJS_PUPPETEER_4_0,
    vpc=vpc
)
```

> **Note:** By default, the Synthetics runtime needs access to the S3 and CloudWatch APIs, which will fail in a private subnet without internet access enabled (e.g. an isolated subnnet).
>
> Ensure that the Canary is placed in a VPC either with internet connectivity or with VPC Endpoints for S3 and CloudWatch enabled and configured.
>
> See [Synthetics VPC docs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_VPC.html).

### Alarms

You can configure a CloudWatch Alarm on a canary metric. Metrics are emitted by CloudWatch automatically and can be accessed by the following APIs:

* `canary.metricSuccessPercent()` - percentage of successful canary runs over a given time
* `canary.metricDuration()` - how much time each canary run takes, in seconds.
* `canary.metricFailed()` - number of failed canary runs over a given time

Create an alarm that tracks the canary metric:

```python
import aws_cdk.aws_cloudwatch as cloudwatch

# canary: synthetics.Canary

cloudwatch.Alarm(self, "CanaryAlarm",
    metric=canary.metric_success_percent(),
    evaluation_periods=2,
    threshold=90,
    comparison_operator=cloudwatch.ComparisonOperator.LESS_THAN_THRESHOLD
)
```

### Artifacts

You can pass an S3 bucket to store artifacts from canary runs. If you do not,
one will be auto-generated when the canary is created. You may add
[lifecycle rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html)
to the auto-generated bucket.

```python
canary = synthetics.Canary(self, "MyCanary",
    schedule=synthetics.Schedule.rate(Duration.minutes(5)),
    test=synthetics.Test.custom(
        code=synthetics.Code.from_asset(path.join(__dirname, "canary")),
        handler="index.handler"
    ),
    runtime=synthetics.Runtime.SYNTHETICS_NODEJS_PUPPETEER_4_0,
    artifacts_bucket_lifecycle_rules=[LifecycleRule(
        expiration=Duration.days(30)
    )]
)
```
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

import aws_cdk as _aws_cdk_ceddda9d
import aws_cdk.aws_cloudwatch as _aws_cdk_aws_cloudwatch_ceddda9d
import aws_cdk.aws_ec2 as _aws_cdk_aws_ec2_ceddda9d
import aws_cdk.aws_iam as _aws_cdk_aws_iam_ceddda9d
import aws_cdk.aws_s3 as _aws_cdk_aws_s3_ceddda9d
import aws_cdk.aws_s3_assets as _aws_cdk_aws_s3_assets_ceddda9d
import constructs as _constructs_77d1e7e8


@jsii.data_type(
    jsii_type="@aws-cdk/aws-synthetics-alpha.ArtifactsBucketLocation",
    jsii_struct_bases=[],
    name_mapping={"bucket": "bucket", "prefix": "prefix"},
)
class ArtifactsBucketLocation:
    def __init__(
        self,
        *,
        bucket: _aws_cdk_aws_s3_ceddda9d.IBucket,
        prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(deprecated) Options for specifying the s3 location that stores the data of each canary run.

        The artifacts bucket location **cannot**
        be updated once the canary is created.

        :param bucket: (deprecated) The s3 location that stores the data of each run.
        :param prefix: (deprecated) The S3 bucket prefix. Specify this if you want a more specific path within the artifacts bucket. Default: - no prefix

        :stability: deprecated
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_synthetics_alpha as synthetics_alpha
            from aws_cdk import aws_s3 as s3
            
            # bucket: s3.Bucket
            
            artifacts_bucket_location = synthetics_alpha.ArtifactsBucketLocation(
                bucket=bucket,
            
                # the properties below are optional
                prefix="prefix"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c97027ffb7c3e1ed6531ba25f1eb4e6e2af525b8b67b6ace4855effcca2b9919)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument prefix", value=prefix, expected_type=type_hints["prefix"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket": bucket,
        }
        if prefix is not None:
            self._values["prefix"] = prefix

    @builtins.property
    def bucket(self) -> _aws_cdk_aws_s3_ceddda9d.IBucket:
        '''(deprecated) The s3 location that stores the data of each run.

        :stability: deprecated
        '''
        result = self._values.get("bucket")
        assert result is not None, "Required property 'bucket' is missing"
        return typing.cast(_aws_cdk_aws_s3_ceddda9d.IBucket, result)

    @builtins.property
    def prefix(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The S3 bucket prefix.

        Specify this if you want a more specific path within the artifacts bucket.

        :default: - no prefix

        :stability: deprecated
        '''
        result = self._values.get("prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ArtifactsBucketLocation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_aws_cdk_aws_ec2_ceddda9d.IConnectable)
class Canary(
    _aws_cdk_ceddda9d.Resource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-synthetics-alpha.Canary",
):
    '''(deprecated) Define a new Canary.

    :stability: deprecated
    :exampleMetadata: infused

    Example::

        canary = synthetics.Canary(self, "MyCanary",
            schedule=synthetics.Schedule.rate(Duration.minutes(5)),
            test=synthetics.Test.custom(
                code=synthetics.Code.from_asset(path.join(__dirname, "canary")),
                handler="index.handler"
            ),
            runtime=synthetics.Runtime.SYNTHETICS_NODEJS_PUPPETEER_4_0,
            environment_variables={
                "stage": "prod"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        runtime: "Runtime",
        test: "Test",
        artifacts_bucket_lifecycle_rules: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_s3_ceddda9d.LifecycleRule, typing.Dict[builtins.str, typing.Any]]]] = None,
        artifacts_bucket_location: typing.Optional[typing.Union[ArtifactsBucketLocation, typing.Dict[builtins.str, typing.Any]]] = None,
        canary_name: typing.Optional[builtins.str] = None,
        cleanup: typing.Optional["Cleanup"] = None,
        enable_auto_delete_lambdas: typing.Optional[builtins.bool] = None,
        environment_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        failure_retention_period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        schedule: typing.Optional["Schedule"] = None,
        security_groups: typing.Optional[typing.Sequence[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup]] = None,
        start_after_creation: typing.Optional[builtins.bool] = None,
        success_retention_period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        time_to_live: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
        vpc_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param runtime: (deprecated) Specify the runtime version to use for the canary.
        :param test: (deprecated) The type of test that you want your canary to run. Use ``Test.custom()`` to specify the test to run.
        :param artifacts_bucket_lifecycle_rules: (deprecated) Lifecycle rules for the generated canary artifact bucket. Has no effect if a bucket is passed to ``artifactsBucketLocation``. If you pass a bucket to ``artifactsBucketLocation``, you can add lifecycle rules to the bucket itself. Default: - no rules applied to the generated bucket.
        :param artifacts_bucket_location: (deprecated) The s3 location that stores the data of the canary runs. Default: - A new s3 bucket will be created without a prefix.
        :param canary_name: (deprecated) The name of the canary. Be sure to give it a descriptive name that distinguishes it from other canaries in your account. Do not include secrets or proprietary information in your canary name. The canary name makes up part of the canary ARN, which is included in outbound calls over the internet. Default: - A unique name will be generated from the construct ID
        :param cleanup: (deprecated) Specify the underlying resources to be cleaned up when the canary is deleted. Using ``Cleanup.LAMBDA`` will create a Custom Resource to achieve this. Default: Cleanup.NOTHING
        :param enable_auto_delete_lambdas: (deprecated) Whether or not to delete the lambda resources when the canary is deleted. Default: false
        :param environment_variables: (deprecated) Key-value pairs that the Synthetics caches and makes available for your canary scripts. Use environment variables to apply configuration changes, such as test and production environment configurations, without changing your Canary script source code. Default: - No environment variables.
        :param failure_retention_period: (deprecated) How many days should failed runs be retained. Default: Duration.days(31)
        :param role: (deprecated) Canary execution role. This is the role that will be assumed by the canary upon execution. It controls the permissions that the canary will have. The role must be assumable by the AWS Lambda service principal. If not supplied, a role will be created with all the required permissions. If you provide a Role, you must add the required permissions. Default: - A unique role will be generated for this canary. You can add permissions to roles by calling 'addToRolePolicy'.
        :param schedule: (deprecated) Specify the schedule for how often the canary runs. For example, if you set ``schedule`` to ``rate(10 minutes)``, then the canary will run every 10 minutes. You can set the schedule with ``Schedule.rate(Duration)`` (recommended) or you can specify an expression using ``Schedule.expression()``. Default: 'rate(5 minutes)'
        :param security_groups: (deprecated) The list of security groups to associate with the canary's network interfaces. You must provide ``vpc`` when using this prop. Default: - If the canary is placed within a VPC and a security group is not specified a dedicated security group will be created for this canary.
        :param start_after_creation: (deprecated) Whether or not the canary should start after creation. Default: true
        :param success_retention_period: (deprecated) How many days should successful runs be retained. Default: Duration.days(31)
        :param time_to_live: (deprecated) How long the canary will be in a 'RUNNING' state. For example, if you set ``timeToLive`` to be 1 hour and ``schedule`` to be ``rate(10 minutes)``, your canary will run at 10 minute intervals for an hour, for a total of 6 times. Default: - no limit
        :param vpc: (deprecated) The VPC where this canary is run. Specify this if the canary needs to access resources in a VPC. Default: - Not in VPC
        :param vpc_subnets: (deprecated) Where to place the network interfaces within the VPC. You must provide ``vpc`` when using this prop. Default: - the Vpc default strategy if not specified

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77f74ffae78f48cc052608780149daa4ac131f47fdbfc7d99da3a7883cc0e8a3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CanaryProps(
            runtime=runtime,
            test=test,
            artifacts_bucket_lifecycle_rules=artifacts_bucket_lifecycle_rules,
            artifacts_bucket_location=artifacts_bucket_location,
            canary_name=canary_name,
            cleanup=cleanup,
            enable_auto_delete_lambdas=enable_auto_delete_lambdas,
            environment_variables=environment_variables,
            failure_retention_period=failure_retention_period,
            role=role,
            schedule=schedule,
            security_groups=security_groups,
            start_after_creation=start_after_creation,
            success_retention_period=success_retention_period,
            time_to_live=time_to_live,
            vpc=vpc,
            vpc_subnets=vpc_subnets,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="metricDuration")
    def metric_duration(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
        '''(deprecated) Measure the Duration of a single canary run, in seconds.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: avg over 5 minutes

        :stability: deprecated
        '''
        options = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricDuration", [options]))

    @jsii.member(jsii_name="metricFailed")
    def metric_failed(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
        '''(deprecated) Measure the number of failed canary runs over a given time period.

        Default: sum over 5 minutes

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: deprecated
        '''
        options = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricFailed", [options]))

    @jsii.member(jsii_name="metricSuccessPercent")
    def metric_success_percent(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_aws_cdk_aws_cloudwatch_ceddda9d.Unit] = None,
    ) -> _aws_cdk_aws_cloudwatch_ceddda9d.Metric:
        '''(deprecated) Measure the percentage of successful canary runs.

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :default: avg over 5 minutes

        :stability: deprecated
        '''
        options = _aws_cdk_aws_cloudwatch_ceddda9d.MetricOptions(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_aws_cdk_aws_cloudwatch_ceddda9d.Metric, jsii.invoke(self, "metricSuccessPercent", [options]))

    @builtins.property
    @jsii.member(jsii_name="artifactsBucket")
    def artifacts_bucket(self) -> _aws_cdk_aws_s3_ceddda9d.IBucket:
        '''(deprecated) Bucket where data from each canary run is stored.

        :stability: deprecated
        '''
        return typing.cast(_aws_cdk_aws_s3_ceddda9d.IBucket, jsii.get(self, "artifactsBucket"))

    @builtins.property
    @jsii.member(jsii_name="canaryId")
    def canary_id(self) -> builtins.str:
        '''(deprecated) The canary ID.

        :stability: deprecated
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "canaryId"))

    @builtins.property
    @jsii.member(jsii_name="canaryName")
    def canary_name(self) -> builtins.str:
        '''(deprecated) The canary Name.

        :stability: deprecated
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "canaryName"))

    @builtins.property
    @jsii.member(jsii_name="canaryState")
    def canary_state(self) -> builtins.str:
        '''(deprecated) The state of the canary.

        For example, 'RUNNING', 'STOPPED', 'NOT STARTED', or 'ERROR'.

        :stability: deprecated
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "canaryState"))

    @builtins.property
    @jsii.member(jsii_name="connections")
    def connections(self) -> _aws_cdk_aws_ec2_ceddda9d.Connections:
        '''(deprecated) Access the Connections object.

        Will fail if not a VPC-enabled Canary

        :stability: deprecated
        '''
        return typing.cast(_aws_cdk_aws_ec2_ceddda9d.Connections, jsii.get(self, "connections"))

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> _aws_cdk_aws_iam_ceddda9d.IRole:
        '''(deprecated) Execution role associated with this Canary.

        :stability: deprecated
        '''
        return typing.cast(_aws_cdk_aws_iam_ceddda9d.IRole, jsii.get(self, "role"))


@jsii.data_type(
    jsii_type="@aws-cdk/aws-synthetics-alpha.CanaryProps",
    jsii_struct_bases=[],
    name_mapping={
        "runtime": "runtime",
        "test": "test",
        "artifacts_bucket_lifecycle_rules": "artifactsBucketLifecycleRules",
        "artifacts_bucket_location": "artifactsBucketLocation",
        "canary_name": "canaryName",
        "cleanup": "cleanup",
        "enable_auto_delete_lambdas": "enableAutoDeleteLambdas",
        "environment_variables": "environmentVariables",
        "failure_retention_period": "failureRetentionPeriod",
        "role": "role",
        "schedule": "schedule",
        "security_groups": "securityGroups",
        "start_after_creation": "startAfterCreation",
        "success_retention_period": "successRetentionPeriod",
        "time_to_live": "timeToLive",
        "vpc": "vpc",
        "vpc_subnets": "vpcSubnets",
    },
)
class CanaryProps:
    def __init__(
        self,
        *,
        runtime: "Runtime",
        test: "Test",
        artifacts_bucket_lifecycle_rules: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_s3_ceddda9d.LifecycleRule, typing.Dict[builtins.str, typing.Any]]]] = None,
        artifacts_bucket_location: typing.Optional[typing.Union[ArtifactsBucketLocation, typing.Dict[builtins.str, typing.Any]]] = None,
        canary_name: typing.Optional[builtins.str] = None,
        cleanup: typing.Optional["Cleanup"] = None,
        enable_auto_delete_lambdas: typing.Optional[builtins.bool] = None,
        environment_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        failure_retention_period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
        schedule: typing.Optional["Schedule"] = None,
        security_groups: typing.Optional[typing.Sequence[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup]] = None,
        start_after_creation: typing.Optional[builtins.bool] = None,
        success_retention_period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        time_to_live: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
        vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
        vpc_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''(deprecated) Properties for a canary.

        :param runtime: (deprecated) Specify the runtime version to use for the canary.
        :param test: (deprecated) The type of test that you want your canary to run. Use ``Test.custom()`` to specify the test to run.
        :param artifacts_bucket_lifecycle_rules: (deprecated) Lifecycle rules for the generated canary artifact bucket. Has no effect if a bucket is passed to ``artifactsBucketLocation``. If you pass a bucket to ``artifactsBucketLocation``, you can add lifecycle rules to the bucket itself. Default: - no rules applied to the generated bucket.
        :param artifacts_bucket_location: (deprecated) The s3 location that stores the data of the canary runs. Default: - A new s3 bucket will be created without a prefix.
        :param canary_name: (deprecated) The name of the canary. Be sure to give it a descriptive name that distinguishes it from other canaries in your account. Do not include secrets or proprietary information in your canary name. The canary name makes up part of the canary ARN, which is included in outbound calls over the internet. Default: - A unique name will be generated from the construct ID
        :param cleanup: (deprecated) Specify the underlying resources to be cleaned up when the canary is deleted. Using ``Cleanup.LAMBDA`` will create a Custom Resource to achieve this. Default: Cleanup.NOTHING
        :param enable_auto_delete_lambdas: (deprecated) Whether or not to delete the lambda resources when the canary is deleted. Default: false
        :param environment_variables: (deprecated) Key-value pairs that the Synthetics caches and makes available for your canary scripts. Use environment variables to apply configuration changes, such as test and production environment configurations, without changing your Canary script source code. Default: - No environment variables.
        :param failure_retention_period: (deprecated) How many days should failed runs be retained. Default: Duration.days(31)
        :param role: (deprecated) Canary execution role. This is the role that will be assumed by the canary upon execution. It controls the permissions that the canary will have. The role must be assumable by the AWS Lambda service principal. If not supplied, a role will be created with all the required permissions. If you provide a Role, you must add the required permissions. Default: - A unique role will be generated for this canary. You can add permissions to roles by calling 'addToRolePolicy'.
        :param schedule: (deprecated) Specify the schedule for how often the canary runs. For example, if you set ``schedule`` to ``rate(10 minutes)``, then the canary will run every 10 minutes. You can set the schedule with ``Schedule.rate(Duration)`` (recommended) or you can specify an expression using ``Schedule.expression()``. Default: 'rate(5 minutes)'
        :param security_groups: (deprecated) The list of security groups to associate with the canary's network interfaces. You must provide ``vpc`` when using this prop. Default: - If the canary is placed within a VPC and a security group is not specified a dedicated security group will be created for this canary.
        :param start_after_creation: (deprecated) Whether or not the canary should start after creation. Default: true
        :param success_retention_period: (deprecated) How many days should successful runs be retained. Default: Duration.days(31)
        :param time_to_live: (deprecated) How long the canary will be in a 'RUNNING' state. For example, if you set ``timeToLive`` to be 1 hour and ``schedule`` to be ``rate(10 minutes)``, your canary will run at 10 minute intervals for an hour, for a total of 6 times. Default: - no limit
        :param vpc: (deprecated) The VPC where this canary is run. Specify this if the canary needs to access resources in a VPC. Default: - Not in VPC
        :param vpc_subnets: (deprecated) Where to place the network interfaces within the VPC. You must provide ``vpc`` when using this prop. Default: - the Vpc default strategy if not specified

        :stability: deprecated
        :exampleMetadata: infused

        Example::

            canary = synthetics.Canary(self, "MyCanary",
                schedule=synthetics.Schedule.rate(Duration.minutes(5)),
                test=synthetics.Test.custom(
                    code=synthetics.Code.from_asset(path.join(__dirname, "canary")),
                    handler="index.handler"
                ),
                runtime=synthetics.Runtime.SYNTHETICS_NODEJS_PUPPETEER_4_0,
                environment_variables={
                    "stage": "prod"
                }
            )
        '''
        if isinstance(artifacts_bucket_location, dict):
            artifacts_bucket_location = ArtifactsBucketLocation(**artifacts_bucket_location)
        if isinstance(vpc_subnets, dict):
            vpc_subnets = _aws_cdk_aws_ec2_ceddda9d.SubnetSelection(**vpc_subnets)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae7e63c36ba56bf570a16580ca3cc6aa4f4d25f66ba54d26f3f7a90413d04d63)
            check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
            check_type(argname="argument test", value=test, expected_type=type_hints["test"])
            check_type(argname="argument artifacts_bucket_lifecycle_rules", value=artifacts_bucket_lifecycle_rules, expected_type=type_hints["artifacts_bucket_lifecycle_rules"])
            check_type(argname="argument artifacts_bucket_location", value=artifacts_bucket_location, expected_type=type_hints["artifacts_bucket_location"])
            check_type(argname="argument canary_name", value=canary_name, expected_type=type_hints["canary_name"])
            check_type(argname="argument cleanup", value=cleanup, expected_type=type_hints["cleanup"])
            check_type(argname="argument enable_auto_delete_lambdas", value=enable_auto_delete_lambdas, expected_type=type_hints["enable_auto_delete_lambdas"])
            check_type(argname="argument environment_variables", value=environment_variables, expected_type=type_hints["environment_variables"])
            check_type(argname="argument failure_retention_period", value=failure_retention_period, expected_type=type_hints["failure_retention_period"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument start_after_creation", value=start_after_creation, expected_type=type_hints["start_after_creation"])
            check_type(argname="argument success_retention_period", value=success_retention_period, expected_type=type_hints["success_retention_period"])
            check_type(argname="argument time_to_live", value=time_to_live, expected_type=type_hints["time_to_live"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "runtime": runtime,
            "test": test,
        }
        if artifacts_bucket_lifecycle_rules is not None:
            self._values["artifacts_bucket_lifecycle_rules"] = artifacts_bucket_lifecycle_rules
        if artifacts_bucket_location is not None:
            self._values["artifacts_bucket_location"] = artifacts_bucket_location
        if canary_name is not None:
            self._values["canary_name"] = canary_name
        if cleanup is not None:
            self._values["cleanup"] = cleanup
        if enable_auto_delete_lambdas is not None:
            self._values["enable_auto_delete_lambdas"] = enable_auto_delete_lambdas
        if environment_variables is not None:
            self._values["environment_variables"] = environment_variables
        if failure_retention_period is not None:
            self._values["failure_retention_period"] = failure_retention_period
        if role is not None:
            self._values["role"] = role
        if schedule is not None:
            self._values["schedule"] = schedule
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if start_after_creation is not None:
            self._values["start_after_creation"] = start_after_creation
        if success_retention_period is not None:
            self._values["success_retention_period"] = success_retention_period
        if time_to_live is not None:
            self._values["time_to_live"] = time_to_live
        if vpc is not None:
            self._values["vpc"] = vpc
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets

    @builtins.property
    def runtime(self) -> "Runtime":
        '''(deprecated) Specify the runtime version to use for the canary.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_Library.html
        :stability: deprecated
        '''
        result = self._values.get("runtime")
        assert result is not None, "Required property 'runtime' is missing"
        return typing.cast("Runtime", result)

    @builtins.property
    def test(self) -> "Test":
        '''(deprecated) The type of test that you want your canary to run.

        Use ``Test.custom()`` to specify the test to run.

        :stability: deprecated
        '''
        result = self._values.get("test")
        assert result is not None, "Required property 'test' is missing"
        return typing.cast("Test", result)

    @builtins.property
    def artifacts_bucket_lifecycle_rules(
        self,
    ) -> typing.Optional[typing.List[_aws_cdk_aws_s3_ceddda9d.LifecycleRule]]:
        '''(deprecated) Lifecycle rules for the generated canary artifact bucket.

        Has no effect
        if a bucket is passed to ``artifactsBucketLocation``. If you pass a bucket
        to ``artifactsBucketLocation``, you can add lifecycle rules to the bucket
        itself.

        :default: - no rules applied to the generated bucket.

        :stability: deprecated
        '''
        result = self._values.get("artifacts_bucket_lifecycle_rules")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_s3_ceddda9d.LifecycleRule]], result)

    @builtins.property
    def artifacts_bucket_location(self) -> typing.Optional[ArtifactsBucketLocation]:
        '''(deprecated) The s3 location that stores the data of the canary runs.

        :default: - A new s3 bucket will be created without a prefix.

        :stability: deprecated
        '''
        result = self._values.get("artifacts_bucket_location")
        return typing.cast(typing.Optional[ArtifactsBucketLocation], result)

    @builtins.property
    def canary_name(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The name of the canary.

        Be sure to give it a descriptive name that distinguishes it from
        other canaries in your account.

        Do not include secrets or proprietary information in your canary name. The canary name
        makes up part of the canary ARN, which is included in outbound calls over the internet.

        :default: - A unique name will be generated from the construct ID

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/servicelens_canaries_security.html
        :stability: deprecated
        '''
        result = self._values.get("canary_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cleanup(self) -> typing.Optional["Cleanup"]:
        '''(deprecated) Specify the underlying resources to be cleaned up when the canary is deleted.

        Using ``Cleanup.LAMBDA`` will create a Custom Resource to achieve this.

        :default: Cleanup.NOTHING

        :stability: deprecated
        '''
        result = self._values.get("cleanup")
        return typing.cast(typing.Optional["Cleanup"], result)

    @builtins.property
    def enable_auto_delete_lambdas(self) -> typing.Optional[builtins.bool]:
        '''(deprecated) Whether or not to delete the lambda resources when the canary is deleted.

        :default: false

        :deprecated: this feature has been deprecated by the service team, use ``cleanup: Cleanup.LAMBDA`` instead which will use a Custom Resource to achieve the same effect.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-deletelambdaresourcesoncanarydeletion
        :stability: deprecated
        '''
        result = self._values.get("enable_auto_delete_lambdas")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def environment_variables(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''(deprecated) Key-value pairs that the Synthetics caches and makes available for your canary scripts.

        Use environment variables
        to apply configuration changes, such as test and production environment configurations, without changing your
        Canary script source code.

        :default: - No environment variables.

        :stability: deprecated
        '''
        result = self._values.get("environment_variables")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def failure_retention_period(self) -> typing.Optional[_aws_cdk_ceddda9d.Duration]:
        '''(deprecated) How many days should failed runs be retained.

        :default: Duration.days(31)

        :stability: deprecated
        '''
        result = self._values.get("failure_retention_period")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.Duration], result)

    @builtins.property
    def role(self) -> typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole]:
        '''(deprecated) Canary execution role.

        This is the role that will be assumed by the canary upon execution.
        It controls the permissions that the canary will have. The role must
        be assumable by the AWS Lambda service principal.

        If not supplied, a role will be created with all the required permissions.
        If you provide a Role, you must add the required permissions.

        :default:

        - A unique role will be generated for this canary.
        You can add permissions to roles by calling 'addToRolePolicy'.

        :see: required permissions: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-synthetics-canary.html#cfn-synthetics-canary-executionrolearn
        :stability: deprecated
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole], result)

    @builtins.property
    def schedule(self) -> typing.Optional["Schedule"]:
        '''(deprecated) Specify the schedule for how often the canary runs.

        For example, if you set ``schedule`` to ``rate(10 minutes)``, then the canary will run every 10 minutes.
        You can set the schedule with ``Schedule.rate(Duration)`` (recommended) or you can specify an expression using ``Schedule.expression()``.

        :default: 'rate(5 minutes)'

        :stability: deprecated
        '''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional["Schedule"], result)

    @builtins.property
    def security_groups(
        self,
    ) -> typing.Optional[typing.List[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup]]:
        '''(deprecated) The list of security groups to associate with the canary's network interfaces.

        You must provide ``vpc`` when using this prop.

        :default:

        - If the canary is placed within a VPC and a security group is
        not specified a dedicated security group will be created for this canary.

        :stability: deprecated
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup]], result)

    @builtins.property
    def start_after_creation(self) -> typing.Optional[builtins.bool]:
        '''(deprecated) Whether or not the canary should start after creation.

        :default: true

        :stability: deprecated
        '''
        result = self._values.get("start_after_creation")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def success_retention_period(self) -> typing.Optional[_aws_cdk_ceddda9d.Duration]:
        '''(deprecated) How many days should successful runs be retained.

        :default: Duration.days(31)

        :stability: deprecated
        '''
        result = self._values.get("success_retention_period")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.Duration], result)

    @builtins.property
    def time_to_live(self) -> typing.Optional[_aws_cdk_ceddda9d.Duration]:
        '''(deprecated) How long the canary will be in a 'RUNNING' state.

        For example, if you set ``timeToLive`` to be 1 hour and ``schedule`` to be ``rate(10 minutes)``,
        your canary will run at 10 minute intervals for an hour, for a total of 6 times.

        :default: - no limit

        :stability: deprecated
        '''
        result = self._values.get("time_to_live")
        return typing.cast(typing.Optional[_aws_cdk_ceddda9d.Duration], result)

    @builtins.property
    def vpc(self) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc]:
        '''(deprecated) The VPC where this canary is run.

        Specify this if the canary needs to access resources in a VPC.

        :default: - Not in VPC

        :stability: deprecated
        '''
        result = self._values.get("vpc")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection]:
        '''(deprecated) Where to place the network interfaces within the VPC.

        You must provide ``vpc`` when using this prop.

        :default: - the Vpc default strategy if not specified

        :stability: deprecated
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CanaryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="@aws-cdk/aws-synthetics-alpha.Cleanup")
class Cleanup(enum.Enum):
    '''(deprecated) Different ways to clean up underlying Canary resources when the Canary is deleted.

    :stability: deprecated
    :exampleMetadata: infused

    Example::

        canary = synthetics.Canary(self, "Canary",
            test=synthetics.Test.custom(
                handler="index.handler",
                code=synthetics.Code.from_inline("/* Synthetics handler code")
            ),
            cleanup=synthetics.Cleanup.LAMBDA,
            runtime=synthetics.Runtime.SYNTHETICS_NODEJS_PUPPETEER_4_0
        )
    '''

    NOTHING = "NOTHING"
    '''(deprecated) Clean up nothing.

    The user is responsible for cleaning up
    all resources left behind by the Canary.

    :stability: deprecated
    '''
    LAMBDA = "LAMBDA"
    '''(deprecated) Clean up the underlying Lambda function only.

    The user is
    responsible for cleaning up all other resources left behind
    by the Canary.

    :stability: deprecated
    '''


class Code(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="@aws-cdk/aws-synthetics-alpha.Code",
):
    '''(deprecated) The code the canary should execute.

    :stability: deprecated
    :exampleMetadata: infused

    Example::

        canary = synthetics.Canary(self, "MyCanary",
            schedule=synthetics.Schedule.rate(Duration.minutes(5)),
            test=synthetics.Test.custom(
                code=synthetics.Code.from_asset(path.join(__dirname, "canary")),
                handler="index.handler"
            ),
            runtime=synthetics.Runtime.SYNTHETICS_NODEJS_PUPPETEER_4_0,
            environment_variables={
                "stage": "prod"
            }
        )
    '''

    def __init__(self) -> None:
        '''
        :stability: deprecated
        '''
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="fromAsset")
    @builtins.classmethod
    def from_asset(
        cls,
        asset_path: builtins.str,
        *,
        deploy_time: typing.Optional[builtins.bool] = None,
        readers: typing.Optional[typing.Sequence[_aws_cdk_aws_iam_ceddda9d.IGrantable]] = None,
        asset_hash: typing.Optional[builtins.str] = None,
        asset_hash_type: typing.Optional[_aws_cdk_ceddda9d.AssetHashType] = None,
        bundling: typing.Optional[typing.Union[_aws_cdk_ceddda9d.BundlingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        follow_symlinks: typing.Optional[_aws_cdk_ceddda9d.SymlinkFollowMode] = None,
        ignore_mode: typing.Optional[_aws_cdk_ceddda9d.IgnoreMode] = None,
    ) -> "AssetCode":
        '''(deprecated) Specify code from a local path.

        Path must include the folder structure ``nodejs/node_modules/myCanaryFilename.js``.

        :param asset_path: Either a directory or a .zip file.
        :param deploy_time: Whether or not the asset needs to exist beyond deployment time; i.e. are copied over to a different location and not needed afterwards. Setting this property to true has an impact on the lifecycle of the asset, because we will assume that it is safe to delete after the CloudFormation deployment succeeds. For example, Lambda Function assets are copied over to Lambda during deployment. Therefore, it is not necessary to store the asset in S3, so we consider those deployTime assets. Default: false
        :param readers: A list of principals that should be able to read this asset from S3. You can use ``asset.grantRead(principal)`` to grant read permissions later. Default: - No principals that can read file asset.
        :param asset_hash: Specify a custom hash for this asset. If ``assetHashType`` is set it must be set to ``AssetHashType.CUSTOM``. For consistency, this custom hash will be SHA256 hashed and encoded as hex. The resulting hash will be the asset hash. NOTE: the hash is used in order to identify a specific revision of the asset, and used for optimizing and caching deployment activities related to this asset such as packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will need to make sure it is updated every time the asset changes, or otherwise it is possible that some deployments will not be invalidated. Default: - based on ``assetHashType``
        :param asset_hash_type: Specifies the type of hash to calculate for this asset. If ``assetHash`` is configured, this option must be ``undefined`` or ``AssetHashType.CUSTOM``. Default: - the default is ``AssetHashType.SOURCE``, but if ``assetHash`` is explicitly specified this value defaults to ``AssetHashType.CUSTOM``.
        :param bundling: Bundle the asset by executing a command in a Docker container or a custom bundling provider. The asset path will be mounted at ``/asset-input``. The Docker container is responsible for putting content at ``/asset-output``. The content at ``/asset-output`` will be zipped and used as the final asset. Default: - uploaded as-is to S3 if the asset is a regular file or a .zip file, archived into a .zip file and uploaded to S3 otherwise
        :param exclude: File paths matching the patterns will be excluded. See ``ignoreMode`` to set the matching behavior. Has no effect on Assets bundled using the ``bundling`` property. Default: - nothing is excluded
        :param follow_symlinks: A strategy for how to handle symlinks. Default: SymlinkFollowMode.NEVER
        :param ignore_mode: The ignore behavior to use for ``exclude`` patterns. Default: IgnoreMode.GLOB

        :return: ``AssetCode`` associated with the specified path.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_WritingCanary.html#CloudWatch_Synthetics_Canaries_write_from_scratch
        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c04ee0a7f625fce33d3003e388d6a831237f31cbc709e9c551a1bc356475ede)
            check_type(argname="argument asset_path", value=asset_path, expected_type=type_hints["asset_path"])
        options = _aws_cdk_aws_s3_assets_ceddda9d.AssetOptions(
            deploy_time=deploy_time,
            readers=readers,
            asset_hash=asset_hash,
            asset_hash_type=asset_hash_type,
            bundling=bundling,
            exclude=exclude,
            follow_symlinks=follow_symlinks,
            ignore_mode=ignore_mode,
        )

        return typing.cast("AssetCode", jsii.sinvoke(cls, "fromAsset", [asset_path, options]))

    @jsii.member(jsii_name="fromBucket")
    @builtins.classmethod
    def from_bucket(
        cls,
        bucket: _aws_cdk_aws_s3_ceddda9d.IBucket,
        key: builtins.str,
        object_version: typing.Optional[builtins.str] = None,
    ) -> "S3Code":
        '''(deprecated) Specify code from an s3 bucket.

        The object in the s3 bucket must be a .zip file that contains
        the structure ``nodejs/node_modules/myCanaryFilename.js``.

        :param bucket: The S3 bucket.
        :param key: The object key.
        :param object_version: Optional S3 object version.

        :return: ``S3Code`` associated with the specified S3 object.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_WritingCanary.html#CloudWatch_Synthetics_Canaries_write_from_scratch
        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__628908b4951e36d41574e89af118f4b8a140822fc9499275e081e1168a75bf43)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument object_version", value=object_version, expected_type=type_hints["object_version"])
        return typing.cast("S3Code", jsii.sinvoke(cls, "fromBucket", [bucket, key, object_version]))

    @jsii.member(jsii_name="fromInline")
    @builtins.classmethod
    def from_inline(cls, code: builtins.str) -> "InlineCode":
        '''(deprecated) Specify code inline.

        :param code: The actual handler code (limited to 5MB).

        :return: ``InlineCode`` with inline code.

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__534ebde2ca6177d2b07962ff163fa4be8fff02237e20a67c89fca238f2a43b12)
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
        return typing.cast("InlineCode", jsii.sinvoke(cls, "fromInline", [code]))

    @jsii.member(jsii_name="bind")
    @abc.abstractmethod
    def bind(
        self,
        scope: _constructs_77d1e7e8.Construct,
        handler: builtins.str,
        family: "RuntimeFamily",
    ) -> "CodeConfig":
        '''(deprecated) Called when the canary is initialized to allow this object to bind to the stack, add resources and have fun.

        :param scope: The binding scope. Don't be smart about trying to down-cast or assume it's initialized. You may just use it as a construct scope.
        :param handler: -
        :param family: -

        :return: a bound ``CodeConfig``.

        :stability: deprecated
        '''
        ...


class _CodeProxy(Code):
    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: _constructs_77d1e7e8.Construct,
        handler: builtins.str,
        family: "RuntimeFamily",
    ) -> "CodeConfig":
        '''(deprecated) Called when the canary is initialized to allow this object to bind to the stack, add resources and have fun.

        :param scope: The binding scope. Don't be smart about trying to down-cast or assume it's initialized. You may just use it as a construct scope.
        :param handler: -
        :param family: -

        :return: a bound ``CodeConfig``.

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d4fce9f2879e280253f79f346736f1e74cabefddf0199d5d40b9e187d207f46)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument handler", value=handler, expected_type=type_hints["handler"])
            check_type(argname="argument family", value=family, expected_type=type_hints["family"])
        return typing.cast("CodeConfig", jsii.invoke(self, "bind", [scope, handler, family]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Code).__jsii_proxy_class__ = lambda : _CodeProxy


@jsii.data_type(
    jsii_type="@aws-cdk/aws-synthetics-alpha.CodeConfig",
    jsii_struct_bases=[],
    name_mapping={"inline_code": "inlineCode", "s3_location": "s3Location"},
)
class CodeConfig:
    def __init__(
        self,
        *,
        inline_code: typing.Optional[builtins.str] = None,
        s3_location: typing.Optional[typing.Union[_aws_cdk_aws_s3_ceddda9d.Location, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''(deprecated) Configuration of the code class.

        :param inline_code: (deprecated) Inline code (mutually exclusive with ``s3Location``). Default: - none
        :param s3_location: (deprecated) The location of the code in S3 (mutually exclusive with ``inlineCode``). Default: - none

        :stability: deprecated
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk.aws_synthetics_alpha as synthetics_alpha
            
            code_config = synthetics_alpha.CodeConfig(
                inline_code="inlineCode",
                s3_location=Location(
                    bucket_name="bucketName",
                    object_key="objectKey",
            
                    # the properties below are optional
                    object_version="objectVersion"
                )
            )
        '''
        if isinstance(s3_location, dict):
            s3_location = _aws_cdk_aws_s3_ceddda9d.Location(**s3_location)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__651318556062d0bfa41111177f4d584c07af87721369012008e7234cd7a9bc9d)
            check_type(argname="argument inline_code", value=inline_code, expected_type=type_hints["inline_code"])
            check_type(argname="argument s3_location", value=s3_location, expected_type=type_hints["s3_location"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if inline_code is not None:
            self._values["inline_code"] = inline_code
        if s3_location is not None:
            self._values["s3_location"] = s3_location

    @builtins.property
    def inline_code(self) -> typing.Optional[builtins.str]:
        '''(deprecated) Inline code (mutually exclusive with ``s3Location``).

        :default: - none

        :stability: deprecated
        '''
        result = self._values.get("inline_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_location(self) -> typing.Optional[_aws_cdk_aws_s3_ceddda9d.Location]:
        '''(deprecated) The location of the code in S3 (mutually exclusive with ``inlineCode``).

        :default: - none

        :stability: deprecated
        '''
        result = self._values.get("s3_location")
        return typing.cast(typing.Optional[_aws_cdk_aws_s3_ceddda9d.Location], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CodeConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-synthetics-alpha.CronOptions",
    jsii_struct_bases=[],
    name_mapping={
        "day": "day",
        "hour": "hour",
        "minute": "minute",
        "month": "month",
        "week_day": "weekDay",
    },
)
class CronOptions:
    def __init__(
        self,
        *,
        day: typing.Optional[builtins.str] = None,
        hour: typing.Optional[builtins.str] = None,
        minute: typing.Optional[builtins.str] = None,
        month: typing.Optional[builtins.str] = None,
        week_day: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(deprecated) Options to configure a cron expression.

        All fields are strings so you can use complex expressions. Absence of
        a field implies '*' or '?', whichever one is appropriate.

        :param day: (deprecated) The day of the month to run this rule at. Default: - Every day of the month
        :param hour: (deprecated) The hour to run this rule at. Default: - Every hour
        :param minute: (deprecated) The minute to run this rule at. Default: - Every minute
        :param month: (deprecated) The month to run this rule at. Default: - Every month
        :param week_day: (deprecated) The day of the week to run this rule at. Default: - Any day of the week

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries_cron.html
        :stability: deprecated
        :exampleMetadata: infused

        Example::

            schedule = synthetics.Schedule.cron(
                hour="0,8,16"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__742d0a0d854616bacaf4bdd6a72aad127dcb8726f67f61aa6c6b3864b56f48d9)
            check_type(argname="argument day", value=day, expected_type=type_hints["day"])
            check_type(argname="argument hour", value=hour, expected_type=type_hints["hour"])
            check_type(argname="argument minute", value=minute, expected_type=type_hints["minute"])
            check_type(argname="argument month", value=month, expected_type=type_hints["month"])
            check_type(argname="argument week_day", value=week_day, expected_type=type_hints["week_day"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if day is not None:
            self._values["day"] = day
        if hour is not None:
            self._values["hour"] = hour
        if minute is not None:
            self._values["minute"] = minute
        if month is not None:
            self._values["month"] = month
        if week_day is not None:
            self._values["week_day"] = week_day

    @builtins.property
    def day(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The day of the month to run this rule at.

        :default: - Every day of the month

        :stability: deprecated
        '''
        result = self._values.get("day")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hour(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The hour to run this rule at.

        :default: - Every hour

        :stability: deprecated
        '''
        result = self._values.get("hour")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minute(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The minute to run this rule at.

        :default: - Every minute

        :stability: deprecated
        '''
        result = self._values.get("minute")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def month(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The month to run this rule at.

        :default: - Every month

        :stability: deprecated
        '''
        result = self._values.get("month")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def week_day(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The day of the week to run this rule at.

        :default: - Any day of the week

        :stability: deprecated
        '''
        result = self._values.get("week_day")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CronOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@aws-cdk/aws-synthetics-alpha.CustomTestOptions",
    jsii_struct_bases=[],
    name_mapping={"code": "code", "handler": "handler"},
)
class CustomTestOptions:
    def __init__(self, *, code: Code, handler: builtins.str) -> None:
        '''(deprecated) Properties for specifying a test.

        :param code: (deprecated) The code of the canary script.
        :param handler: (deprecated) The handler for the code. Must end with ``.handler``.

        :stability: deprecated
        :exampleMetadata: infused

        Example::

            canary = synthetics.Canary(self, "MyCanary",
                schedule=synthetics.Schedule.rate(Duration.minutes(5)),
                test=synthetics.Test.custom(
                    code=synthetics.Code.from_asset(path.join(__dirname, "canary")),
                    handler="index.handler"
                ),
                runtime=synthetics.Runtime.SYNTHETICS_NODEJS_PUPPETEER_4_0,
                environment_variables={
                    "stage": "prod"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d39435eead5e47a061f03cad4755b1155a750477abcae0773406c33664c00ba2)
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
            check_type(argname="argument handler", value=handler, expected_type=type_hints["handler"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "code": code,
            "handler": handler,
        }

    @builtins.property
    def code(self) -> Code:
        '''(deprecated) The code of the canary script.

        :stability: deprecated
        '''
        result = self._values.get("code")
        assert result is not None, "Required property 'code' is missing"
        return typing.cast(Code, result)

    @builtins.property
    def handler(self) -> builtins.str:
        '''(deprecated) The handler for the code.

        Must end with ``.handler``.

        :stability: deprecated
        '''
        result = self._values.get("handler")
        assert result is not None, "Required property 'handler' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomTestOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class InlineCode(
    Code,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-synthetics-alpha.InlineCode",
):
    '''(deprecated) Canary code from an inline string.

    :stability: deprecated
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_synthetics_alpha as synthetics_alpha
        
        inline_code = synthetics_alpha.InlineCode("code")
    '''

    def __init__(self, code: builtins.str) -> None:
        '''
        :param code: -

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da247d1ca5cbecd8aaea9b8c84a618be5cc639917820e7ecc42df6986fc5041c)
            check_type(argname="argument code", value=code, expected_type=type_hints["code"])
        jsii.create(self.__class__, self, [code])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: _constructs_77d1e7e8.Construct,
        handler: builtins.str,
        _family: "RuntimeFamily",
    ) -> CodeConfig:
        '''(deprecated) Called when the canary is initialized to allow this object to bind to the stack, add resources and have fun.

        :param _scope: -
        :param handler: -
        :param _family: -

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6275d20cffbb7f9580a932831ea3fe3cd5b65bfb421b1f8b04d770dc3508f7f3)
            check_type(argname="argument _scope", value=_scope, expected_type=type_hints["_scope"])
            check_type(argname="argument handler", value=handler, expected_type=type_hints["handler"])
            check_type(argname="argument _family", value=_family, expected_type=type_hints["_family"])
        return typing.cast(CodeConfig, jsii.invoke(self, "bind", [_scope, handler, _family]))


class Runtime(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-synthetics-alpha.Runtime",
):
    '''(deprecated) Runtime options for a canary.

    :stability: deprecated
    :exampleMetadata: infused

    Example::

        canary = synthetics.Canary(self, "MyCanary",
            schedule=synthetics.Schedule.rate(Duration.minutes(5)),
            test=synthetics.Test.custom(
                code=synthetics.Code.from_asset(path.join(__dirname, "canary")),
                handler="index.handler"
            ),
            runtime=synthetics.Runtime.SYNTHETICS_NODEJS_PUPPETEER_4_0,
            environment_variables={
                "stage": "prod"
            }
        )
    '''

    def __init__(self, name: builtins.str, family: "RuntimeFamily") -> None:
        '''
        :param name: The name of the runtime version.
        :param family: The Lambda runtime family.

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f432dbd029db5a952a9c04e6756b31fce0e5e19c4f214b45729fe31a4228a68)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument family", value=family, expected_type=type_hints["family"])
        jsii.create(self.__class__, self, [name, family])

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_1_0")
    def SYNTHETICS_1_0(cls) -> "Runtime":
        '''(deprecated) **Deprecated by AWS Synthetics. You can't create canaries with deprecated runtimes.**.

        ``syn-1.0`` includes the following:

        - Synthetics library 1.0
        - Synthetics handler code 1.0
        - Lambda runtime Node.js 10.x
        - Puppeteer-core version 1.14.0
        - The Chromium version that matches Puppeteer-core 1.14.0

        :deprecated: Use the latest version instead

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_nodejs_puppeteer.html#CloudWatch_Synthetics_runtimeversion-1.0
        :stability: deprecated
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_1_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_NODEJS_2_0")
    def SYNTHETICS_NODEJS_2_0(cls) -> "Runtime":
        '''(deprecated) **Deprecated by AWS Synthetics. You can't create canaries with deprecated runtimes.**.

        ``syn-nodejs-2.0`` includes the following:

        - Lambda runtime Node.js 10.x
        - Puppeteer-core version 3.3.0
        - Chromium version 83.0.4103.0

        :deprecated: Use the latest version instead

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_nodejs_puppeteer.html#CloudWatch_Synthetics_runtimeversion-2.0
        :stability: deprecated
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_NODEJS_2_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_NODEJS_2_1")
    def SYNTHETICS_NODEJS_2_1(cls) -> "Runtime":
        '''(deprecated) **Deprecated by AWS Synthetics. You can't create canaries with deprecated runtimes.**.

        ``syn-nodejs-2.1`` includes the following:

        - Lambda runtime Node.js 10.x
        - Puppeteer-core version 3.3.0
        - Chromium version 83.0.4103.0

        :deprecated: Use the latest version instead

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_nodejs_puppeteer.html#CloudWatch_Synthetics_runtimeversion-2.1
        :stability: deprecated
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_NODEJS_2_1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_NODEJS_2_2")
    def SYNTHETICS_NODEJS_2_2(cls) -> "Runtime":
        '''(deprecated) **Deprecated by AWS Synthetics. You can't create canaries with deprecated runtimes.**.

        ``syn-nodejs-2.2`` includes the following:

        - Lambda runtime Node.js 10.x
        - Puppeteer-core version 3.3.0
        - Chromium version 83.0.4103.0

        :deprecated: Use the latest version instead

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_nodejs_puppeteer.html#CloudWatch_Synthetics_runtimeversion-2.2
        :stability: deprecated
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_NODEJS_2_2"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_NODEJS_PUPPETEER_3_0")
    def SYNTHETICS_NODEJS_PUPPETEER_3_0(cls) -> "Runtime":
        '''(deprecated) **Deprecated by AWS Synthetics. You can't create canaries with deprecated runtimes.**.

        ``syn-nodejs-puppeteer-3.0`` includes the following:

        - Lambda runtime Node.js 12.x
        - Puppeteer-core version 5.5.0
        - Chromium version 88.0.4298.0

        :deprecated: Use the latest version instead

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_nodejs_puppeteer.html#CloudWatch_Synthetics_runtimeversion-nodejs-puppeteer-3.0
        :stability: deprecated
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_NODEJS_PUPPETEER_3_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_NODEJS_PUPPETEER_3_1")
    def SYNTHETICS_NODEJS_PUPPETEER_3_1(cls) -> "Runtime":
        '''(deprecated) **Deprecated by AWS Synthetics. You can't create canaries with deprecated runtimes.**.

        ``syn-nodejs-puppeteer-3.1`` includes the following:

        - Lambda runtime Node.js 12.x
        - Puppeteer-core version 5.5.0
        - Chromium version 88.0.4298.0

        :deprecated: Use the latest version instead

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_nodejs_puppeteer.html#CloudWatch_Synthetics_runtimeversion-nodejs-puppeteer-3.1
        :stability: deprecated
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_NODEJS_PUPPETEER_3_1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_NODEJS_PUPPETEER_3_2")
    def SYNTHETICS_NODEJS_PUPPETEER_3_2(cls) -> "Runtime":
        '''(deprecated) **Deprecated by AWS Synthetics. You can't create canaries with deprecated runtimes.**.

        ``syn-nodejs-puppeteer-3.2`` includes the following:

        - Lambda runtime Node.js 12.x
        - Puppeteer-core version 5.5.0
        - Chromium version 88.0.4298.0

        :deprecated: Use the latest version instead

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_nodejs_puppeteer.html#CloudWatch_Synthetics_runtimeversion-nodejs-puppeteer-3.2
        :stability: deprecated
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_NODEJS_PUPPETEER_3_2"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_NODEJS_PUPPETEER_3_3")
    def SYNTHETICS_NODEJS_PUPPETEER_3_3(cls) -> "Runtime":
        '''(deprecated) ``syn-nodejs-puppeteer-3.3`` includes the following: **Deprecated by AWS Synthetics. You can't create canaries with deprecated runtimes.**.

        - Lambda runtime Node.js 12.x
        - Puppeteer-core version 5.5.0
        - Chromium version 88.0.4298.0

        :deprecated: Use the latest version instead

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_nodejs_puppeteer.html#CloudWatch_Synthetics_runtimeversion-nodejs-puppeteer-3.3
        :stability: deprecated
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_NODEJS_PUPPETEER_3_3"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_NODEJS_PUPPETEER_3_4")
    def SYNTHETICS_NODEJS_PUPPETEER_3_4(cls) -> "Runtime":
        '''(deprecated) **Deprecated by AWS Synthetics. You can't create canaries with deprecated runtimes.**.

        ``syn-nodejs-puppeteer-3.4`` includes the following:

        - Lambda runtime Node.js 12.x
        - Puppeteer-core version 5.5.0
        - Chromium version 88.0.4298.0

        :deprecated: Use the latest version instead

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_nodejs_puppeteer.html#CloudWatch_Synthetics_runtimeversion-nodejs-puppeteer-3.4
        :stability: deprecated
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_NODEJS_PUPPETEER_3_4"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_NODEJS_PUPPETEER_3_5")
    def SYNTHETICS_NODEJS_PUPPETEER_3_5(cls) -> "Runtime":
        '''(deprecated) ``syn-nodejs-puppeteer-3.5`` includes the following: - Lambda runtime Node.js 14.x - Puppeteer-core version 10.1.0 - Chromium version 92.0.4512.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_nodejs_puppeteer.html#CloudWatch_Synthetics_runtimeversion-nodejs-puppeteer-3.5
        :stability: deprecated
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_NODEJS_PUPPETEER_3_5"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_NODEJS_PUPPETEER_3_6")
    def SYNTHETICS_NODEJS_PUPPETEER_3_6(cls) -> "Runtime":
        '''(deprecated) ``syn-nodejs-puppeteer-3.6`` includes the following: - Lambda runtime Node.js 14.x - Puppeteer-core version 10.1.0 - Chromium version 92.0.4512.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_nodejs_puppeteer.html#CloudWatch_Synthetics_runtimeversion-nodejs-puppeteer-3.6
        :stability: deprecated
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_NODEJS_PUPPETEER_3_6"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_NODEJS_PUPPETEER_3_7")
    def SYNTHETICS_NODEJS_PUPPETEER_3_7(cls) -> "Runtime":
        '''(deprecated) ``syn-nodejs-puppeteer-3.7`` includes the following: - Lambda runtime Node.js 14.x - Puppeteer-core version 10.1.0 - Chromium version 92.0.4512.

        New Features:

        - **Logging enhancement**: The canary will upload logs to Amazon S3 even if it times out or crashes.
        - **Lambda layer size reduced**: The size of the Lambda layer used for canaries is reduced by 34%.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_nodejs_puppeteer.html#CloudWatch_Synthetics_runtimeversion-nodejs-puppeteer-3.7
        :stability: deprecated
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_NODEJS_PUPPETEER_3_7"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_NODEJS_PUPPETEER_3_8")
    def SYNTHETICS_NODEJS_PUPPETEER_3_8(cls) -> "Runtime":
        '''(deprecated) ``syn-nodejs-puppeteer-3.8`` includes the following: - Lambda runtime Node.js 14.x - Puppeteer-core version 10.1.0 - Chromium version 92.0.4512.

        New Features:

        - **Profile cleanup**: Chromium profiles are now cleaned up after each canary run.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_nodejs_puppeteer.html#CloudWatch_Synthetics_runtimeversion-nodejs-puppeteer-3.8
        :stability: deprecated
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_NODEJS_PUPPETEER_3_8"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_NODEJS_PUPPETEER_3_9")
    def SYNTHETICS_NODEJS_PUPPETEER_3_9(cls) -> "Runtime":
        '''(deprecated) ``syn-nodejs-puppeteer-3.9`` includes the following:.

        - Lambda runtime Node.js 14.x
        - Puppeteer-core version 5.5.0
        - Chromium version 92.0.4512

        New Features:

        - **Dependency upgrades**: Upgrades some third-party dependency packages.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_nodejs_puppeteer.html#CloudWatch_Synthetics_runtimeversion-nodejs-puppeteer-3.9
        :stability: deprecated
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_NODEJS_PUPPETEER_3_9"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_NODEJS_PUPPETEER_4_0")
    def SYNTHETICS_NODEJS_PUPPETEER_4_0(cls) -> "Runtime":
        '''(deprecated) ``syn-nodejs-puppeteer-4.0`` includes the following: - Lambda runtime Node.js 16.x - Puppeteer-core version 5.5.0 - Chromium version 92.0.4512.

        New Features:

        - **Dependency upgrades**: The Node.js dependency is updated to 16.x.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_nodejs_puppeteer.html#CloudWatch_Synthetics_runtimeversion-nodejs-puppeteer-4.0
        :stability: deprecated
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_NODEJS_PUPPETEER_4_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_NODEJS_PUPPETEER_5_0")
    def SYNTHETICS_NODEJS_PUPPETEER_5_0(cls) -> "Runtime":
        '''(deprecated) ``syn-nodejs-puppeteer-5.0`` includes the following: - Lambda runtime Node.js 16.x - Puppeteer-core version 19.7.0 - Chromium version 111.0.5563.146.

        New Features:

        - **Dependency upgrade**: The Puppeteer-core version is updated to 19.7.0. The Chromium version is upgraded to 111.0.5563.146.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_nodejs_puppeteer.html#CloudWatch_Synthetics_runtimeversion-nodejs-puppeteer-5.0
        :stability: deprecated
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_NODEJS_PUPPETEER_5_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_NODEJS_PUPPETEER_5_1")
    def SYNTHETICS_NODEJS_PUPPETEER_5_1(cls) -> "Runtime":
        '''(deprecated) ``syn-nodejs-puppeteer-5.1`` includes the following: - Lambda runtime Node.js 16.x - Puppeteer-core version 19.7.0 - Chromium version 111.0.5563.146.

        Bug fixes:

        - **Bug fix**: This runtime fixes a bug in ``syn-nodejs-puppeteer-5.0`` where the HAR files created by the canaries were missing request headers.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_nodejs_puppeteer.html#CloudWatch_Synthetics_runtimeversion-nodejs-puppeteer-5.1
        :stability: deprecated
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_NODEJS_PUPPETEER_5_1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_PYTHON_SELENIUM_1_0")
    def SYNTHETICS_PYTHON_SELENIUM_1_0(cls) -> "Runtime":
        '''(deprecated) ``syn-python-selenium-1.0`` includes the following: - Lambda runtime Python 3.8 - Selenium version 3.141.0 - Chromium version 83.0.4103.0.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_python_selenium.html#CloudWatch_Synthetics_runtimeversion-syn-python-selenium-1.0
        :stability: deprecated
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_PYTHON_SELENIUM_1_0"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_PYTHON_SELENIUM_1_1")
    def SYNTHETICS_PYTHON_SELENIUM_1_1(cls) -> "Runtime":
        '''(deprecated) ``syn-python-selenium-1.1`` includes the following: - Lambda runtime Python 3.8 - Selenium version 3.141.0 - Chromium version 83.0.4103.0.

        New Features:

        - **Custom handler function**: You can now use a custom handler function for your canary scripts.
        - **Configuration options for adding metrics and step failure configurations**: These options were already available in runtimes for Node.js canaries.
        - **Custom arguments in Chrome**: You can now open a browser in incognito mode or pass in proxy server configuration.
        - **Cross-Region artifact buckets**: A canary can store its artifacts in an Amazon S3 bucket in a different Region.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_python_selenium.html#CloudWatch_Synthetics_runtimeversion-syn-python-selenium-1.1
        :stability: deprecated
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_PYTHON_SELENIUM_1_1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_PYTHON_SELENIUM_1_2")
    def SYNTHETICS_PYTHON_SELENIUM_1_2(cls) -> "Runtime":
        '''(deprecated) ``syn-python-selenium-1.2`` includes the following: - Lambda runtime Python 3.8 - Selenium version 3.141.0 - Chromium version 92.0.4512.0.

        New Features:

        - **Updated dependencies**: The only new features in this runtime are the updated dependencies.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_python_selenium.html#CloudWatch_Synthetics_runtimeversion-syn-python-selenium-1.2
        :stability: deprecated
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_PYTHON_SELENIUM_1_2"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="SYNTHETICS_PYTHON_SELENIUM_1_3")
    def SYNTHETICS_PYTHON_SELENIUM_1_3(cls) -> "Runtime":
        '''(deprecated) ``syn-python-selenium-1.3`` includes the following: - Lambda runtime Python 3.8 - Selenium version 3.141.0 - Chromium version 92.0.4512.0.

        New Features:

        - **More precise timestamps**: The start time and stop time of canary runs are now precise to the millisecond.

        :see: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Library_python_selenium.html#CloudWatch_Synthetics_runtimeversion-syn-python-selenium-1.3
        :stability: deprecated
        '''
        return typing.cast("Runtime", jsii.sget(cls, "SYNTHETICS_PYTHON_SELENIUM_1_3"))

    @builtins.property
    @jsii.member(jsii_name="family")
    def family(self) -> "RuntimeFamily":
        '''(deprecated) The Lambda runtime family.

        :stability: deprecated
        '''
        return typing.cast("RuntimeFamily", jsii.get(self, "family"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''(deprecated) The name of the runtime version.

        :stability: deprecated
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))


@jsii.enum(jsii_type="@aws-cdk/aws-synthetics-alpha.RuntimeFamily")
class RuntimeFamily(enum.Enum):
    '''(deprecated) All known Lambda runtime families.

    :stability: deprecated
    '''

    NODEJS = "NODEJS"
    '''(deprecated) All Lambda runtimes that depend on Node.js.

    :stability: deprecated
    '''
    PYTHON = "PYTHON"
    '''(deprecated) All lambda runtimes that depend on Python.

    :stability: deprecated
    '''
    OTHER = "OTHER"
    '''(deprecated) Any future runtime family.

    :stability: deprecated
    '''


class S3Code(
    Code,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-synthetics-alpha.S3Code",
):
    '''(deprecated) S3 bucket path to the code zip file.

    :stability: deprecated
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_synthetics_alpha as synthetics_alpha
        from aws_cdk import aws_s3 as s3
        
        # bucket: s3.Bucket
        
        s3_code = synthetics_alpha.S3Code(bucket, "key", "objectVersion")
    '''

    def __init__(
        self,
        bucket: _aws_cdk_aws_s3_ceddda9d.IBucket,
        key: builtins.str,
        object_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: -
        :param key: -
        :param object_version: -

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b38ad713f473c7c074c298bcd50e4520db7596d9bbfee5b75e35fd29ecc2ae71)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
            check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            check_type(argname="argument object_version", value=object_version, expected_type=type_hints["object_version"])
        jsii.create(self.__class__, self, [bucket, key, object_version])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: _constructs_77d1e7e8.Construct,
        _handler: builtins.str,
        _family: RuntimeFamily,
    ) -> CodeConfig:
        '''(deprecated) Called when the canary is initialized to allow this object to bind to the stack, add resources and have fun.

        :param _scope: -
        :param _handler: -
        :param _family: -

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5715f987d53b5baf64123cc83ba9844c119abb443bcd5f14c619000f4687689b)
            check_type(argname="argument _scope", value=_scope, expected_type=type_hints["_scope"])
            check_type(argname="argument _handler", value=_handler, expected_type=type_hints["_handler"])
            check_type(argname="argument _family", value=_family, expected_type=type_hints["_family"])
        return typing.cast(CodeConfig, jsii.invoke(self, "bind", [_scope, _handler, _family]))


class Schedule(
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-synthetics-alpha.Schedule",
):
    '''(deprecated) Schedule for canary runs.

    :stability: deprecated
    :exampleMetadata: infused

    Example::

        canary = synthetics.Canary(self, "MyCanary",
            schedule=synthetics.Schedule.rate(Duration.minutes(5)),
            test=synthetics.Test.custom(
                code=synthetics.Code.from_asset(path.join(__dirname, "canary")),
                handler="index.handler"
            ),
            runtime=synthetics.Runtime.SYNTHETICS_NODEJS_PUPPETEER_4_0,
            environment_variables={
                "stage": "prod"
            }
        )
    '''

    @jsii.member(jsii_name="cron")
    @builtins.classmethod
    def cron(
        cls,
        *,
        day: typing.Optional[builtins.str] = None,
        hour: typing.Optional[builtins.str] = None,
        minute: typing.Optional[builtins.str] = None,
        month: typing.Optional[builtins.str] = None,
        week_day: typing.Optional[builtins.str] = None,
    ) -> "Schedule":
        '''(deprecated) Create a schedule from a set of cron fields.

        :param day: (deprecated) The day of the month to run this rule at. Default: - Every day of the month
        :param hour: (deprecated) The hour to run this rule at. Default: - Every hour
        :param minute: (deprecated) The minute to run this rule at. Default: - Every minute
        :param month: (deprecated) The month to run this rule at. Default: - Every month
        :param week_day: (deprecated) The day of the week to run this rule at. Default: - Any day of the week

        :stability: deprecated
        '''
        options = CronOptions(
            day=day, hour=hour, minute=minute, month=month, week_day=week_day
        )

        return typing.cast("Schedule", jsii.sinvoke(cls, "cron", [options]))

    @jsii.member(jsii_name="expression")
    @builtins.classmethod
    def expression(cls, expression: builtins.str) -> "Schedule":
        '''(deprecated) Construct a schedule from a literal schedule expression.

        The expression must be in a ``rate(number units)`` format.
        For example, ``Schedule.expression('rate(10 minutes)')``

        :param expression: The expression to use.

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67f4f45e1902e3d8ba8eb545d45bd88f6630cdbcfd293fb8ce069c9a9d32e633)
            check_type(argname="argument expression", value=expression, expected_type=type_hints["expression"])
        return typing.cast("Schedule", jsii.sinvoke(cls, "expression", [expression]))

    @jsii.member(jsii_name="once")
    @builtins.classmethod
    def once(cls) -> "Schedule":
        '''(deprecated) The canary will be executed once.

        :stability: deprecated
        '''
        return typing.cast("Schedule", jsii.sinvoke(cls, "once", []))

    @jsii.member(jsii_name="rate")
    @builtins.classmethod
    def rate(cls, interval: _aws_cdk_ceddda9d.Duration) -> "Schedule":
        '''(deprecated) Construct a schedule from an interval.

        Allowed values: 0 (for a single run) or between 1 and 60 minutes.
        To specify a single run, you can use ``Schedule.once()``.

        :param interval: The interval at which to run the canary.

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed81e99d860f614edbd9653f58417542e72548f67d8562ec60e3581ea3c1b7a5)
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
        return typing.cast("Schedule", jsii.sinvoke(cls, "rate", [interval]))

    @builtins.property
    @jsii.member(jsii_name="expressionString")
    def expression_string(self) -> builtins.str:
        '''(deprecated) The Schedule expression.

        :stability: deprecated
        '''
        return typing.cast(builtins.str, jsii.get(self, "expressionString"))


class Test(metaclass=jsii.JSIIMeta, jsii_type="@aws-cdk/aws-synthetics-alpha.Test"):
    '''(deprecated) Specify a test that the canary should run.

    :stability: deprecated
    :exampleMetadata: infused

    Example::

        canary = synthetics.Canary(self, "MyCanary",
            schedule=synthetics.Schedule.rate(Duration.minutes(5)),
            test=synthetics.Test.custom(
                code=synthetics.Code.from_asset(path.join(__dirname, "canary")),
                handler="index.handler"
            ),
            runtime=synthetics.Runtime.SYNTHETICS_NODEJS_PUPPETEER_4_0,
            environment_variables={
                "stage": "prod"
            }
        )
    '''

    @jsii.member(jsii_name="custom")
    @builtins.classmethod
    def custom(cls, *, code: Code, handler: builtins.str) -> "Test":
        '''(deprecated) Specify a custom test with your own code.

        :param code: (deprecated) The code of the canary script.
        :param handler: (deprecated) The handler for the code. Must end with ``.handler``.

        :return: ``Test`` associated with the specified Code object

        :stability: deprecated
        '''
        options = CustomTestOptions(code=code, handler=handler)

        return typing.cast("Test", jsii.sinvoke(cls, "custom", [options]))

    @builtins.property
    @jsii.member(jsii_name="code")
    def code(self) -> Code:
        '''(deprecated) The code that the canary should run.

        :stability: deprecated
        '''
        return typing.cast(Code, jsii.get(self, "code"))

    @builtins.property
    @jsii.member(jsii_name="handler")
    def handler(self) -> builtins.str:
        '''(deprecated) The handler of the canary.

        :stability: deprecated
        '''
        return typing.cast(builtins.str, jsii.get(self, "handler"))


class AssetCode(
    Code,
    metaclass=jsii.JSIIMeta,
    jsii_type="@aws-cdk/aws-synthetics-alpha.AssetCode",
):
    '''(deprecated) Canary code from an Asset.

    :stability: deprecated
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk.aws_synthetics_alpha as synthetics_alpha
        import aws_cdk as cdk
        from aws_cdk import aws_iam as iam
        
        # docker_image: cdk.DockerImage
        # grantable: iam.IGrantable
        # local_bundling: cdk.ILocalBundling
        
        asset_code = synthetics_alpha.AssetCode("assetPath",
            asset_hash="assetHash",
            asset_hash_type=cdk.AssetHashType.SOURCE,
            bundling=cdk.BundlingOptions(
                image=docker_image,
        
                # the properties below are optional
                bundling_file_access=cdk.BundlingFileAccess.VOLUME_COPY,
                command=["command"],
                entrypoint=["entrypoint"],
                environment={
                    "environment_key": "environment"
                },
                local=local_bundling,
                network="network",
                output_type=cdk.BundlingOutput.ARCHIVED,
                platform="platform",
                security_opt="securityOpt",
                user="user",
                volumes=[cdk.DockerVolume(
                    container_path="containerPath",
                    host_path="hostPath",
        
                    # the properties below are optional
                    consistency=cdk.DockerVolumeConsistency.CONSISTENT
                )],
                volumes_from=["volumesFrom"],
                working_directory="workingDirectory"
            ),
            deploy_time=False,
            exclude=["exclude"],
            follow_symlinks=cdk.SymlinkFollowMode.NEVER,
            ignore_mode=cdk.IgnoreMode.GLOB,
            readers=[grantable]
        )
    '''

    def __init__(
        self,
        asset_path: builtins.str,
        *,
        deploy_time: typing.Optional[builtins.bool] = None,
        readers: typing.Optional[typing.Sequence[_aws_cdk_aws_iam_ceddda9d.IGrantable]] = None,
        asset_hash: typing.Optional[builtins.str] = None,
        asset_hash_type: typing.Optional[_aws_cdk_ceddda9d.AssetHashType] = None,
        bundling: typing.Optional[typing.Union[_aws_cdk_ceddda9d.BundlingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
        exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
        follow_symlinks: typing.Optional[_aws_cdk_ceddda9d.SymlinkFollowMode] = None,
        ignore_mode: typing.Optional[_aws_cdk_ceddda9d.IgnoreMode] = None,
    ) -> None:
        '''
        :param asset_path: The path to the asset file or directory.
        :param deploy_time: Whether or not the asset needs to exist beyond deployment time; i.e. are copied over to a different location and not needed afterwards. Setting this property to true has an impact on the lifecycle of the asset, because we will assume that it is safe to delete after the CloudFormation deployment succeeds. For example, Lambda Function assets are copied over to Lambda during deployment. Therefore, it is not necessary to store the asset in S3, so we consider those deployTime assets. Default: false
        :param readers: A list of principals that should be able to read this asset from S3. You can use ``asset.grantRead(principal)`` to grant read permissions later. Default: - No principals that can read file asset.
        :param asset_hash: Specify a custom hash for this asset. If ``assetHashType`` is set it must be set to ``AssetHashType.CUSTOM``. For consistency, this custom hash will be SHA256 hashed and encoded as hex. The resulting hash will be the asset hash. NOTE: the hash is used in order to identify a specific revision of the asset, and used for optimizing and caching deployment activities related to this asset such as packaging, uploading to Amazon S3, etc. If you chose to customize the hash, you will need to make sure it is updated every time the asset changes, or otherwise it is possible that some deployments will not be invalidated. Default: - based on ``assetHashType``
        :param asset_hash_type: Specifies the type of hash to calculate for this asset. If ``assetHash`` is configured, this option must be ``undefined`` or ``AssetHashType.CUSTOM``. Default: - the default is ``AssetHashType.SOURCE``, but if ``assetHash`` is explicitly specified this value defaults to ``AssetHashType.CUSTOM``.
        :param bundling: Bundle the asset by executing a command in a Docker container or a custom bundling provider. The asset path will be mounted at ``/asset-input``. The Docker container is responsible for putting content at ``/asset-output``. The content at ``/asset-output`` will be zipped and used as the final asset. Default: - uploaded as-is to S3 if the asset is a regular file or a .zip file, archived into a .zip file and uploaded to S3 otherwise
        :param exclude: File paths matching the patterns will be excluded. See ``ignoreMode`` to set the matching behavior. Has no effect on Assets bundled using the ``bundling`` property. Default: - nothing is excluded
        :param follow_symlinks: A strategy for how to handle symlinks. Default: SymlinkFollowMode.NEVER
        :param ignore_mode: The ignore behavior to use for ``exclude`` patterns. Default: IgnoreMode.GLOB

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8bf4f7b9198aa65c5cde28608e12d3a1aaeec0ce84754b8fbb221ea9a3432c7d)
            check_type(argname="argument asset_path", value=asset_path, expected_type=type_hints["asset_path"])
        options = _aws_cdk_aws_s3_assets_ceddda9d.AssetOptions(
            deploy_time=deploy_time,
            readers=readers,
            asset_hash=asset_hash,
            asset_hash_type=asset_hash_type,
            bundling=bundling,
            exclude=exclude,
            follow_symlinks=follow_symlinks,
            ignore_mode=ignore_mode,
        )

        jsii.create(self.__class__, self, [asset_path, options])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: _constructs_77d1e7e8.Construct,
        handler: builtins.str,
        family: RuntimeFamily,
    ) -> CodeConfig:
        '''(deprecated) Called when the canary is initialized to allow this object to bind to the stack, add resources and have fun.

        :param scope: -
        :param handler: -
        :param family: -

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__143fc4bffb5cfb09c7d51862845fedf3824b9a58f7e721a8ed7a6f4907e17f47)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument handler", value=handler, expected_type=type_hints["handler"])
            check_type(argname="argument family", value=family, expected_type=type_hints["family"])
        return typing.cast(CodeConfig, jsii.invoke(self, "bind", [scope, handler, family]))


__all__ = [
    "ArtifactsBucketLocation",
    "AssetCode",
    "Canary",
    "CanaryProps",
    "Cleanup",
    "Code",
    "CodeConfig",
    "CronOptions",
    "CustomTestOptions",
    "InlineCode",
    "Runtime",
    "RuntimeFamily",
    "S3Code",
    "Schedule",
    "Test",
]

publication.publish()

def _typecheckingstub__c97027ffb7c3e1ed6531ba25f1eb4e6e2af525b8b67b6ace4855effcca2b9919(
    *,
    bucket: _aws_cdk_aws_s3_ceddda9d.IBucket,
    prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77f74ffae78f48cc052608780149daa4ac131f47fdbfc7d99da3a7883cc0e8a3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    runtime: Runtime,
    test: Test,
    artifacts_bucket_lifecycle_rules: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_s3_ceddda9d.LifecycleRule, typing.Dict[builtins.str, typing.Any]]]] = None,
    artifacts_bucket_location: typing.Optional[typing.Union[ArtifactsBucketLocation, typing.Dict[builtins.str, typing.Any]]] = None,
    canary_name: typing.Optional[builtins.str] = None,
    cleanup: typing.Optional[Cleanup] = None,
    enable_auto_delete_lambdas: typing.Optional[builtins.bool] = None,
    environment_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    failure_retention_period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    schedule: typing.Optional[Schedule] = None,
    security_groups: typing.Optional[typing.Sequence[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup]] = None,
    start_after_creation: typing.Optional[builtins.bool] = None,
    success_retention_period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    time_to_live: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
    vpc_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae7e63c36ba56bf570a16580ca3cc6aa4f4d25f66ba54d26f3f7a90413d04d63(
    *,
    runtime: Runtime,
    test: Test,
    artifacts_bucket_lifecycle_rules: typing.Optional[typing.Sequence[typing.Union[_aws_cdk_aws_s3_ceddda9d.LifecycleRule, typing.Dict[builtins.str, typing.Any]]]] = None,
    artifacts_bucket_location: typing.Optional[typing.Union[ArtifactsBucketLocation, typing.Dict[builtins.str, typing.Any]]] = None,
    canary_name: typing.Optional[builtins.str] = None,
    cleanup: typing.Optional[Cleanup] = None,
    enable_auto_delete_lambdas: typing.Optional[builtins.bool] = None,
    environment_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    failure_retention_period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    role: typing.Optional[_aws_cdk_aws_iam_ceddda9d.IRole] = None,
    schedule: typing.Optional[Schedule] = None,
    security_groups: typing.Optional[typing.Sequence[_aws_cdk_aws_ec2_ceddda9d.ISecurityGroup]] = None,
    start_after_creation: typing.Optional[builtins.bool] = None,
    success_retention_period: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    time_to_live: typing.Optional[_aws_cdk_ceddda9d.Duration] = None,
    vpc: typing.Optional[_aws_cdk_aws_ec2_ceddda9d.IVpc] = None,
    vpc_subnets: typing.Optional[typing.Union[_aws_cdk_aws_ec2_ceddda9d.SubnetSelection, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c04ee0a7f625fce33d3003e388d6a831237f31cbc709e9c551a1bc356475ede(
    asset_path: builtins.str,
    *,
    deploy_time: typing.Optional[builtins.bool] = None,
    readers: typing.Optional[typing.Sequence[_aws_cdk_aws_iam_ceddda9d.IGrantable]] = None,
    asset_hash: typing.Optional[builtins.str] = None,
    asset_hash_type: typing.Optional[_aws_cdk_ceddda9d.AssetHashType] = None,
    bundling: typing.Optional[typing.Union[_aws_cdk_ceddda9d.BundlingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
    follow_symlinks: typing.Optional[_aws_cdk_ceddda9d.SymlinkFollowMode] = None,
    ignore_mode: typing.Optional[_aws_cdk_ceddda9d.IgnoreMode] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__628908b4951e36d41574e89af118f4b8a140822fc9499275e081e1168a75bf43(
    bucket: _aws_cdk_aws_s3_ceddda9d.IBucket,
    key: builtins.str,
    object_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__534ebde2ca6177d2b07962ff163fa4be8fff02237e20a67c89fca238f2a43b12(
    code: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d4fce9f2879e280253f79f346736f1e74cabefddf0199d5d40b9e187d207f46(
    scope: _constructs_77d1e7e8.Construct,
    handler: builtins.str,
    family: RuntimeFamily,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__651318556062d0bfa41111177f4d584c07af87721369012008e7234cd7a9bc9d(
    *,
    inline_code: typing.Optional[builtins.str] = None,
    s3_location: typing.Optional[typing.Union[_aws_cdk_aws_s3_ceddda9d.Location, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__742d0a0d854616bacaf4bdd6a72aad127dcb8726f67f61aa6c6b3864b56f48d9(
    *,
    day: typing.Optional[builtins.str] = None,
    hour: typing.Optional[builtins.str] = None,
    minute: typing.Optional[builtins.str] = None,
    month: typing.Optional[builtins.str] = None,
    week_day: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d39435eead5e47a061f03cad4755b1155a750477abcae0773406c33664c00ba2(
    *,
    code: Code,
    handler: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da247d1ca5cbecd8aaea9b8c84a618be5cc639917820e7ecc42df6986fc5041c(
    code: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6275d20cffbb7f9580a932831ea3fe3cd5b65bfb421b1f8b04d770dc3508f7f3(
    _scope: _constructs_77d1e7e8.Construct,
    handler: builtins.str,
    _family: RuntimeFamily,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f432dbd029db5a952a9c04e6756b31fce0e5e19c4f214b45729fe31a4228a68(
    name: builtins.str,
    family: RuntimeFamily,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b38ad713f473c7c074c298bcd50e4520db7596d9bbfee5b75e35fd29ecc2ae71(
    bucket: _aws_cdk_aws_s3_ceddda9d.IBucket,
    key: builtins.str,
    object_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5715f987d53b5baf64123cc83ba9844c119abb443bcd5f14c619000f4687689b(
    _scope: _constructs_77d1e7e8.Construct,
    _handler: builtins.str,
    _family: RuntimeFamily,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67f4f45e1902e3d8ba8eb545d45bd88f6630cdbcfd293fb8ce069c9a9d32e633(
    expression: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed81e99d860f614edbd9653f58417542e72548f67d8562ec60e3581ea3c1b7a5(
    interval: _aws_cdk_ceddda9d.Duration,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bf4f7b9198aa65c5cde28608e12d3a1aaeec0ce84754b8fbb221ea9a3432c7d(
    asset_path: builtins.str,
    *,
    deploy_time: typing.Optional[builtins.bool] = None,
    readers: typing.Optional[typing.Sequence[_aws_cdk_aws_iam_ceddda9d.IGrantable]] = None,
    asset_hash: typing.Optional[builtins.str] = None,
    asset_hash_type: typing.Optional[_aws_cdk_ceddda9d.AssetHashType] = None,
    bundling: typing.Optional[typing.Union[_aws_cdk_ceddda9d.BundlingOptions, typing.Dict[builtins.str, typing.Any]]] = None,
    exclude: typing.Optional[typing.Sequence[builtins.str]] = None,
    follow_symlinks: typing.Optional[_aws_cdk_ceddda9d.SymlinkFollowMode] = None,
    ignore_mode: typing.Optional[_aws_cdk_ceddda9d.IgnoreMode] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__143fc4bffb5cfb09c7d51862845fedf3824b9a58f7e721a8ed7a6f4907e17f47(
    scope: _constructs_77d1e7e8.Construct,
    handler: builtins.str,
    family: RuntimeFamily,
) -> None:
    """Type checking stubs"""
    pass
