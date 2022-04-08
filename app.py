#!/usr/bin/env python3

from aws_cdk import core

from bobo_explorer.bobo_explorer_stack import AiSurvivalGuideStack


app = core.App()
BoboExplorerStack(app, "bobo_explorer")

app.synth()
