from aws_cdk import aws_lambda as _lambda
from constructs import Construct


class HitCounter(Construct):

    def __init__(self, scope: Construct, id: str, downstream: _lambda.IFunction, **kwargs):
        super().__init__(scope, id, **kwargs)

        # TODO
