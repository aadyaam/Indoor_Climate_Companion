import streamlit as st
import pandas as pd
from pathlib import Path

# ---------------- PAGE ----------------
st.set_page_config(
    page_title="Indoor Climate Companion",
    page_icon="🌿",
    layout="wide"
)

BASE_DIR = Path(__file__).parent

# ---------------- DATA ----------------
df = pd.read_csv(BASE_DIR / "environment_data.csv")

avg_temp = df["Temperature (°C)"].mean()
min_temp = df["Temperature (°C)"].min()
max_temp = df["Temperature (°C)"].max()

avg_humidity = df["Humidity (%)"].mean()
min_humidity = df["Humidity (%)"].min()
max_humidity = df["Humidity (%)"].max()

# ---------------- HEADER ----------------

st.title("🌿 Your Indoor Climate Companion")

st.caption("Bedroom • 24-Hour Monitoring • 7–8 July 2026")

st.divider()

# ---------------- TOP ----------------

left, right = st.columns([2.2,1])

with left:

    st.markdown("### Comfort Level")

    st.progress(0.68)

    st.success(
        f"🌿 Your room is currently comfortable • "
        f"{avg_temp:.1f}°C • {avg_humidity:.0f}%"
    )

with right:

    st.subheader("Today's Snapshot")

    st.write(f"❄️ **Coolest:** {min_temp:.1f}°C")

    st.write(f"🔥 **Warmest:** {max_temp:.1f}°C")

    st.write(f"🌡️ **Average:** {avg_temp:.1f}°C")

    st.write(f"💧 **Humidity:** {min_humidity:.0f}%–{max_humidity:.0f}%")

    st.divider()

    st.write("🪟 Open windows for fresh air.")

    st.write("🪴 Indoor conditions are comfortable for plants.")

    st.write("😊 Comfortable for studying or relaxing.")

    st.write("🧺 Clothes can be air-dried indoors.")

st.divider()

# ---------------- GRAPHS ----------------

col1,col2 = st.columns([1.6,1])

with col1:

    st.subheader("🌡️ Temperature Throughout the Day")

    st.image(BASE_DIR/"Figure_1.png",
             use_container_width=True)

    st.subheader("💧 Humidity Throughout the Day")

    st.image(BASE_DIR/"Figure_2.png",
             use_container_width=True)

with col2:

    st.subheader("🔄 Temperature vs Humidity")

    st.image(BASE_DIR/"Figure_3.png",
             use_container_width=True)

    st.markdown("## Observations")

    st.markdown(f"""
- Temperature stayed between **{min_temp:.1f}°C** and **{max_temp:.1f}°C**.
- Average temperature remained **{avg_temp:.1f}°C**.
- Humidity stayed between **{min_humidity:.0f}%** and **{max_humidity:.0f}%**.
- Conditions remained fairly stable through most of the day.
- No sudden extreme changes were observed.
""")

st.divider()

st.caption(
    f"Last Updated • Sensor: DHT11 • Data Points: {len(df)}"
)