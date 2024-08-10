// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export function myInvoke(args: MyInvokeArgs, opts?: pulumi.InvokeOptions): Promise<MyInvokeResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("simple-invoke:index:myInvoke", {
        "value": args.value,
    }, opts);
}

export interface MyInvokeArgs {
    value: string;
}

export interface MyInvokeResult {
    readonly result: string;
}
export function myInvokeOutput(args: MyInvokeOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<MyInvokeResult> {
    return pulumi.output(args).apply((a: any) => myInvoke(a, opts))
}

export interface MyInvokeOutputArgs {
    value: pulumi.Input<string>;
}