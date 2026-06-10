import streamlit as st
from datetime import datetime
import random

st.title("🚨 AgentOps AI - Incident Investigator")
st.caption("AI-powered incident analysis for IT Operations")

incident = st.text_area(
    "Paste Incident Log Here",
    height=200
)

if st.button("Investigate Incident"):

    if not incident.strip():
        st.warning("Please paste an incident log first.")

    else:

        incident_id = random.randint(1000, 9999)

        incident_lower = incident.lower()

        if "cpu" in incident_lower:
            severity = "High"
            summary = "CPU utilization issue detected."
            root_cause = "Possible resource exhaustion."

        elif "memory" in incident_lower:
            severity = "High"
            summary = "Memory-related issue detected."
            root_cause = "Possible memory leak or insufficient RAM."

        elif "disk" in incident_lower:
            severity = "High"
            summary = "Disk space issue detected."
            root_cause = "Storage may be reaching capacity."

        elif "error" in incident_lower:
            severity = "Medium"
            summary = "Application error detected."
            root_cause = "Service or application failure."

        else:
            severity = "Low"
            summary = "General incident detected."
            root_cause = "Further investigation required."

        st.subheader("Investigation Report")

        st.write("Incident ID:", incident_id)
        st.write("Timestamp:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        st.write("### Summary")
        st.write(summary)

        st.write("### Possible Root Cause")
        st.write(root_cause)

        st.write("### Recommended Actions")

        if severity == "High":
            st.write("- Check system resources")
            st.write("- Review recent deployments")
            st.write("- Inspect application logs")

        elif severity == "Medium":
            st.write("- Review application logs")
            st.write("- Monitor system health")

        else:
            st.write("- Continue monitoring")

        st.write("### Incident Status")

        if severity == "High":
            st.error("CRITICAL")

        elif severity == "Medium":
            st.warning("OPEN")

        else:
            st.success("MONITORING")

        st.write("### Severity")

        if severity == "High":
            st.error(severity)

        elif severity == "Medium":
            st.warning(severity)

        else:
            st.success(severity)