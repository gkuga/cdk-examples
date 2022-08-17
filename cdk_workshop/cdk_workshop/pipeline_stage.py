from aws_cdk import Stage
from constructs import Construct

from .cdk_workshop_stack import CdkWorkshopStack


class WorkshopPipelineStage(Stage):

    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        service = CdkWorkshopStack(self, 'WebService')
