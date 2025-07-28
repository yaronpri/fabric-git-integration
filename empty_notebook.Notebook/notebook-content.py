# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

# This code uses AI. Always review output for mistakes. 
# Read terms: https://azure.microsoft.com/en-us/support/legal/preview-supplemental-terms/

import synapse.ml.aifunc as aifunc
import pandas as pd
import openai

df= pd.DataFrame([
    ("Microsoft Teams", "2017",
    """
    The ultimate messaging app for your organization—a workspace for real-time 
    collaboration and communication, meetings, file and app sharing, and even the 
    occasional emoji! All in one place, all in the open, all accessible to everyone.
    """),
    ("Microsoft Fabric", "2023",
    """
    An enterprise-ready, end-to-end analytics platform that unifies data movement, 
    data processing, ingestion, transformation, and report building into a seamless,
    user-friendly SaaS experience. Transform raw data into actionable insights.
    """)
    ], columns=["product", "release_year", "description"])

df["summaries"] = df["description"].ai.summarize()
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
