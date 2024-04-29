# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from devtools_testutils import AzureRecordedTestCase, PowerShellPreparer
import functools
from resiliency.srv.driven2 import ResiliencyServiceDrivenClient


class ResiliencyServiceDrivenClientTestBase(AzureRecordedTestCase):

    def create_client(self, endpoint):
        credential = self.get_credential(ResiliencyServiceDrivenClient)
        return self.create_client_from_credential(
            ResiliencyServiceDrivenClient,
            credential=credential,
            endpoint=endpoint,
        )


ResiliencyServiceDrivenPreparer = functools.partial(
    PowerShellPreparer,
    "resiliencyservicedriven",
    resiliencyservicedriven_endpoint="https://fake_resiliencyservicedriven_endpoint.com",
)