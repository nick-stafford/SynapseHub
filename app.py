"""
SynapseHub - Enterprise Integration Orchestrator
Unified integration platform connecting your entire business stack
"""

import streamlit as st
from datetime import datetime
import time

st.set_page_config(
    page_title="SynapseHub",
    page_icon="🧠",
    layout="wide"
)

# Connected systems
SYSTEMS = {
    "salesforce": {"name": "Salesforce", "status": "connected", "color": "#00A1E0", "syncs": 12847},
    "quickbooks": {"name": "QuickBooks", "status": "connected", "color": "#2CA01C", "syncs": 8923},
    "slack": {"name": "Slack", "status": "connected", "color": "#4A154B", "syncs": 45231},
    "stripe": {"name": "Stripe", "status": "connected", "color": "#635BFF", "syncs": 3421},
    "hubspot": {"name": "HubSpot", "status": "connected", "color": "#FF7A59", "syncs": 7832},
    "aws": {"name": "AWS", "status": "connected", "color": "#FF9900", "syncs": 98234},
}

def main():
    st.title("🧠 SynapseHub")
    st.subheader("Enterprise Integration Orchestrator")

    # Top metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Connected Systems", len(SYSTEMS))
    with col2:
        st.metric("Active Connections", "15")
    with col3:
        total_syncs = sum(s["syncs"] for s in SYSTEMS.values())
        st.metric("Total Syncs Today", f"{total_syncs:,}")
    with col4:
        st.metric("Avg Latency", "12ms")

    st.divider()

    # System status grid
    st.header("🔌 Connected Systems")

    cols = st.columns(3)
    for i, (key, system) in enumerate(SYSTEMS.items()):
        with cols[i % 3]:
            with st.container():
                st.markdown(f"""
                <div style="
                    padding: 1rem;
                    border-radius: 8px;
                    border: 2px solid {system['color']};
                    background: {system['color']}15;
                    margin-bottom: 1rem;
                ">
                    <h4 style="color: {system['color']}; margin: 0;">{system['name']}</h4>
                    <p style="margin: 0.5rem 0 0 0; font-size: 0.9rem;">
                        ● Connected | {system['syncs']:,} syncs/hr
                    </p>
                </div>
                """, unsafe_allow_html=True)

    st.divider()

    # Recent activity feed
    st.header("📊 Real-Time Activity")

    activities = [
        {"time": "2s ago", "from": "Stripe", "to": "QuickBooks", "action": "Payment $2,450 synced"},
        {"time": "5s ago", "from": "Salesforce", "to": "HubSpot", "action": "Contact updated: John Smith"},
        {"time": "8s ago", "from": "Slack", "to": "Salesforce", "action": "Deal note added from #sales"},
        {"time": "12s ago", "from": "AWS", "to": "Slack", "action": "Deploy notification sent"},
        {"time": "15s ago", "from": "QuickBooks", "to": "Salesforce", "action": "Invoice #4521 created"},
    ]

    for activity in activities:
        col1, col2, col3, col4 = st.columns([1, 2, 2, 3])
        with col1:
            st.caption(activity["time"])
        with col2:
            st.write(f"**{activity['from']}**")
        with col3:
            st.write(f"→ **{activity['to']}**")
        with col4:
            st.write(activity["action"])

    st.divider()

    # Data flow visualization placeholder
    st.header("🌐 Integration Map")
    st.info("Interactive visualization of data flows between systems")

    # Connection matrix
    st.header("🔗 Connection Matrix")
    st.write("Configure bidirectional sync rules between systems")

if __name__ == "__main__":
    main()
