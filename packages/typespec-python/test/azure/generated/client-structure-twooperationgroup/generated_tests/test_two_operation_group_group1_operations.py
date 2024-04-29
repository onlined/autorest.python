# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) Python Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import pytest
from devtools_testutils import recorded_by_proxy
from testpreparer import TwoOperationGroupClientTestBase, TwoOperationGroupPreparer


@pytest.mark.skip("you may need to update the auto-generated test case before run it")
class TestTwoOperationGroupGroup1Operations(TwoOperationGroupClientTestBase):
    @TwoOperationGroupPreparer()
    @recorded_by_proxy
    def test_one(self, twooperationgroup_endpoint):
        client = self.create_client(endpoint=twooperationgroup_endpoint)
        response = client.group1.one()

        # please add some check logic here by yourself
        # ...

    @TwoOperationGroupPreparer()
    @recorded_by_proxy
    def test_three(self, twooperationgroup_endpoint):
        client = self.create_client(endpoint=twooperationgroup_endpoint)
        response = client.group1.three()

        # please add some check logic here by yourself
        # ...

    @TwoOperationGroupPreparer()
    @recorded_by_proxy
    def test_four(self, twooperationgroup_endpoint):
        client = self.create_client(endpoint=twooperationgroup_endpoint)
        response = client.group1.four()

        # please add some check logic here by yourself
        # ...