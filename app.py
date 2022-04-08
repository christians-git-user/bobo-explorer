#!/usr/bin/env python3

from aws_cdk import core

from bobo_explorer.bobo_explorer_stack import BoboExplorerStack


app = core.App()
BoboExplorerStack(app, "bobo-explorer")

app.synth()
